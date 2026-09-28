def evennums(n):
    while True:
        if(n%2==0):
            yield n
        n+=1

n=int(input("ENTER NUMBER "))
lim=int(input("ENTER THE LIMIT "))

even=evennums(n)
value=next(even)

while value<lim:
    print(value)
    value=next(even)

