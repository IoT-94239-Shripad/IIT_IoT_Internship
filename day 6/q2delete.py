import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="smart_agriculture2",
    use_pure=True
)

sensor_id = int(input("Enter Sensor ID to delete: "))

query = "DELETE FROM soil_moisture WHERE sensor_id = %s"

cursor = connection.cursor()
cursor.execute(query, (sensor_id,))
connection.commit()

cursor.close()
connection.close()

print("Record deleted successfully")
