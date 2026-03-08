def factorial(n):
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return 1 
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
def main():
    print("--- Factorial Calculator ---")
    try:
        user_input = input("Enter a non-negative integer: ")
        number = int(user_input)
        result = factorial(number)
        if result is None:
            print("Error: Please enter a non-negative integer.")
        else:
            print(f"The factorial of {number} is: {result}")
    except ValueError:
        print("Error: Invalid input. Please enter a valid whole number (integer).")
if __name__ == "__main__":
    main()