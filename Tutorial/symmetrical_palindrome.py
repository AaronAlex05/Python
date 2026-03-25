def is_symmetrical(s):
    """Checks if the first half of the string matches the second half."""
    n = len(s)
    mid = n // 2
    
    if n % 2 == 0:
        half1 = s[:mid]
        half2 = s[mid:]
    else:
        # For odd length, exclude the middle character
        half1 = s[:mid]
        half2 = s[mid+1:]
        
    return half1 == half2

def is_palindrome(s):
    """Checks if the string reads the same forwards and backwards."""
    return s == s[::-1]

def main():
    print("--- Symmetrical and Palindrome Checker ---")
    string = input("Enter a string: ").strip().lower()
    
    if not string:
        print("Empty string provided.")
        return

    sym = is_symmetrical(string)
    pal = is_palindrome(string)
    
    print(f"\nString: '{string}'")
    print(f"Symmetrical: {'Yes' if sym else 'No'}")
    print(f"Palindrome: {'Yes' if pal else 'No'}")
    
    # Explanatory logic
    if sym and pal:
        print("Result: Both Symmetrical and Palindrome")
    elif sym:
        print("Result: Symmetrical but Not Palindrome")
    elif pal:
        print("Result: Palindrome but Not Symmetrical")
    else:
        print("Result: Neither Symmetrical nor Palindrome")

if __name__ == "__main__":
    main()
