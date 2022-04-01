txt1="mark allen"
print(txt1.capitalize())
txt2="ALL I NEED"
print(txt2.casefold())
txt3="zim"
print(txt3.center(10,"@"))
txt4="i am 23 years old"
print(txt4.count("23",4,10))
txt5 = "My name is Ståle"
print(txt5.encode(encoding="ascii",errors="ignore"))
txt6="welcome to my world."
print(txt6.endswith("."))
txt7="z\ti\tm"
print(txt7.expandtabs(20))
print(txt3.find("i"))
txt8="My car is very {},it is around {} dollar".format("expensive","3k")
print(txt8)
print(txt8.index("car"))
print (txt8.isalnum()) #here some space in txt8
print(txt3.isalpha())  #here is no space and number
print(txt3.isdecimal())#here is no decimal number
txt9="12234"
print(txt9.isdigit())
print(txt3.islower()) #here all the character at lower case
print(txt3.isupper()) #here all the character is not upper case
print(txt5.isspace()) #here not only space 
print(txt6.istitle()) #turn tne first character of any word into upper case
txt10=("you", "are" ,"my","love")
a="-".join(txt10)
print(a)
txt11="*****zim"
a1=txt11.lstrip("*")
print(a1)
txt12="i brush my teeth everyday"
a3=txt12.partition("teeth")
print(a3)
txt13="i love my car"
a4=txt13.replace("car","bike")
print(a4)
txt14="apple,orange,mango"
a5=txt14.split(",")
print(a5)
txt15="good"
print(txt15.swapcase())
print(txt15.upper())