import csv

with open('colon_delimited_stock_prices.txt', 'rb') as f: 
    reader = csv.DictReader(f, delimiter=':')
    for row in reader:
        date = row["date"]
        symbol = row["symbol"]
        closing_price = float(row["closing_price"]) 
        print(date, symbol, closing_price)