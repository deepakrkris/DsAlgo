#
# search in a sorted array with rotation/circular {8,9,1,2,3,4,5,6,7} -> the target is 2, return its position 3
#
"""
binary search
logn

0   1   2   3   4   5   6   7   8
5   6,  7,  8,  9,  1,  2,  3,  4

if M > R and T < R :
    move window to right
if M > R and T > R :
    move window to left
if M < R and T < M :
    move window to left
if M < R and T > M and T < R :
    move window to right
if M < R and T > M and T > R :
    move window to left
"""
def find_target(arr, target) :
    
    left = 0
    right = len(arr) - 1

    while left <= right :
        mid = (left + right)//2
 
        if arr[mid] == target :
            return mid
        if arr[mid] > arr[right] :
            if target <= arr[right] :
                left = mid + 1
            else :
                right = mid - 1 
        else :
            if target < arr[mid] :
                right = mid - 1
            elif target <= arr[right] :
                left = mid + 1
            else :
                right = mid - 1

    return -1

test_data = [ [5,  6,  7,  8,  9,  1,  2,  3,  4],
              [8,  9,  1,  2,  3,  4,  5,  6,  7]
            ]


for i , t in enumerate(test_data) :
    print(i + 1, './t', 'test data is ', t)
    print(find_target(t, 2))
    print("_" * 30)
