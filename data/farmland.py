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


farm_ids = np.arange(101, 201)
farmer_ids = np.random.choice([1, 2], size=100)
locations = np.random.choice(["Location A", "Location B", "Location C"], size=100)
soil_types = np.random.choice(["Clay", "Sandy", "Loamy"], size=100)
sizes = np.random.uniform(1, 50, size=100)
latitudes = np.random.uniform(30, 40, size=100)
longitudes = np.random.uniform(-80, -70, size=100)
temperatures = np.random.uniform(10, 30, size=100)
humidities = np.random.uniform(40, 90, size=100)
rainfalls = np.random.uniform(10, 100, size=100)

farm_lands_df = pd.DataFrame({
    "farm_id": farm_ids,
    "farmer_id": farmer_ids,
    "location": locations,
    "soil_type": soil_types,
    "size_in_acres": sizes,
    "latitude": latitudes,
    "longitude": longitudes,
    "temperature": temperatures,
    "humidity": humidities,
    "rainfall": rainfalls
})

# Get farmer ids from farmers table
cursor = conn.cursor()
cursor.execute("SELECT farmer_id FROM farmers")
farmer_ids = [row[0] for row in cursor.fetchall()]

for _, row in farm_lands_df.iterrows():
    sql = "INSERT INTO farm_lands (farm_id, farmer_id, location, soil_type, size_in_acres, latitude, longitude, temperature, humidity, rainfall) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (int(row["farm_id"]), np.random.choice(farmer_ids), row["location"], row["soil_type"], float(row["size_in_acres"]), float(row["latitude"]), float(row["longitude"]), float(row["temperature"]), float(row["humidity"]), float(row["rainfall"]))
    cursor.execute(sql, values)

conn.commit()
conn.close()
