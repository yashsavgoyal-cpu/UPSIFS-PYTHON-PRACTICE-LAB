#WAF to return the factorial of a number
def fact(n):
    f=1
    for i in range(n,0,-1):
        f*=i
    print(f)

fact(5)
