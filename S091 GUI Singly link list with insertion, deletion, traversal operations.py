import tkinter as tk
from tkinter import messagebox


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

    def delete(self, data):
        if self.head is None:
            return False

        if self.head.data == data:
            self.head = self.head.next
            return True

        temp = self.head

        while temp.next and temp.next.data != data:
            temp = temp.next

        if temp.next is None:
            return False

        temp.next = temp.next.next
        return True

    def traverse(self):
        if self.head is None:
            return "List is Empty"

        temp = self.head
        result = ""

        while temp:
            result += str(temp.data) + " → "
            temp = temp.next

        result += "None"
        return result


linked_list = SinglyLinkedList()


def insert_node():
    try:
        data = int(entry.get())
        linked_list.insert(data)
        messagebox.showinfo("Success", f"{data} Inserted Successfully")
        update_display()
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer.")


def delete_node():
    try:
        data = int(entry.get())
        if linked_list.delete(data):
            messagebox.showinfo("Success", f"{data} Deleted Successfully")
        else:
            messagebox.showerror("Error", "Element Not Found")
        update_display()
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer.")


def update_display():
    display_label.config(text=linked_list.traverse())
    entry.delete(0, tk.END)


def exit_program():
    root.destroy()


# ---------------- GUI ----------------

root = tk.Tk()
root.title("Singly Linked List GUI")
root.geometry("550x430")
root.configure(bg="#E6E6FA")   # Light Purple (Lavender)

title = tk.Label(
    root,
    text="Singly Linked List",
    font=("Arial", 20, "bold"),
    bg="#E6E6FA",
    fg="#4B0082"
)
title.pack(pady=15)

entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=20,
    justify="center"
)
entry.pack(pady=10)

button_frame = tk.Frame(root, bg="#E6E6FA")
button_frame.pack()

tk.Button(
    button_frame,
    text="Insert",
    width=15,
    bg="#C8A2C8",
    fg="black",
    font=("Arial", 11, "bold"),
    command=insert_node
).grid(row=0, column=0, padx=10, pady=10)

tk.Button(
    button_frame,
    text="Delete",
    width=15,
    bg="#C8A2C8",
    fg="black",
    font=("Arial", 11, "bold"),
    command=delete_node
).grid(row=0, column=1, padx=10, pady=10)

tk.Button(
    button_frame,
    text="Traverse",
    width=15,
    bg="#C8A2C8",
    fg="black",
    font=("Arial", 11, "bold"),
    command=update_display
).grid(row=1, column=0, padx=10, pady=10)

tk.Button(
    button_frame,
    text="Exit",
    width=15,
    bg="#FFB6C1",
    fg="black",
    font=("Arial", 11, "bold"),
    command=exit_program
).grid(row=1, column=1, padx=10, pady=10)

display_label = tk.Label(
    root,
    text="List is Empty",
    font=("Arial", 14, "bold"),
    bg="white",
    fg="black",
    width=40,
    height=5,
    relief="ridge",
    bd=3
)
display_label.pack(pady=20)

root.mainloop()
