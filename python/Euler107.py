import collections


graph_file = open("network.txt", "r")
str_matrix = [line.strip().split(",") for line in graph_file]
matrix = [[int(elem) if elem != "-" else 0 for elem in row] for row in str_matrix]
num_nodes = len(matrix)

edge_weights = {}
for i in range(num_nodes):
  for j in range(num_nodes):
    if matrix[i][j] != 0:
      edge_weights.setdefault(i, set()).add((j, matrix[i][j]))
      edge_weights.setdefault(j, set()).add((j, matrix[j][i]))


def isConnected(num_nodes, edges):
  visited_nodes = set()
  next_nodes = set([0])
  while next_nodes:
    current = next_nodes.pop()
    for adjacent in edges[current]:
      if adjacent not in visited_nodes:
        next_nodes.add(adjacent)
  return visited_nodes == num_nodes
