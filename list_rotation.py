
s=[7,8,120,25,44,20,27]
n=int(input('enter no of rotations:'))
print(s[0:len(s)-1])
print(s[len(s)-1:])
for i in range(n):
    s=s[len(s)-1:]+s[0:len(s)-1]
print(s)

