"""
[  10   5    8    2    9     1     3     6    4 ]   ,  13

            1        2        3         4         5         6        8        9       10






"""

def k_sum_subset(v, target_sum) :
    pass

def main():
    v = [([8,13,3,22,17,39,87,45,36] , 3), ([8,13,3,22,17,39,87,45,36], 135), ([8,13,3,22,17,39,87,45,36], 270)]

    for i in range(len(v)) :
        print(i + 1, "list : ", v[i][0], sep = '')
        print(i + 1, "Target SUM : ", v[i][1], sep = '')
        subsets = k_sum_subset(v[i][0], v[i][1])
        print("  Subsets with Target Sum :", subsets)
        print("-"*100)

if __name__ == '__main__':
    main()
