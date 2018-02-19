class Stack:
    def __init__(self):
        self.mStack = []
        self.maxSize = 2
        self.top = 0

    def push(self, data):
        if self.top >= self.maxSize:
            print ("Stack is Full!")
        else:
            self.mStack.append(data)
            self.top += 1

    def pop(self):
        if self.top <= 0:
            print ("Stack is  Empty!")
        else:
            item = self.mStack.pop()
            self.top -= 1
            print "Removed item : %d" % int(item)

    def display(self):
        for item in self.mStack:
            print item

    def size(self):
        return self.top
        #return len(self.mStack)


if __name__ == "__main__":
    mStack = Stack()

    print "Menu items"
    print "1. Display the stack"
    print "2. Push "
    print "3. Pop "
    print "4. For Size "
    print "5. Quit "

    while True:
        user_input = input("Enter your Choice: ")

        if user_input == 1:
            mStack.display()
        elif user_input == 2:
            item = (raw_input("Enter the item to be inserted: "))
            mStack.push(item)
        elif user_input == 3:
            mStack.pop()
        elif user_input == 4:
            print mStack.size()
        elif user_input == 5:
            break