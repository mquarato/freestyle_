from pandas_datareader import data
from datetime import date, timedelta
from datetime import datetime
import datetime
from dateutil.parser import parse
import csv

csv_file_path = "data/stock_prices.csv"

print("\nSTOCK PRICE LOOKUP APPLICATION")
print("Welcome! Today's date is: " +  str(datetime.date.today()))
print("\nSelect one of the following options by inputting the corresponding number: ")
print("\n1 - STOCK PRICE")
print("2 - STOCK PERFORMANCE")

operation = input("\nPlease make a selection: ")

stock_symbols = []

def price_lookup():
    while True:
        symbol = input("\nPlease select a stock by symbol or 'DONE' if there are no more items: ")
        symbol = symbol.upper()
        if symbol == "DONE":
            break
        else:
            stock_symbols.append(symbol)
    if len(stock_symbols) > 0:
        date_start = input("Please select a start date in the format yyyy-mm-dd: ")
        end_date = input("Please select an end date in the format yyyy-mm-dd: ")
        try:
            date_start = datetime.datetime.strptime(date_start, '%Y-%m-%d')
            end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        except ValueError:
            print("\nIncorrect Dates!\n")
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
        if daily_closing_prices.empty:
            print("\nThe market was closed that day. Try a different date.\n ")
        else:
            print("\nHere are the Stock Prices for the days you indicated:\n")
            print(daily_closing_prices)
            confirmation = input("\nWould you like to save this data to a file? (Y/N) ")
            confirmation = confirmation.upper()
        if confirmation == "Y":
            prices = daily_closing_prices.to_csv(csv_file_path)
            print("\nGreat! The data has been saved to data/stock_prices.csv\n")
        else:
            print("\nOK. The data is not saved\n")

    else:
        print("\nOperation not selected. Ending program.\n")

def performance():
    symbol =input("Please select a stock by symbol: ")
    symbol = symbol.upper()
    stock_symbols.append(symbol)

    date_start = input("When did you buy the stock? input in the format yyyy-mm-dd: ")
    end_date = input("When did you sell the stock? input in the format yyyy-mm-dd: ")

    date_start = datetime.datetime.strptime(date_start, '%Y-%m-%d')
    end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')

    number_of_stocks = input("Please input quantity of shares owned: ")
    number_of_stocks = float(number_of_stocks)
    data_source = 'google'

    response = data.DataReader(stock_symbols, data_source, date_start, date_start)
    response2 = data.DataReader(stock_symbols, data_source, end_date, end_date)

    daily_closing_prices = response.ix["Close"]
    daily_closing_prices2 = response2.ix["Close"]
    if daily_closing_prices.empty or daily_closing_prices2.empty:
        print("\nThe market was closed that day. Try a different date.\n ")
    else:
        print(daily_closing_prices)
        print(daily_closing_prices2)

        difference = daily_closing_prices2.values-daily_closing_prices.values
        difference = float(difference)

        perform = number_of_stocks*difference

        if daily_closing_prices2.values > daily_closing_prices.values:
            print("\nYour gain is: " + str('${0:.2f}'.format(perform)))
        else:
            print("\nYour loss is: " + str('${0:.2f}'.format(abs(perform))))

if operation == "1": price_lookup()
elif operation == "2": performance()
else:
    print("PLEASE CHOOSE ONE OF THE AVAILABLE OPERATIONS")
