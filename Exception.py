#Example check int or not
while True:
    try:
        num = raw_input("Please enter an integer: ")
        num = int(num)
        break
    except ValueError:
        print("No valid integer! Please try again ...")
print "Great, you successfully entered an integer!"

#Example number or string
var1 = '2'
try:
    var1 = var1 + 1
except:
    print(var1, " is not a number")
print(var1)

#Example IndexError
name = 'Imtiaz Abedin'
try:
   print(name[15])
except IndexError:
   print('IndexError has been found!')
