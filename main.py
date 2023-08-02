import discord
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from commands.countdown_Message import send_countdown_Message
from env.load_env import TOKEN

#--------->  Private token ⚠️ do not share in public
DISCORD_TOKEN = TOKEN
CHANNEL_ID = '1135894155374116914' #---------> this is the channel where the bot send message
CHANNEL_OBJECT = discord.Object(id=CHANNEL_ID)
#---------> configuring client
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
my_Activity_Status = ("6 x 7 = 42,  maintened by Sebou") #---------> discord Status
my_Status = discord.Status.online
#---------> connection du bot et démarrage de la boucle
@client.event
async def on_ready():
    print(f'✅ Succefully Logged in as {client.user.name} in the serveur ')
    print(f'✅ Succefully launch discord activity')
    print(f'✅ Listen commands start')
    activity=discord.Activity(type=discord.ActivityType.listening, name=my_Activity_Status)
    await client.change_presence(status=my_Status, activity=activity)
    scheduler = AsyncIOScheduler()
    scheduler.add_job(send_all_date_reminders, CronTrigger(hour=12, minute=0, second=0))
    scheduler.start()
#---------> event date :
events = [
    {
        'name': 'juillet',
        'start_Date': datetime(2023, 7, 3, 9, 42, 0),
        'end_Date': datetime(2023, 7, 28, 18, 0, 0),
        'id_Check_Date': datetime(2023, 6, 28, 15, 0, 0),
        'id_Check_End_Date': datetime(2023, 7, 2, 15, 0, 0)
    },
    {
        'name': 'août',
        'start_Date': datetime(2023, 8, 7, 9, 42, 0),
        'end_Date': datetime(2023, 9, 1, 18, 0, 0),
        'id_Check_Date': datetime(2023, 8, 2, 15, 0, 0),
        'id_Check_End_Date': datetime(2023, 8, 3, 15, 0, 0)
    },
    {
        'name': 'septembre',
        'start_Date': datetime(2023, 9, 1, 9, 42, 0),
        'end_Date': datetime(2023, 10, 1, 18, 0, 0),
        'id_Check_Date': datetime(2023, 9, 1, 15, 0, 0),
        'id_Check_End_Date': datetime(2023, 9, 3, 15, 0, 0)
    }
]
#---------> bot command :
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$42alldays'):
        for event in events:
            await send_countdown_Message(message.channel, event, event['name'])

#---------> send message to the channel
async def send_all_date_reminders():
    for event in events:
        await send_countdown_Message(CHANNEL_OBJECT, event, event['name'])

client.run(DISCORD_TOKEN)