"""
check if two strings are rotations of each other

waterbottle ,
   erbottlewat

ddpa
  padd

jar, 
  rja

1234,
   4123

"""

def is_rotation(s1, s2) :
    if len(s1) != len(s2) :
        return False
    
    s = s1 + s1
    s1_index = 0
    s2_index = 0

    while s1_index < len(s) :
        if s[s1_index] != s2[s2_index] :
            s2_index = 0
        else :
            s2_index += 1
        s1_index += 1
    
    if s2_index == 0 :
        return False

    print(s1[0 : len(s1) - s2_index] , s2[s2_index  : ])

    if s1[0 : len(s1) - s2_index] == s2[s2_index  : ] :
        return True
    
    return False


test_data = [  
    [ "waterbottle" , "erbottlewat" ],
    [ "abaabbaaab", 
               "abbaaababa" ],
    [ "dogma", "dogma" ],
]

for i, t in enumerate(test_data) :
    print(i + 1, './t', 'test data ', t)
    print('result ', is_rotation(t[0], t[1]))
    print('_' * 30)
