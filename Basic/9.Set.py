print("Take a set:")
s1=set()
for i in range(3):
    s1.add(int(input()))
print(s1)
s10=s1.copy()
print(s10)
s2={"samsung","nokia","xiaomi"}
s3={"good","best","better"}
s2.add("apple")
print(s2)
s2.update(s3)
print(s2)
s2.remove("good")
print(s2)
s2.discard("best")
print(s2)
x=s2.pop()
print(x)
print(s2)
s2.clear()
print(s2)
s4={"10","20","30"}
s5={"10","40","50"}
x1=s4.union(s5)
print(x1)
x2=s4.intersection(s5)
print(x2)
x3=s4.symmetric_difference(s5)
print(x3)
x4=s4.difference(s5)
print(x4)
s6={"1","2"}
s7={"1","2","3","4"}
x5=s6.issubset(s7)
print(x5)
x6=s6.issuperset(s7)
x7=s7.issuperset(s6)
print(x6,x7)
for l in s1:
    print(l)