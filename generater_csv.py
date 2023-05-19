import csv
import random

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

with open('sales_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Product', 'Category', 'Price', 'Quantity', 'Sales', 'Month'])

    products = ['Apple', 'Samsung', 'Sony', 'HP', 'Nike']
    categories = ['iPhone', 'Galaxy', 'PlayStation', 'Laptop', 'Shoes']

    for _ in range(1000):
        product = random.choice(products)
        category = random.choice(categories)
        price = random.randint(100, 1000)
        quantity = random.randint(1, 10)
        sales = price * quantity
        month = random.choice(months)

        writer.writerow([product, category, price, quantity, sales, month])
