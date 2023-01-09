def swap_bits(num, i, j) :
    if num >> j != num >> i :
        left = 1 << j
        right = 1 << i
        mask = left | right

        print('mask is ', mask, 'in binary', bin(mask))

        num = num ^ mask

    return num

def main() :
    test_data = [ [ 720, 3, 7, 600 ] ]

    for i, [num, start, end, expected] in enumerate(test_data) :
        print(i + 1, '\t', 'input number is ', num , ' binary : ' , bin(num), 'swaping bits', start, 'and', end)
        print(i + 1, '\t', 'result ', swap_bits(num, start, end), ' is as expected ' if swap_bits(num, start, end) == expected else 'is NOT as expected')
        print("_" * 30)

if __name__ == '__main__' :
    main()
