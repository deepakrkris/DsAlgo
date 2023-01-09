def drop_lowest_bit(num) :
    return (num & num - 1)


def main() :
    test_data = [ [101 , 100] , [1010 , 1008 ] ]

    for i, [num, expected] in enumerate(test_data) :
        print(i + 1, '\t', 'input number is ', bin(num))
        print(i + 1, '\t', 'result is ', bin(drop_lowest_bit(num)) == bin(expected))
        print("_" * 30)

if __name__ == '__main__' :
    main()
