def count(n):
    while True:
        yield n
        n += 1

c = count(0)
try:
    print(c[10:20])
except TypeError as e:
    print(e)

# use itertools.isslice()
import itertools
try:
    print(list(itertools.islice(c,10,20)))
except Exception as e:
    print(e)