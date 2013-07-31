
def euler1():
    l = range(1000)
    return sum(set(l[::3] + l[::5]))

def euler1a():
    return sum(x for x in range(1000) if x % 3 == 0 or x % 5 == 0)
