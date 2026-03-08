def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def list_primes(start, end):
    """Return a list of primes in the range [start, end]."""
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def main():
    print("--- Prime Number Program ---")
    print("1. Check if a number is prime")
    print("2. List primes in a range")
    print("3. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '1':
            try:
                num = int(input("Enter a number: "))
                if is_prime(num):
                    print(f"{num} is a prime number.")
                else:
                    print(f"{num} is not a prime number.")
            except ValueError:
                print("Invalid input. Please enter an integer.")
        
        elif choice == '2':
            try:
                start = int(input("Enter start of range: "))
                end = int(input("Enter end of range: "))
                primes = list_primes(start, end)
                print(f"Primes between {start} and {end}: {primes}")
            except ValueError:
                print("Invalid input. Please enter integers for the range.")
        
        elif choice == '3':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
