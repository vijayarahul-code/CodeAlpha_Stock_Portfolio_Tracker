# Stock Portfolio Tracker

stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 150
}

total_amount = 0

print("Welcome to Stock Portfolio Tracker")

while True:
    stock_name = input("Enter stock name (or type EXIT to finish): ").upper()

    if stock_name == "EXIT":
        break

    if stock_name in stocks:
        quantity = int(input("Enter quantity: "))

        price = stocks[stock_name]
        investment = price * quantity

        total_amount = total_amount + investment

        print("Stock value:", investment)

    else:
        print("Stock not available")

print("\nTotal Investment Amount:", total_amount)

# Saving result in a text file
file = open("portfolio_result.txt", "w")

file.write("Total Investment Amount: " + str(total_amount))

file.close()

print("Result saved in portfolio_result.txt")