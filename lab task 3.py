#Print numbers from 1 to 10.
for i in range (1,11,1):
      print(i)

#Print all even numbers from 1 to 20

for i in range (1,20):
    if i%2==0:
      print(i)

#Print all odd numbers from 1 to 20.

for i in range (1,20):
    if i%2!=0:
        print(i)


#Print the multiplication table of 5.


a=int(input("enter number:"))
for i in range (1,6):
    print(i,'x',a,'=',a*i)


#Find the sum of numbers from 1 to 10

add=0
for i in range (1,10):
    add+=i
print("Total:",add)


#Print each character in the string "PYTHON".

a="PYTHON"
for i in a:
    print(i)

#Count the number of vowels in "programming".

text=str(input("enter a:"))
count=0
for i in text:
    if i in "AEIOUaeiou":
        count+=1
        print(count)

#Print numbers from 10 to 1.

for i in range (10,0,-1):
      print(i)

#Find the factorial of 5.

n=int(input("enter the number:"))
f=1
for i in range (1,n+1):
    f*=i
    print("factorial:",f)

#pattern

for i in range (1,6):
    for j in range (i):
        print('*',end="")
    print()  


#Count the vowels in your name.

name=str(input("enter name:"))
count=0
for i in name:
    if i in "AEIOUaeiou":
        count+=1
        print(count)


#WHILE LOOP – Tasks

#Print numbers from 1 to 10.

i=1
while i<=10:
    print(i)
    i+=1


#Print numbers from 10 to 1

i=10
while i>=1:
    print(i)
    i-=1 

#Print all even numbers from 1 to 20
i = 1
while i<=20:
    if i%2==0:
        print(i)
    i+=1

#Find the sum of numbers from 1 to 10.
i = 1
sum = 0
while i <= 10:
    sum = sum + i
    i += 1

print(sum)


#Print the multiplication table of 7.

i = 1
while i <= 5:
    print(7 * i)
    i += 1


#Find the factorial of 5.

i=1
f=1
while i<=5:
    f=f*i
    i+=1
print(f)

#Count the digits in a number.

n = int(input("Enter a number: "))
count = 0
while n != 0:
    n = n // 10
    count += 1
print("Number of digits:", count)
