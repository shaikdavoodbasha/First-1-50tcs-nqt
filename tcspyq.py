# print("Practising The TCS NQT PYQ'S")

# Question-1
# import sys
# n= list(map(int,sys.stdin.readline().strip().split(",")))
# v=[]
# for i in n:
#     if i!=0:
#         v.append(i)
# print(v)
# for j in n:
#     if j==0:
#         v.append(j)
# for k in v:
#     print(k,end=" ")

#question 2

# import sys

# a,b = map(int,sys.stdin.readline().strip().split())

# a = abs(a)
# b = abs(b)
# while b !=0:
#     a,b = b, a%b
# print(a)