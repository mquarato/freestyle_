from pandas_datareader import data
from datetime import date, timedelta
from datetime import datetime
import datetime
from dateutil.parser import parse
import csv

csv_file_path = "data/stock_prices.csv"

print("\nSTOCK PRICE LOOKUP APPLICATION\n")
print("Today's date is: " +  str(datetime.date.today()))

stock_symbols = []

while True:
    symbol = input("\nPlease select a stock by symbol or 'DONE' if there are no more items: ")
    if symbol == "DONE":
        break
    else:
        stock_symbols.append(symbol)

date_start = input("Please select a start date in the format yyyy-mm-dd: ")
end_date = input("Please select an end date in the format yyyy-mm-dd: ")

date_start = datetime.datetime.strptime(date_start, '%Y-%m-%d')
end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')

# COMPILE REQUEST PARAMS

data_source = 'google'

# ISSUE REQUEST

response = data.DataReader(stock_symbols, data_source, date_start, end_date)

# PARSE RESPONSE

daily_closing_prices = response.ix["Close"] # ix() is a pandas DataFrame function
print(type(daily_closing_prices))
print("\nHere are the Stock Prices for the days you indicated:\n")
print(daily_closing_prices)
confirmation = input("\nWould you like to save this data to a file? (Y/N)")
if confirmation == "Y":
    prices = daily_closing_prices.to_csv(csv_file_path)
    print("Great! The data has been saved")
else:
    print("OK. We won't save the data")
