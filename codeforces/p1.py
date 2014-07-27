n = int(raw_input())
s = raw_input()

ip = ["vaporeon", "jolteon", "flareon", "espeon", "umbreon", "leafeon", "glaceon", "sylveon"]
ip_n = 8
match = [0]*8
max = 0
max_i = 0

for id, char in enumerate(s):
    if char == '.':
        continue
    else:
        for i in range(8):
            try:
                if ip[i][id] == char:
                    match[i] += 1
                if match[i] > max:
                    max = match[i]
                    max_i = i
            except:
                pass

print ip[max_i]
