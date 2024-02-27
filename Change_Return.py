def change_return(cost, money):
    change = money - cost
    change = round(change, 2)
    change = str(change)
    change = change.split('.')
    change[0] = int(change[0])
    change[1] = int(change[1])
    print(change)
    print(f"Change: {change[0]} dollars and {change[1]} cents")

def main():
    cost = float(input("Enter the cost of the item: "))
    money = float(input("Enter the amount of money given: "))
    change_return(cost, money)

if __name__ == "__main__":
    main()