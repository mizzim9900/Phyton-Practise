print("Enter gender,service and Qulification:")
i=input("Gender=")
s=int(input("Service Year="))
q=input("Quilification=")
if i.capitalize()=="M" and s>=10 and q.capitalize()=="P":
    print("Salary=15000")
elif i.capitalize()=="M" and s>=10 and q.capitalize()=="G":
    print("Salary=10000")
elif i.capitalize()=="M" and s<10 and q.capitalize()=="P":
    print("Salary=10000")
elif i.capitalize()=="M" and s<10 and q.capitalize()=="G":
    print("Salary=7000")
elif i.capitalize()=="F" and s>=10 and q.capitalize()=="P":
    print("Salary=12000")
elif i.capitalize()=="F" and s>=10 and q.capitalize()=="G":
    print("Salary=9000")
elif i.capitalize()=="F" and s<10 and q.capitalize()=="P":
    print("Salary=10000")
else:
    print("Salary=6000")