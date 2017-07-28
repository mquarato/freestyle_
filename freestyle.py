from pandas_datareader import data
from datetime import date, timedelta
from datetime import datetime
import datetime
from dateutil.parser import parse
import csv

csv_file_path = "data/stock_prices.csv"

print("\nSTOCK PRICE LOOKUP APPLICATION")
print("Welcome! Today's date is: " +  str(datetime.date.today()))
print("\nPlease select one of the following options by inputting the corresponding number: ")
print("\n1 - STOCK PRICE")
print("2 - STOCK PERFORMANCE")

operation = input("")

stock_symbols = []
prices = []

def price_lookup():
    while True:
        symbol = input("\nPlease select a stock by symbol or 'DONE' if there are no more items: ")
        symbol = symbol.upper()
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

    print("\nHere are the Stock Prices for the days you indicated:\n")
    print(daily_closing_prices)
    confirmation = input("\nWould you like to save this data to a file? (Y/N) ")
    if confirmation == "Y":
        prices = daily_closing_prices.to_csv(csv_file_path)
        print("Great! The data has been saved")
    else:
        print("OK. The data is not saved")

def performance():
    symbol =input("Please select a stock by symbol: ")
    symbol = symbol.upper()
    stock_symbols.append(symbol)

    date_start = input("Please select a start date in the format yyyy-mm-dd: ")
    end_date = input("Please select an end date in the format yyyy-mm-dd: ")

    date_start = datetime.datetime.strptime(date_start, '%Y-%m-%d')
    end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')

    number_of_stocks = input("Please input number of stocks owned: ")
    number_of_stocks = float(number_of_stocks)
    data_source = 'google'

    response = data.DataReader(stock_symbols, data_source, date_start, date_start)
    response2 = data.DataReader(stock_symbols, data_source, end_date, end_date)
    
    daily_closing_prices = response.ix["Close"]
    daily_closing_prices2 = response2.ix["Close"]
    print(daily_closing_prices)
    print(daily_closing_prices2)

    difference = daily_closing_prices2.values-daily_closing_prices.values
    difference = float(difference)

    perform = number_of_stocks*difference
    perform = '${0:.2f}'.format(perform)
    print("\nYour gain or loss is: " + str(perform))

if operation == "1": price_lookup()
elif operation == "2": performance()
else:
    print("PLEASE CHOOSE ONE OF THE AVAILABLE OPERATIONS")
