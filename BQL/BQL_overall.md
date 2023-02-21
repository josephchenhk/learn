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
