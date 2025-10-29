# stock_tracker.py
import csv
import os
from datetime import datetime

stock_prices = {
    "AAPL": 180.0,
    "TSLA": 250.0,
    "MSFT": 320.0,
    "GOOGL": 135.0,
    "AMZN": 95.0
}

def get_stock_symbol():
    s = input("Enter stock symbol (or press Enter to finish): ").strip().upper()
    return s

def get_positive_int(prompt):
    while True:
        val = input(prompt).strip()
        if not val:
            print("Please enter a number.")
            continue
        if not val.isdigit():
            print("Enter a whole positive number (0 or greater).")
            continue
        return int(val)

def show_available_prices():
    print("Available Stocks and Prices (hardcoded):")
    for sym, price in stock_prices.items():
        print(f"  {sym:6} -> ₹{price:.2f}")
    print()

def main():
    print("-------- Stock Portfolio Tracker --------\n")
    show_available_prices()

    portfolio = [] 

    while True:
        sym = get_stock_symbol()
        if sym == "":
            break

        if sym not in stock_prices:
            print(f"Symbol '{sym}' not in price list.")

            add_anyway = input("Do you want to add it with a custom price? (y/N): ").strip().lower()

            if add_anyway == 'y':
                while True:
                    try:
                        custom_price = float(input("Enter custom price per share: ").strip())
                        if custom_price < 0:
                            print("Price cannot be negative.")
                            continue
                        stock_prices[sym] = custom_price
                        break
                    except ValueError:
                        print("Enter a valid number like 123.45")
            else:
                print("Skip this symbol. Enter another or press Enter to finish.")
                continue

        qty = get_positive_int(f"Enter quantity of {sym}: ")
        price = stock_prices[sym]
        total_val = qty * price
        portfolio.append((sym, qty, price, total_val))
        print(f"Added: {sym}  qty={qty}  price={price:.2f}  value={total_val:.2f}\n")

    if not portfolio:
        print("No stocks entered. Exiting.")
        return

    
    print("-------- Portfolio Summary --------\n")
    total_investment = 0.0
    print(f"{'Symbol':6} {'Qty':>5} {'Price':>10} {'Value':>12}")
    print("-" * 38)
    for sym, qty, price, value in portfolio:
        total_investment += value
        print(f"{sym:6} {qty:5d} {price:10.2f} {value:12.2f}")
    print("-" * 38)
    print(f"{'TOTAL':6} {'':5s} {'':10s} {total_investment:12.2f}\n")

    choice = input("Save result? (1) CSV  (2) TXT  (Enter to skip): ").strip()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    if choice == '1':
        fname = f"portfolio_{timestamp}.csv"
        try:
            with open(fname, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Symbol", "Quantity", "PricePerShare", "Value"])
                for row in portfolio:
                    writer.writerow(row)
                writer.writerow([])
                writer.writerow(["TOTAL", "", "", f"{total_investment:.2f}"])
            print(f"Saved CSV -> {fname}")
        except Exception as e:
            print("Failed to save CSV:", e)
    elif choice == '2':
        fname = f"portfolio_{timestamp}.txt"
        try:
            with open(fname, 'w') as f:
                f.write("Portfolio Summary\n")
                f.write("=" * 30 + "\n")
                for sym, qty, price, value in portfolio:
                    f.write(f"{sym}  qty={qty}  price={price:.2f}  value={value:.2f}\n")
                f.write("\n")
                f.write(f"TOTAL INVESTMENT: {total_investment:.2f}\n")
            print(f"Saved TXT -> {fname}")
        except Exception as e:
            print("Failed to save TXT:", e)
    else:
        print("Not saved. Done.")

if __name__ == "__main__":
    main()
