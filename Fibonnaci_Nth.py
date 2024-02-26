from functools import lru_cache

@lru_cache(maxsize=1000)
def fibonnaci(n):
    if n <= 1:
        return n
    
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)
    
def main():
    print(fibonnaci(100))

if __name__ == "__main__":
    main()
