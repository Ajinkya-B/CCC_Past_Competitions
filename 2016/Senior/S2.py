mthd = int(input())
num = int(input())
cnt = 0

g1 = list(map(int, input().split()))
g2 = list(map(int, input().split()))

if mthd == 1:
    g1.sort()
    g2.sort()
else:
    g1.sort()
    g2.sort(reverse=True)

for i in range(num):
    cnt += max(g1[i], g2[i])

print(cnt)