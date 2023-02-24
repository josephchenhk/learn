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

    - `wavg`: weighted average
    
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

     - `corr`: correlation
    
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

    - `rsq`: R-square
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

    - `cut`: x-tile rank

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

    - `quantile`: quantile cut-off point

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

    - `bins`: custom sized bins to bucket your data items

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

    - `rank`: rank results ascending or descending

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

* Time Series
  ```shell
  cumavg, cummax, cummin, cumprod, cumsum, diff, net_chg, pct_chg, pct_diff, rolling
  ```

* Grouping
  ```shell
  group, ungroup, groupavg, groupcount, groupmax, groupmedian, groupmin, grouprank, groupsort, groupstd, groupsum, groupwavg, groupzscore
  ```

* Conditional
  ```shell
  if_, and_, in_, not_, or_, xor, all, any, between, mathematical operators
  ```

    - `mathematical operators`: include `==, >, >=, <. <=, !=`

* Data and Error Handling
  ```shell
  avail, dropna, znav, replacenonnumeric, replacena, first, last, sort, matches
  ```

    - `avail`: the first non-null value

    For members of the UKX, give EBITDA if available. Otherwise return Operating Income:

    ```python
    index = bq.univ.members('UKX Index')

    ebitda = bq.data.ebitda(fpt='a', fpo='3Y') 
    eps_a = bq.data.is_oper_inc(fpt='a', fpo='3Y')
    data = bq.func.avail(ebitda, eps_a) / 10**6

    req = bql.Request(index, {'Ebitda or Operating Income':data})
    res = bq.execute(req)
    dataset = res[0].df()
    dataset.head(5)
    ```

    - `znav`: replaces missing values (NA) with 0
    - `replacenonnumeric`: replaces missing values (NA) with specific number
    - `first`: return first `n` elements from the whole data set, e.g., `first(10)`
    - `last`: return last `n` elements from the whole data set, e.g., `last(7)`
    - `sort`: sort the elements in either descending/ascending order, `sort(order='desc')`
    - `match`: match specified criteria, e.g., `bq.func.matches(my_return, bq.data.px_volume() > '150M')`

* Date and Time

  ```shell
  today, dayofweek, dayofmonth, week, month, year
  ```
  
    - `today`: today's date, e.g., `bq.func.today()`
    - `dayofweek`: the day of the week (1-7), `bq.data.px_last(dates=bq.func.range('-1m', '0d'))['DATE'].dayofweek()`
    - `dayofmonth`: the day of month (1-31), `bq.data.px_last(dates=bq.func.range('-1m', '0d'))['DATE'].dayofmonth()`
    - `week`: the week of the year (1-53), `bq.data.px_last(dates=bq.func.range('-1m', '0d'))['DATE'].week()`
    - `month`: the month of the year (1-12), `bq.data.px_last(dates=bq.func.range('-1m', '0d'))['DATE'].month()`
    - `year`: the month of the year (e.g., 2021, 2022...), `bq.data.px_last(dates=bq.func.range('-2y', '0d'))['DATE'].year()`

* String

  ```shell
  concat, left, len, replace, right, startswith, tolower, toupper
  ```
  
    - `concat`: `concat()` or simply `+` to merge two strings

      ```python
      apple = ['AAPL US Equity']
      name = bq.data.name()
      sector = bq.data.classification_name()
      
      # use concat():
      name_and_sector = name.concat("-" + sector) 
      # use "+":
      # name_and_sector = name + "-" + sector 

      req = bql.Request(apple, {'Name and Sector':name_and_sector})
      res = bq.execute(req)
      data = res[0].df()
      data
      ```
    
    - `right`: get n characters from the right
    - `left`: get n characters from the left

      ```python
      vod_bonds = bq.univ.bonds('VOD LN Equity')
      name = bq.data.name()
      name_from_left = name.left(18)

      req = bql.Request(vod_bonds, {'From the Left':name_from_left})
      res = bq.execute(req)
      data = res[0].df()
      data.head()
      ```
      
    - `len`: get length of a string
      
      ```python
      apple = ['AAPL US Equity']
      name = bq.data.name()
      start = name.len()-2
      new_text = "Corporation"
      characters = 3
      new_name = name.replace(start.toscalar(), characters, new_text)

      request = bql.Request(apple, {'New Name':new_name, 'Original Name':name})
      response = bq.execute(request)
      pd.concat([x.df() for x in response], axis=1)
      
      -->
                      New Name	        Original Name
      ID		
      AAPL US Equity	Apple Corporation	Apple Inc
      ```
      
    - `startwith`: bool to indicate whether a string starts with something

      ```python
      tpx = bq.univ.members('TPX Index')
      sector = bq.data.classification_name('GICS','1')
      consumer_sector = sector.matches(sector.startswith('Consumer')).dropna('true')

      req = bql.Request(tpx, {'Consumer stocks':consumer_sector})
      res = bq.execute(req)
      data = res[0].df()
      data.head()
      
      -->
                      Consumer stocks
      ID	
      2812 JT Equity	Consumer Staples
      2767 JT Equity	Consumer Discretionary
      8860 JT Equity	Consumer Discretionary
      3186 JT Equity	Consumer Discretionary
      3116 JT Equity	Consumer Discretionary
      ```
     
* Universe

  ```shell
  filter, members, bond, loans, mortgages, municipals, preferreds, cds, futures, options, bondsuniv, loansuniv, 
  mortgagesuniv, debtuniv, issuerof, parent, equitiesuniv, fundsuniv, relativeindex, value, translateSymbols, 
  setdiff*, intersect*, union*, peers*
  ```
  `*` = New for 2021


