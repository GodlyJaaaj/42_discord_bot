from datetime import datetime
import discord
async def send_countdown_Message(channel, event, command):
    global embed_message
    current_Date = datetime.now()
    start_Date = event['start_Date']
    end_Date = event['end_Date']
    id_Check_Date = event['id_Check_Date']
    id_Check_End_Date = event['id_Check_End_Date']
    time_Left = start_Date - current_Date if current_Date < start_Date else end_Date - current_Date
    days = time_Left.days
    hours, remainder = divmod(time_Left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    if current_Date.date() < start_Date.date():
        embed_message = discord.Embed(title=f"🏊‍♂️ La piscine de {command} 🏊‍♂️", color=0xc4c700)
        embed_message.add_field(name="La piscine n'a pas encore commencé !",
                                value=f"⏳ Il reste **{days} jours**, **{hours} heures**,"
                                      f" **{minutes} minutes**, et **{seconds} secondes** avant"
                                      f" la piscine de **{command}** à l'école 42! 🏊‍♂️\nPensez à"
                                      f" prendre votre bonnet !💧", inline=False)
    elif current_Date.date() >= start_Date.date() and current_Date.date() <= end_Date.date():
        embed_message = discord.Embed(title=f"🏊‍♂️ La piscine de {command} 🏊‍♂️", color=0x31a300)
        embed_message.add_field(name="✅ La piscine de {command} a commencé ! :)", value="", inline=False)
    elif current_Date.date() >= end_Date.date():
        embed_message = discord.Embed(title=f"🏊‍♂️ La piscine de {command} 🏊‍♂️", color=0xe60000)
        embed_message.add_field(name=f"🔴 La piscine de {command} est terminée ! :)", value="", inline=False)
    if current_Date.date() < id_Check_Date.date():
        embed_message.add_field(name=f"⏳ Vérification d'identité non commencée !",
                                value=f"La vérification d'identité pour la piscine de {command} n'a pas encore commencé !",
                                inline=False)
        embed_message.add_field(name=f"Date prévu pour la vérification :", value=f"{id_Check_Date.strftime('%d-%m-%Y')}", inline=False)
    if current_Date.date() >= id_Check_Date.date() and current_Date.date() <= id_Check_End_Date.date():
        embed_message.add_field(name=f"✅ ⚠️ Vérification d'identité en cours ! ✅ ⚠️",
                                value=f"N'oubliez pas de vérifier votre identité pour la piscine de {command}! ⚠️", inline=False)
    elif current_Date.date() >= id_Check_End_Date.date():
        embed_message.add_field(name=f"🔴 ⚠️ Vérification d'identité terminée ! 🔴 ⚠️",
                                value=f"La vérification d'identité pour la piscine de {command} est terminée ! ⚠️",
                                inline=False)
    await channel.send(embed=embed_message)
