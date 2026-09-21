#WAF remove_last(L) that removes the last element of the list
def remove_last(l):
    l.pop(-1)
    print(l)

remove_last([1,4,3,5,6,3])
