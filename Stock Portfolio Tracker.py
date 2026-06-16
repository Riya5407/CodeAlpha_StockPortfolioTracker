#Stock Portfolio Tracker

stock_prices = {
    "AAPL" : 180,
    "GOOGL" : 2800,
    "AMZN" : 3500,
    "TSLA" : 700,
    "MSFT" : 3000
}

def calculate_portfolio_value(portfolio):
    total_value = 0
    for stock, shares in portfolio.items():
        if stock in stock_prices:
            total_value += stock_prices[stock] * shares
    return total_value


portfolio = {}
print("========= Stock Portfolio Tracker ========")

print("Available stocks:")
for stock in stock_prices:
    print(f" - {stock}")


while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock symbol not recognized. Please try again.")
        continue

    shares = int(input("Enter quantity: "))

    portfolio[stock] = portfolio.get(stock,0) + shares

total_value = calculate_portfolio_value(portfolio)

print("========= Your Portfolio Summary =========")

for stock, shares in portfolio.items():
    print(f"{stock} | Quantity:{shares} | Price: ${stock_prices[stock]:.2f} | Value: ${stock_prices[stock] * shares:.2f}")

print(f"Total Portfolio Value: ${total_value:.2f}")

#save to the file
with open("portfolio_summary.txt", "w") as file:
    file.write("========= Your Portfolio Summary =========\n")
    for stock, shares in portfolio.items():
        file.write(f"{stock}: {shares} shares\n")
        file.write(f"Current Price: ${stock_prices[stock]:.2f}\n")
        file.write(f"Value: ${stock_prices[stock] * shares:.2f}\n")
    file.write(f"Total Portfolio Value: ${total_value:.2f}\n")

print("Portfolio summary saved to portfolio_summary.txt")