def remove_bits(num, i, j) :

    j_bits = (1 << j + 1) - 1
    left_of_j_bits = j_bits << j + 1
    right_of_i_bits = (1 << i) - 1

    mask = left_of_j_bits | right_of_i_bits
    print(bin(mask))

    return num & mask

def main() :
    test_data = [ [48 , 3, 4, 32], [720, 3, 8, 512] ]

    for i, [num, start, end, expected] in enumerate(test_data) :
        print(i + 1, '\t', 'input number is ', num , ' binary : ' , bin(num), 'removing bits', start, 'to', end)
        print(i + 1, '\t', 'result ', remove_bits(num, start, end), ' is as expected ' if remove_bits(num, start, end) == expected else 'is NOT as expected')
        print("_" * 30)

if __name__ == '__main__' :
    main()
