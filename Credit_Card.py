# luhn algorithm validation for credit card numbers
def is_valid_credit_card(number):
    # Remove any spaces or dashes from the input
    number = number.replace(" ", "").replace("-", "")
    
    # Check if the input consists of digits only and has a length of at least 2
    if not number.isdigit() or len(number) < 2:
        return False
    
    # Reverse the number and convert it to a list of integers
    digits = list(map(int, number[::-1]))
    
    # Double every second digit
    for i in range(1, len(digits), 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    
    # Sum all the digits
    total = sum(digits)
    
    # If the total is divisible by 10, the card number is valid
    return total % 10 == 0

def test():
    # Test the function with some credit card numbers
    credit_cards = [
        "4111 1111 1111 1111",  # VISA
        "5500 0000 0000 0004",  # MasterCard
        "3400 0000 0000 009",   # American Express
        "3000 0000 0000 04",    # Diners Club
        "6011 0000 0000 0004",  # Discover
        "3530 1113 3330 0001",  # JCB
        "6011 6011 6011 6611",  # Discover
        "5105 1051 0510 5100",  # MasterCard
        "6011 6011 6011 6611",  # Discover
        "4111 1111 1111 1112",  # VISA
    ]
    for number in credit_cards:
        print(f"{number} is valid: {is_valid_credit_card(number)}")

def main():
    num = input("Enter a credit card number: ")
    if is_valid_credit_card(num):
        print("This is a valid credit card number.")
    else:
        print("This is not a valid credit card number.")

if __name__ == "__main__":
    main()
    test()
