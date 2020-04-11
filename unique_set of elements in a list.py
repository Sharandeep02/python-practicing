#python program to have a unique set of elements in a list
s=[5,2,5,6,1,4,3,5,3,5,4,9,2,3,4,5,6,2,9,0,1,7]
d=[]
for i in range(len(s)):
    if s[i] not in d:
        d.append(s[i])
print(d)
