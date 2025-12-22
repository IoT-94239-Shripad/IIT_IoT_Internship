import mysql.connector
from datetime import datetime

# establish connection with mysql server
connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="smart_agriculture2",
    use_pure=True
)

sensor_id = int(input("Enter Sensor ID : "))
moisture_level = int(input("Enter Moisture Level : "))
date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

query = """
INSERT INTO soil_moisture (sensor_id, moisture_level, date_time)
VALUES (%s, %s, %s)
"""

cursor = connection.cursor()
cursor.execute(query, (sensor_id, moisture_level, date_time))
connection.commit()

cursor.close()
connection.close()

print("Record inserted successfully")
