def find_char(input):
    count = {}

    for i, char in enumerate(input):
        count_so_far = count.get(char, (0, 0))[0]
        count[char] = (count_so_far+1, i)

    min_pos = len(input)
    min_char = None
    
    for char, value in count.items():
        c, p = value
        if c == 1 and p < min_pos:
            min_pos = p
            min_char = char

    return min_char

print find_char("AABBC")
print find_char("AABBCCDEEFF")
