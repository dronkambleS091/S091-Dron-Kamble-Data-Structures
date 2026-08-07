import tkinter as tk
from tkinter import ttk, messagebox
import heapq
from collections import Counter


# ---------------- Huffman Tree ----------------

class Node:
    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(frequencies):
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]


def generate_codes(node, prefix="", codebook=None):
    if codebook is None:
        codebook = {}

    if node:
        if node.char is not None:
            codebook[node.char] = prefix if prefix else "0"

        generate_codes(node.left, prefix + "0", codebook)
        generate_codes(node.right, prefix + "1", codebook)

    return codebook


def huffman_encoding(data):
    if not data:
        return "", {}

    frequencies = Counter(data)

    root = build_huffman_tree(frequencies)
    codebook = generate_codes(root)

    encoded = "".join(codebook[ch] for ch in data)

    return encoded, codebook, frequencies


def huffman_decoding(encoded_data, codebook):
    reverse = {v: k for k, v in codebook.items()}

    decoded = ""
    current = ""

    for bit in encoded_data:
        current += bit

        if current in reverse:
            decoded += reverse[current]
            current = ""

    return decoded


# ---------------- GUI ----------------

class HuffmanGUI:

    def __init__(self, root):

        self.root = root
        self.root.title("Huffman Coding Visualizer")
        self.root.geometry("750x650")
        self.root.configure(bg="#EAF6FF")

        self.codebook = {}
        self.encoded = ""

        title = tk.Label(
            root,
            text="HUFFMAN CODING APPLICATION",
            font=("Arial", 20, "bold"),
            bg="#0B5394",
            fg="white",
            pady=10
        )
        title.pack(fill="x")

        frame = tk.Frame(root, bg="#EAF6FF")
        frame.pack(pady=15)

        tk.Label(
            frame,
            text="Enter Text",
            font=("Arial", 13, "bold"),
            bg="#EAF6FF"
        ).grid(row=0, column=0, sticky="w")

        self.entry = tk.Entry(frame, width=50, font=("Arial", 13))
        self.entry.grid(row=1, column=0, padx=5, pady=5)

        btnframe = tk.Frame(root, bg="#EAF6FF")
        btnframe.pack()

        ttk.Button(
            btnframe,
            text="Encode",
            command=self.encode
        ).grid(row=0, column=0, padx=10)

        ttk.Button(
            btnframe,
            text="Decode",
            command=self.decode
        ).grid(row=0, column=1, padx=10)

        ttk.Button(
            btnframe,
            text="Clear",
            command=self.clear
        ).grid(row=0, column=2, padx=10)

        self.output = tk.Text(
            root,
            width=85,
            height=25,
            font=("Consolas", 11)
        )
        self.output.pack(pady=15)

    def encode(self):

        text = self.entry.get()

        if text == "":
            messagebox.showwarning("Warning", "Please enter text.")
            return

        encoded, self.codebook, freq = huffman_encoding(text)
        self.encoded = encoded

        self.output.delete("1.0", tk.END)

        self.output.insert(tk.END, "Character Frequencies\n")
        self.output.insert(tk.END, "-------------------------\n")

        for ch, f in freq.items():
            self.output.insert(tk.END, f"{repr(ch)} : {f}\n")

        self.output.insert(tk.END, "\nGenerated Codebook\n")
        self.output.insert(tk.END, "-------------------------\n")

        for ch, code in self.codebook.items():
            self.output.insert(tk.END, f"{repr(ch)} : {code}\n")

        self.output.insert(tk.END, "\nEncoded Data\n")
        self.output.insert(tk.END, "-------------------------\n")
        self.output.insert(tk.END, encoded)

    def decode(self):

        if self.encoded == "":
            messagebox.showwarning("Warning", "Encode first.")
            return

        decoded = huffman_decoding(self.encoded, self.codebook)

        self.output.insert(tk.END, "\n\nDecoded Data\n")
        self.output.insert(tk.END, "-------------------------\n")
        self.output.insert(tk.END, decoded)

    def clear(self):

        self.entry.delete(0, tk.END)
        self.output.delete("1.0", tk.END)
        self.codebook = {}
        self.encoded = ""


# ---------------- Main ----------------

root = tk.Tk()
app = HuffmanGUI(root)
root.mainloop()
