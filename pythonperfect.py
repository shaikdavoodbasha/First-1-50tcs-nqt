# import sys

# def solve():
#     n = int(sys.stdin.readline().strip())
#     if n<0:
#         print("Invalid input")
#     elif n==0:
#         print(1)
#     else:
#         s=1
#         for i in range(1,n+1):
#             s = i*s 
#         print(s)

# if __name__ == "__main__":
#     solve()

# import sys,math

# def solve():
#     diameter = int(sys.stdin.readline().strip())
#     radius = diameter/2
#     area_of_circle = 3.14*radius*radius
#     print(area_of_circle)
   

# if __name__ == "__main__":
#     solve()

# import sys

# def solve():
#     a, b = map(int, sys.stdin.readline().strip().split())
    
#     # Make numbers positive (handles negative inputs safely)
#     a = abs(a)
#     b = abs(b)
    
#     # Euclidean Algorithm
#     while b != 0:
#         a, b = b, a % b
    
#     print(a)

# if __name__ == "__main__":
#     solve()

# import sys

# def solve():
#     n1, n2 = map(int, sys.stdin.readline().split()) # very Important bro remember it 
#     for i in range(n1,n2+1):
#         if(i<0):
#             pass
         
#         elif i==0 or i==1:
#             pass
            
#         else:
#             flag=0
#             for j in range(2,i):
#                 if(i%j==0):
#                     flag=1
#                     break
#             if(flag==1):
#                 pass
#             else:
#                 print(i,end=" ")
# if __name__ == "__main__":
#     solve()

import sys

def solve():
    n1, n2 = map(int, sys.stdin.readline().split()) # very Important bro remember it 
    s=0
    for i in range(n1,n2+1):
        if(i<0):
            pass
         
        elif i==0 or i==1:
            pass
            
        else:
            flag=0
            
            for j in range(2,i):
                if(i%j==0):
                    flag=1
                    break
            if(flag==1):
                pass
            else:
                s=s+i
    print(s)
                # print(i,end=" ")
if __name__ == "__main__":
    solve()

