from math import log2, floor, pow

def extract_highest_bit(num) :
    highest_bit = 1 << ( floor(log2(num)) )
    return num & highest_bit

def highest_bit_position(num) :
    highest_bit = 1 << ( floor(log2(num)) )
    return floor(log2(num & highest_bit))

def extract_lowest_bit(num) :
    return num & ~(num - 1)

def main() :
    test_data = [ [18, 2],  [36 , 4], [16 , 16], [720, 16], [640, 128] ]

    for i, [num, expected] in enumerate(test_data) :
        print(i + 1, '\t', 'input number is ', num , ' binary : ' , bin(num))
        print(i + 1, '\t', 'lowest bit ', extract_lowest_bit(num), ' is as expected ' if extract_lowest_bit(num) == expected else 'is NOT as expected')
        highest_bit = floor(log2(num))
        print(i + 1, '\t', 'highest bit position ', highest_bit_position(num), ' is as expected ' if highest_bit_position(num) == floor(log2(pow(2, highest_bit))) else 'is NOT as expected')
        print(i + 1, '\t', 'highest bit ', extract_highest_bit(num), ' is as expected ' if extract_highest_bit(num) == num & 1 << highest_bit else 'is NOT as expected')
        print("_" * 30)

if __name__ == '__main__' :
    main()
