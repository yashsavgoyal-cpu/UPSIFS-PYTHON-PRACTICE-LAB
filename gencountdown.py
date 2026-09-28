def  countdown(n):
    while n>0:
        yield n
        n-=1

num=int(input("ENTER NUMBER"))
counter=countdown(num)

lim=int(input("TILL WHEN YOU WANT TO COUNTDOWN"))
while True:
    value = next(counter)

    if value < lim:
        break

    print(value)