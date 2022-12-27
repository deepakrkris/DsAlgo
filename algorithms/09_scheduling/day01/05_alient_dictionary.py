from collections import defaultdict, Counter

def alien_order(words):
    adj_list = defaultdict(set)
    print("\n\tGetting unique characters")
    counts = Counter({c: 1 for word in words for c in word})
    print("\t\t", counts, sep="")


def main():
    words = [
        ["mzosr", "mqov", "xxsvq", "xazv", "xazau", "xaqu",
            "suvzu", "suvxq", "suam", "suax", "rom", "rwx", "rwv"],
        ["vanilla", "alpine", "algor", "port",
            "norm", "nylon", "ophellia", "hidden"],
        ["passengers", "to", "the", "unknown"],
        ["alpha", "bravo", "charlie", "delta"],
        ["jupyter", "ascending"]]

    for i in range(len(words)):
        print(i + 1, ".\twords = ", words[i], sep="")
        print("\tDictionary = \"", alien_order(words[i]), "\"", sep="")
        print("-"*100)


if __name__ == "__main__":
    main()
