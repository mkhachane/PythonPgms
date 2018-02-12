# While loop Example
nterms = int(input("Enter terms: "))
n1 = 0
n2 =1
count =0
while count <nterms:
    temp = n1 + n2
    n1 =n2
    n2 = temp
    print temp
    count +=1

#Example for sum of natural number:
num = int(input("Enter number: "))
sum =0
i =1
while i <= num:
    sum =sum + i
    i += 1
print "The sum of",num,"is",sum