def frange(start, end, increment):
    x = start
    while x<end:
        yield x
        x += increment

if __name__=="__main__":
    for n in frange(0, 4, 0.5):
        print(n)

    print("---------------------------\n")
    f = frange(0, 4, 0.5)
    print(next(f), next(f), next(f))