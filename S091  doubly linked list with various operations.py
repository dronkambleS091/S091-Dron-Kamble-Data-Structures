class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def insert_position(self, pos, data):
        if pos == 0:
            self.insert_beginning(data)
            return

        temp = self.head
        for i in range(pos - 1):
            if temp is None:
                print("Invalid Position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid Position")
            return

        new_node = Node(data)
        new_node.next = temp.next
        new_node.prev = temp

        if temp.next:
            temp.next.prev = new_node

        temp.next = new_node

    def delete_beginning(self):
        if self.head is None:
            print("List is Empty")
            return

        self.head = self.head.next
        if self.head:
            self.head.prev = None

    def delete_end(self):
        if self.head is None:
            print("List is Empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.prev.next = None

    def delete_position(self, pos):
        if self.head is None:
            print("List is Empty")
            return

        if pos == 0:
            self.delete_beginning()
            return

        temp = self.head
        for i in range(pos):
            if temp is None:
                print("Invalid Position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid Position")
            return

        if temp.next:
            temp.next.prev = temp.prev

        temp.prev.next = temp.next

    def search(self, key):
        temp = self.head
        pos = 0

        while temp:
            if temp.data == key:
                return pos
            temp = temp.next
            pos += 1

        return -1

    def display(self):
        if self.head is None:
            print("List is Empty")
            return

        temp = self.head
        print("Doubly Linked List:", end=" ")

        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def length(self):
        count = 0
        temp = self.head

        while temp:
            count += 1
            temp = temp.next

        return count


dll = DoublyLinkedList()

while True:
    print("\n----- Doubly Linked List Menu -----")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Insert at Position")
    print("4. Delete from Beginning")
    print("5. Delete from End")
    print("6. Delete from Position")
    print("7. Search")
    print("8. Display")
    print("9. Length")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter data: "))
        dll.insert_beginning(data)

    elif choice == 2:
        data = int(input("Enter data: "))
        dll.insert_end(data)

    elif choice == 3:
        pos = int(input("Enter position: "))
        data = int(input("Enter data: "))
        dll.insert_position(pos, data)

    elif choice == 4:
        dll.delete_beginning()

    elif choice == 5:
        dll.delete_end()

    elif choice == 6:
        pos = int(input("Enter position: "))
        dll.delete_position(pos)

    elif choice == 7:
        key = int(input("Enter element to search: "))
        result = dll.search(key)
        if result == -1:
            print("Element not found")
        else:
            print("Element found at position", result)

    elif choice == 8:
        dll.display()

    elif choice == 9:
        print("Length of list:", dll.length())

    elif choice == 10:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
