import operator

def Euler11():
  with open("grid11.txt", "r") as grid_file:
    grid_str = [line.split() for line in grid_file]
    grid = matrix_map(int, grid_str)
    print grid
    max_4 = max(check_grid(grid, i, j) for i in range(20) for j in range(20))
    return max_4


def product(iterable):
  return reduce(operator.mul, iterable, 1)

def matrix_map(f, matrix):
  return [[f(x) for x in row] for row in matrix]

def check_grid(grid, x, y):
  products = [0]
  if x < 17:
    products.append(product(grid[x + i][y] for i in range(4)))
  if y < 17:
    products.append(product(grid[x][y + j] for j in range(4)))
  if x < 17 and y < 17:
    products.append(product(grid[x + i][y + i] for i in range(4)))
  if x < 17 and y > 2:
    products.append(product(grid[x + i][y - i] for i in range(4)))
  print x, y, max(products)
  return max(products)
