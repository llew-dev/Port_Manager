{\rtf1\ansi\ansicpg1252\cocoartf2865
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\froman\fcharset0 Times-Roman;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Interactive Portfolio Risk & Return Calculator\
\
This is a portfolio analysis program written in Python, that analyses the risk and return profile of a user-defined stock portfolio.\
\
The script prompts the user to enter any number of stock tickers and their desired portfolio weights. It then downloads the last 365 days of stock data and calculates two key financial metrics: **Annualised Return** and **Annualised Volatility (Risk)**.\
\
This project demonstrates skills in data-handling with `pandas`, API data retrieval with `yfinance`, and numerical computing with `numpy`.\
\
---\
\
## Key Features\
\
* **Interactive User Input:** Asks for tickers and weights, making the tool flexible for any portfolio.\
* **Robust Input Validation:**\
    * Uses a `try/except` block to ensure weight inputs are valid numbers.\
    * Uses a `while` loop to re-prompt the user if an input is invalid (e.g., text instead of a number).\
    * Validates that portfolio weights do not exceed 100%.\
* **Dynamic Data Fetching:** Downloads the most recent 1-year data from Yahoo! Finance, so the analysis is always up-to-date.\
* **Core Financial Analysis:** Implements the standard industry formulas for calculating portfolio return and volatility.\
* **Clean User Experience:** Suppresses the `yfinance` `FutureWarning` to provide a clean, professional-looking output in the terminal.\
\
---\
\
## How It Works: The Data Pipeline\
\
1.  **Input:** Gathers stock tickers (e.g., `JPM, AAPL, MSFT`) and their weights (e.g., `40`, `30`, `30`) from the user.\
2.  **Data Download:** Uses `yfinance.download()` to fetch the daily 
\f1 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 `\'92
\f0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 Close
\f1 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 \'92`
\f0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0  price for all tickers from one year ago to today's date.\
3.  **Calculate Daily Returns:** Uses `pandas.pct_change()` to convert the table of prices into a table of daily percentage returns.\
4.  **Calculate Portfolio Daily Return:** Uses `numpy.dot()` to calculate the weighted average return of the entire portfolio for every single day in the dataset.\
5.  **Analyze Metrics:**\
    * Calculates the **average daily return** (`.mean()`).\
    * Calculates the **daily volatility**, or risk, using the **standard deviation** (`.std()`).\
6.  **Annualise & Report:** Scales these daily figures to annual figures and prints the final, formatted analysis to the user.\
\
---\
\
## Core Concepts & Calculations \
\
This project relies on foundational principles of quantitative finance.\
\
### Portfolio Daily Return\
The daily return of the portfolio is the weighted sum of the individual asset returns. This is calculated for every day in the dataset.\
\
```\
Portfolio Daily Return = (Return_Stock_A * Weight_A) + (Return_Stock_B * Weight_B) + ...\
```\
This is efficiently computed using the `daily_returns.dot(weights)` method.\
\
### Annualised Return\
To make the daily return figure useful, we annualise it. This is achieved by multiplying the average daily return by the number of trading days in a year (the standard practice is 252).\
\
* `average_daily_return = portfolio_daily_returns.mean()`\
* `annualized_return = average_daily_return * 252`\
\
### Annualised Volatility (Risk)\
Volatility is the standard deviation of the returns, which measures how much the portfolio's value "bounces around" its average. It is the most common measure of financial risk.\
\
Crucially, **risk does not scale linearly with time**. It scales with the **square root of time**. Therefore, we annualise the daily standard deviation by multiplying it by the square root of 252.\
\
* `daily_risk = portfolio_daily_returns.std()`\
* `annualized_volatility = daily_risk * numpy.sqrt(252)`\
\
---\
\
## How to Run This Project\
\
1.  **Ensure Python is installed.**\
\
2.  **Install the required libraries:**\
    Open your terminal or command prompt and run:\
    ```bash\
    pip install yfinance pandas numpy\
    ```\
\
3.  **Save the Code:**\
    Save the project code as `portfolio.py` (or any `.py` name you choose).\
\
4.  **Run the script:**\
    In the same terminal, navigate to the folder where you saved the file and run:\
    ```bash\
    python portfolio.py\
    ```\
5.  **Follow the prompts:**\
    The script will ask you for your tickers and weights, and then it will print the final analysis.\
\
    **Example Output:**\
    ```\
    Enter the stock tickers, separated by a comma (e.g., AAPL,MSFT,GOOGL): JPM,GOOGL\
    You selected these tickers: ['JPM', 'GOOGL']\
    Enter the weight for JPM (as a %): 60\
    Enter the weight for GOOGL (as a %): 40\
    \
    Weights add up to 100%. Great!\
    \
    Downloading 1-Year of stock data...\
    [*********************100%***********************]  2 of 2 completed\
    \
    --- Portfolio Analysis ---\
    Tickers: ['JPM', 'GOOGL']\
    Weights: ['60%', '40%']\
    \
    Annualised Return: 14.82%\
    Annualised Volatility (Risk): 21.35%\
    ```}