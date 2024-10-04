def fibonacci(n):
    # Initialize the first two Fibonacci numbers
    fib_sequence = [0, 1]
    
    # Generate the Fibonacci series up to n
    for i in range(2, n):
        next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_fib)
    
    return fib_sequence[:n]

# Example usage:
n = 10  # Change this value for a different length
print(fibonacci(n))
