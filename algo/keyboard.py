def make_trie(words):
    root = {}
    for word in words:
        trie = root
        for letter in word:
            if letter not in trie:
                trie[letter] = {}
            trie = trie[letter]
        if "_end_" not in trie:
            trie["_end_"] = "_end_"

    return root

def insert_word():
    trie = make_trie(["foo", "bar", "baz", "barz"])
    typed_so_far = "bar"

    for letter in typed_so_far:
        trie = trie[letter]

    if len(trie) == 2:
        for i in trie.keys():
            if i != "_end_":
                print i

        
print make_trie(["foo", "bar", "baz", "barz"])
insert_word()
