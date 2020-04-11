#program to take list of words and returns the longest word with size
s=['i','love','my','country','india']
d=''

for i in range(len(s)):
    if len(s[i])>len(d):
        d=s[i]
print('The longest string in list is:',d)
print('The length of the string is:',len(d))
