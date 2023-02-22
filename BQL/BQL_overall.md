# BQL and the PyBQL API

There are two ways to execute BQL queries via PyBQLL:

## The String Model

The very basic string interface query in BQL include a `get` and a `for` clause:

```python
request = """
get(PX_HIGH - PX_LOW)
for(['AAPL US Equity'])
"""

response = bq.execute(request)
```

## The Object Model
````python
import bql

bq = bql.Service()

# universe
univ = bq.univ.members('BE500 Index')

# data
high = bq.data.px_high()
low = bq.data.px_low()

# request
request = bql.Request(univ, high - low)

# Execute the request
response = bq.execute(request)

# get data in DataFrame
df = response[0].df()
````

## All BQL Functions and Universes

* Statistical

```shell
sum, count, avg, wavg, min, max, median, product, corr, rsq, std, var, skew,
kurt, zscore, compoundgrowthrate, cut, quantile, bins, rank
```

-- `wavg`: weighted average
```python
daimler = 'DAI EU Equity'
price = bq.data.px_last(dates= bq.func.range('-1y','0d'), frq='d')
vol = bq.data.px_volume(dates=bq.func.range('-1y','0d'), frq='d')
weighted_avg = price.wavg(vol)

req = bql.Request(daimler, {'Weighted Avg Price by Vol':weighted_avg})
res = bq.execute(req)
data = res[0].df()
data
```

-- `corr`: correlation
```python
dow = bq.univ.members('INDU Index', dates='0d')
vol = bq.data.px_volume(dates = bq.func.range('-1m','-1d')).dropna()
rtrn = bq.data.day_to_day_total_return(dates = bq.func.range('-1m','-1d')).dropna()
vol_to_rtrn_correlation = vol.corr(rtrn)

req = bql.Request(dow, {'Correlation':vol_to_rtrn_correlation})
res = bq.execute(req)
data = res[0].df()
data.head()
```

-- `rsq`: R-square
```python
dow = bq.univ.members('INDU Index')
a = ['1','2','3','4','5','6','7','8','9','10']
# ae: actual/estimate, fpt: annually,quarterly,monthly,weekly,daily, fpo:period offset, i.e., the time range
itm = bq.data.is_eps(ae='a', fpt='a', fpo=bq.func.range('-9y','0y'))
r_squared = itm.rsq(a)

req = bql.Request(dow, {'% Variance explained':r_squared})
res = bq.execute(req)
data = res[0].df()
data.head()
```

-- `cut`: x-tile rank

The following example creating volume deciles within range of 1 to 10:

```python
facebook = 'META US Equity'
vol = bq.data.px_volume(dates=bq.func.range('-2w','0d')).dropna()
deciles = vol.cut('10')

req = bql.Request(facebook, {'Volume Deciles':deciles})
res = bq.execute(req)
data = res[0].df()
data.head()
```

-- `quantile`: quantile cut-off point

The following example returns a volume deciles 93%:

```python
facebook = 'META US Equity'
vol = bq.data.px_volume(dates=bq.func.range('-2w','0d'))
top_decile_cut_off = vol.quantile('0.93')

req = bql.Request(facebook, {'Top Decile Cut-Off':top_decile_cut_off})
res = bq.execute(req)
data = res[0].df()
data.head()
```

-- `bins`: custom sized bins to bucket your data items

The following example returns duration bucket of IBM bonds falling into based on 3.5 and 7 as the cut-off points

```python
bonds = bq.univ.bonds('IBM US Equity')
duration = bq.data.duration()
duration_bins = duration.bins([3.5, 7], ['1-3', '4-7','Above'])

req = bql.Request(bonds, {'Duration Bins':duration_bins})
res = bq.execute(req)
data = res[0].df()
data.head()
```

-- `rank`: rank results ascending or descending

The following example returns ranks of Cat US Sales between past 4 years and next 2 years

```python
cat = 'CAT US Equity'
sales = bq.data.sales_rev_turn(fpt='a', fpo=bq.func.range('-3','2'))
sales_rank = sales.rank(order='desc')

req = bql.Request(cat, {'Rank of Sales':sales_rank})
res = bq.execute(req)
data = res[0].df()
data
```

* Mathematical

```shell
abs, ceil, exp, floor, ln, log, round, sign, sqrt, square, mod, -, ^
```
