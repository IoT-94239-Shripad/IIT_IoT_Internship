import mysql.connector
from datetime import datetime

# establish connection with mysql server
connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="iot_data2",
    use_pure=True
)

id = int(input("Enter id : "))
temperature = float(input("Enter temperature : "))
humidity = float(input("Enter Humidity : "))
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

query = """
INSERT INTO sensor_readings   (id, temperature, humidity, timestamp)
VALUES (%s, %s, %s, %s)
"""

cursor = connection.cursor()
cursor.execute(query, (id, temperature, humidity, timestamp))
connection.commit()

cursor.close()
connection.close()

print("Record inserted successfully")
