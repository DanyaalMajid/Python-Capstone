from functools import lru_cache

@lru_cache(maxsize=1000)
def fibonnaci(n):
    if n <= 1:
        return n
    
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)
    
def main():
    num = int(input("Enter a number between 0-100: "))
    if num > 100 or num < 0:
        print("Invalid Input, Try Again")
        main()
    else:
        print(fibonnaci(num))

if __name__ == "__main__":
    main()
