import csv
import sqlite3

connection = sqlite3.connect("degress.db")
cursor = connection.cursor()

# Table Definition
create_table = '''CREATE TABLE health(
                age VARCHAR(10),
                cholesterol VARCHAR(10),
                body_pressure VARCHAR(10)
                );
                '''

# Creating the table into our database
# Comment out if table already exists
# cursor.execute(create_table)

# Opening the person-records.csv file
file = open('./dev-data/dataset20231130.csv')

# Reading data
contents = csv.reader(file)

# INSERT SQL query
insert_records = "INSERT INTO health (age, cholesterol, body_pressure) VALUES(?, ?, ?)"

# Importing data
cursor.executemany(insert_records, contents)

# SELECT SQL query
select_records = "SELECT * from health"

# Selecting all data
records = cursor.execute(select_records).fetchall()

# Output to the console
for r in records:
    print(r)

# Committing the changes
connection.commit()

#Closing the db operations
connection.close()