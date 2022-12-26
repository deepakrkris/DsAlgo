
"""
2, 5, 7
      2  
      2, 5
      2, 7
      2, 5, 7
      5
      5, 7
      7
"""
def find_all_subsets(v, size) :
    print("iteration   ", size - len(v), v)

    result = [[]] 

    if len(v) == 0 :
        return result

    for i in range(len(v)) :
        combined = find_all_subsets(v[i+1 : ], size)
        for s in combined:
            s.append(v[i])
        result.extend(combined)

    return result

def main():
    v = [[], [2, 5, 7], [1, 2], [1, 2, 3, 4], [7, 3, 1, 5]]

    for i in range(len(v)):
        print(i + 1, ". Set: ", v[i], sep='')
        subsets = find_all_subsets(v[i], len(v[i]))
        print("   Subsets:", subsets)
        print("-"*100)

if __name__ == '__main__':
    main()
