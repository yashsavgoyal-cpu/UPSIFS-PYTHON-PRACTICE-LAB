def show_info(func):
     def wrapper(*args):
        print("THE INFO:")
        func(*args)
        print("========")
     return wrapper

def sqr(num):
    print(num*num)
@show_info
def sqr(num):
    print(num*num)

sqr(5)