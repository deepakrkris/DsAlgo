def find_bitwise_complement(num):
    all_bits_set = ~0
    return num ^ all_bits_set

def operations(num1, num2) :
    print('\t', num1 , 'in binary', bin(num1))
    print('\t', num2 , 'in binary', bin(num2))
    print('\t', ' = bits complement of num1 ' , ~num1 , 'in binary', bin(~num1))
    print('\t', ' = bits complement of num2 ' , ~num2 , 'in binary', bin(~num2))
    print('\t', ' = 2\'s complement of num1 ' , find_bitwise_complement(num1) + 1 , 'in binary', bin(find_bitwise_complement(num1) + 1))
    print('\t', ' = 2\'s complement of num2 ' , find_bitwise_complement(num2) + 1 , 'in binary', bin(find_bitwise_complement(num2) + 1))
    print('\t', ' = AND ' , num1 & num2, 'in binary', bin(num1 & num2))
    print('\t', ' = OR ' , num1 | num2, 'in binary', bin(num1 | num2))
    print('\t', ' = XOR ' , num1 ^ num2, 'in binary', bin(num1 ^ num2))

def main() :
    test_data = [ [ 0 , 1 ] ,  [ 1 , 1 ] ,  [ 2 , 4 ] ,  [ 8 , 8 ] , [ 8 , 4 ] ]

    for i, [num1, num2] in enumerate(test_data) :
        print(i + 1, '\t', 'input numbers are ', num1, num2)
        operations(num1, num2)
        print("_" * 30)

if __name__ == '__main__' :
    main()
