def fibonacci(n):
    sequence = []
    
    a, b = 0, 1
    
    for i in range(n):
        sequence.append(a)
        a, b = b, a + b
    
    return sequence


# Ask user for input
num = int(input("Enter a number: "))

# Validate input
if num <= 0:
    print("Please enter a positive number.")
else:
    result = fibonacci(num)
    print("Fibonacci sequence:")
    print(result)