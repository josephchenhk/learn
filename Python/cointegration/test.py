# -*- coding: utf-8 -*-
# @Time    : 19/3/2021 10:31 AM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: test.py
# @Software: PyCharm

"""
Simple stationarity tests on time series
Ref: https://medium.com/bluekiri/simple-stationarity-tests-on-time-series-ad227e2e6d48
"""
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma

from statsmodels.regression.linear_model import OLS
from statsmodels.tsa.tsatools import lagmat, add_trend
from statsmodels.tsa.adfvalues import mackinnonp
from statsmodels.tsa.stattools import coint
from statsmodels.tsa.stattools import adfuller

from hurst import compute_Hc, random_walk

def adf2(ts, maxlag:int=1):
    """
    Augmented Dickey-Fuller unit root test
    """
    # make sure we are working with an array, convert if necessary
    ts = np.asarray(ts)

    # # Get the dimension of the array
    # nobs = ts.shape[0]

    # Calculate the discrete difference
    tsdiff = np.diff(ts)

    # Create a 2d array of lags, trim invalid observations on both sides
    tsdall = lagmat(tsdiff[:, None], maxlag, trim='both', original='in')
    # Get dimension of the array
    nobs = tsdall.shape[0]

    # replace 0 xdiff with level of x
    tsdall[:, 0] = ts[-nobs - 1:-1]
    tsdshort = tsdiff[-nobs:]

    # Calculate the linear regression using an ordinary least squares model
    results = OLS(tsdshort, add_trend(tsdall[:, :maxlag + 1], 'c')).fit()
    adfstat = results.tvalues[0]

    # Get approx p-value from a precomputed table (from stattools)
    pvalue = mackinnonp(adfstat, 'c', N=1)
    return adfstat, pvalue

def adf(ts, maxlag:int=None):
    """
    Augmented Dickey-Fuller unit root test

    tsdall[explanatory variable] (maxlag=3 as an example)
    * 1st column(tsdall[:,0]): [x3, x4, ..., x_{t-2}, x_{t-1}] are X variables (corresponding to coefficient *lambda*)
    * 2nd column(tsdall[:,1]): [x3-x2, x4-x3, ..., x_{t-2}-x_{t-3}, x_{t-1}-x_{t-2}] are X variables (corresponding to coeff *alpha_1*)
    * 3rd column(tsdall[:,2]): [x2-x1, x3-x2, ..., x_{t-3}-x_{t-4}, x_{t-2}-x_{t-3}] are X variables (corresponding to coeff *alpha_2*)
    * 4th column(tsdall[:,3]): [x1-x0, x2-x1, ..., x_{t-4}-x_{t-3}, x_{t-3}-x_{t-4}] are X variables (corresponding to coeff *alpha_3*)

    tsdshort[response variable]:
    * [x4-x3, x5-x4, ..., x_{t-1}-x_{t-2}, x_t-x_{t-1}] are the Y variables

    Regression:
    * x4-x3 = lambda*x3 + alpha1*(x3-x2) + alpha2*(x2-x1) + alpha3*(x1-x0) + mu + epsilon
    * x5-x4 = lambda*x4 + alpha1*(x4-x3) + alpha2*(x3-x2) + alpha3*(x2-x1) + mu + epsilon
    * ...
    * x_t-x_{t-1} = lambda*x_{t-1} + alpha1*(x_{t-1}-x_{t-2}) + alpha2*(x_{t-2}-x_{t-3}) + alpha3*(x_{t-3}-x_{t-4}) + mu + epsilon
    """
    # Maximum lag which is included in test, default 12*(nobs/100)^{1/4}
    # Ref: https://www.statsmodels.org/stable/generated/statsmodels.tsa.stattools.adfuller.html
    if maxlag is None:
        maxlag = int(np.ceil(12 * (len(ts) / 100) ** (1 / 4)))

    # make sure we are working with an array, convert if necessary
    ts = np.asarray(ts)

    # Calculate the discrete difference
    tsdiff = np.diff(ts)

    # Create a 2d array of lags, trim invalid observations on both sides
    tsdall = lagmat(tsdiff[:, None], maxlag, trim='both', original='in')

    # Get dimension of the array
    nobs = tsdall.shape[0]

    # [explanatory variable] replace first column ([:,0]) xdiff with level of x
    tsdall[:, 0] = ts[-nobs - 1:-1]

    # [response variable]
    tsdshort = tsdiff[-nobs:]

    # Calculate the linear regression using an ordinary least squares model
    results = OLS(tsdshort, add_trend(tsdall[:, :maxlag + 1], 'c')).fit()

    # adfstat = DF = lambda / SE(lambda)
    adfstat = results.tvalues[0]

    # Get approx p-value from a precomputed table (from stattools)
    pvalue = mackinnonp(adfstat, 'c', N=1)

    return adfstat, pvalue


