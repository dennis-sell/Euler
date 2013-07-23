
def euler1():
  l = range(1000)
  t = l[::3] + l[::5]
  return sum(set(t))
