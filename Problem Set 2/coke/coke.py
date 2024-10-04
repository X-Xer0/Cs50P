def main():
    cost = 50  # Cost of the Coke in cents
    amount_due = cost

    while amount_due > 0:
        print(f"Amount Due: {amount_due} cents")
        coin = int(input("Insert coin (25, 10, 5): "))
        if coin in [25, 10, 5]:
            amount_due -= coin

    change = abs(amount_due)
    print(f"Change Owed: {change} cents")

if __name__ == "__main__":
    main()
