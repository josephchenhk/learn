# BQL Object Model

## Multiple securities and multiple data items

Different usage cases:

```python
# Single security and single data item
request = bql.Request("AAPL US Equity", last)

# Single security and multiple data items (data items in list with default assigned names)
request = bql.Request(AAPL US Equity", [last, high, low])

# Multiple securities and single data item
request = bql.Request(["AAPL US Equity", "IBM US Equity"], {'CLOSE': last})

# Multiple securities and multiple data items (data items in dict with specified names)
request = bql.Request(["AAPL US Equity", "IBM US Equity"], {'CLOSE': last, 'HIGH': high, 'LOW':low})
```

Note that the dates are associated with the data items, not the request.

```python
# Import the BQL library
import bql

# Instantiate an object to interface with the BQL service
bq = bql.Service()

# Define the date range for the request
date_range = bq.func.range('2017-06-05','2017-06-09')
date_range2 = bq.func.range('2017-06-05','2017-06-07')

# Define data items for the pricing fields
# Pass the defined date range
last = bq.data.px_last(dates=date_range)
high = bq.data.px_high(dates=date_range)
low = bq.data.px_low(dates=date_range2)

# Multiple securities and multiple data items
request = bql.Request(["AAPL US Equity", "IBM US Equity"], {'CLOSE': last, 'HIGH': high, 'LOW':low})

# Execute the request
response = bq.execute(request)

# Display the response in a data frame
# Use the combined_df function to display 
# the three returned values in a single data frame 
df = bql.combined_df(response)
```

Here is the result of `df`:

|  	          |DATE	       |CURRENCY	|CLOSE	|HIGH	|LOW |
|-------------|------------|----------|-------|----------|
|ID	          |		         |          |       |          |
|AAPL US Equity|2017-06-05|USD|38.482500|38.612500|38.365000|
|AAPL US Equity|2017-06-06|USD|38.612500|38.952500|38.445000|
|AAPL US Equity|2017-06-07|USD|38.842500|38.995000|38.620000|
|AAPL US Equity|2017-06-08|USD|38.747500|38.885000|NaN|
|AAPL US Equity|2017-06-09|USD|37.245000|38.797500|NaN|
|IBM US Equity|2017-06-05|USD|145.576545|146.073231|144.881783|
|IBM US Equity|2017-06-06|USD|145.538339|146.035024|145.184928|
|IBM US Equity|2017-06-07|USD|144.210661|147.286289|144.038731|
|IBM US Equity|2017-06-08|USD|145.280444|145.968162|NaN|
|IBM US Equity|2017-06-09|USD|147.190772|147.348374|NaN|
