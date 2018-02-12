# Example's for loop:
num = int(input("Enter Number: "))
for i in range(1,10+1):
    print i, "*", num ,"=",num*i

# 2nd Example:
num = int(input("Enter number: "))
for num in range(1,num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print