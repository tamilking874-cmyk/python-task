#upper and lower

a="TAMILARASAN"
print(a.lower())
print(a.casefold())


b="tamilarasan"
print(b.upper())

#Swapcase
a="TAMILARASAN"
print(a.casefold())
b="tamilarasan"
print(a.capitalize())

#capitalize
c="tamilarasan is learning python"
print(c.capitalize())

#Startswith

d="Python"
print(d.startswith('t'))
print(d.startswith('T'))

#Endswith
a="Python"
print(a.endswith('on'))
print(a.endswith('py'))

#Replace

a="tamilarasan is learning java"
print(a.replace('java','python'))

#strip
a="         tamilarasan          "
print(a.strip())
print(a.lstrip())
print(a.rstrip())


#Formatting Methods
#Format

a="Tamilarasan"
b="29"
c="Dharmapuri"
print(f" My name is {a}, I am {b} years old and I live in {c}")

a=str(input("name:"))
b=int(input("age:"))
c=str(input("city:"))
print(f" My name is {a}, I am {b} years old and I live in {c}")

#Center
a="Tamilarasan"
print(a.center(29))
print(a.center(29,'*'))

#Ljust
a="gopika"
print(a.ljust(29,'*'))

#rjust
a="tamilarasan"
print(a.rjust(29,'*'))

#Zfill

a="5"
print(a.zfill(6))


#Checking Methods
#Isdigit
a="1234abc"
b="abcd"
c="1234"
print(a.isdigit())
print(b.isdigit())
print(c.isdigit())

#Isalpha
a="1234abc"
b="abcd"
c="1234"
print(a.isalpha())
print(b.isalpha())
print(c.isalpha())

#Isascii
a="1234abc"
b="abcd"
c="1234"
print(a.isascii())
print(b.isascii())
print(c.isascii())

#Combined Tasks
#17
a="tamilarasan is learning python  "
print(a.strip())
print(a.capitalize())
print(a.startswith('A'))

#18
a="python2006"
print(a.isascii())
print(a.endswith('py'))
print(a.isalpha())
print(a.isdigit())


#19
a="6382258883"
print(a.isdigit())
print(a.zfill(16))


#20
a="tamilarasan is learning python"
print(a.upper())
print(a.replace(' ','-'))
print(a.split())

#For-else Task

for i in range (1,6):
    print(i)
else:
    print("loop completed")


for i in range (1,11):
    if i%2==0:
        print(i)


numbers=[1,2,3,4,5]
for i in numbers:
    if i==5:
        print("found")
        break
else:
    print("not found")
numbers=[2,4,6,8]
for i in numbers:
    if i==10:
        print("found")
        break
else:
    print("not found")

a='apple','banana','orange'
for i in a:
    if i=="apple":
        print("its apple")
        break
else:
   print("its not apple")

a="python"
for char in a:
    print(char)
else:
    print("finished")
