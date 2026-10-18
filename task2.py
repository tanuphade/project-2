# Stock Investment Calculator

# Hard-coded dictionary of stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = {}
total_investment = 0

print("Available stocks:", ", ".join(stock_prices.keys()))

# Get number of different stocks
n = int(input("How many stocks do you want to buy? "))

# Input stock names and quantities
for i in range(n):
    stock = input(f"Enter stock name {i + 1}: ").upper()

    if stock not in stock_prices:
        print("Stock not found in price dictionary.")
        continue

    quantity = int(input(f"Enter quantity of {stock}: "))

    portfolio[stock] = quantity

# Calculate investment value
print("\n--- Investment Summary ---")

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_investment += value

    print(f"{stock}: {quantity} shares × ${price} = ${value}")

print(f"\nTotal Investment Value: ${total_investment}")

# Optional file saving
save = input("\nDo you want to save the result? (yes/no): ").lower()

if save == "yes":
    file_type = input("Enter file type (txt/csv): ").lower()

    if file_type == "txt":
        with open("investment.txt", "w") as file:
            file.write("Stock Investment Summary\n")
            file.write("------------------------\n")

            for stock, quantity in portfolio.items():
                value = stock_prices[stock] * quantity
                file.write(f"{stock}: {quantity} shares = ${value}\n")

            file.write(f"\nTotal Investment Value: ${total_investment}\n")

        print("Result saved to investment.txt")

    elif file_type == "csv":
        import csv

        with open("investment.csv", "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow(["Stock", "Quantity", "Price", "Investment Value"])

            for stock, quantity in portfolio.items():
                price = stock_prices[stock]
                value = price * quantity
                writer.writerow([stock, quantity, price, value])

            writer.writerow([])
            writer.writerow(["Total Investment", "", "", total_investment])

        print("Result saved to investment.csv")

    else:
        print("Invalid file type.")
