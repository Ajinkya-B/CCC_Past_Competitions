needle = str(input())
haystack = str(input())
count = 0
done = []


def str_sort(s):
    s = "".join(sorted(list(s)))
    return s


needle_s = str_sort(needle)

for i in range(len(haystack)-len(needle)+1):
    temp = haystack[i:i+len(needle)]
    temp_s = str_sort(temp)

    if temp_s == needle_s and temp not in done:
        count += 1
        done.append(temp)

print(count)
