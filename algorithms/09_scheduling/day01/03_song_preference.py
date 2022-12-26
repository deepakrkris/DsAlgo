"""
You have access to ranked lists of songs for various users. Each song is represented as an integer,
and more preferred songs appear earlier in each list.
For example, the list [4, 1, 7] indicates that a user likes song 4 the best, followed by songs 1 and 7.

Given a set of these ranked lists,
interleave them to create a playlist that satisfies everyone's priorities.

For example, suppose your input is {[1, 7, 3], [2, 1, 6, 7, 9], [3, 9, 5]}. In this case a satisfactory playlist could be [2, 1, 6, 7, 3, 9, 5].

We will be sending the solution tomorrow, along with tomorrow's question.
As always, feel free to shoot us an email if there's anything we can help with.
"""


def preference_order(user_preferences):
  g = {}
  indegrees = {}
  root = None
  order = []
  
  def connections(p) :
    for i in range(len(p) - 1, -1, -1) :
      if p[i] not in g :
        g[p[i]] = set()
        indegrees = set()
      for j in range (i) :
        g[p[i]].add(p[j])
    for n in g.keys() :
      for out in g[n] :
        indegrees[out].add(n)
        
  
  def topology(root) :
    indeg_lst = list(indegrees[root])
    
    for in_node in indeg:
      order.append(in_node)
      indeg.delete(in_node)

  for p in user_preferences :
    connections(p)
  
  for s in g.keys() :
    if len(g[s]) == 0 :
      root = s
      break

  if root is None :
    return []

  return topology(root)

def main():
  print(preference_order([[1, 7, 3], [2, 1, 6, 7, 9], [3, 9, 5]]))


if __name__ == "__main__":
  main()
