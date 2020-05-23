#Given input String of combination of the lower and upper case ,arrange characters in such a way that all lowercase letters should come first.

a=list(input())
b: str=""
c=[]
d=[]
for i in range(len(a)):
    if a[i].islower():
        b+=a[i]
        c.append(i)
for j in range(len(a)):
    if j not in c:
        d.append(a[j])
print(b+"".join(d))
