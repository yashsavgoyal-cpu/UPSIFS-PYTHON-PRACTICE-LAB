#WAF to add an entry into a dictionary
def add_entry(d):
    k=input("ENTER KEY")
    v=int(input("ENTER VALUE"))
    d[k]=v
    print(d)

#WAF to to reassign a dictionary varibles to a new dictionary
def reassign_dict(d):
    d2={}
    for k,v in d.items():
        d2[k]=v
    print(d2)

add_entry({"Y":18,"A":7,"S":11})
reassign_dict({"Y":18,"A":7,"S":11})
