
def euler9():
  possible_triples = []
  for i in range(1000):
    for j in range(i, 1000):
      for k in range(j+1, 1000):
        if i + j + k == 1000:
          possible_triples.append((i,j,k))

  for a,b,c in possible_triples:
    if a**2 + b**2 == c**2:
      return a*b*c
