def fizzbuzz(num)
    if num % 3 == 0 and num % 2 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

def main():
    for num in range(1, 100001):
        print(fizzbuzz(num))

if __name__ == "__main__":
    main()