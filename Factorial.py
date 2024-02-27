def factorial_recursive(n):
    print(f"Factorial of {n} Recursive:")
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)
    
def factorial_iterative(n):
    print(f"Factorial of {n} Iterative:")
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


print(factorial_recursive(100))
print(factorial_iterative(100))