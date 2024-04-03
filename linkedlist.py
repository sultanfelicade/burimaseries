class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def display(self):
        current = self.head
        while current != None:
            print(current.getData())
            current = current.getNext()

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def insertPrevious(self, item, target):
        current = self.head
        previous = None
        while current != None and current.getData() != target:
            previous = current
            current = current.getNext()
        if current == None:  # Target not found
            print("Target not found in the list.")
            return
        else:
            temp = Node(item)
            if previous == None:  # Inserting before the head
                temp.setNext(self.head)
                self.head = temp
            else:
                temp.setNext(current)
                previous.setNext(temp)

    def insertNext(self, item, target):
        current = self.head
        while current != None and current.getData() != target:
            current = current.getNext()
        if current == None:  # Target not found
            print("Target not found in the list.")
            return
        else:
            temp = Node(item)
            temp.setNext(current.getNext())
            current.setNext(temp)


mylist = LinkedList()
mylist.add(45)
mylist.add(34)
mylist.add(70)
mylist.add(84)
mylist.add(97)
mylist.display()

# Insert before 70
mylist.insertPrevious(50, 70)
mylist.display()

# Insert after 70
mylist.insertNext(60, 70)
mylist.display()
