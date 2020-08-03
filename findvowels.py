vowels = ['a','e','i','o','u']
s=input("Enter string: ")
i=0
v=0
while i<len(s):
    c=s[i]
    i+=1
    try:
        v = int(vowels.index(c)>=0)+v
    except ValueError:
        v=v
print(f'The string contains {v} vowels')


