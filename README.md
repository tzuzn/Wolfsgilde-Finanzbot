# Wolfsgilde-Finanzbot

Dieser Bot ist auf einer RaspberryPi gehosted.
Auf dem RaspberryPi werden die Datei:
```
Plugins/SimpleClans/SimpleClans.db
```
und das Verzeichnis:
```
Plugins/SimpleClans/logs/bank
```
vom Minecraft Server in 
```
/home/pi
```
kopiert.

Um die Daily message zu senden wird mithilfe von cron [discordBotDaily.py](https://github.com/tzuzn/Wolfsgilde-Finanzbot/edit/main/discordBotDaily.py) jeden Tag um 6:00 Uhr ausgeführt.
```
crontab -e
```
am ende folgende Zeile einfügen:
```
0 6 * * * \usr\bin\python3 \home\pi\discordBotDaily.py
```
