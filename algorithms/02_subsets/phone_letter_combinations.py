Number_Map = {
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz"
}


"""
   9          2     3
  wxyz       abc   def
"""
def letter_combinations(digits) :
    if len(digits) == 0 :
        return [""]

    first_digit = int(digits[0:1])
    result = []

    for letter in Number_Map[first_digit] :
        c_lst = letter_combinations(digits[1:])
        for c in c_lst :
            result.append(letter + c)

    return result

def main():
    digits_array = ["2", "73", "426", "78", "925", "2345"]
    counter = 1
    for digits in digits_array:
        print(counter, ".\t All letter combinations for '",
              digits, "': ", letter_combinations(digits), sep="")
        counter += 1
        print("-" * 100)

if __name__ == "__main__":
    main()