def hurst(ts):
    """
    Returns the Hurst Exponent of the time series vector ts
    """
    # make sure we are working with an array, convert if necessary
    ts = np.asarray(ts)

    # number of observations
    nobs = len(ts)
    assert nobs >= 64, f"Number of data points not sufficient! len(ts)={nobs}."

    # divide into 6 groups:
    # (a). length of sub ts: nobs
    # (b). length of sub ts: int(nobs/2)
    # (c). length of sub ts: int(nobs/4)
    # (d). length of sub ts: int(nobs/8)
    # (e). length of sub ts: int(nobs/16)
    # (f). length of sub ts: int(nobs/32)
    size = [int(nobs/(2**n)) for n in range(6)]
    ARS = list()
    for lag in size: # every sub ts contains `lag` elements
        nsub = int(nobs / lag)
        # print(nsub)
        RS = list()
        for i in range(nsub): # there are `nsub` sub ts
            mean = ts[i*lag:i*lag+lag].mean()
            y = ts[i*lag:i*lag+lag] - mean # mean-adjusted series
            z = np.cumsum(y)
            R = max(z) - min(z)
            S = y.std()
            if S==0:
                continue
            RS.append(R/S)
        RS = np.array(RS)

        if lag>340:
            ERS = 1.0 / np.sqrt(lag * np.pi / 2.0) * sum(np.sqrt((lag - j) / j) for j in range(1, lag))
        elif lag<=340:
            ERS = gamma((lag-1)/2.0) / (np.sqrt(np.pi)*gamma(lag/2.0)) * sum(np.sqrt((lag - j) / j) for j in range(1, lag))

        ARS.append(RS.mean() - ERS + np.sqrt(0.5*np.pi*lag))

    H = np.polyfit(np.log(np.asarray(size)),
                   np.log(np.asarray(ARS)),
                   1)
    return H[0]


def variance_ratio(ts, lag=2):
    """
    Returns the variance ratio test result
    """
    # make sure we are working with an array, convert if necessary
    ts = np.asarray(ts)

    # Apply the formula to calculate the test
    n = len(ts)
    mu = sum(ts[1:n] - ts[:n - 1]) / n
    m = (n - lag + 1) * (1 - lag / n)
    b = sum(np.square(ts[1:n] - ts[:n - 1] - mu)) / (n - 1)
    t = sum(np.square(ts[lag:n] - ts[:n - lag] - lag * mu)) / m
    return t / (lag * b)

def variance_ratio2(ts, lag=2):
    """
    Returns the variance ratio test result

    Original solution:
    -----------------
    # make sure we are working with an array, convert if necessary
    ts = np.asarray(ts)

    # Apply the formula to calculate the test
    n = len(ts)
    mu = sum(ts[1:n] - ts[:n - 1]) / n;
    m = (n - lag + 1) * (1 - lag / n);
    b = sum(np.square(ts[1:n] - ts[:n - 1] - mu)) / (n - 1)
    t = sum(np.square(ts[lag:n] - ts[:n - lag] - lag * mu)) / m
    return t / (lag * b);
    """
    # make sure we are working with an array, convert if necessary
    ts = np.asarray(ts)

    # Apply the formula to calculate the test
    n = len(ts)
    assert n>lag, f"n={n}, but lag={lag}, we should have n>lag."

    # lag=1
    mu = (ts[n-1] - ts[0]) / (n-1) # same as sum(ts[1:n] - ts[:n - 1]) / (n-1)
    b = sum(np.square(ts[1:n] - ts[:n - 1] - mu)) / (n - 1)

    # lag>1
    mu = sum(ts[lag:n] - ts[:n - lag]) / (n - lag)
    t = sum(np.square(ts[lag:n] - ts[:n - lag] - mu)) / (n - lag)
    return t / (lag * b)


