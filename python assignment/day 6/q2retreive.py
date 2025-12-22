import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="smart_agriculture2",
    use_pure=True
)

threshold = int(input("Enter moisture threshold: "))

query = """
SELECT * FROM soil_moisture
WHERE moisture_level < %s
"""

cursor = connection.cursor()
cursor.execute(query, (threshold,))

records = cursor.fetchall()

print("Records below threshold:")
for row in records:
    print(row)

cursor.close()
connection.close()
