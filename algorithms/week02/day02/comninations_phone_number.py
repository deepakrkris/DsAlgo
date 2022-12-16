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

def generate_suffix(digits, index) :
    if index == len(digits) :
        return ['']

    result = []
    suffixes = generate_suffix(digits, index + 1)
    code = Number_Map[int(digits[index])]

    for i in range(len(code)) :
        for s in suffixes :
            result.append(code[i] + s)
    return result

def letter_combinations(digits):
    
    """
      23 
       - abc * def 
       a - d , e , f
       b - d , e , f
       c - d , e , f
    """

    return generate_suffix(digits, 0)

# Use backtrack function to generate all possible combinations
def backtrack(index, path, digits, letters, combinations):
    # If the length of path and digits is same,
    # we have a complete combination
    if len(path) == len(digits):
        s = ""
        s = s.join(path)
        combinations.append(s)
        return  # Backtrack
    # Get the list of letters using the index and digits[index]
    possible_letters = letters[digits[index]]
    if possible_letters:
        for letter in possible_letters:
            # Add the letter to our current path
            path.append(letter)
            # Move on to the next category
            backtrack(index + 1, path, digits, letters, combinations)
            # Backtrack by removing the letter before moving onto the next
            path.pop()


def letter_combinations(digits):
    combinations = []
    
    # If the input is empty, immediately return an empty answer array
    if len(digits) == 0:
        return []

    #  Mapping the digits to their corresponding letters
    digits_mapping = {
        "1": [""],
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]}

    # Initiate backtracking with an empty path and starting index of 0

    backtrack(0, [], digits, digits_mapping, combinations)
    return combinations
