def validate(str1, str2, str3):
    pos_a = 0
    pos_b = 0

    for i in str3:
        if pos_a < len(str1) and str1[pos_a] == i:
            pos_a += 1
        elif pos_b < len(str2) and str2[pos_b] == i:
            pos_b +=1
        else:
            return False

    return True

print validate("abc", "def", "dabecf")
