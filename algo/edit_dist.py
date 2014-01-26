def edit_distance(word1, word2):
    len1 = len(word1)
    len2 = len(word2)

    table = [[0]*(len2+1) for i in range(len1+1)]
    
    for i in range(len1+1):
        table[i][0] = i

    for j in range(len2+1):
        table[0][j] = j
    
    for i in range(1, len1+1):
        for j in range(1, len2+1):
            diag = 0 if word1[i-1] == word2[j-1] else 1
            table[i][j] = min([table[i-1][j-1]+diag,
                              table[i-1][j]+1,
                              table[i][j-1]+1])

    return table[len1][len2]

print "cat", "bat", edit_distance("cat", "bat")
print "cat", "catt", edit_distance("cat", "catt")
print "bat", "catt", edit_distance("bat", "catt")            
