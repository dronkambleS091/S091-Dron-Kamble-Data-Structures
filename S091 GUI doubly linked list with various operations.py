import tkinter as tk
from tkinter import messagebox


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new

    def insert_end(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new
        new.prev = temp

    def delete_beginning(self):
        if self.head is None:
            return

        self.head = self.head.next
        if self.head:
            self.head.prev = None

    def delete_end(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.prev.next = None

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
        elements = []
        temp = self.head

        while temp:
            elements.append(str(temp.data))
            temp = temp.next

        return " <-> ".join(elements) if elements else "List is Empty"

    def length(self):
        count = 0
        temp = self.head

        while temp:
            count += 1
            temp = temp.next

        return count


dll = DoublyLinkedList()


def insert_beginning():
    try:
        dll.insert_beginning(int(entry.get()))
        update_display()
    except:
        messagebox.showerror("Error", "Enter a valid integer")


def insert_end():
    try:
        dll.insert_end(int(entry.get()))
        update_display()
    except:
        messagebox.showerror("Error", "Enter a valid integer")


def delete_beginning():
    dll.delete_beginning()
    update_display()


def delete_end():
    dll.delete_end()
    update_display()


def search():
    try:
        pos = dll.search(int(entry.get()))
        if pos == -1:
            messagebox.showinfo("Search", "Element Not Found")
        else:
            messagebox.showinfo("Search", f"Element Found at Position {pos}")
    except:
        messagebox.showerror("Error", "Enter a valid integer")


def show_length():
    messagebox.showinfo("Length", f"Length = {dll.length()}")


def update_display():
    output.config(text=dll.display())
    entry.delete(0, tk.END)


root = tk.Tk()
root.title("Doubly Linked List GUI")
root.geometry("500x400")
root.configure(bg="lightblue")

title = tk.Label(root, text="Doubly Linked List", font=("Arial", 18, "bold"), bg="lightblue")
title.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

frame = tk.Frame(root, bg="lightblue")
frame.pack()

tk.Button(frame, text="Insert Beginning", width=18, command=insert_beginning).grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame, text="Insert End", width=18, command=insert_end).grid(row=0, column=1, padx=5, pady=5)

tk.Button(frame, text="Delete Beginning", width=18, command=delete_beginning).grid(row=1, column=0, padx=5, pady=5)
tk.Button(frame, text="Delete End", width=18, command=delete_end).grid(row=1, column=1, padx=5, pady=5)

tk.Button(frame, text="Search", width=18, command=search).grid(row=2, column=0, padx=5, pady=5)
tk.Button(frame, text="Length", width=18, command=show_length).grid(row=2, column=1, padx=5, pady=5)

output = tk.Label(root, text="List is Empty", font=("Arial", 14), bg="white", width=40, height=4)
output.pack(pady=20)

root.mainloop()
