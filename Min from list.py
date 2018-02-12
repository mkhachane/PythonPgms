#Example of Max/Min from list:
lst=[]
numbers = int(input("How many numbers: "))

for n in range(numbers):
    numbers = int(input("Enter a Number: "))
    lst.append(numbers)

print "Maximum of lst is: ",max(lst)
print "Minimum of lst is: ",min(lst)
