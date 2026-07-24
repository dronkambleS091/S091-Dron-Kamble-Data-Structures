import time
from colorama import Fore, init

# Initialize Colorama
init(autoreset=True)


class Queue:
    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.max_size

    def enqueue(self, item):
        if self.is_full():
            print(Fore.RED + "Queue is full. Cannot enqueue.")
        else:
            self.queue.append(item)
            print(Fore.GREEN + f"Enqueued: {item}")
        time.sleep(0.5)

    def dequeue(self):
        if self.is_empty():
            print(Fore.RED + "Queue is empty. Cannot dequeue.")
            return

        item = self.queue.pop(0)
        print(Fore.YELLOW + f"Dequeued: {item}")
        time.sleep(0.5)

    def peek(self):
        if self.is_empty():
            print(Fore.RED + "Queue is empty.")
        else:
            print(Fore.BLUE + f"Front element: {self.queue[0]}")
        time.sleep(0.5)

    def traverse(self):
        if self.is_empty():
            print(Fore.RED + "Queue is empty.")
        else:
            print(Fore.CYAN + "Queue:", end=" ")
            for item in self.queue:
                print(item, end=" ")
                time.sleep(0.2)
            print()
        time.sleep(0.5)

    def display_list(self):
        if self.is_empty():
            print(Fore.RED + "Queue is empty.")
        else:
            print(Fore.MAGENTA + "\nCurrent Queue:")
            for i, item in enumerate(self.queue, start=1):
                print(f"{i}. {item}")
                time.sleep(0.2)
        time.sleep(0.5)


# Main Program
max_size = int(input("Enter the maximum size of the queue: "))
q = Queue(max_size)

while True:
    print("\n========== QUEUE MENU ==========")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Traverse")
    print("5. Display Queue")
    print("6. Check Empty")
    print("7. Check Full")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item: ")
        q.enqueue(item)

    elif choice == "2":
        q.dequeue()

    elif choice == "3":
        q.peek()

    elif choice == "4":
        q.traverse()

    elif choice == "5":
        q.display_list()

    elif choice == "6":
        if q.is_empty():
            print(Fore.RED + "Queue is Empty.")
        else:
            print(Fore.GREEN + "Queue is Not Empty.")

    elif choice == "7":
        if q.is_full():
            print(Fore.RED + "Queue is Full.")
        else:
            print(Fore.GREEN + "Queue is Not Full.")

    elif choice == "8":
        print(Fore.MAGENTA + "Exiting Program... Goodbye!")
        break

    else:
        print(Fore.RED + "Invalid Choice!")

    input("\nPress Enter to continue...")
