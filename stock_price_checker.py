#Script to pull stock prices and show on a chart from Yahoo Finance for a list
#of mutual funds.

#Libraries
import yfinance as yf
from matplotlib import pyplot as plt


ticker_list = ['LIKKX', 'LINKX', '0P0000IUYI.TO', '0P0000IUYJ.TO','0P0000IUYH.TO' ]
stock_names = ['BlackRock Lifepath 2040', 'BlackRock Lifepath 2030', 'TD Comfort Balanced Growth',
               'TD Comfort Balanced', 'TD Comfort Growth']

#Create a dictionary of stock names with their ticker symbols.
stocks_dict = dict(zip(ticker_list, stock_names))


#Create a a plot to show stock prices for all funds for the year to date.
plt.figure(figsize=(10,5))
for key, value in stocks_dict.items():
    ticker = yf.Ticker(key)
    stock_df = ticker.history(period="ytd")
    stock_df['Close'].plot(title= 'Fund Stock Price Chart', ylabel='Stock Price ($)', label=f'{value}', legend=True)

plt.legend(bbox_to_anchor =(1, 0.65))
plt.tight_layout()

#Save stock prices chart to a PNG file.
plt.savefig('Fund_stock_prices_2022_YTD.png')
