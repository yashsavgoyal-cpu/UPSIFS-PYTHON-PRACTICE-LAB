def double_result(func):
    def wrapper(*args):
        print("DOUBLED VALUE")
        print(func(*args)*2)
    return wrapper

@double_result
def add(a,b):
    return a+b

add(27,83)