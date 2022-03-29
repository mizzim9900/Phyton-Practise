s="Md Sadikul Hasan Zim"
print("Cut=",s[1])
print("String Length:",len(s))
print("Zim" in s)
#Slicing String
print(s[3])
print(s[3:])
print(s[3:8])
print(s[:16])
print(s[-9:-4])
#Concatanation of string
a="Hello"
b="World"
print(a + " " + b)
#format string
a,b="name","zim"
data="My {} is {}"
i,j="am","23"
data1="i {0} {1} years old"
print(data.format(a,b))
print(data1.format(i,j))
data2="i {1} {0} years old"
print(data2.format(i,j))
#Semicoloum
txt = "We are the so-called \"Vikings\" from the north."
print(txt)
#Repetative string
print("zim "*5)