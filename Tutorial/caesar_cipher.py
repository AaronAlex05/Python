def caesar_cipher(text, shift, mode='encrypt'):
    """
    Encrypts or decrypts text using the Caesar Cipher algorithm.
    """
    result = ""
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isalpha():
            # Determine if uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')
            # Shift the character and wrap around using modulo 26
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
            result += shifted_char
        else:
            # Keep non-alphabetical characters unchanged
            result += char
            
    return result

def main():
    print("--- Caesar Cipher Program ---")
    while True:
        mode = input("Do you want to (E)ncrypt or (D)ecrypt? (Q to quit): ").strip().lower()
        if mode == 'q':
            break
        if mode not in ['e', 'd', 'encrypt', 'decrypt']:
            print("Invalid mode. Please choose E, D, or Q.")
            continue
            
        text = input("Enter the text: ")
        try:
            shift = int(input("Enter the shift value (integer): "))
        except ValueError:
            print("Invalid shift value. Please enter an integer.")
            continue
            
        mode_full = 'encrypt' if mode in ['e', 'encrypt'] else 'decrypt'
        result = caesar_cipher(text, shift, mode_full)
        
        print(f"\nResult ({mode_full}ed): {result}\n")

if __name__ == "__main__":
    main()
