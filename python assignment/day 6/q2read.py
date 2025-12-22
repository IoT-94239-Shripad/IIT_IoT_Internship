import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="smart_agriculture2",
    use_pure=True
)

cursor = connection.cursor()

query = "SELECT * FROM soil_moisture"
cursor.execute(query)

records = cursor.fetchall()

print("SensorID  Moisture  Date & Time")
for row in records:
    print(row)

cursor.close()
connection.close()
