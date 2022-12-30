# Design a LRU Cache, size is 1000

"""
 Least recently cache
 eviction policy = remove items not accessed in the recent
 
 { a, b, c , d}
  3 
  c b a
   dict + doubly_linked_list
"""

cache = {}

def add_item(value) :
    cache[key] = Node()
