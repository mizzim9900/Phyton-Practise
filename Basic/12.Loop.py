a=["apple","orange","bannana"]
for i in a:
    print(i)
print("Break statement:")
for i in a:
    print(i)
    if(i == "orange"):
        break
print("Continue statement:")
for i in a:
    if(i == "orange"):
        continue
    print(i)
print("Range statement:")
for i in range(1,10,2):
    print(i)
print("Else statement:")
for x in range(6):
  print(x)
  if(x==4):
      break
else:
  print("Finally finished!")
print("Only else:")
for x in range(1,10,5):
  print(x)
else:
  print("Finally finished!")
print("Star print:")
for i in range(5):
    print("*"*i)
