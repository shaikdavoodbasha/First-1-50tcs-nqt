# a = 123
# s=0
# while a>0:
#     r = a%10
#     s = s+r
#     a =a//10
# print(s)

# a = 123
# s=0
# while a>0:
#     r = a%10
#     s = s*10 +r
#     a =a//10
# print(s)

# a = 12345
# s=0
# while a>0:
#     r = a%10
#     s = s+1
#     a =a//10
# print(s)

# a = int(input())
# b = str(a)
# c = len(b)
# print(c)
# s = 0 
# for i in b:
#     s = s + pow(int(i),c)
# print(s)
# if s == a:
#     print("Armstrong")
# else :
#     print("Not Armstrong")

# Check Perfect number
# a = int(input())
# divisors = []
# for i in range(1,a):
#     if(a%i==0):
#         divisors.append(i)
# print(divisors)
# if a == sum(divisors):
#     print('perfect number')
# else:
#     print("Not a perfect number")

#Check Strong number
# a = int(input())
# b=a
# s = 0
# while a>0:
#     r = a%10
#     fac=1
#     for i in range(1,r+1):
#         fac = fac*i
#     print(fac)
#     s = s+fac
#     a = a//10
# print(s)
# print(b)
# if b == s:
#     print("strong number")
# else:
#     print("Not a strong number")
        
#Check Harshad number
# a = int(input())
# b = str(a)
# s=0
# for i in b:
#     s=s+int(i)
# print(s)
# if a%s==0:
#     print("Harshad number")
# else:
#     print("Not harshad number")

# Print Fibonacci series
# n= int(input())
# a=0
# b=1
# while a<=n:
#     print(a,end=" ")
#     c=a+b
#     a=b
#     b=c

#Find GCD/HCF of two numbers
# a,b = map(int,input().split(" "))
# a = abs(a)
# b= abs(b)
# while b!=0:
#     a,b = b,a%b
# print(a)

#Find LCM of two numbers
# a,b = map(int,input().split(' '))
# bi = max(a,b)
# while True:
#     if bi %a==0 and bi%b==0:
#         print(bi)
#         break
#     bi = bi+1

#Check Leap year
# 4x1=400
# n = int(input())
# if((n%4==0 and n%100 !=0) or n%400==0):
#     print("Leap year")
# else:
#     print("Not a leap year")

# ---------------------------------------------------------
# Find largest element in array
# a = list(map(int,input().split(" ")))
# print(max(a))

# Find smallest element
# a = list(map(int,input().split(" ")))
# print(min(a))

# Find second largest element
# a = list(map(int,input().split(" ")))
# b = sorted(set(a))
# print(b[-2])

# Find second smallest element
# a = list(map(int,input().split(" ")))
# b = sorted(set(a))
# print(b[1])

#Reverse an array
# a = list(map(int,input().split(" ")))
# rev = list(reversed(a))
# print(rev)

# Sort array ascending
# a = list(map(int,input().split(" ")))
# # b= sorted(a)
# print(sorted(a,reverse=True))

# Find sum of array elements
# a = list(map(int,input().split(" ")))
# s = 0
# for i in a:
#     s= s+i
# print(s)

# Find average of array
# a = list(map(int,input().split(" ")))
# s = 0
# for i in a:
#     s= s+i
# # print(s)
# avg = s/len(a)

# Count even and odd numbers
# a = list(map(int,input().split(" ")))
# eve=0
# odd =0
# for i in a :
#     if i%2==0:
#         eve=eve+1
#     else:
#         odd=odd+1
# print("count of even",eve)
# print("count of odd",odd)
        

# Move all zeros to end
# a = list(map(int,input().split(" ")))
# b = []
# for i in a:
#     if i!=0:
#         b.append(i)
# for j in a:
#     if j==0:
#         b.append(j)
# print(b)

# Find frequency of each element

# a = list(map(int,input().split(" ")))
# new = {}
# for i in a:
#     if i not in new:
#         new[i] =1
#     else:
#         new[i] = new[i]+1
# print(new)

# Merge two arrays
# a = [1,2,3]
# b = [4,5,6]
# print(a+b)

# a = [1,2,3,4,5,6,7]
# b = 3
# print(a[len(a)-b:] + a[:len(a)-b])


# a = input()
# print(a[::-1])

# if a == a[::-1]:
#     print("palindrome")
# else:
#     print("Not palindrome")

# v =0
# c=0
# for i in  a:
#     if i in 'aeiouAEIOU':
#         v = v+1
#     else:
#         c=c+1
# print(v)
# freq ={}
# for i in a:
#     if i not in freq:
#         freq[i] = 1
#     else:
#         freq[i] = freq[i]+1
# print(freq)

# print(sorted(list(set(a))))

# Find largest word in string
# a = input()
# print(max(a.split(), key=len))

# a = 97
# print(chr(a))
# print(ord('a'))
# a =4
# b=3
# a,b=b,a
# print(a,b)
# print(pow(2,3))

# x = int(input())
# a=bin(x)
# print(a[2:])

# a = input("")
# decimal = int(a,2)
# print(decimal)

# a = int(input())
# print(oct(a)[2:])

# a = input("")
# octal = int(a,8)
# print(octal)

a = list(map(int,input("Enter list here").split()))
max_right=a[-1]
simple =[]
simple.append(max_right)
for i in range(len(a)-2,-1,-1):
    if a[i]>max_right:
        max_right=a[i]
        simple.append(a[i])
simple.reverse()
print(simple)



