words = "oolf folo oolf lfoo fool oofl fool loof oofl folo abr bra bar rab rba abr arb bar abr abr"
words = [word.strip() for word in words.split(" ")]

anagrams = {}

for word in words:
    sorted_word = ''.join(sorted(word))
    anagrams[sorted_word] = anagrams.get(sorted_word, []) + [word]

print anagrams
