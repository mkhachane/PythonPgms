try:
    a = 1 / "devide"
    print a
except (ZeroDivisionError,TypeError):
    print "You can't devide by zero or string"


try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print "Error: can\'t find file or read data"
else:
   print "Written content in the file successfully"
   fh.close()