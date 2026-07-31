import tkinter as tk
from tkinter import ttk, messagebox


class FoodDeliveryQueue:
    def __init__(self, capacity):
        self.queue = []
        self.capacity = capacity

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) >= self.capacity

    def add_order(self, customer, food, priority):
        if self.is_full():
            return False
        self.queue.append((customer, food, priority))
        self.queue.sort(key=lambda x: x[2])
        return True

    def deliver_order(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)


class FoodDeliveryGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Food Delivery Priority Queue")
        self.root.geometry("850x600")
        self.root.configure(bg="lightblue")

        self.fd = None

        title = tk.Label(
            root,
            text="FOOD DELIVERY PRIORITY QUEUE",
            font=("Arial", 18, "bold"),
            bg="lightblue",
            fg="darkblue"
        )
        title.pack(pady=10)

        top = tk.Frame(root, bg="lightblue")
        top.pack()

        tk.Label(top, text="Maximum Capacity", bg="lightblue").grid(row=0, column=0, padx=5, pady=5)

        self.capacity_entry = tk.Entry(top, width=10)
        self.capacity_entry.grid(row=0, column=1)

        tk.Button(
            top,
            text="Create Queue",
            bg="green",
            fg="white",
            command=self.create_queue
        ).grid(row=0, column=2, padx=10)

        form = tk.Frame(root, bg="lightblue")
        form.pack(pady=15)

        tk.Label(form, text="Customer", bg="lightblue").grid(row=0, column=0)

        self.customer = tk.Entry(form)
        self.customer.grid(row=0, column=1)

        tk.Label(form, text="Food Item", bg="lightblue").grid(row=1, column=0)

        self.food = tk.Entry(form)
        self.food.grid(row=1, column=1)

        tk.Label(form, text="Priority", bg="lightblue").grid(row=2, column=0)

        self.priority = ttk.Combobox(
            form,
            values=[
                "1 - VIP",
                "2 - Express",
                "3 - Normal"
            ],
            state="readonly"
        )
        self.priority.current(2)
        self.priority.grid(row=2, column=1)

        button_frame = tk.Frame(root, bg="lightblue")
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Add Order", width=15,
                  bg="green", fg="white",
                  command=self.add_order).grid(row=0, column=0, padx=5)

        tk.Button(button_frame, text="Deliver Order", width=15,
                  bg="orange",
                  command=self.deliver_order).grid(row=0, column=1, padx=5)

        tk.Button(button_frame, text="Show Orders", width=15,
                  bg="skyblue",
                  command=self.show_orders).grid(row=0, column=2, padx=5)

        tk.Button(button_frame, text="Ascending", width=15,
                  command=self.show_ascending).grid(row=1, column=0, pady=10)

        tk.Button(button_frame, text="Descending", width=15,
                  command=self.show_descending).grid(row=1, column=1)

        tk.Button(button_frame, text="Queue Status", width=15,
                  command=self.status).grid(row=1, column=2)

        self.tree = ttk.Treeview(
            root,
            columns=("Customer", "Food", "Priority"),
            show="headings",
            height=12
        )

        self.tree.heading("Customer", text="Customer")
        self.tree.heading("Food", text="Food")
        self.tree.heading("Priority", text="Priority")

        self.tree.column("Customer", width=220)
        self.tree.column("Food", width=220)
        self.tree.column("Priority", width=120)

        self.tree.pack(pady=15)

    def create_queue(self):
        try:
            capacity = int(self.capacity_entry.get())

            if capacity <= 0:
                raise ValueError

            self.fd = FoodDeliveryQueue(capacity)

            messagebox.showinfo(
                "Success",
                f"Queue Created\nCapacity = {capacity}"
            )

        except ValueError:
            messagebox.showerror(
                "Error",
                "Enter a valid capacity."
            )

    def add_order(self):

        if self.fd is None:
            messagebox.showwarning(
                "Warning",
                "Create Queue First!"
            )
            return

        customer = self.customer.get()
        food = self.food.get()

        if customer == "" or food == "":
            messagebox.showwarning(
                "Warning",
                "Fill all fields."
            )
            return

        priority = int(self.priority.get()[0])

        if self.fd.add_order(customer, food, priority):
            messagebox.showinfo(
                "Success",
                "Order Added Successfully."
            )

            self.customer.delete(0, tk.END)
            self.food.delete(0, tk.END)

            self.show_orders()

        else:
            messagebox.showerror(
                "Queue Full",
                "Cannot Add More Orders."
            )

    def deliver_order(self):

        if self.fd is None:
            messagebox.showwarning(
                "Warning",
                "Create Queue First!"
            )
            return

        order = self.fd.deliver_order()

        if order is None:
            messagebox.showerror(
                "Empty",
                "No Orders Available."
            )
        else:
            messagebox.showinfo(
                "Delivered",
                f"Customer : {order[0]}\nFood : {order[1]}\nPriority : {order[2]}"
            )

            self.show_orders()

    def clear_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

    def show_orders(self):

        if self.fd is None:
            return

        self.clear_table()

        for customer, food, priority in self.fd.queue:
            self.tree.insert(
                "",
                tk.END,
                values=(customer, food, priority)
            )

    def show_ascending(self):
        self.show_orders()

    def show_descending(self):

        if self.fd is None:
            return

        self.clear_table()

        for customer, food, priority in sorted(
                self.fd.queue,
                key=lambda x: x[2],
                reverse=True):

            self.tree.insert(
                "",
                tk.END,
                values=(customer, food, priority)
            )

    def status(self):

        if self.fd is None:
            messagebox.showwarning(
                "Warning",
                "Create Queue First!"
            )
            return

        if self.fd.is_empty():
            messagebox.showinfo(
                "Status",
                "Queue is Empty."
            )

        elif self.fd.is_full():
            messagebox.showinfo(
                "Status",
                "Queue is Full."
            )

        else:
            messagebox.showinfo(
                "Status",
                f"Orders : {len(self.fd.queue)} / {self.fd.capacity}"
            )


root = tk.Tk()
FoodDeliveryGUI(root)
root.mainloop()
