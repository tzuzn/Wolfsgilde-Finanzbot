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

# Query the data
c.execute("SELECT * FROM logs")
rows = c.fetchall()
for row in rows:
    print(row[1])
    print(row[2])

# Close the connection
conn.close()