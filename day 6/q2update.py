import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="smart_agriculture2",
    use_pure=True
)

sensor_id = int(input("Enter Sensor ID to update: "))
new_moisture = int(input("Enter new Moisture Level: "))

query = """
UPDATE soil_moisture
SET moisture_level = %s
WHERE sensor_id = %s
"""

cursor = connection.cursor()
cursor.execute(query, (new_moisture, sensor_id))
connection.commit()

cursor.close()
connection.close()

print("Record updated successfully")
