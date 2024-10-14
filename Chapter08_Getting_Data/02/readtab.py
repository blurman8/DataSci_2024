import csv
with open('tab_delimited_stock_prices.txt', 'rb') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        rdate = row[0]
        symbol = row[1]
        closing_price = float(row[2])

        print (rdate , symbol , closing_price) 