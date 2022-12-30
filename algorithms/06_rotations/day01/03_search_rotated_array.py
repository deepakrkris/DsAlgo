#
# search in a sorted array with rotation/circular {8,9,1,2,3,4,5,6,7} -> the target is 2, return its position 3
#

"""
binary search
logn

8,9,1,2,3,4,5,6,7

l = 8
r = 7

   p = find_pivot_index(arr)
   binary_search(0, p) binary_search(p + 1, arr.length)

  M = 8
  6, 7, 8, 1, 2, 3, 4
  L     M        R

if M > R  and Target > M :

if M < L  and Target < M :
"""

def find_target(arr, target) :
    
    left = 0
    right = len(arr) - 1
    
    # 
    # 6, 7, 8, 1, 2, 3,
    # 8,9,1,2,3,4,5,6,7
    # m = 2, l = 8, r = 7 target is 5
    # 2 < 7 -> the right part is sorted
    #  if t > m && t < r -> move right else search left
    while left <= right :
        mid = (left + right) // 2
        
        if arr[mid] == target :
            return True
        
        if arr[mid] < arr[right] and target > arr[mid] and target < arr[right] :
            left = mid + 1
        else :            
            if arr[mid] < arr[right] :
                if target > arr[mid] and target < arr[right] :
                   left = mid + 1
                else :
                    right = mid -1
            else :
                if target > arr[left] and target < arr[mid] :
                    right = mid - 1
                else :
                     left = mid + 1







