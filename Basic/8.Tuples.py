print("Create a tuple:\n")
a=[]
for i in range(5):
    a.append(input())
b=tuple(a)
print(b)
c=('6','7','8')
d=('9','10')
sum=c+d
print(sum)
l1=list(c)
l1.append("999")
c=tuple(l1)
print(l1)
l2=list(d)
l2[0]="999"
d=tuple(l2)
print(d)
print(c[2])
x=c.count(999)
y=c.index(7)
print(x)
print(y)