import numpy as np
import pandas as pd
import pymysql

# Connect to the database
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="harvest1"
)

# Fetch all crop and customer IDs from the respective tables
crops_df = pd.read_sql("SELECT crop_id FROM crops", conn)
customers_df = pd.read_sql("SELECT customer_id FROM customers", conn)

# Generate random order IDs and quantities
order_ids = np.arange(101, 201)
quantities = np.random.randint(1, 50, size=100)

# Randomly assign crop and customer IDs to each order
crop_ids = np.random.choice(crops_df['crop_id'], size=100)
customer_ids = np.random.choice(customers_df['customer_id'], size=100)

# Fetch crop prices and calculate total price for each order
cursor = conn.cursor()
total_prices = []
for crop_id, quantity in zip(crop_ids, quantities):
    cursor.execute("SELECT crop_price FROM crops WHERE crop_id=%s", (crop_id,))
    crop_price = cursor.fetchone()[0]
    total_prices.append(crop_price * quantity)

# Generate latitude and longitude coordinates for each order
latitudes = np.random.uniform(37, 42, size=100)
longitudes = np.random.uniform(-120, -75, size=100)

# Create a DataFrame of order data
orders_df = pd.DataFrame({
    "order_id": order_ids,
    "customer_id": customer_ids,
    "crop_id": crop_ids,
    "order_date": pd.Timestamp.now(),
    "quantity": quantities,
    "total_price": total_prices,
    "latitude": latitudes,
    "longitude": longitudes
})

# Insert the order data into the database
cursor = conn.cursor()
for _, row in orders_df.iterrows():
    sql = "INSERT INTO orders (order_id, customer_id, crop_id, order_date, quantity, total_price, latitude, longitude) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    values = (int(row["order_id"]), int(row["customer_id"]), int(row["crop_id"]), row["order_date"], int(row["quantity"]), float(row["total_price"]), float(row["latitude"]), float(row["longitude"]))
    cursor.execute(sql, values)
conn.commit()

# Close the database connection
conn.close()
