import tkinter as tk
from tkinter import ttk
import heapq

# ---------------- AVL Tree ---------------- #

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None


class AVLTree:

    def insert(self, root, key):

        if not root:
            return AVLNode(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):

        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left),
                           self.get_height(z.right))

        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))

        return y

    def right_rotate(self, z):

        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left),
                           self.get_height(z.right))

        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))

        return y

    def get_height(self, root):
        return root.height if root else 0

    def get_balance(self, root):
        return self.get_height(root.left) - self.get_height(root.right) if root else 0

    def preorder(self, root):

        result = []

        def traverse(node):
            if node:
                result.append(str(node.key))
                traverse(node.left)
                traverse(node.right)

        traverse(root)
        return " ".join(result)


# ---------------- GUI ---------------- #

class AVLGUI:

    def __init__(self, root):

        self.root = root
        self.root.title("AVL Tree, Heap & Priority Queue")
        self.root.geometry("850x650")
        self.root.configure(bg="#EAF6FF")

        self.avl = AVLTree()
        self.rootNode = None
        self.tasks = []

        title = tk.Label(
            root,
            text="AVL TREE • HEAP • PRIORITY QUEUE",
            bg="#003366",
            fg="white",
            font=("Arial",20,"bold"),
            pady=10
        )
        title.pack(fill="x")

        frame = tk.Frame(root,bg="#EAF6FF")
        frame.pack(pady=15)

        tk.Label(frame,text="Insert AVL Node",
                 bg="#EAF6FF",
                 font=("Arial",12,"bold")).grid(row=0,column=0)

        self.entry=tk.Entry(frame,font=("Arial",12),width=15)
        self.entry.grid(row=0,column=1,padx=10)

        ttk.Button(frame,text="Insert",
                   command=self.insert_node).grid(row=0,column=2,padx=10)

        ttk.Button(frame,text="Heap Demo",
                   command=self.heap_demo).grid(row=0,column=3,padx=10)

        ttk.Button(frame,text="Priority Queue",
                   command=self.priority_demo).grid(row=0,column=4,padx=10)

        ttk.Button(frame,text="Clear",
                   command=self.clear).grid(row=0,column=5,padx=10)

        self.output=tk.Text(root,width=95,height=28,font=("Consolas",11))
        self.output.pack(pady=15)

    def insert_node(self):

        try:
            value=int(self.entry.get())
        except:
            return

        self.rootNode=self.avl.insert(self.rootNode,value)

        self.output.delete(1.0,tk.END)
        self.output.insert(tk.END,"AVL Tree Preorder Traversal\n")
        self.output.insert(tk.END,"-----------------------------\n")
        self.output.insert(tk.END,self.avl.preorder(self.rootNode))

        self.entry.delete(0,tk.END)

    def heap_demo(self):

        data=[9,5,6,2,3]

        self.output.insert(tk.END,"\n\nHeap Demonstration\n")
        self.output.insert(tk.END,"-----------------------------\n")

        minheap=data.copy()
        heapq.heapify(minheap)

        self.output.insert(tk.END,f"Min Heap : {minheap}\n")

        maxheap=[-x for x in data]
        heapq.heapify(maxheap)

        self.output.insert(tk.END,
                           f"Max Heap : {[-x for x in maxheap]}\n")

    def priority_demo(self):

        pq=[]

        heapq.heappush(pq,(2,"Backup Database"))
        heapq.heappush(pq,(1,"Emergency Patient"))
        heapq.heappush(pq,(3,"Run Diagnostics"))

        self.output.insert(tk.END,"\nPriority Queue\n")
        self.output.insert(tk.END,"-----------------------------\n")

        while pq:
            p,t=heapq.heappop(pq)
            self.output.insert(tk.END,
                               f"Priority {p} --> {t}\n")

    def clear(self):

        self.output.delete(1.0,tk.END)
        self.entry.delete(0,tk.END)


root=tk.Tk()
AVLGUI(root)
root.mainloop()
