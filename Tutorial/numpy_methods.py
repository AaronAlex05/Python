import numpy as np

def main():
    print("--- NumPy Methods Demo ---")
    
    # 1. Creating Arrays
    arr = np.array([1, 2, 3, 4, 5])
    print(f"Array: {arr}")
    print(f"Shape: {arr.shape}")
    print(f"Zeros: {np.zeros(5)}")
    print(f"Ones: {np.ones((2, 3))}")
    print(f"Arange: {np.arange(0, 10, 2)}")
    print(f"Linspace: {np.linspace(0, 1, 5)}")

    # 2. Reshaping and Manipulation
    matrix = np.arange(12).reshape(3, 4)
    print(f"\nMatrix (3x4):\n{matrix}")
    print(f"Transpose:\n{matrix.T}")
    print(f"Flatten: {matrix.flatten()}")

    # 3. Mathematical Operations
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    print(f"\nAddition: {a + b}")
    print(f"Multiplication: {a * b}")
    print(f"Dot Product: {np.dot(a, b)}")

    # 4. Statistical Methods
    data = np.array([10, 20, 30, 40, 50])
    print(f"\nData: {data}")
    print(f"Mean: {np.mean(data)}")
    print(f"Median: {np.median(data)}")
    print(f"Std Deviation: {np.std(data):.2f}")
    print(f"Max: {np.max(data)} (at index {np.argmax(data)})")
    
    # 5. Accessing and Slicing
    print(f"\nSlicing (first 3): {data[:3]}")
    print(f"Conditional: {data[data > 25]}")

if __name__ == "__main__":
    main()