def half_life(ts):
    """
    Calculates the half life of a mean reversion
    """
    # make sure we are working with an array, convert if necessary
    ts = np.asarray(ts)

    # delta = y(t) - y(t-1) = ts[1:] - ts[:-1]
    delta_ts = np.diff(ts)

    # calculate the vector of lagged values. lag = 1
    lag_ts = np.vstack([ts[1:], np.ones(len(ts[1:]))]).T

    # calculate the slope of the deltas vs the lagged values
    beta = np.linalg.lstsq(lag_ts, delta_ts)

    # compute and return half life
    return (np.log(2) / beta[0])[0]


def cadf(x, y):
    """
    Returns the result of the Cointegrated Augmented Dickey-Fuller Test
    """
    # Calculate the linear regression between the two time series
    ols_result = OLS(x, y).fit()

    # Augmented Dickey-Fuller unit root test
    return adf(ols_result.resid)

def create_random_walk(N:int=1000):
    from random import seed
    from random import random
    seed(1)
    random_walk = list()
    random_walk.append(-1 if random() < 0.5 else 1)
    for i in range(1, N):
        movement = -1 if random() < 0.5 else 1
        value = random_walk[i - 1] + movement
        random_walk.append(value)
    return random_walk

def create_data(data_type:str):
    np.random.seed(2021)

    if data_type=="random_walk":
        N = 999
        random_noise = np.random.randn(N)
        lambda_ = 0
        mu = -2e-2 # Drift set to be small to avoid overflow
        y0 = 0
    elif data_type=="mean_reverting":
        N = 9999
        random_noise = np.random.randn(N)
        lambda_ = -0.2
        mu = 1
        y0 = 5  # [long term mean of the ts] = mu / (-lambda_)
    elif data_type=="trending":
        N = 999 # number of observations set to be small to avoid overflow
        random_noise = np.random.randn(N) # allow stronger noise
        lambda_ = 1e-5  # set to small otherwise the data would explode quickly
        mu = -2e-2
        y0 = 0
    else:
        raise ValueError(f"data_type={data_type} is not supported!")

    ts = [y0]
    for n in range(N):
        y1 = y0 + mu  + lambda_*y0 + random_noise[n]
        ts.append(y1)
        y0 = y1

    fig = plt.figure()
    plt.plot(range(len(ts)), ts)
    plt.xlabel("Time")
    plt.ylabel("Data")
    fig.savefig(f"ts-{data_type}.png")
    return np.array(ts)

if __name__=="__main__":

    ############
    # ADF Test

    ts = create_data(data_type="random_walk")
    print("< ADF Tests (random_walk) >")
    print(f"ADF implemented: {adf(ts)}")
    print(f"ADF in statsmodels: {adfuller(ts, autolag=None)}")
    print(f"Hurst implemented: H={hurst(ts)}")
    print("-"*50)

    ts = create_data(data_type="mean_reverting")
    print("< ADF Tests (mean_reverting) >")
    print(f"ADF implemented: {adf(ts)}")
    print(f"ADF in statsmodels: {adfuller(ts, autolag=None)}")
    print(f"Hurst implemented: H={hurst(ts)}")
    print("-"*50)

    ts = create_data(data_type="trending")
    print("< ADF Tests (trending) >")
    print(f"ADF implemented: {adf(ts)}")
    print(f"ADF in statsmodels: {adfuller(ts, autolag=None)}")
    print(f"Hurst implemented: H={hurst(ts)}")
    print("-"*50)

    ############

    ############
    # Hurst

    # np.random.seed(2021)
    # random_changes = 1. + np.random.randn(9999) / 1000.
    # ts = np.cumprod(random_changes)

    print("< Hurst >")
    # ts_err = ts[1:] / ts[:-1] - 1
    # H = hurst(ts_err)
    H = hurst(ts)
    print(f"Hurst implemented: H={H}")
    H, c, data = compute_Hc(ts, kind='price', simplified=True)
    print(f"Hurst simplified in hurst module: H={H}")
    H, c, data = compute_Hc(ts, kind='price', simplified=False)
    print(f"Hurst advanced in hurst module: H={H}")
    print("-" * 50)


    var = variance_ratio(ts_err, lag=3)
    print(var)
    var = variance_ratio2(ts_err, lag=3)
    print(var)



    x = np.linspace(0, 1, 1000)
    y = [d + random.randint(0, 1000) / 100000 for d in x]

    print(cadf(x, y))
    print()

    np.random.normal()