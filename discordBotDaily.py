import discord
from discord import app_commands
import sqlite3
from datetime import datetime, timedelta
import csv

def yesterday(frmt='%Y-%m-%d', string=True):
    yesterday = datetime.now() - timedelta(1)
    if string:
        return yesterday.strftime(frmt)
    return yesterday

balance = sqlite3.connect('SimpleClans.db').cursor().execute("SELECT balance From sc_clans WHERE name = 'Wolfsgilde'").fetchall()
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

csvpath = "bank/"+yesterday() + ".csv"
#csvpath = "bank/2023-02-20.csv"
operation = ['DEPOSIT']
log = []
out= ""



# Open the CSV file
with open(csvpath, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # Iterate over each row in the CSV file
    for row in csv_reader:

        # Check if the value in the 'column_name' column is equal to 'target_value'
        if row['Operation'] in operation and row['Clan Name'] == 'Wolfsgilde':
            if row['Operation'] == 'DEPOSIT':
                log.append(row['Sender']+' hat '+row['Amount']+'€ eingezahlt.')
            


@client.event
async def on_ready():
    await tree.sync()
    print("Sending!")

    channel = client.get_channel(1076856398450786344)
    if(log):
        out = "\n".join(log)
        await channel.send(yesterday()+"\n"+out)
    else:
        await channel.send(yesterday()+"\nEs gabe keine Ein/Auszahlungen.")
        await channel.send("Der GildenKontostand wurde gestern mit " + str(balance).translate({ord(i): None for i in '[(,)]'})+"€ abgeschlossen.")
    print("schedule_daily_message has been sent.")

    exit()

client.run("token")