def goat_latin(ip):
    ans = []
    vowels = ['e', 'i', 'a', 'o', 'u']
    
    for id, i in enumerate(ip.split(' ')):
        word = ""
        if i[0].lower() in vowels:
            word += i
        else:
            word += i[1:]+i[0]
        word += "ma"
        word += 'a'*(id+1)
        ans.append(word)

    return ' '.join(ans)

def goat_latin_using_list(ip):
    ans = []
    vowels = ['e', 'i', 'a', 'o', 'u']
    
    for id, i in enumerate(ip.split(' ')):
        word = []
        i = list(i)
        if i[0].lower() in vowels:
            word.extend(i)
        else:
            word.extend(i[1:])
            word.append(i[0])

        word.extend(["m", "a"])
        word.extend(['a']*(id+1))
        ans.append(''.join(word))

    return ' '.join(ans)

text = "Such wow Much fancy ate"
print goat_latin(text)
assert(goat_latin(text) == goat_latin_using_list(text))
