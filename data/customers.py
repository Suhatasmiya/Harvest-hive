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

customer_ids = np.arange(1, 101)
customer_names = np.random.choice(["Alice", "Bob", "Charlie", "David", "Emily"], size=100)
emails = [name.lower() + "@example.com" for name in customer_names]
phone_numbers = np.random.randint(100000000, 999999999, size=100).astype(str)
addresses = ["Lorem ipsum" for _ in range(100)]
passwords = np.random.choice(["password123", "qwertyuiop", "123456789", "iloveyou", "letmein"], size=100)

# print(len(customer_ids))
# print(len(customer_names))
# print(len(emails))
# print(len(phone_numbers))
# print(len(addresses))
# print(len(passwords))

customers_df = pd.DataFrame({
    "customer_id": customer_ids,
    "customer_name": customer_names,
    "email": emails,
    "phone_number": phone_numbers,
    "address": addresses,
    "password": passwords
})

cursor = conn.cursor()
for _, row in customers_df.iterrows():
    sql = "INSERT INTO customers (customer_id, customer_name, email, phone_number, address, password) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (int(row["customer_id"]), row["customer_name"], row["email"], row["phone_number"], row["address"], row["password"])
    cursor.execute(sql, values)

conn.commit()
conn.close()
