def find_repeated_sequences(s, k) :
    left = 0
    right = k - 1
    tracker = {}
    result = set()
   
    while right < len(s) :
        if s[left : right + 1] in tracker :
            result.add(s[left : right + 1])
        else :
            tracker[s[left : right + 1]] = True
        right += 1
        left += 1

    return result

def main():
    inputs_string = ["ACGT", "AGACCTAGAC", "AAAAACCCCCAAAAACCCCCC", "GGGGGGGGGGGGGGGGGGGGGGGGG",
                     "TTTTTCCCCCCCTTTTTTCCCCCCCTTTTTTT", "TTTTTGGGTTTTCCA",
                     "AAAAAACCCCCCCAAAAAAAACCCCCCCTG", "ATATATATATATATAT"]
    inputs_k = [3, 3, 8, 12, 10, 14, 10, 6]

    for i in range(len(inputs_k)):
        print(i+1, ".\tInput Sequence: \'", inputs_string[i], "\'", sep="")
        print("\tk: ", inputs_k[i], sep="")
        print("\tRepeated Subsequence: ",
              find_repeated_sequences(inputs_string[i], inputs_k[i]))
        print("-"*100)


if __name__ == '__main__':
    main()
