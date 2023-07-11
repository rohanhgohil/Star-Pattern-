"""
Pattern Printing
input = n
boolean = true or false
"""

n = int(input("Enter number: "))
b = int(input("Enter 0 or 1: "))
boolean = bool(b)

i=1
while(i<=n):
    if boolean==True:
        print("*"*i)
        i=i+1
    else:
        print("*"*((n+1)-i))
        i=i+1