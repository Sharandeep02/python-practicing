s=['red','green','black']
d=[]
for i in range(len(s)):
    if s[i] not in d:
        d.append("@")
        d.append(s[i])
print(d)

