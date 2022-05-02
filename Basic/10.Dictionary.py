print("Make a dictoanry:")
dict1={}
for i in range(2):
    l = int(input("keys:"))
    j = input("value:")
    dict1.update({l:j})
print(dict1)
print(type(dict1))
dict={101:"Course1",102:"Course2",103:"Course3"}
dict[104]="Course4"
print(dict)
x=dict.keys()
y=dict.values()
z=dict.items()
print(x,"\n",y,"\n",z)
dict[104]="Course99"
print(dict)
dict.popitem()
print(dict)
del dict[101]
print(dict)
dict.clear()
print(dict)
a=("201","202","203")
b=("w","e","t")
dict2=dict.fromkeys(a,b)
print(dict2)
print(type(dict2))
my={
    "emp1" : {
        "name1" : "zim",
        "age" : 23
    },
    "emp2" : {
        "name2" : "niloy",
        "age" : 22
    }
}
print(my)