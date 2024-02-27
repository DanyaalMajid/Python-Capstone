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
        print("The Current Sequence Is:\n")
        for outcome in self.sequence:
            print(outcome)
    
    def print_count(self):
        print(f"The Number of Heads & Tails Are:\nHeads: {self.heads}\nTails: {self.tails}")


def main():
    coin = Coin()

    while True:
        choice = input("\nSelect An Option:\n1. Flip Coin\n2. Show Sequence\n3. Show Flip Count\n4. Exit\n\n>>> ")
        
        if choice == "1":
            coin.flip_coin()
            coin.print_count()
        
        elif choice == "2":
            coin.print_sequence()

        elif choice == "3":
            coin.print_count()

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid Input, Try Again.")

if __name__ == "__main__":
    main()

        