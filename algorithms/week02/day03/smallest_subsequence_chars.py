from collections import defaultdict

def get_shortest_unique_substring(arr, str):
    # iterate index from 0 to len(str) - 1
    #   find a match within range indexx to len(str) - 1
    #    if a match found in arr, remove it from arr
    # if list is empty 
    
    # "xyyzyzyx" , ["x", "y", "z"]
    # N^2

    """
    is O(N) possible ?
    what if the index is just a sliding window ?
    within a window if there is a smaller window how to find it ?
    """
    countMap = {}
    uniqueCounter = 0
    left = 0
    minLength = float('inf')
    result = ""

    for c in arr :
        countMap[c] = 0

    for index in range(len(str)) :

        if str[index] in countMap :
            countMap[str[index]] += 1
    
        if countMap[str[index]] == 1 :
            uniqueCounter += 1
    
        while uniqueCounter == len(arr) :

            if (minLength > len(str[left : index + 1])):
                result = str[left : index + 1]
                minLength = len(result)

            if str[left] in countMap :
                countMap[str[left]] -= 1
                if countMap[str[left]] == 0 :
                    uniqueCounter -= 1
        
            left = left + 1

    return result, minLength

print(get_shortest_unique_substring(["x", "y", "z"], "xyyzyzyx"))
