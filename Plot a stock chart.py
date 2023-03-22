#stock chart plot. Indian it seems
import yfinance as yf
import matplotlib.pyplot as plt

#download historical data of STOCK.NS
ticker = input("Enter Stock code Name : ")
data = yf.download(ticker, start="2021-01-01", end="2023-03-13")

#plot the stock chart
plt.figure(figsize=(10, 5))
plt.plot(data["Close"])
plt.title(f"{ticker} Stock Chart")
plt.xlabel("Date")
plt.ylabel("Price (INR)")
plt.show()