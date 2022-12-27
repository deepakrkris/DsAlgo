"""
Given a string, input_string find the longest substring without repeating characters, and return the length of that longest substring.

1 ≤ input_string.length ≤ 5 × 10^4

input_string consists of English letters, digits, symbols, and spaces.

abcdea => abcde
abcbda => abcd
abcbafcde => bafcde  

"""

def longest_subs(input) :
  char_last_seen = {}
  window_left = 0
  window_right = 0
  max_window = ""
  max_window_size = 0

  for c in input :
    char_last_seen[c] = -1

  while window_right < len(input) :
    current_char_last_seen = char_last_seen[input[window_right]]
    if current_char_last_seen > window_left :
        window_left = current_char_last_seen + 1
    substr = input[window_left : window_right]
    if len(substr) > max_window_size :
      max_window = substr
      max_window_size = len(max_window)
    char_last_seen[input[window_right]] = window_right
    window_right += 1

  return max_window

def main() :
  test_data = [ "abcdea", "abcdba", "abcbafcde" ]

  for i , input in enumerate(test_data) : 
    print(i + 1, ". \t Input String: ", input, sep="")
    print("longest substring non repeating chars", longest_subs(input))
    print("-" * 30)

if __name__ == "__main__" :
  main()
