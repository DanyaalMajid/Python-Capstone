import random

class Coin:

    def __init__(self):
        self.heads = 0
        self.tails = 0
        self.sequence = []
        self.outcomes = ["heads", "tails"]

    def flip_coin(self):
        result = random.choice(self.outcomes)

        if result == "heads":
            self.heads += 1
        
        else:
            self.tails += 1

        self.sequence.append(result)

    def print_sequence(self):
        print("The Current Sequence Is:")
        for outcome in self.sequence:
            print(outcome + "\n")
    
    def print_count(self):
        print(f"The Number of Heads & Tails Are:\nHeads: {self.heads}\nTails: {self.tails}")


def main():
    coin = Coin()

    choice = 0
    while True:
        while choice not in ["1", "2", "3"]:
            choice = input("Select An Option:\n1. Flip Coin\n2. Show Sequence\n3. Show Flip Count\n\n>>> ")
        
        if choice == "1":
            coin.flip_coin()
            coin.print_count()
            break
        
        elif choice == "2":
            coin.print_sequence()
            break

        elif choice == "3":
            coin.print_count()
            break

        else:
            print("Invalid Input, Try Again.")
            break

if __name__ == "__main__":
    main()

        