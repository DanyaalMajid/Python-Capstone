def palindrome(string):
    string = string.lower()
    reverse_string = string[::-1]
    if string == reverse_string:
        return True

    return False

def main():
    string = input("Enter a string: ")
    if palindrome(string):
        print("The string is a palindrome")

    else:
        print("The string is not a palindrome")

if __name__ == "__main__":
    main()