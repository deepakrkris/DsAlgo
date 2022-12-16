def merge(lst1, lst2) :
    result = []
    index1 = 0
    index2 = 0
    inv_count = 0

    while index1 < len(lst1) and index2 < len(lst2) :
        if lst1[index1] > lst2[index2] :
            result.append(lst2[index2])
            index2 += 1
            inv_count += 1
        else :
            result.append(lst1[index1])
            index1 += 1
    
    result.extend(lst1[index1 : ])
    result.extend(lst2[index2 : ])
   
    return inv_count, result

def divide_and_merge(lst) :
    if len(lst) <= 1 :
        return 0, lst
    
    mid = len(lst) // 2

    part1 = divide_and_merge(lst[ : mid])
    part2 = divide_and_merge(lst[mid : ])

    return merge(part1, part2)

def find_inversions(lst) :

    
