pop = int(input())
init = int(input())
spread = int(input())

infect = init

i = 1
while infect <= pop:
    infect += spread**i * init
    i += 1

print(i)
