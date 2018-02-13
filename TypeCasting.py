try:
    a = 1 / "devide"
    print a
except (ZeroDivisionError,TypeError):
    print "You can't devide by zero or string"



