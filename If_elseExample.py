# Example for odd and even number:
num = int(input("Enter any Positive number: "))
if num % 2 == 0:
    print "%d Number is even."% num
else:
    print "%d Number is odd."% num



#Largest Number
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))

if num1 < num2:
    largest = num2
elif num2 < num3:
    largest = num3
elif num3 < num1:
    largest = num1
print "The largest number of ",num1,num2,"and",num3,"is",largest


# Example for  leap year
year = int(input("Enter year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print "%d is leap year"% year
        else:
            print "%d is not leap year"% year
    print "%d is leap year"% year
else:
    print "%d is not leap year"% year
