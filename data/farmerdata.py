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

# Generate random data
farmer_ids = np.arange(1, 101)
farmer_names = ["Farmer " + str(i) for i in farmer_ids]
emails = [name.lower().replace(" ", "") + "@example.com" for name in farmer_names]
phone_numbers = np.random.randint(999999, 9999999, size=100)
passwords = ["password" for _ in range(100)]

farmers_df = pd.DataFrame({
    "farmer_id": farmer_ids,
    "farmer_name": farmer_names,
    "email": emails,
    "phone_number": phone_numbers,
    "password": passwords
})

# Insert data into the database
cursor = conn.cursor()
for _, row in farmers_df.iterrows():
    sql = "INSERT INTO farmers (farmer_id, farmer_name, email, phone_number, password) VALUES (%s, %s, %s, %s, %s)"
    values = (int(row["farmer_id"]), row["farmer_name"], row["email"], str(row["phone_number"]), row["password"])
    cursor.execute(sql, values)
conn.commit()

conn.close()
