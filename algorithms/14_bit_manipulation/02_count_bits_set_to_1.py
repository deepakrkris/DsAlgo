def count_bits(num) :
    result = 0
    while num :
        if num & 1 :
             result += 1
        num = num >> 1
    
    return result

def main() :
    test_data = [ [10, 2] , [32000, 1] ]

    for i , [num , expected] in enumerate(test_data) :
        print(i + 1, '\t', ' number is ', num , ' bits are ', bin(num) )
        print(i + 1, '\t', ' result is ', count_bits(num) == expected)
        print("_" * 30)

if __name__ == '__main__' :
    main()
