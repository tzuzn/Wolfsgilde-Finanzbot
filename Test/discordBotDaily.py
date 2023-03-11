# coding: utf-8
import discord
from discord import app_commands
import sqlite3
from datetime import datetime, timedelta
import csv
import calendar

balance = sqlite3.connect('SimpleClans.db').cursor().execute("SELECT balance From sc_clans WHERE name = 'Wolfsgilde'").fetchall()
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

Token ="token"
#csvpath = "bank/"+yesterday() + ".csv"
csvpath = "bank/2023-02-20.csv"
date = "2023-02-20"

operation = ['DEPOSIT']
log = []
out= ""

monthname = calendar.month_name[datetime.now().month]

name = ""
amount = 0
inout = 0

moneyIn = ""
moneyOut= ""
moneyInName=""
moneyOutName=""

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
                name=row['Sender']
                amount=row['Amount']
                # Insert some data
                c.execute("INSERT INTO logs (name,amount,inout,date) VALUES (?, ?, 0, ?)", (name, amount, date))

# Commit the changes
conn.commit()

# Query the data
c.execute('SELECT * FROM logs Where date like "'+ date[:8]+'%"')
rows = c.fetchall()
for row in rows:
    if(row[3]==0):
        moneyInName+="\n"+str(row[2])
        moneyIn+="\n"+row[1]
    else:
        moneyOutName=moneyOutName.join("\n"+str(row[2]))
        moneyOut=moneyOut.join("\n"+row[1])

            
embed2=discord.Embed(title=monthname, color=0xfdfdfd)
embed2.add_field(name="Einzahlungen", value=moneyIn, inline=True)
embed2.add_field(name="", value="", inline=True)
embed2.add_field(name="Amount", value=moneyInName, inline=True)
embed2.add_field(name="Ausgaben", value=moneyOutName, inline=True)
embed2.add_field(name="", value="", inline=True)
embed2.add_field(name="Amount", value=moneyOut, inline=True)
embed2.add_field(name="Kontostand", value=str(balance).translate({ord(i): None for i in '[(,)]'}), inline=False)
embed2.set_footer(text="Wird jeden Morgen aktualisiert")

@client.event
async def on_ready():
    await tree.sync()
    print("Sending!")

    channel = client.get_channel(1062455891246456936)
    
    message = await channel.send(embed=embed2)
    message_id = ""
    message_id = message.id
    c.execute("INSERT INTO messages (message_id) VALUES (?)",(message_id,))
    
    # Close the connection
    conn.close()
    #else:
        #await channel.send("Der GildenKontostand wurde gestern mit " + str(balance).translate({ord(i): None for i in '[(,)]'})+"€ abgeschlossen.")
    print("schedule_daily_message has been sent.")
    exit()


client.run(Token)
