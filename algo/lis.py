arr = [1, 6, 3, 5, 9, 7]

ans = [1]

for i in range(1, len(arr)):
    t = []
    for j in range(i):
        if arr[i] > arr[j]:
            t.append(ans[j]+1)
        else:
            t.append(ans[j])

    ans.append(max(t))

print max(ans)
