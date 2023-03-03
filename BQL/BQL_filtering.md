# BQL Filtering

## Combine criteria with and_() function

```python
criteria_list = bq.func.and_(criteria_1, criteria_2).and_(criteria_3)
```

## Apply to the universe

```python
filtered_univ = bq.univ.filter(start_univ, criteria_list)
```

## An example

This example filters the members of the HSI Index to return only companies with
a market cap between 50 - 100 billion HKD, **and** with P/E ratios below the
sector average.

```python
import pandas as pd
import bql

bq = bql.Service()

# Starting universe
start_univ = bq.univ.members('HSI Index')

# 3 Criteria
criteria_1 = bq.data.cur_mkt_cap(currency='HKD') >= 50*10**9
criteria_2 = bq.data.cur_mkt_cap(currency='HKD') <= 100*10**9
sector = bq.data.gics_sector_name()
pe_ratio = bq.data.pe_ratio()
sector_avg_pe_ratio = pe_ratio.groupavg(sector)
criteria_3 = pe_ratio < sector_avg_pe_ratio

# combine all criteria
criteria_list = bq.func.and_(criteria_1, criteria_2).and_(criteria_3)

# filter universe
filtered_univ = bq.univ.filter(start_univ, criteria_list)

# Now we get some data fields
mkt_cap = bq.data.cur_mkt_cap(currency='HKD')
name = bq.data.name()

request = bql.Request(filtered_univ, {'Name': name, 'Market_Cap': mkt_cap})

response = bq.execute(request)

# Outer join the dataframes. The response is a list of the results
df = pd.concat([x.df()[x.name] for x in response], sort=False, axis=1)
```

The result `df` could be something like this:

|ID            |Name     |Market_cap  |
|--------------|---------|------------|
|101 HK Equity |7.27e+10 |Hang Lung Properties Ltd |
|992 HK Equity |8.62e+10 |Lenovo Group Ltd|
|...           |...      |...|

## Multiple Criteria

Use `reduce` to aggregate multiple criteria:

```python
from functools import reducce

filters = []
filters.append(criteria_1)
filters.append(criteria_2)
filters.append(criteria_3)
agg_filter = reduce(bq.func.and_, filters)
```
