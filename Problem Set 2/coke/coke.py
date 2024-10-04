def main():
    cost = 50
    amount_due = cost

    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        coin = int(input("Insert Coin: "))
        if coin in [25, 10, 5]:
            amount_due -= coin

    change = abs(amount_due)
    print(f"Change Owed: {change}")

if __name__ == "__main__":
    main()
