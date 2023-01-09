
def prefix_function(pattern : str) :
    n = len(pattern)
    f = [0] * n
    k = 0

    for i in range(1, n) :
        print("suffix boundary ", i, pattern[i])
        while pattern[k] != pattern[i] and k > 0 :
            print("backing off to ", str(f[k-1]), " from pos ", str(k), pattern[k], " for suffix ", i, pattern[i])
            k = f[k-1]
        if pattern[k] == pattern[i] :
            k += 1
        print("max boundary is ", k, "at suffix positiom ", i)
        f[i] = k
    return f

print(['' + str(c) + '' for c in prefix_function("ABABAC") ])
print('', ['' + str(c) + '' for c in list("ABABAC")] )


def kmp_dfa(pattern : str) :
    # dfa[i][j] = k denotes the transition function will go k'th state 
    # with character i from state j
 
    M = len(pattern)
    Z = ord('A')
    R = abs(Z - ord('C')) + 2
 
    print(R)

    def char_code (c) :
        return abs(Z - ord(c))

    print(char_code('A'))

    dfa = [ [ 0 ] * M for _ in range(R) ]

    # DFA will go always (i + 1)'th state from i'th state 
    # if the character c is equal to current character of pattern 
    dfa[char_code( pattern[0] )][0] = 1

    # here X is initialized with LPS (longest prefix suffix) 
    # of pattern[0....j - 1]. LPS[0] is always 0
    X = 0
    for j in range(1, M) :
        for c in range(R) :  # for all possible characters
            # transition function from j'th state taking character c 
            # will go to the same state where it went from X(LPS)'th state
            # taking character c (justify it with an example) 
            dfa[c][j] = dfa[c][X]
        # DFA will go always (i + 1)th state from i'th state if 
        # the character c is equal to current character of pattern
        dfa[char_code (  pattern[j] )][j] = j + 1
        X = dfa[char_code (  pattern[j] )][X] # update LPS

    return dfa

out = kmp_dfa("ABABAC")

chars = ['A', 'B', 'C', ' ']

print('  j  ', ['' + str(c) + '' for c in [0, 1, 2, 3, 4, 5]] )

print('     ', [c for c in list("ABABAC")])

for i , r in enumerate(out) :
    print(chars[i], '   ',  ['' + str(c) + '' for c in r] )
