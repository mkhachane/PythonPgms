
class Stack:
    def __init__(self):
        self.mStack = []
        self.maxSize = 5
        self.top = 0

    def isEmpty(self):
        return self.mStack == []


    def push(self, item):
        if self.top >= self.maxSize:
            print "Stack is full"
        else:
            self.mStack.append(item)
            self.top += 1
            print "Inserted item: %d"% int(item)

    def pop(self):
        if self.top <= 0:
            print "Stack is Empty"
        else:
            item = self.mStack.pop()
            self.top -= 1
            print "Removed item : %d" % int(item)


    def display(self):
        if self.isEmpty() == False:
            for item in self.mStack:
                print item
        else:
            print "No item in stack"

    def size(self):
        return len(self.mStack)


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