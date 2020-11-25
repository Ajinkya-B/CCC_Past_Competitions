needle = str(input())
hay = str(input())
l_n = len(needle)
l_h = len(hay)

cnt = 0
done = []

count = {}


for char in needle:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1


for i in range(l_h - l_n + 1):
    wrong = False
    temp_count = count.copy()
    temp = hay[i:i+l_n]

    if temp not in done:
        done.append(temp)

        for char in temp:
            if char in temp_count:
                temp_count[char] -= 1

        for i in temp_count:
            if temp_count[i] != 0:
                wrong = True

        if not wrong:
            cnt += 1

print(cnt)
