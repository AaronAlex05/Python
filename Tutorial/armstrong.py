def is_armstrong(number):
    """Checks if a given number is an Armstrong number."""
    # Convert number to string to easily iterate over digits
    num_str = str(number)
    num_digits = len(num_str)
    
    # Calculate the sum of digits raised to the power of the number of digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    
    return armstrong_sum == number

def main():
    print("--- Armstrong Number Checker ---")
    user_input = input("Enter a positive integer: ")
    
    try:
        num = int(user_input)
        if num < 0:
            print("Please enter a positive integer.")
            return

        if is_armstrong(num):
            print(f"Yes, {num} is an Armstrong number!")
        else:
            print(f"No, {num} is not an Armstrong number.")
            
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    main()
