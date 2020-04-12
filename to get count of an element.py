#program to check number of occurance of a element in list
s=[3,4,5,3,4,5,6,7,3,5,6,6,5,7,2,3,4,5,6]
x=int(input("enter a number to check no of occurances :"))
count=0
for i in s:
    if i==x:
        count+=1
print("{} has occured {}times in the list".format(x,count))
#we have count method for returning the count of occurance of an element
print(s.count(3))
