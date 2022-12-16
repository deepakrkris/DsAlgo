def word_break(s, word_dict):
    
    result = []

    def split(prefix, split_prefix) :

        if len(prefix) == 0 :
            result.append(split_prefix.strip())
            return

        for i in range(1, len(prefix) + 1) :
            if prefix[:i] in word_dict :
                split(prefix[i:], split_prefix + prefix[:i] + ' ')
                print(prefix[:i])

    split(s, "")

    return result

def word_break_memoize(s, word_dict):
    memo = {}

    def split(prefix) :

        if len(prefix) == 0 :
            return ['']

        if prefix in memo :
            return memo[prefix]

        res = []

        for i in range(1, len(prefix) + 1) :
            if prefix[:i] in word_dict :
                suffixes = split(prefix[i:])
                for s in suffixes :
                    res.append((prefix[:i] + ' ' + s).strip())

        memo[prefix] = res

        return res

    return split(s)

print(word_break("catsanddogs", ["cat", "cats", "and", "sand", "dogs"]))
print(word_break_memoize("catsanddogs", ["cat", "cats", "and", "sand", "dogs"]))