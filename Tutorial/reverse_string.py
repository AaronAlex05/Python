def reverse_string_slicing(s):
    """Reverses a string using Python slicing."""
    return s[::-1]

def reverse_string_loop(s):
    """Reverses a string using a loop."""
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

def main():
    print("--- String Reversal Program ---")
    user_input = input("Enter a string to reverse: ")
    
    # Using slicing (most Pythonic way)
    result_slicing = reverse_string_slicing(user_input)
    
    # Using loop (traditional way)
    result_loop = reverse_string_loop(user_input)
    
    print(f"\nOriginal: {user_input}")
    print(f"Reversed (Slicing): {result_slicing}")
    print(f"Reversed (Loop):    {result_loop}")

if __name__ == "__main__":
    main()
