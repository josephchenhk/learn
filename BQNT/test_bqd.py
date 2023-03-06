import sys

print(sys.executable)

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
print()