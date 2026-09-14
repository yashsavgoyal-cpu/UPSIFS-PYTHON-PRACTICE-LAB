#1 string performing operations on a string

s=input("ENTER STRING")
print(s.upper())
print(s.lower())
print(s[::-1])
l=['a','e','i','o','u']
v=0
for i in s:
    if i.lower() in l:
        v+=1
print("THE NUMBER OF VOWELS:",v)

#2 string count the frequency of words

t=input("ENTER STRING")
d={}
word=""
for i in t:
   if i==" ":
       if word in d:
           d[word]+=1
       else :
            d[word]=1
       word=""
       continue
   else:
        word+=i
for k,v in d.items():
    print(k,":",v)
  
   

#1 list return 4th and 5th element

l=eval(input("ENTER LIST OF 5 FRUITS"))
print(l[1])
print(l[3])
l[-1]="MANGO"
print(l)

#2 list return sum and average

l1=eval(input("ENTER LIST OF POSITIVE NUMBERS"))
sum=0
for i in l1:
    sum+=i
print("SUM=" ,sum)
print("AVERAGE=",sum/len(l1))

#4 return max and min element 

l2=eval(input("ENTER LIST OF NUMBERS"))
l2.sort()
print("MAX: ",l2[len(l2)-1])
print("MIN: ",l2[0])

        
        
