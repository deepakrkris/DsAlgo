"""
Input: "123"
Output: "121"

Input: "1000"
Output: "999"

Input: "9077"
Output: "9009"

Input: "9000"
Output: "8998"

Input: "23456"
Output: "23432"

"""

def closest_palindrome(num: str) :
    num_digits = len(num)
    first_digit_place = pow(10, num_digits - 1)
    num_int = int(num)


