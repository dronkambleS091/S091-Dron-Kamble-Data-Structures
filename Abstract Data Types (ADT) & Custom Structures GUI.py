import tkinter as tk
from tkinter import messagebox


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.items[-1]

    def size(self):
        return len(self.items)


class StackGUI:
    def __init__(self, root):
        self.stack = Stack()
        self.root = root
        self.root.title("Interactive Stack Operations")
        self.root.geometry("500x600")
        self.root.config(bg="#EAF4FC")

        title = tk.Label(
            root,
            text="Stack Operations",
            font=("Arial", 18, "bold"),
            bg="#EAF4FC",
            fg="#003366",
        )
        title.pack(pady=10)

        self.entry = tk.Entry(root, font=("Arial", 14), width=20)
        self.entry.pack(pady=10)

        btn_frame = tk.Frame(root, bg="#EAF4FC")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Push", width=12, bg="#4CAF50",
                  fg="white", command=self.push_item).grid(row=0, column=0, padx=5, pady=5)

        tk.Button(btn_frame, text="Pop", width=12, bg="#F44336",
                  fg="white", command=self.pop_item).grid(row=0, column=1, padx=5, pady=5)

        tk.Button(btn_frame, text="Peek", width=12, bg="#2196F3",
                  fg="white", command=self.peek_item).grid(row=1, column=0, padx=5, pady=5)

        tk.Button(btn_frame, text="Is Empty?", width=12, bg="#FF9800",
                  fg="white", command=self.check_empty).grid(row=1, column=1, padx=5, pady=5)

        tk.Button(btn_frame, text="Size", width=12, bg="#9C27B0",
                  fg="white", command=self.show_size).grid(row=2, column=0, padx=5, pady=5)

        tk.Button(btn_frame, text="Clear Stack", width=12, bg="#607D8B",
                  fg="white", command=self.clear_stack).grid(row=2, column=1, padx=5, pady=5)

        tk.Label(
            root,
            text="Stack (Top → Bottom)",
            font=("Arial", 14, "bold"),
            bg="#EAF4FC",
        ).pack(pady=5)

        self.stack_display = tk.Listbox(
            root,
            width=30,
            height=15,
            font=("Arial", 14),
            bg="white",
            fg="blue",
        )
        self.stack_display.pack(pady=10)

        self.status = tk.Label(
            root,
            text="Welcome!",
            font=("Arial", 12),
            bg="#EAF4FC",
            fg="green",
        )
        self.status.pack(pady=10)

    def update_display(self):
        self.stack_display.delete(0, tk.END)
        for item in reversed(self.stack.items):
            self.stack_display.insert(tk.END, item)

    def push_item(self):
        item = self.entry.get().strip()

        if item == "":
            messagebox.showwarning("Warning", "Enter an item first.")
            return

        self.stack.push(item)
        self.entry.delete(0, tk.END)
        self.update_display()
        self.status.config(text=f"'{item}' pushed onto stack.", fg="green")

    def pop_item(self):
        try:
            item = self.stack.pop()
            self.update_display()
            self.status.config(text=f"'{item}' popped from stack.", fg="red")
        except IndexError as e:
            messagebox.showerror("Error", str(e))

    def peek_item(self):
        try:
            item = self.stack.peek()
            messagebox.showinfo("Top Item", f"Top Item: {item}")
        except IndexError as e:
            messagebox.showerror("Error", str(e))

    def check_empty(self):
        if self.stack.is_empty():
            messagebox.showinfo("Stack Status", "The stack is EMPTY.")
        else:
            messagebox.showinfo("Stack Status", "The stack is NOT EMPTY.")

    def show_size(self):
        messagebox.showinfo("Stack Size", f"Stack Size: {self.stack.size()}")

    def clear_stack(self):
        self.stack.items.clear()
        self.update_display()
        self.status.config(text="Stack cleared.", fg="purple")


if __name__ == "__main__":
    root = tk.Tk()
    app = StackGUI(root)
    root.mainloop()
