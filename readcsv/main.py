import csv

def read_csv_file(file_name):
    data = []
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def calculate_total_sales(data):
    total_sales = 0
    for row in data:
        quantity = int(row['quantity'])
        total_sales += quantity
    return total_sales

def find_highest_sales_transaction(data):
    highest_sales_transaction = max(data, key=lambda x: int(x['quantity']))
    return highest_sales_transaction

def count_transactions(data):
    transaction_count = len(data)
    return transaction_count

def find_sold_products(data):
    sold_products = set()
    for row in data:
        product = row['product']
        sold_products.add(product)
    return list(sold_products)

# Using the defined functions above
csv_file_name = 'data.csv'
csv_data = read_csv_file(csv_file_name)

total_sales = calculate_total_sales(csv_data)
print(f"Total sales: {total_sales}")

highest_sales_transaction = find_highest_sales_transaction(csv_data)
print("Transaction with the highest sales:")
print(highest_sales_transaction)

transaction_count = count_transactions(csv_data)
print(f"Transaction count: {transaction_count}")

sold_products = find_sold_products(csv_data)
print("List of sold products:")
for product in sold_products:
    print(product)
