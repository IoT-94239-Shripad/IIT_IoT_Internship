import mysql.connector
from datetime import datetime

# establish connection with mysql server
connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "iot_data2",
    use_pure = True
)
id = int(input("Enter id : "))
temperature = float(input("Enter temperature : "))
humidity= float(input("Enter Humidity : "))
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

query = f"insert into sensor_readings({id}, '{temperature}', '{humidity}', '{timestamp}');"

# create a cursor to execute a query
cursor = connection.cursor()

# execute a query
cursor.execute(query)

# commit your changes on mysql server
connection.commit()

# close the cursor
cursor.close()

# close the connection with mysql server
connection.close()


