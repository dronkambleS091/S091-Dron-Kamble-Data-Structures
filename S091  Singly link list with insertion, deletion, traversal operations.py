class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

        print(data, "inserted.")

    def delete(self, data):
        if self.head is None:
            print("List is empty.")
            return

        if self.head.data == data:
            self.head = self.head.next
            print(data, "deleted.")
            return

        temp = self.head

        while temp.next and temp.next.data != data:
            temp = temp.next

        if temp.next is None:
            print("Element not found.")
        else:
            temp.next = temp.next.next
            print(data, "deleted.")

    def traverse(self):
        if self.head is None:
            print("List is empty.")
            return

        temp = self.head
        print("Linked List:", end=" ")

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


linked_list = SinglyLinkedList()

while True:
    print("\n----- Singly Linked List -----")
    print("1. Insert")
    print("2. Delete")
    print("3. Traverse")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter value to insert: "))
        linked_list.insert(data)

    elif choice == 2:
        data = int(input("Enter value to delete: "))
        linked_list.delete(data)

    elif choice == 3:
        linked_list.traverse()

    elif choice == 4:
        print("Program Ended.")
        break

    else:
        print("Invalid choice.")
