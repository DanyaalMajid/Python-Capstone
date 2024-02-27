def fast_exponent(a, b):
    if b == 0:
        return 1
    if b % 2 == 0:
        return fast_exponent(a * a, b // 2)
    return a * fast_exponent(a, b - 1)

def main():
    a = int(input("Enter base number: "))
    b = int(input("Enter exponent factor number: "))

    if a < 0 or b < 0:
        print("Invalid number")
        main()

    print(fast_exponent(a, b))

if __name__ == "__main__":
    main()