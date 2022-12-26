from collections import defaultdict
from collections import deque

def find_compilation_order(lst) :
  graph = {}
  indeg = defaultdict(int)
  result = []

  for edge in lst :
    graph[edge[0]] = []
    graph[edge[1]] = []
  
  for edge in lst :
    graph[edge[0]].append(edge[1])
    indeg[edge[1]] += 1

  print("-" * 20)
  print('input', lst)
  print('g', graph)
  print('indeg', indeg)
  print("-" * 20)

  Q = deque()
  for node in graph.keys() :
    print ('node indeg', node , indeg[node])
    if indeg[node] == 0 :
      Q.append(node)

  while Q :
    parent = Q.pop()
    result.append(parent)
    for child in graph[parent] :
      indeg[child] -= 1
      if indeg[child] == 0 :
        Q.append(child)

  return result

def main():
    dependencies = [[['B', 'A'], ['C', 'A'], ['D', 'C'], ['E', 'D'], ['E', 'B']],
        [['B', 'A'], ['C', 'A'], ['D', 'B'], ['E', 'B'], ['E', 'D'], ['E', 'C'], ['F', 'D'], ['F', 'E'], ['F', 'C']],
        [['A', 'B'], ['B', 'A']],
        [['B', 'C'], ['C', 'A'], ['A', 'F']],
        [['C', 'C']]]
    for i in range(len(dependencies)):
        print(i + 1, ".\tdependencies: ", dependencies[i], sep = "")
        print("\tCompilation Order: ", find_compilation_order(dependencies[i]), sep = "")
        print("-"*100, "\n", sep ="")


if __name__ == "__main__":
    main()