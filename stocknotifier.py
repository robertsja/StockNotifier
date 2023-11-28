import pandas
import yfinance as yf

aapl = yf.Ticker("AAPL")

# Balance sheet and dividends
print(aapl.quarterly_balancesheet)