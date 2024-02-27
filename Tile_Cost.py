def tile_cost(width, height, cost):
    area = width * height
    cost = area * cost

    return cost

def main():
    width = float(input("Enter the width of the floor: "))
    height = float(input("Enter the height of the floor: "))
    cost = float(input("Enter the cost of the tile per square foot: "))

    print("The cost to tile the floor is: $", tile_cost(width, height, cost))

if __name__ == "__main__":
    main()
