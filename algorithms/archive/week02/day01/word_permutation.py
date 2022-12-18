def create_words(prefix, word) :
    if len(word) == 0 :
        return [prefix]

    if len(word) == 1 :
        return [prefix + word]

    result = []

    for i in range(len(word)) :
        result.extend(create_words(prefix + word[i] , word[:i] + word[i + 1:]))

    return result
 
def permute_word(word):
    result = []
    result.extend(create_words("", word))

    return result
