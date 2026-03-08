def binary_to_decimal(binary_str):
    """Converts a binary string to a decimal integer."""
    try:
        return int(binary_str, 2)
    except ValueError:
        return None

def decimal_to_binary(decimal_int):
    """Converts a decimal integer to a binary string."""
    try:
        return bin(decimal_int).replace("0b", "")
    except (ValueError, TypeError):
        return None

def main():
    print("--- Binary-Decimal Converter ---")
    while True:
        print("\nOptions:")
        print("1. Binary to Decimal")
        print("2. Decimal to Binary")
        print("3. Exit")
        
        choice = input("Enter choice (1/2/3): ")
        
        if choice == '1':
            binary_str = input("Enter a binary number: ")
            decimal_val = binary_to_decimal(binary_str)
            if decimal_val is not None:
                print(f"Decimal equivalent: {decimal_val}")
            else:
                print("Invalid binary input! Please use only 0s and 1s.")
        
        elif choice == '2':
            try:
                decimal_val = int(input("Enter a decimal number: "))
                binary_str = decimal_to_binary(decimal_val)
                if binary_str is not None:
                    print(f"Binary equivalent: {binary_str}")
                else:
                    print("Error in conversion.")
            except ValueError:
                print("Invalid decimal input! Please enter an integer.")
        
        elif choice == '3':
            print("Exiting... Goodbye!")
            break
        
        else:
            print("Invalid choice! Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
