# 🧾 Stock Portfolio Tracker

A simple Python program that calculates total stock investment based on hardcoded stock prices.  
Created as part of the **CodeAlpha Python Internship**.

---

## 🎯 Goal
To build a basic console-based stock tracker that:
- Takes user input for stock names and quantities.
- Uses a predefined dictionary of stock prices.
- Calculates total investment value.
- Optionally saves the result in `.txt` or `.csv` format.

---

## ⚙️ How It Works
1. Displays available stocks and their prices.  
2. You enter stock symbols (like AAPL, TSLA, MSFT) and quantities.  
3. It calculates total value per stock and the overall portfolio value.  
4. You can choose to save the summary as a file.

---

## 🧩 Example Run
=== Stock Portfolio Tracker ===

Available Stocks and Prices (hardcoded):
AAPL -> ₹180.00
TSLA -> ₹250.00
MSFT -> ₹320.00
GOOGL -> ₹135.00
AMZN -> ₹95.00

Enter stock symbol (or press Enter to finish): AAPL
Enter quantity of AAPL: 10
Added: AAPL qty=10 price=180.00 value=1800.00

Enter stock symbol (or press Enter to finish): TSLA
Enter quantity of TSLA: 4
Added: TSLA qty=4 price=250.00 value=1000.00

Enter stock symbol (or press Enter to finish):
=== Portfolio Summary ===
AAPL 10 x ₹180.00 = ₹1800.00
TSLA 4 x ₹250.00 = ₹1000.00

Total Investment: ₹2800.00


---

## 🧠 Key Concepts Used
- **dictionary** → stores stock names and prices  
- **input/output** → takes user input via console  
- **basic arithmetic** → computes total values  
- **file handling** *(optional)* → saves results in `.txt` or `.csv`  

---

## 🚀 How to Run
1. Install Python 3 if not already installed.  
2. Save the file as `stock_tracker.py`.  
3. Open the terminal or command prompt in that folder.  
4. Run:
   ```bash
   python stock_tracker.py

📁 Files in This Repository
stock_tracker.py     # Main program
README.md            # Project details

🧷 Author
Samridha Das
B.Tech CSE (AIML) — CodeAlpha Internship Project