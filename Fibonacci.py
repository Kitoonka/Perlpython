def fibonacci(n):
    if n <= 0:
        return []  # Return an empty list for non-positive input
    elif n == 1:
        return [0]  # Return the first Fibonacci number
    elif n == 2:
        return [0, 1]  # Return the first two Fibonacci numbers

    fib_sequence = [0, 1]  # Start with the first two Fibonacci numbers
    for i in range(2, n):
        next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]  # Calculate the next Fibonacci number
        fib_sequence.append(next_fib)  # Append it to the list

    return fib_sequence

# Example usage
print(fibonacci(5))
print(fibonacci(10))