#1 Print Hello World
# print("Hello world")

#2.Swap two numbers without third variable
# n1 = int(input('Enter n1 number: '))
# n2 = int(input("Enter n2 number: "))
# print("Numbers before swapping n1:{} n2:{}".format(n1,n2))
# n1 = n1+n2
# n2 = n1-n2
# n1 = n1-n2
# print("Number after swapping without third variable: n1:{} n2:{}".format(n1,n2))

# OR n1,n2 = n2,n1

#3.Check even or odd
# x = int(input("Enter a number: "))
# if(x %2 ==0):
#     print("Even number")
# else:
#     print("Odd number")

#4.Find largest of three numbers
# a = int(input("Enter number a: "))
# b = int(input("Enter number b: "))
# c = int(input("Enter number c: "))
# if(a >= b and a>=c):
#     print("a is greater then both b and c")
# elif(b>=a and b>=c):
#     print("b is greater then a and c")
# else:
#     print("c is greater then both a and b")
# OR print(max(a,b,c))

#5.Check leap year
# year = int(input().strip())

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Leap Year")
# else:
#     print("Not Leap Year")

#6.Simple calculator
# n1 = int(input("Enter n1:"))
# n2 = int(input("Enter n2:"))
# operand = input("Enter operand:")
# match(operand):
#     case '+':
#         print(n1+n2)
#     case '-':
#         print(n1-n2)
#     case "*":
#         print(n1*n2)
#     case "/":
#         if(n1 !=0):
#             print(n1/n2)
#         else:
#             print("Zero division Error")
#     case "%":
#         if(n1 !=0):
#             print(n1%n2)
#         else:
#             print("Modulo Error")
#     case "_":
#         print("Invalid operator")

#7.Print multiplication table
# try:
#     x = int(input())
#     for i in range(1,11):
#         print("{} X {} = {}".format(x,i,x*i))
# except:
#     print("Invalid input")

#8.Sum of first N numbers
# x=int(input())
# if(x<0):
#     print("Invalid input")
# else:
#     sum=0
#     i =0
#     while(i<=x):
#         sum = sum+i
#         i=i+1
#         print(sum)

#9.Factorial of number
# x=int(input())
# if(x<0):
#     print("Invalid input")
# else:
#     total = 1
#     for i in range(1,x+1):
#         total *= i
#     print(total)

#10.Check prime number
# x=int(input())
# flag = 0
# if(x ==0 or x==1):
#     print('Enter a valid number to check where it is prime or not')
# elif(x<0):
#     print("Negative numbers are can't be prime numbers")
# else:
#     for i in range(2,x):
#         if(x%i==0):
#             flag = 1
#             break
#     if(flag==1):
#         print("Not Prime")
#     else:
#         print("Prime")

#11 Print all primes till N

# y=int(input())
# for i in range(y+1):
#     flag=0
#     if(i==0 or i==1):
#         pass
#     else:
#         for j in range(2,i):
#             if(i%j==0):
#                 flag=1
#                 break
#         if(flag==0):
#             print(i)

#12.Reverse a number
# n = int(input())

# sign = -1 if n < 0 else 1
# n = abs(n)

# rev = 0

# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n = n // 10

# print(sign * rev)

#13.Check palindrome number

# n = int(input())

# if n < 0:
#     print("It is not a palindrome")
# else:
#     original = n
#     rev = 0
#     while n > 0:
#         digit = n % 10
#         rev = rev * 10 + digit
#         n //= 10
#     if original == rev:
#         print("It is a palindrome")
#     else:
#         print("It is not a palindrome")

#14.Armstrong number
# x=int(input())
# original = x
# s=0
# def cou(x):
#     c=0
#     while x>0:
#         d = x%10
#         c=c+1
#         x=x//10
#     return c
# l = cou(x)
# while x>0:
#     d = x%10
#     sq = pow(d,l)
#     print(d,sq)
#     s = s+sq
#     x=x//10
# if(original == s):
#     print("It is a ARMSTRONG BRO")
# else:
#     print("Not ARMSTRONG")
# 15count of digits 

# x = int(input())
# count = 0
# while(x>0):
#     d = x%10
#     count= count+1
#     x=x//10
# print(count)

#16.Sum of digits

x=int(input())
if x<0:
    print("This is negative number")
else:
    s=0
    while x>0:
        d = x%10
        s=s+d
        x=x//10
    print(s)
