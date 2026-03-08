def generate_fibonacci(n):
    """Generates a Fibonacci sequence up to n terms."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    sequence = [0, 1]
    while len(sequence) < n:
        next_val = sequence[-1] + sequence[-2]
        sequence.append(next_val)
    return sequence

def main():
    print("--- Fibonacci Sequence Generator ---")
    try:
        user_input = input("Enter the number of terms: ")
        terms = int(user_input)
        
        if terms < 0:
            print("Please enter a non-negative integer.")
        else:
            result = generate_fibonacci(terms)
            print(f"Fibonacci sequence with {terms} terms:")
            print(result)
            
    except ValueError:
        print(f"Invalid input: '{user_input}'. Please enter a valid integer.")

if __name__ == "__main__":
    main()
