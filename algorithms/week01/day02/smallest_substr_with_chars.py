from collections import defaultdict

def get_shortest_unique_substring(arr, str):
  # iterate index from 0 to len(str) - 1
  #   find a match within range indexx to len(str) - 1
  #    if a match found in arr, remove it from arr
  # if list is empty
  
  # "xyyzyzyx" x - 0 , z - 3 4
  # N^2
  """
  xyy
  """
  
  # use a sliding window
  # have two pointers startIndex , moveIndex
  # have one counter for the arr, matchCounter
  #   have a temp map which maps every arr element to false/true (arrMap)
  #   When value of the str at moveIndex is found in arrMap[index] and if arrMap is false
  #        increment counter matchCounter
  #      if matchCounter == len(arr)
  #           save the window size endIndex - startIndex
  #

  moveIndex = 0
  arrMap = {}
  for char in arr :
    arrMap[char] = False
  
  counter = 0
  minLength = float('inf')
  minMatch = ""

  while moveIndex < len(str) :
    if str[moveIndex] in arrMap :
      if arrMap[str[moveIndex]] == False :
          counter = counter + 1
          arrMap[str[moveIndex]] = True

    if counter == len(arr) :
        endIndex = moveIndex
        startIndex = moveIndex
        while counter > 0 :
          if str[moveIndex] in arrMap and arrMap[str[moveIndex]] == True :
            counter = counter - 1
            arrMap[str[moveIndex]] = False
            startIndex = moveIndex
          moveIndex = moveIndex - 1

        if minLength > len(str[startIndex : endIndex + 1]) :
          minMatch = str[startIndex : endIndex + 1]
          minLength = len(minMatch)
        moveIndex = endIndex
    moveIndex = moveIndex + 1
  return minMatch

print(get_shortest_unique_substring(["A","B","C"], "ADOBECODEBANCDDD"))
"""
arr = ['x','y','z'], str = "xyyzyzyx"
                                 ___
                                 
reverse_str = "xyzyzyyx"
'x____y'

2 pointers.
left_ptr
right_ptr 

1.
  scan from left first
  scan from right
  
2.
  scan from right first
  scan from left

"""