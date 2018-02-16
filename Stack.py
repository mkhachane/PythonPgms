class Stack:
    def __init__(self):
        self.mStack = []

    def isEmpty(self):
        return self.mStack == []


    def push(self, item):
        self.mStack.append(item)
        print "Inserted item: %d"% int(item)

    def pop(self):
        if self.isEmpty() == False:
            item = self.mStack.pop()
            print "Removed item : %d"% int(item)
        else:
            print "No item in stack"

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