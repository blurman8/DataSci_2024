import requests
from bs4 import BeautifulSoup
import csv
 
def write_to_csv(product_data):
    # Open the CSV file for writing
    with open('./products.csv', 'w', newline='', encoding='utf-8') as csvfile:
        # Define the field names for the CSV header
        fieldnames = ['Product Name', 'Price']
         # Create a DictWriter object
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
      
        # Write CSV header
        writer.writeheader()
        
        # Loop through the product data list
        for product in product_data:
            # Write a new row with product name and price
            writer.writerow({'Product Name': product['name'], 'Price': product['price']})
 
base_url = 'https://scrapingclub.com/exercise/list_infinite_scroll/'
page_number = 1  # Start with the base URL
total_pages = 6 
product_data = []
 
while page_number <= total_pages:
    # Construct ajax request URL
    url = f'{base_url}?page={page_number}'
    
    # Make GET request
    response = requests.get(url)
    
    # Retrieve the response content
    html_content = response.text
        
    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(html_content, 'html.parser')
        
    # Extract product names and prices
    products = soup.select('div.p-4 h4 > a')
    prices = soup.select('div.p-4 h5')
        
    # Collect product information
    for product, price in zip(products, prices):
        product_name = product.get_text(strip=True)
        product_price = price.get_text(strip=True)
        
        #add data to product_data []
        product_data.append({'name': product_name, 'price': product_price})   
        print ({product_name, product_price})  
    # Move to the next page
    page_number += 1
 
# Call the function to write data to CSV
write_to_csv(product_data)
