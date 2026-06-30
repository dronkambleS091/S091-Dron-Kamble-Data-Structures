import tkinter as tk
from tkinter import messagebox


class Stack:
    def __init__(self):
        self.items = []

    def insert(self, item, position):
        if position < 0 or position > len(self.items):
            raise IndexError("Invalid position")
        self.items.insert(position, item)

    def delete(self, position):
        if position < 0 or position >= len(self.items):
            raise IndexError("Invalid position")
        return self.items.pop(position)

    def peek(self):
        if not self.items:
            raise IndexError("Stack is empty")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def traverse(self):
        return " <- ".join(self.items) if self.items else "Stack is empty"

    def __str__(self):
        return " <- ".join(reversed(self.items)) if self.items else "Stack is empty"


stack = Stack()


def update_stack():
    stack_label.config(text="Stack: " + str(stack))


def insert_item():
    item = item_entry.get()
    pos = position_entry.get()

    try:
        pos = int(pos)
        stack.insert(item, pos)
        update_stack()
        messagebox.showinfo("Success", f"'{item}' inserted at position {pos}")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def delete_item():
    pos = position_entry.get()

    try:
        pos = int(pos)
        item = stack.delete(pos)
        update_stack()
        messagebox.showinfo("Deleted", f"'{item}' deleted")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def peek_item():
    try:
        messagebox.showinfo("Top Item", stack.peek())
    except Exception as e:
        messagebox.showerror("Error", str(e))


def check_empty():
    if stack.is_empty():
        messagebox.showinfo("Stack", "Stack is Empty")
    else:
        messagebox.showinfo("Stack", "Stack is Not Empty")


def stack_size():
    messagebox.showinfo("Size", f"Stack Size: {stack.size()}")


def traverse_stack():
    messagebox.showinfo("Traverse", stack.traverse())


# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Stack Operations")
root.geometry("500x450")
root.configure(bg="lightblue")

title = tk.Label(root, text="Stack Operations Using GUI",
                 font=("Arial", 18, "bold"),
                 bg="lightblue")
title.pack(pady=10)

tk.Label(root, text="Item", bg="lightblue").pack()
item_entry = tk.Entry(root, width=30)
item_entry.pack()

tk.Label(root, text="Position (0-based)", bg="lightblue").pack()
position_entry = tk.Entry(root, width=30)
position_entry.pack(pady=5)

tk.Button(root, text="Insert", width=20,
          bg="green", fg="white",
          command=insert_item).pack(pady=5)

tk.Button(root, text="Delete", width=20,
          bg="red", fg="white",
          command=delete_item).pack(pady=5)

tk.Button(root, text="Peek", width=20,
          command=peek_item).pack(pady=5)

tk.Button(root, text="Is Empty?", width=20,
          command=check_empty).pack(pady=5)

tk.Button(root, text="Stack Size", width=20,
          command=stack_size).pack(pady=5)

tk.Button(root, text="Traverse", width=20,
          command=traverse_stack).pack(pady=5)

stack_label = tk.Label(root,
                       text="Stack: Stack is empty",
                       font=("Arial", 12, "bold"),
                       bg="white",
                       width=45,
                       height=2)
stack_label.pack(pady=15)

root.mainloop()
