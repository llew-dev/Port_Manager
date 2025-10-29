import yfinance as yf
import pandas as pd
import numpy as np
import datetime
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# --- 1. GET USER INPUT FOR TICKERS ---
# Ask the user for tickers, separated by commas
ticker_string = input("Enter the stock tickers, separated by a comma (e.g., AAPL,MSFT,GOOGL): ")

# Clean up the input string and split it into a list
# .strip() removes any accidental spaces at the beginning or end
# .upper() makes all tickers uppercase (like 'aapl' -> 'AAPL')
# .split(',') creates the list: 'AAPL,MSFT' -> ['AAPL', 'MSFT']
tickers = [ticker.strip().upper() for ticker in ticker_string.split(',')]

print(f"You selected these tickers: {tickers}")


# --- 2. GET USER INPUT FOR WEIGHTS ---
weights = []
total_weight = 0
num_tickers = len(tickers)

for i in range(num_tickers):
    # Ask for the weight of each ticker one by one
    while True:
        try:
            # We ask for the weight as a percentage (e.g., 40, 60)
            prompt = f"Enter the weight for {tickers[i]} (as a %): "
            weight = float(input(prompt))
            
            if weight <= 0:
                print("Weight must be greater than 0.")
            # Check if this weight would make the total go over 100
            elif weight + total_weight > 100.0:
                print(f"Error: Weights cannot exceed 100%. You only have {100.0 - total_weight:.2f}% remaining.")
            else:
                # If the weight is valid, add it to our list
                weights.append(weight)
                total_weight += weight
                break # Exit the 'while True' loop and go to the next ticker
        
        except ValueError:
            print("Invalid input. Please enter a number (e.g., 40).")

# --- 3. VALIDATE WEIGHTS AND CONVERT TO NUMPY ---
# Final check to see if the weights add up to 100
if abs(total_weight - 100.0) > 0.01: # Use a small tolerance for floating point math
    print(f"\nWarning: Your weights only add up to {total_weight:.2f}%.")
    print("This is NOT a fully invested portfolio. Proceeding anyway.")
else:
    print("\nWeights add up to 100%. Great!")

# Convert the weights from percentages (40, 60) to decimals (0.4, 0.6)
# and store them in the numpy array for our calculations.
weights = np.array(weights) / 100.0


# --- 4. SET TIME FRAME ---
end_date = datetime.date.today()
start_date = end_date - datetime.timedelta(days=365)

# --- 5. DOWNLOAD STOCK DATA ---
print("\nDownloading 1-Year of stock data...")
try:
    data = yf.download(tickers, start=start_date, end=end_date)['Close']
    # If the user enters only ONE ticker, yf.download doesn't create a
    # DataFrame in the same way. This line fixes that.
except Exception as e:
    print(f"Error downloading data: {e}")
    print("Please check your tickers and try again.")
    exit() # Stop the script if data download fails

# --- 6. CALCULATE DAILY RETURNS ---
daily_returns = data.pct_change()
daily_returns = daily_returns.dropna()

# --- 7. CALCULATE PORTFOLIO PERFORMANCE ---
# This line works perfectly, even with 1 or 100 tickers!
portfolio_daily_returns = daily_returns.dot(weights)
average_daily_return = portfolio_daily_returns.mean()
portfolio_daily_risk = portfolio_daily_returns.std()

# --- 8. ANNUALIZE THE RESULTS ---
trading_days = 252
annualised_return = average_daily_return * trading_days
annualised_volatility = portfolio_daily_risk * np.sqrt(trading_days)

# --- 9. DISPLAY THE FINAL RESULTS ---
print("\n==== Portfolio Analysis ====")
print(f"Tickers: {tickers}")
# Format the weights back to percentages for easy reading
print(f"Weights: {[f'{w*100:.0f}%' for w in weights]}")
print("\n")
print(f"Annualized Return: {annualised_return * 100:.2f}%")
print(f"Annualized Volatility (Risk): {annualised_volatility * 100:.2f}%")

