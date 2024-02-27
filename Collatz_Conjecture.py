def collatz_conjecture(n):
    count = 0
    while n != 1:
        print(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    print(n)

    return count


def main():
    n = int(input("Enter a number: "))
    if n < 1:
        print("Invalid number")
        main()
    print("Number of steps:", collatz_conjecture(n))

if __name__ == "__main__":
    main()