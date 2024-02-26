def euler_approximation(n):
    euler = 2  # Initial approximation of Euler's number
    factorial = 1
    term = 2  # Initial term value

    for i in range(2, n + 1):
        factorial *= i
        term = 1 / factorial
        euler += term

    return round(euler, n)

n = int(input("Enter the number of digits: "))
print(euler_approximation(n))
