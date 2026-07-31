from colorama import init, Fore, Style
import time

# Initialize Colorama
init(autoreset=True)

class FoodDeliveryQueue:
    def __init__(self, max_capacity):
        self.queue = []
        self.max_capacity = max_capacity

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) >= self.max_capacity

    def add_order(self, customer, food, priority):
        if self.is_full():
            print(Fore.RED + "Order Queue is Full!")
            return

        self.queue.append((customer, food, priority))
        self.queue.sort(key=lambda x: x[2])

        print(Fore.GREEN + f"Order placed for {customer} ({food}) with Priority {priority}")
        self.loading()

    def deliver_order(self):
        if self.is_empty():
            print(Fore.RED + "No orders to deliver.")
            return

        customer, food, priority = self.queue.pop(0)

        print(Fore.CYAN + f"\nDelivered Order")
        print(f"Customer : {customer}")
        print(f"Food     : {food}")
        print(f"Priority : {priority}")
        self.loading()

    def show_orders(self):
        if self.is_empty():
            print(Fore.YELLOW + "No pending orders.")
        else:
            print(Fore.BLUE + "\nPending Orders")
            print("-" * 45)
            print(f"{'Customer':<15}{'Food':<15}{'Priority'}")
            print("-" * 45)

            for customer, food, priority in self.queue:
                print(f"{customer:<15}{food:<15}{priority}")

    def ascending(self):
        if self.is_empty():
            print("Queue is Empty")
            return

        print(Fore.GREEN + "\nOrders in Ascending Priority")
        for customer, food, priority in sorted(self.queue, key=lambda x: x[2]):
            print(f"{customer} - {food} - Priority {priority}")

    def descending(self):
        if self.is_empty():
            print("Queue is Empty")
            return

        print(Fore.GREEN + "\nOrders in Descending Priority")
        for customer, food, priority in sorted(self.queue, key=lambda x: x[2], reverse=True):
            print(f"{customer} - {food} - Priority {priority}")

    def loading(self):
        print("Processing", end="")
        for _ in range(3):
            time.sleep(0.3)
            print(".", end="")
        print()


def main():
    capacity = int(input("Enter Maximum Order Capacity: "))
    fd = FoodDeliveryQueue(capacity)

    while True:
        print("\n========== FOOD DELIVERY PRIORITY QUEUE ==========")
        print("1. Add Food Order")
        print("2. Deliver Order")
        print("3. Show Pending Orders")
        print("4. Check Queue Empty")
        print("5. Check Queue Full")
        print("6. Show Ascending Priority")
        print("7. Show Descending Priority")
        print("8. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            customer = input("Customer Name: ")
            food = input("Food Item: ")

            print("\nPriority")
            print("1 = VIP Customer")
            print("2 = Express Delivery")
            print("3 = Normal Delivery")

            priority = int(input("Enter Priority: "))
            fd.add_order(customer, food, priority)

        elif choice == "2":
            fd.deliver_order()

        elif choice == "3":
            fd.show_orders()

        elif choice == "4":
            if fd.is_empty():
                print(Fore.YELLOW + "Order Queue is Empty.")
            else:
                print(Fore.GREEN + "Orders are Available.")

        elif choice == "5":
            if fd.is_full():
                print(Fore.RED + "Order Queue is Full.")
            else:
                print(Fore.GREEN + "Order Queue is Not Full.")

        elif choice == "6":
            fd.ascending()

        elif choice == "7":
            fd.descending()

        elif choice == "8":
            print(Fore.RED + "Thank You! Exiting...")
            break

        else:
            print(Fore.RED + "Invalid Choice!")


if __name__ == "__main__":
    main()
