#verify a binary tree is a binary search tree

"""

root 
left -> smaller
right -> bigger
          ()
           8 
     (-inf , 8)  (8 , inf)      
    4              10
(-inf, 4)     (4, 8)
2     10        7
     
 
"""

class Node :
    def __init__(self, value, left, right) :
      self.left = left
      self.right = right
      self.value = value

def is_valid_bst(root, lower, upper) :
    if not root :
        return True

    if root.value > lower and root.value < upper :
        return False

    return is_valid_bst(root.left, lower, root.value) and is_valid_bst(root.right, root.value, upper)
