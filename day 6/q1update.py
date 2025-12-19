import mysql.connector
from datetime import datetime

# Database connection
connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="iot_data2",
    use_pure=True
)

cursor = connection.cursor()

# User input
id = int(input("Enter sensor ID to update: "))
temperature = float(input("Enter new temperature: "))
humidity = float(input("Enter new humidity: "))
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# UPDATE query
query = """
UPDATE sensor_readings
SET temperature = %s,
    humidity = %s,
    timestamp = %s
WHERE id = %s
"""

# Execute query
cursor.execute(query, (temperature, humidity, timestamp, id))
connection.commit()

if cursor.rowcount > 0:
    print("Record updated successfully")
else:
    print("No record found with given ID")

# Close resources
cursor.close()
connection.close()
