import csv
from pandas_datareader import data
from datetime import date, timedelta

daily_closing_prices = []
csv_file_path = "data/stock_prices.csv"
# symbols = input('Enter Symbol: ')

#with open(csv_file_path, "r") as csv_file:
#    reader = csv.reader(csv_file)
#    for row in reader:
#        daily_closing_prices.append(row)
# COMPILE REQUEST PARAMS

stock_symbol = input("Enter stock symbol:")
symbols = [stock_symbol]
data_source = 'yahoo'
start = str(date.today() - timedelta(days=30)) #> '2017-07-09'
end = str(date.today()) #> '2017-07-24'

# ISSUE REQUEST
# ... see docs at https://pandas-datareader.readthedocs.io/en/latest/remote_data.html

response = data.DataReader(symbols, data_source, start, end)

# PARSE RESPONSE

daily_closing_prices = response.ix["Close"] # ix() is a pandas DataFrame function

print(daily_closing_prices)
daily_closing_prices.to_csv(csv_file_path)

#def writerows(self,rows):
#    for row in rows:
#        self.writerow(row)

#    writer = csv.writer(csv_file, delimiter=' ')
#    writer.writerows(daily_closing_prices)

# response.to_csv('/Users/jascharf/Desktop/Freestyle/data/stock_prices.csv')
#> AAPL   MSFT
#> Date
#> 2017-07-10  145.06  69.98
#> 2017-07-11  145.53  69.99
#> 2017-07-12  145.74  71.15
#> 2017-07-13  147.77  71.77
#> 2017-07-14  149.04  72.78
#> 2017-07-17  149.56  73.35
#> 2017-07-18  150.08  73.30
#> 2017-07-19  151.02  73.86
#> 2017-07-20  150.34  74.22
