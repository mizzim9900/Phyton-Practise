print("Data type changing:")
a=2
b=2.3
c=2J
x=int(b)
y=float(a)
z=complex(a)
print("X=",x,type(x))
print("Y=",y,type(y))
print("Z=",z,type(z))
print("Make all different data to one data type:")
#for integer
i=int(2.3)                  #float to integer
j=int("4")                  #string to integer
print("I=",i,type(i))
print("J=",j,type(j))
#for float
c1=float(2)                 #integer to float
c2=float("4")               #string to float
print("C1=",c1,type(c1))
print("C2=",c2,type(c2))
#for string
s1=str(2)                   #integer to string
s2=str(2.4)                 #float to string
print("S1=",s1,type(s1))
print("S2=",s2,type(s2))