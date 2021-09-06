import os
import discord
import time
import requests
import keep_alive
import json
import random
from discord.ext import commands
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

bot = commands.Bot(command_prefix="$")

keep_alive.keep_alive()


def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]["q"] + " -" + json_data[0]["a"]
  return (quote)

@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Messages of Gazette'))
  print("We have logged in as {0.user}".format(bot))

@bot.command(pass_context=True)
async def ping(ctx):
	await ctx.channel.send("pong")

@bot.command()
async def add(left : int, right : int):
  await bot.say(left + right)

@bot.event
async def on_message(message):
  if message.author == bot.user:
    return

  msg = message.content

  if message.content.startswith("gtell"):
    s = message.content
    x = int(s[8:26])
    channel = bot.get_channel(x)
    s = s[28:]
    await channel.trigger_typing()
    time.sleep(3)
    
    if message.attachments :
      for attachment in message.attachments:
        file = attachment.filename
        await attachment.save(file)
        await channel.send(file=discord.File(file))
        os.remove(file)
    if len(s) > 0:
      await channel.send(s)
      
    await message.add_reaction('👍')

  if message.content.startswith("Hello There!!"):
    await message.channel.send("General Kenobi")

  inspire = ["inspire"]
  if any(word in msg for word in inspire):
    quote = get_quote()
    await message.channel.send(quote)

  hillo = ["Hi", "hello", "Hello", "namasthe", "namaskaram", "holla", "bonjour","hlo"]
  if any(word in msg for word in hillo):
    options = ["Namsthe Ji :pray:", "Hey buddy, how are you?","Keep aside Hello & hi and come to the point","Nashta paani ho gaya ?", "https://tenor.com/bEhdp.gif","Life hi zindagi ho gaya, aur yeh abhi bhi hi hello namasthe main atka hai","Apna Bhai agaya","hi","Pad likh ke IAS IPS bano bey Hi bye bad main kar lena ","salam walekum :raised_hand:", "https://tenor.com/XCJm.gif","https://tenor.com/MZPE.gif", "https://tenor.com/bpIpK.gif","https://tenor.com/bpmSf.gif"]
    await message.channel.trigger_typing()
    time.sleep(1)
    await message.reply(random.choice(options))

  join = ["Join", "meet", "Meet"]
  if any(word in msg for word in join):
    please = ["Meet main mai bhi join ho saktha hu kya please?", ":+1:", "coming","5 mins wait please","I can join but my developer did not give me vocal cords :sad:","Have some work at home, you guys carry on", "Ghar wale ane nahi denge"]
    await message.channel.send(random.choice(please))

  mawa = ["bhai "]
  if any(word in msg for word in mawa):
    mwa = ["bhai nahi bro **Boii**"]
    await message.reply(random.choice(mwa))

  op = ["op ", "OP "]
  if any(word in msg for word in op):
    opx = ["https://tenor.com/ux9D.gif"]
    await message.reply(random.choice(opx))

  mass = ["badiya"]
  if any(word in msg for word in mass):
    mowa = ["Yeh tho creativity ki hadd ho gayi yaar"]
    await message.channel.send(random.choice(mowa))

  list1 = ["https://tenor.com/2TXZ.gif", "https://tenor.com/94zt.gif","https://tenor.com/6a41.gif", "https://tenor.com/WzNB.gif","https://tenor.com/bjjDn.gif", "https://tenor.com/bAXm4.gif","https://tenor.com/6iHL.gif","https://tenor.com/bBGUg.gif"]
    
  list2 = ["Bot ko tang kar raho, tumhara network hack karna koi badi bath nahi hai mere liye","Don't trouble the trouble if you trouble the trouble the trouble will trouble you.","Thumko tho fansi hogi","Chote chote batho kelieye disturb mat kar muje","Hoof ab merko intrest na raha","I wont be doing this job anymore","Get a life dude","0.25x mai class sunvauga ab english ka pura agar tag stop nahi kiya tho"]
    
  list3 = ["terse kattif ja", "I am Once again asking you to not trouble me","Ess bar End Term main fail karvadunga dhek lena","Kis janm ka dusmani nikal ne keliye muje bar bar tag kar rahe ho yaar"]
    
  list4 = ["Badd me bat karthe hai :pray:","I will see your end", "boss thoda busy hu","Bina tag kare tag kar","Araam se jine do na yaar","Admi yo se bat karo bhai mai tho bot hu mai kya karunga?"]
    
  list5 = ["https://tenor.com/bmzjk.gif","https://tenor.com/xf3X.gif","https://tenor.com/bgJYD.gif", "https://tenor.com/tjnq.gif","https://tenor.com/vc7E.gif","https://tenor.com/6yrh.gif", "https://tenor.com/3BkQ.gif","https://tenor.com/ba5ie.gif"]

  fn1 = random.choice(list1)
  fn2 = random.choice(list2)
  fn3 = random.choice(list3)
  fn4 = random.choice(list4)
  fn5 = random.choice(list5)

  lists = [fn1, fn2, fn3, fn4,fn5]
  if bot.user.mentioned_in(message):
    await message.reply(random.choice(lists))

  song = ["-p", "-play", "-P", "-Play"]
  if any(word in msg for word in song):
    sang = ["This song is next level","dikne se nahi lagtha par tera music taste super hai bhai","gana :fire::fire::fire: ", "I like this song too","Personally mai bhi isko free time mai suntha hu", "Gana Badlo","this song feels good", "add more songs of such genre dude"]
    await message.channel.trigger_typing()
    time.sleep(3)
    await message.reply(random.choice(sang))

  rofl = ["lol", "haha", "super", ":joy:"]
  if any(word in msg for word in rofl):
    lol = [":joy::joy::joy::joy:"]
    await message.reply(random.choice(lol))

  marvel = ["Marvel", "marvel"]
  if any(word in msg for word in marvel):
    marv = ["I...am.....**Gazette**"]
    await message.reply(random.choice(marv))

  if message.content.startswith("-pause"):
    time.sleep(1.5)
    await message.reply("Why did you pause dude, I just began vibing")

  claps = ['Chapatlu', 'claps', 'clap']
  if any(word in msg for word in claps):
    await message.channel.send(":clap::clap::clap:")

  if message.content.startswith("-stop"):
    stap = ["Too soon dude :smiling_face_with_tear:","I thought you would stay longer"]
    time.sleep(1.5)
    await message.reply(random.choice(stap))

  svari = ['Maffi mango', 'maffi mango', 'Maffi Mango', 'Sorry chappu','sorry cheppu', 'Sorry bolo', 'sorry bolo']
  if any(word in msg for word in svari):
    chorri = ['chota bhacha samaj ke maf kardo :pray:']
    await message.channel.trigger_typing()
    time.sleep(2)
    await message.reply(random.choice(chorri))

  if message.content.startswith("-q"):
    qu = ["add few more songs buddy","It will get over before you even realize add fast","salute to your music taste man"]
    time.sleep(1.5)
    await message.reply(random.choice(qu))

  guda = ["guda"]
  if any(word in msg for word in guda):
    kuda = ["guda kadu ra niyna kuda, ardalu mari potunnai"]
    await message.reply(random.choice(kuda))
    
  if message.content.startswith("-skip"):
    skp = ["Jab skip karna to add hi kyu kiya", "Good job","Mai bhi yehi bolne wala tha", "Acha kam kiya jindagi me pehli baar"]
    time.sleep(1.5)
    await message.reply(random.choice(skp))

  if message.content.startswith("-story"):
    await message.reply("Diamond stories coming soon.....")

bot.run(os.getenv("TOKEN"))