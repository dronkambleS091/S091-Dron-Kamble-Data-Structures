import heapq
from collections import Counter
from colorama import Fore, Style, init
import time
import sys

# Initialize Colorama
init(autoreset=True)


# Node class for Huffman Tree
class Node:
    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


# Build Huffman Tree
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

        # Animation
        print(
            Fore.YELLOW +
            f"Merging nodes: {left.char} ({left.freq}) and {right.char} ({right.freq})"
        )
        time.sleep(0.5)

    return heap[0]


# Generate Huffman Codes
def generate_codes(node, prefix="", codebook=None):
    if codebook is None:
        codebook = {}

    if node:
        if node.char is not None:
            codebook[node.char] = prefix if prefix else "0"

            print(
                Fore.GREEN +
                f"Assigning code to character '{node.char}': {codebook[node.char]}"
            )
            time.sleep(0.3)

        generate_codes(node.left, prefix + "0", codebook)
        generate_codes(node.right, prefix + "1", codebook)

    return codebook


# Huffman Encoding
def huffman_encoding(data):
    if not data:
        return "", {}

    frequencies = Counter(data)

    print(Fore.CYAN + "\nCharacter Frequencies:")
    for char, freq in frequencies.items():
        print(f"'{char}' : {freq}")

    root = build_huffman_tree(frequencies)
    codebook = generate_codes(root)

    encoded_data = "".join(codebook[char] for char in data)

    print(Fore.CYAN + "\nEncoded Data:")
    print(encoded_data)

    return encoded_data, codebook


# Huffman Decoding
def huffman_decoding(encoded_data, codebook):
    reverse_codebook = {v: k for k, v in codebook.items()}

    decoded_data = ""
    current_code = ""

    for bit in encoded_data:
        current_code += bit

        if current_code in reverse_codebook:
            character = reverse_codebook[current_code]
            decoded_data += character

            print(
                Fore.MAGENTA +
                f"Decoding: {current_code} -> '{character}'"
            )

            current_code = ""
            time.sleep(0.2)

    return decoded_data


# Animated Text
def animate_text(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print()


# Main Program
if __name__ == "__main__":

    animate_text(Fore.BLUE + "=" * 50)
    animate_text(Fore.BLUE + "     HUFFMAN CODING CLI APPLICATION")
    animate_text(Fore.BLUE + "=" * 50)

    data = input(Fore.YELLOW + "\nEnter the text to encode: ")

    animate_text(Fore.GREEN + "\nStarting Huffman Encoding...\n")

    encoded_data, codebook = huffman_encoding(data)

    animate_text(Fore.GREEN + "\nEncoding Completed!\n")

    print(Fore.CYAN + "Generated Codebook:")
    for char, code in codebook.items():
        print(f"'{char}' : {code}")

    animate_text(Fore.RED + "\nStarting Huffman Decoding...\n")

    decoded_data = huffman_decoding(encoded_data, codebook)

    animate_text(Fore.RED + "\nDecoding Completed!\n")

    print(Fore.BLUE + "=" * 50)
    print(Fore.BLUE + "Original Data :", Fore.WHITE + data)
    print(Fore.BLUE + "Encoded Data  :", Fore.WHITE + encoded_data)
    print(Fore.BLUE + "Decoded Data  :", Fore.WHITE + decoded_data)
    print(Fore.BLUE + "=" * 50)

    if data == decoded_data:
        print(Fore.GREEN + "\n✔ Success: Original and decoded data match!")
    else:
        print(Fore.RED + "\n✘ Error: Original and decoded data do not match!")
