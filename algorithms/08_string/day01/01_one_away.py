"""
One Away

given 2 strings find if they have only one edit difference,
an edit is an insert or delete or replace of a character

pale , ple    true -> one delete
pale , bale   true -> one replace
pale , spale  true -> one insert
pale , bales  false -> two edits
"""

"""

if abs(len_s1 - lens2) <= 1
    match for all chars s1 and s2 except one   

"""

def is_str_one_away(s1, s2) :

    diff = abs(len(s1) - len(s2))

    if diff > 1 :
        return False

    if len(s2) > len(s1) :
        s1, s2 = s2, s1

    s1_index = 0
    s2_index = 0
    found_diff = False

    while s1_index < len(s1) :
        change_flag = False
        if s1[s1_index] != s2[s2_index] :
            print(diff, s1_index, s2_index)
            if found_diff :
                return False

            found_diff = True
            change_flag = True

        if change_flag and diff == 1 :
               s1_index += 1
        else :
            s1_index += 1
            s2_index += 1 

    return True

def main() :
    test_data = [ [ "pale", "ple" ] , [ "pale", "bale" ] , [ "pale", "spale" ] , [ "pale", "bales" ] ]

    for i, t in enumerate(test_data) :
        print(i + 1, './t', 'Test data is ', t)
        print('result is ', is_str_one_away(t[0], t[1]))
        print("-" * 30)


if __name__ == "__main__" :
    main()
