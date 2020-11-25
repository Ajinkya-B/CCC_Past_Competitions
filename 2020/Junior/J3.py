num = int(input())
minX = 10000000
minY = 10000000
maxX = 0
maxY = 0

for i in range(num):
    line = list(map(int, input().split(",")))
    if line[0] > maxX:
        maxX = line[0]
    if line[1] > maxY:
        maxY = line[1]
    if line[0] < minX:
        minX = line[0]
    if line[1] < minY:
        minY = line[1]

print(str(minX-1) + "," + str(minY-1))
print(str(maxX+1) + "," + str(maxY+1))
