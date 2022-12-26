"""

1445  ->  5144 4514 4451

"""

def num_rotations(num) :

    num_digits = len(str(num))
    first_digit_place = pow(10, num_digits - 1)
    count = num_digits - 1

    result = []

    while count > 0 :
        last_digit = num % 10
        num = num // 10
        num += last_digit * first_digit_place
        result.append(num)
        count -= 1

    return result

print(num_rotations(1445))
