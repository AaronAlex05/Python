import math

def main():
    """
    Prompts the user for a number and calculates its square root.
    """
    print("--- Square Root Calculator ---")
    try:
        # Get input from the user
        number_str = input("Enter a number to find its square root: ")
        number = float(number_str)

        # Check for negative numbers
        if number < 0:
            print("Error: Cannot calculate the square root of a negative number in this program.")
        else:
            # Calculate square root using math.sqrt
            sqrt_val = math.sqrt(number)
            print(f"The square root of {number} is {sqrt_val:.4f}")
            
    except ValueError:
        print("Error: Please enter a valid numerical value.")

if __name__ == "__main__":
    main()
