import mysql.connector

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
id = int(input("Enter sensor ID to delete: "))

# DELETE query
query = """
DELETE FROM sensor_readings
WHERE id = %s
"""

# Execute query
cursor.execute(query, (id,))
connection.commit()

if cursor.rowcount > 0:
    print("Record deleted successfully")
else:
    print("No record found with given ID")

# Close resources
cursor.close()
connection.close()
