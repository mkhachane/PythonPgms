
class Queue:
    def __init__(self):
        self.mqueue = []

    def isEmpty(self):
        return self.mqueue == []

    def enqueue(self, item):
        self.mqueue.append(item)
        print "Inserted item: %d"% int(item)

    def dequeue(self):
        if self.isEmpty() == False:
            item = self.mqueue.pop(0)
            print "Removed item : %d"% int(item)
        else:
            print "No item in queue"

    def display(self):
        if self.isEmpty() == False:
            for item in self.mqueue:
                print item
        else:
            print "No item in queue"

    def size(self):
        return len(self.mqueue)


if __name__ == "__main__":
    mqueue = Queue()

    print "Menu items"
    print "1. Display the Queue"
    print "2. Insert "
    print "3. Delete "
    print "4. For Size "
    print "5. Quit "

    while True:
        user_input = int(raw_input("Enter the option: "))

        if user_input == 1:
            mqueue.display()
        elif user_input == 2:
            item = (raw_input("Enter the item to be inserted: "))
            mqueue.enqueue(item)
        elif user_input == 3:
            mqueue.dequeue()
        elif user_input == 4:
            print mqueue.size()
        elif user_input == 5:
            break
