#1
a=10
b=5
print ("addition : ", a + b)
print ("subtraction : ", a - b)
print ("mutiplication : ", a * b)
print ("floor division : ", a // b)
print (" modulus :", a % b)
print (" power :", a ** b)

num =int (input("Enter a number :"))
last_digit = num % 10
print("last_digit : " , last_digit)


a = int(input("Enter first number :"))
b =int(input("Enter second number :"))
if a > b:
    print("Greater :", a)
    print("smaller :", b)
else:
        print("Greater :", a)
        print("samller :", b)



age = int(input("enter a age : "))
id =input(" do you have valid id ")
if age >=18 and id == "yes" :
    print("eligible to vote")
else :
    print("not eligible")

a= int(input("enter first number :"))
b = int(input("enter second number :"))
if a > 100 or b > 100:
    print("At leastb one number is greater than 100")
else:
        print("both nuymbers are 100 or less")
        
username = input("enter username: ")
password = input("enter password: ")
if username == "admin" and password == "1234" :
    print("login successful")
else:
    print("invalid username or password ")


students = ["joy" , "sam" , "john"]
name = input("enter name: ")
if name in students:
    print("name exists")
else:
    print("name not found")
    
fruits = ["Apple" , "banana", "mango", "orange"]
print("apple" in fruits)
print("mango" in fruits)
    
      
text = "python"
ch = input("enter a character: ")
if ch in text:
    print("character is present")
else:
    print("character is not present")

a =[1, 2, 3]
b =[1, 2, 3]
print(a == b)
print(a is b)

a =[1, 2, 3]
b = a
print(a is b)

a = 5
b = 3
print(a & b)
print(a | b)
print(a ^ b)

a = 5
print (~a)

a = 6
b = 3
print("and =" , a & b)
print("or =" ,a | b)


num = int(input("enter a number : "))
if num % 2 == 0:
    print("even")
else:
    print("odd")

num = int(input("enter a number : "))
if num > 0:
    print("positive")
elif num < 0:
    print("negative")
else:
    print("zero")

age = int(input("enter your age: "))
if age >=18:
    print("eligible to vote")
else:
    print("not eligible to vote")


a = int(input("enter first number: "))
b =int(input("enter second number: "))
if a > b:
    print("first numerb is bigger")
elif b > a:
        print("second number is bigger")
else:
    print("both are equal")

mark = int(input("enter a mark :"))
if mark >50:
    print("pass")
else:
    print("fail")

num =int(input("enter a number:"))
if num % 5== 0:
    print("divisible by 5")
else:
    print("not divisible by 5")

num = int(input("enter a number :"))
last = num % 10
print("last digit is even")
if last % 2== 0:
    print("last digit is odd")

username = input("enter username :")
password = input("enter password :")
if username == "admin" and password == "1234" :
    print("login succesfully")
else:
    print("Login falied")

