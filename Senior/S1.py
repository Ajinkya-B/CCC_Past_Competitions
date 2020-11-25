num = int(input())
pos = []
hSpeed = 0
c = 0

for i in range(num):
    line = list(map(int, input().split()))
    pos.append(line)


for i in range(num):
    for j in range(num):
        if i != j:
            t1 = pos[i][0]
            t2 = pos[j][0]
            d1 = pos[i][1]
            d2 = pos[j][1]

            speed = abs(d2-d1)/abs(t2-t1)
            if speed > hSpeed:
                hSpeed = speed

print(hSpeed)
