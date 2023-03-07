# coding: utf-8
import sqlite3
import csv

name = ""
amount = 0
inout = 0

# Connect to the database (creates a new database if it doesn't already exist)
conn = sqlite3.connect("discordBot.db")

# Create a table
c = conn.cursor()

csvpath = "bank/2023-02-20.csv"
operation = ['DEPOSIT']

with open(csvpath, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # Iterate over each row in the CSV file
    for row in csv_reader:

        # Check if the value in the 'column_name' column is equal to 'target_value'
        if row['Operation'] in operation and row['Clan Name'] == 'Wolfsgilde':
            if row['Operation'] == 'DEPOSIT':
            #    log.append(row['Sender']+' hat '+row['Amount']+'€ eingezahlt.')
            #    print(row['Sender']+' hat '+row['Amount']+'€ eingezahlt.')
                name=row['Sender']
                amount=row['Amount']
                # Insert some data
                c.execute("INSERT INTO logs (name,amount,inout) VALUES (?, ?, 0)", (name, amount))

# Commit the changes
conn.commit()

# Query the data
c.execute("SELECT * FROM logs")
rows = c.fetchall()
for row in rows:
    print(row['name'])

# Close the connection
conn.close()
