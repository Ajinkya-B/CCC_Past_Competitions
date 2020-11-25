data = list
prev_num = None
crt_num = None
msg = "magic"

for i in range(4):
    line = list(map(int, input().split()))
    crt_num = sum(line)
    if prev_num is not None and prev_num != crt_num:
        msg = "not magic"
        break
    prev_num = crt_num

print(msg)
