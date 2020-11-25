dep = input()
hour, minute = dep.split(':')
dep = int(hour) * 60 + int(minute)
arrival = int(dep)
factor = 0

for i in range(dep, dep + 120):
    if 420 <= arrival < 600:
        arrival += 2
    elif 900 <= arrival < 1140:
        arrival += 2
    else:
        arrival += 1

    if arrival == 1440:
        arrival = 0

while arrival >= 60:
    arrival -= 60
    factor += 1
    if arrival < 60:
        break

minute = arrival
if factor < 10:
    factor = '0' + str(factor)

if minute < 10:
    minute = '0' + str(minute)

print(str(factor) + ":" + str(minute))