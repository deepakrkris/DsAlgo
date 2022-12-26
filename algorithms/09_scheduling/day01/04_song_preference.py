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

from collections import deque

def preference_order(user_preferences):
  graph = {}
  indeg = {}
  result = []

  for user_pref in user_preferences :
    for item in user_pref :
      graph[item] = set()
      graph[item].update([])
      indeg[item] = 0

  for user_pref in user_preferences :
    for i in range(len(user_pref)) :
      graph[user_pref[i]].update(user_pref[i + 1 : len(user_pref)])
  
  for node in graph.keys() :
    for child in graph[node] :
        indeg[child] += 1

  print("-" * 20)
  print('input', user_preferences)
  print('g', graph)
  print('indeg', indeg)

  Q = deque()
  for item in indeg.keys() :
    if indeg[item] == 0 :
      Q.append(item)

  print(Q)
  print("-" * 20)

  while Q :
    parent = Q.pop()
    result.append(parent)
    print(Q, parent, graph[parent])
    for children in graph[parent] :
        indeg[children] -= 1
        if indeg[children] == 0 :
          Q.append(children)
        print('indeg', indeg)

  return result

def main():
  print(preference_order([[1, 7, 3], [2, 1, 6, 7, 9], [3, 9, 5]]))


if __name__ == "__main__":
  main()
