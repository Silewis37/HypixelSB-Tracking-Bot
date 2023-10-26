import discord
from discord.ext import commands
from discord import app_commands
import interactions
import pandas as pd
import json
import time
import requests
import os
from tabulate import tabulate
from keep_alive import keep_alive
import asyncio
from enum import Enum

Bigboy8424 = os.getenv("BIGBOY_UUID")
Firefox696 = os.getenv("FIREFOX_UUID")
Zixy42 = os.getenv("ZIXY_UUID")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.dm_messages = True
intents.dm_typing = True
intents.dm_reactions = True
client_id = os.getenv("DC_BOT_CLIENT_ID")
TOKEN = os.getenv("DC_BOT_TOKEN")
bot = interactions.Client(token=TOKEN)
discord_client = discord.Client(intents=intents)
discord_bot = commands.Bot(command_prefix='/', intents=intents)
API = os.getenv("HYPIXLE_API_KEY")
urlh = f'https://api.hypixel.net/skyblock/profile?key={API}&profile=b44178d3-75ec-4f4e-8134-12ac93989fed'


class aclient(discord.Client):

  def __init__(self):
    super().__init__(intents=intents)
    self.synced = False  # added to make sure that the command tree will be synced only once
    self.added = False

  async def on_ready(self):
    await self.wait_until_ready()
    if not self.synced:  #check if slash commands have been synced
      await tree.sync(guild=discord.Object('1095716776987328574'))
      self.synced = True
    if not self.added:
      self.added = True
    print(f"Say hi to {self.user}!")


client = aclient()
tree = app_commands.CommandTree(client)

@client.event
async def event():
  game = discord.Game("with the API")
  await client.change_presence(status=discord.Status.idle, activity=game)

@tree.command(description='Respond hello to you.',
              guild=discord.Object('1095716776987328574'))
async def greet(interaction: discord.Interaction):
  await interaction.response.send_message('Hello!')

@tree.command(name="test2", guild=discord.Object('1095716776987328574'))
async def test2(interaction: discord.Interaction):
  await interaction.response.send_message("Hello fucker!")

@tree.command(name="test", guild=discord.Object('1095716776987328574'))
async def test(interaction: discord.Interaction):
  user = interaction.user.id
  await interaction.response.send_message(f'updater worked <@{user}>!')


PurgeAmount = Enum(value='PurgeAmount', names=['10', '100', '1000', '10000'])
CoopMembers = Enum(value='CoopMembers',
                   names=['Bigboy8424', 'Zixy42', 'Firefox696'])
ForagingItems = Enum(value='ForagingItems',
                     names=[
                       'Oak Log', 'Birch Log', 'Spruce Log', 'Jungle Log',
                       'Acacia Log', 'Dark Oak Log'
                     ])
MiningItems = Enum(value='MiningItems',
                   names=[
                     'Cobblestone', 'Coal', 'Iron Ingot', 'Gold Ingot',
                     'Lapis Lazuli', 'Redstone', 'Emerald', 'Diamond',
                     'Mithril', 'Hard Stone', 'Gemstones', 'Gravel', 'Sand',
                     'Red Sand', 'Ice', 'Obsidian', 'Netherrack',
                     'Glowstone Dust', 'Quartz', 'Sulphur', 'Mycelium',
                     'End Stone'
                   ])
CombatItems = Enum(value='CombatItems',
                   names=[
                     'Rotten Flesh', 'Bones', 'Spider Eyes', 'String', 'Slime',
                     'Gunpowder', 'Blaze Rods', 'Magma Cream', 'Ghast Tears',
                     'Chili Peppers', 'Ender Pearls'
                   ])
FarmingItems = Enum(value='FarmingItems',
                    names=[
                      'Wheat', 'Seeds', 'Potatos', 'Carrots', 'Melon',
                      'Pumpkin', 'Netherwart', 'Cocoa Beans', 'Mushrooms',
                      'Sugar Cane', 'Cactus', 'Leather', 'Pork', 'Feather',
                      'Raw Chicken', 'Mutton', 'Rabbit'
                    ])
FishingItems = Enum(value='FishingItems',
                    names=[
                      'Raw Fish', 'Raw Salmon', 'ClownFish', 'PufferFish',
                      'Clay', 'Sponge', 'Prismarine Crystals',
                      'Prismarine Shards', 'Lily Pads', 'Ink Sacks',
                      'Magma Fish'
                    ])


# AUCTION HOUSE TRACKING #
# Auction House Tracking Outbound / Selling #
@tree.command(
  name='aho',
  guild=discord.Object('1095716776987328574'),
  description=
  "Allows you too see the last 10 OUTBOUND Auctions from one of the Co-Op Members Selected."
)
async def aho(interaction: discord.Interaction, member: CoopMembers):
  if member.name == "Bigboy8424":
    member2 = "Bigboy8424"
  if member.name == "Firefox696":
    member2 = "Firefox696"
  if member.name == "Zixy42":
    member2 = "Zixy42"
  if member2 == "Bigboy8424":
    url = 'https://sky.coflnet.com/api/player/' + Bigboy8424 + '/auctions?page=0'
    response = requests.get(url)
    data = json.loads(response.content)
    pretty_data = json.dumps(data, indent=2)
    f = open("./json/outbound/output-outboundah-bigboy8424.json", "+w")
    f.write(pretty_data)
    f.close()
    time.sleep(2.5)
    # Load the JSON data from a file
    with open('./json/outbound/output-outboundah-bigboy8424.json',
              'r') as file:
      data = json.load(file)
    # Convert the JSON data to a DataFrame
    df = pd.json_normalize(data)
    # Write the DataFrame to a CSV file
    df.to_csv('./csv/outbound/output-outboundah-bigboy8424.csv', index=False)
    dd = pd.read_csv('./csv/outbound/output-outboundah-bigboy8424.csv')
    wanted_info = dd[['itemName', 'bin', 'startingBid', 'highestBid']]
    wantinf = tabulate(wanted_info,
                       headers=['\tItem Name Bin Starting Bid Highest Bid'])
    await interaction.response.send_message(wantinf)
  elif member2 == "Firefox696":
    url = 'https://sky.coflnet.com/api/player/' + Firefox696 + '/auctions?page=0'
    response = requests.get(url)
    data = json.loads(response.content)
    pretty_data = json.dumps(data, indent=2)
    f = open("./json/outbound/output-outboundah-firefox696.json", "w")
    f.write(pretty_data)
    f.close()
    time.sleep(2.5)
    # Load the JSON data from a file
    with open('./json/outbound/output-outboundah-firefox696.json',
              'r') as file:
      data = json.load(file)
    # Convert the JSON data to a DataFrame
    df = pd.json_normalize(data)
    # Write the DataFrame to a CSV file
    df.to_csv('./csv/outbound/output-outboundah-firefox696.csv', index=False)
    dd = pd.read_csv('./csv/outbound/output-outboundah-firefox696.csv')
    wanted_info = dd[['itemName', 'bin', 'startingBid', 'highestBid']]
    wantinf = tabulate(wanted_info,
                       headers=['\tItem Name Bin Starting Bid Highest Bid'])
    await interaction.response.send_message(wantinf)
  elif member2 == "Zixy42":
    url = 'https://sky.coflnet.com/api/player/' + Zixy42 + '/auctions?page=0'
    response = requests.get(url)
    data = json.loads(response.content)
    pretty_data = json.dumps(data, indent=2)
    f = open("./json/outbound/output-outboundah-zixy42.json", "+w")
    f.write(pretty_data)
    f.close()
    time.sleep(2.5)
    # Load the JSON data from a file
    with open('./json/outbound/output-outboundah-zixy42.json', 'r') as file:
      data = json.load(file)
    # Convert the JSON data to a DataFrame
    df = pd.json_normalize(data)
    # Write the DataFrame to a CSV file
    df.to_csv('./csv/outbound/output-outboundah-zixy42.csv', index=False)
    dd = pd.read_csv('./csv/outbound/output-outboundah-zixy42.csv')
    wanted_info = dd[['itemName', 'bin', 'startingBid', 'highestBid']]
    wantinf = tabulate(wanted_info,
                       headers=['\tItem Name Bin Starting Bid Highest Bid'])
    await interaction.response.send_message(wantinf)
  else:
    await interaction.response.send_message(
      "**ERROR** That Player Does Not Exist on this Co-Op. ***Please Try Again***"
    )


# Auction House Tracking Inbound / Buying #
@tree.command(
  name='ahi',
  guild=discord.Object('1095716776987328574'),
  description=
  "Allows you too see the last 10 INBOUND Auctions from one of the Co-Op Members Selected.",
)
async def ahi(interaction: discord.Interaction, member: CoopMembers):
  if member.name == "Bigboy8424":
    member2 = "Bigboy8424"
  if member.name == "Firefox696":
    member2 = "Firefox696"
  if member.name == "Zixy42":
    member2 = "Zixy42"
  if member2 == "Bigboy8424":
    url = 'https://sky.coflnet.com/api/player/' + Bigboy8424 + '/bids?page=0'
    response = requests.get(url)
    data = json.loads(response.content)
    pretty_data = json.dumps(data, indent=2)
    f = open("./json/inbound/output-inboundah-bigboy8424.json", "+w")
    f.write(pretty_data)
    f.close()
    time.sleep(2.5)
    # Load the JSON data from a file
    with open('./json/inbound/output-inboundah-bigboy8424.json', 'r') as file:
      data = json.load(file)
    # Convert the JSON data to a DataFrame
    df = pd.json_normalize(data)
    # Write the DataFrame to a CSV file
    df.to_csv('./csv/inbound/output-inboundah-bigboy8424.csv', index=False)
    dd = pd.read_csv('./csv/inbound/output-inboundah-bigboy8424.csv')
    wanted_info = dd[['itemName', 'bin', 'startingBid', 'highestBid']]
    wantinf = tabulate(wanted_info,
                       headers=['\tItem Name Bin Starting Bid Highest Bid'])
    await interaction.response.send_message(wantinf)
  elif member2 == "Firefox696":
    url = 'https://sky.coflnet.com/api/player/' + Firefox696 + '/bids?page=0'
    response = requests.get(url)
    data = json.loads(response.content)
    pretty_data = json.dumps(data, indent=2)
    f = open("./json/inbound/output-inboundah-firefox696.json", "w")
    f.write(pretty_data)
    f.close()
    time.sleep(2.5)
    # Load the JSON data from a file
    with open('./json/inbound/output-inboundah-firefox696.json', 'r') as file:
      data = json.load(file)
    # Convert the JSON data to a DataFrame
    df = pd.json_normalize(data)
    # Write the DataFrame to a CSV file
    df.to_csv('./csv/inbound/output-inboundah-firefox696.csv', index=False)
    dd = pd.read_csv('./csv/inbound/output-inboundah-firefox696.csv')
    wanted_info = dd[['itemName', 'bin', 'startingBid', 'highestBid']]
    wantinf = tabulate(wanted_info,
                       headers=['\tItem Name Bin Starting Bid Highest Bid'])
    await interaction.response.send_message(wantinf)
  elif member2 == "Zixy42":
    url = 'https://sky.coflnet.com/api/player/' + Zixy42 + '/bids?page=0'
    response = requests.get(url)
    data = json.loads(response.content)
    pretty_data = json.dumps(data, indent=2)
    f = open("./json/inbound/output-inboundah-zixy42.json", "+w")
    f.write(pretty_data)
    f.close()
    time.sleep(2.5)
    # Load the JSON data from a file
    with open('./json/inbound/output-inboundah-zixy42.json', 'r') as file:
      data = json.load(file)
    # Convert the JSON data to a DataFrame
    df = pd.json_normalize(data)
    # Write the DataFrame to a CSV file
    df.to_csv('./csv/inbound/output-inboundah-zixy42.csv', index=False)
    dd = pd.read_csv('./csv/inbound/output-inboundah-zixy42.csv')
    wanted_info = dd[['itemName', 'bin', 'startingBid', 'highestBid']]
    wantinf = tabulate(wanted_info,
                       headers=['\tItem Name Bin Starting Bid Highest Bid'])
    await interaction.response.send_message(wantinf)
  else:
    await interaction.response.send_message(
      "**ERROR** That Player Does Not Exist on this Co-Op. ***Please Try Again***"
    )


# COLLECTION TRACKING #
# Slime only Collection Traker #
@tree.command(
  name='ccolslime',
  guild=discord.Object('1095716776987328574'),
  description=
  'Allows you too view the current number of collection of \nSLIME for the given Member Selected.'
)
async def ccolslime(interaction: discord.Interaction, member: CoopMembers):
  if member.name == "Bigboy8424":
    member2 = "Bigboy8424"
  if member.name == "Firefox696":
    member2 = "Firefox696"
  if member.name == "Zixy42":
    member2 = "Zixy42"
  if member2 == "Bigboy8424":
    response = requests.get(urlh)
    data = json.loads(response.content)
    pretty_data = json.dumps(data, indent=2)
    f = open("./json/ccheck/output-ccheck.json", "+w")
    f.write(pretty_data)
    f.close()
    time.sleep(2.5)
    # Load the JSON data from a file
    with open('./json/ccheck/output-ccheck.json', 'r') as file:
      data = json.load(file)
    # Convert the JSON data to a DataFrame
    df = pd.json_normalize(data)
    # Write the DataFrame to a CSV file
    df.to_csv('./csv/ccheck/output-ccheck.csv', index=False)
    dd = pd.read_csv('./csv/ccheck/output-ccheck.csv', nrows=2)
    wanted_info = dd[[
      'profile.members.c3ca1ae1236c45d5922f2b1ec7eca271.collection.SLIME_BALL'
    ]]
    await interaction.response.send_message(wanted_info)
  elif member2 == "Firefox696":
    response = requests.get(urlh)
    data = json.loads(response.content)
    pretty_data = json.dumps(data, indent=2)
    f = open("./json/ccheck/output-ccheck.json", "+w")
    f.write(pretty_data)
    f.close()
    time.sleep(2.5)
    # Load the JSON data from a file
    with open('./json/ccheck/output-ccheck.json', 'r') as file:
      data = json.load(file)
    # Convert the JSON data to a DataFrame
    df = pd.json_normalize(data)
    # Write the DataFrame to a CSV file
    df.to_csv('./csv/ccheck/output-ccheck.csv', index=False)
    dd = pd.read_csv('./csv/ccheck/output-ccheck.csv', nrows=2)
    wanted_info_f = dd[[
      'profile.members.6c7cd35c6fe14e82b142f1299a3bb759.collection.SLIME_BALL'
    ]]
    await interaction.response.send_message(wanted_info_f)
  elif member2 == "Zixy42":
    response = requests.get(urlh)
    data = json.loads(response.content)
    pretty_data = json.dumps(data, indent=2)
    f = open("./json/ccheck/output-ccheck.json", "+w")
    f.write(pretty_data)
    f.close()
    time.sleep(2.5)
    # Load the JSON data from a file
    with open('./json/ccheck/output-ccheck.json', 'r') as file:
      data = json.load(file)
    # Convert the JSON data to a DataFrame
    df = pd.json_normalize(data)
    # Write the DataFrame to a CSV file
    df.to_csv('./csv/ccheck/output-ccheck.csv', index=False)
    dd = pd.read_csv('./csv/ccheck/output-ccheck.csv', nrows=2)
    wanted_info_z = dd[[
      'profile.members.677b393621554f62b28cd70c0c7dfa80.collection.SLIME_BALL'
    ]]
    await interaction.response.send_message(wanted_info_z)


# All Collection Tracker #
@tree.command(
  name='woodcol',
  guild=discord.Object('1095716776987328574'),
  description=
  'Allows you too see the current number of wood collection in Hypixel Skyblock for Selected Member'
)
async def woodcol(interaction: discord.Interaction, member: CoopMembers,
                  noc: ForagingItems):
  if member.name == "Bigboy8424":
    member2 = "Bigboy8424"
  elif member.name == "Firefox696":
    member2 = "Firefox696"
  elif member.name == "Zixy42":
    member2 = "Zixy42"
  if noc.name == "Oak Log":
    nameofcollection = "LOG"
  elif noc.name == "Brich Log":
    nameofcollection = "LOG:2"
  elif noc.name == "Spruce Log":
    nameofcollection = "LOG:1"
  elif noc.name == "Jungle Log":
    nameofcollection = "LOG:3"
  elif noc.name == "Acacia Log":
    nameofcollection = "LOG_2"
  elif noc.name == "Dark Oak Log":
    nameofcollection = "LOG_2:1"
  if member2 == "Bigboy8424":
    response = requests.get(urlh)
    data = json.loads(response.content)
    pretty_data = json.dumps(data, indent=2)
    f = open("./json/ccheck/output-ccheck.json", "+w")
    f.write(pretty_data)
    f.close()
    time.sleep(2.5)
    # Load the JSON data from a file
    with open('./json/ccheck/output-ccheck.json', 'r') as file:
      data = json.load(file)
    # Convert the JSON data to a DataFrame
    df = pd.json_normalize(data)
    # Write the DataFrame to a CSV file
    df.to_csv('./csv/ccheck/output-ccheck.csv', index=False)
    dd = pd.read_csv('./csv/ccheck/output-ccheck.csv', nrows=2)
    col = 'profile.members.c3ca1ae1236c45d5922f2b1ec7eca271.collection.' + nameofcollection
    wanted_info = dd[[col]]
    print(wanted_info)
    await interaction.response.send_message(content= wanted_info)
  elif member.name == "Firefox696":
    response = requests.get(urlh)
    data = json.loads(response.content)
    pretty_data = json.dumps(data, indent=2)
    f = open("./json/ccheck/output-ccheck.json", "+w")
    f.write(pretty_data)
    f.close()
    time.sleep(2.5)
    # Load the JSON data from a file
    with open('./json/ccheck/output-ccheck.json', 'r') as file:
      data = json.load(file)
    # Convert the JSON data to a DataFrame
    df = pd.json_normalize(data)
    # Write the DataFrame to a CSV file
    df.to_csv('./csv/ccheck/output-ccheck.csv', index=False)
    dd = pd.read_csv('./csv/ccheck/output-ccheck.csv', nrows=2)
    col_f = 'profile.members.6c7cd35c6fe14e82b142f1299a3bb759.collection.' + nameofcollection
    wanted_info_f = dd[[col_f]]
    await interaction.response.send_message(wanted_info_f)
  elif member.name == "Zixy42":
    response = requests.get(urlh)
    data = json.loads(response.content)
    pretty_data = json.dumps(data, indent=2)
    f = open("./json/ccheck/output-ccheck.json", "+w")
    f.write(pretty_data)
    f.close()
    time.sleep(2.5)
    # Load the JSON data from a file
    with open('./json/ccheck/output-ccheck.json', 'r') as file:
      data = json.load(file)
    # Convert the JSON data to a DataFrame
    df = pd.json_normalize(data)
    # Write the DataFrame to a CSV file
    df.to_csv('./csv/ccheck/output-ccheck.csv', index=False)
    dd = pd.read_csv('./csv/ccheck/output-ccheck.csv', nrows=2)
    col_z = 'profile.members.677b393621554f62b28cd70c0c7dfa80.collection.' + nameofcollection
    wanted_info_z = dd[[col_z]]
    await interaction.response.send_message(wanted_info_z)


@tree.command(
  name='miningcol',
  guild=discord.Object('1095716776987328574'),
  description=
  'Allows you too view the current number of collection in Hypixel Skyblock for the Selected Member'
)
async def miningcol(interaction: discord.Interaction, member: CoopMembers,
                    noc: MiningItems):
  if noc.name == "Cobblestone":
    nameofcollection = "COBBLESTONE"
  elif noc.name == "Coal":
    nameofcollection = "COAL"
  elif noc.name == "Iron Ingot":
    nameofcollection = "IRON_INGOT"
  elif noc.name == "Gold Ingot":
    nameofcollection = "GOLD_INGOT"
  elif noc.name == "Lapis Lazuli":
    nameofcollection = "INK_SACK:4"
  elif noc.name == "Redstone":
    nameofcollection = "REDSTONE"
  elif noc.name == "Emerald":
    nameofcollection = "EMERALD"
  elif noc.name == "Diamond":
    nameofcollection = "DIAMOND"
  elif noc.name == "Mithril":
    nameofcollection = "MITHRIL_ORE"
  elif noc.name == "Hard Stone":
    nameofcollection = "HARD_STONE"
  elif noc.name == "Gemstones":
    nameofcollection = "GEMSTONE_COLLECTION"
  elif noc.name == "Gravel":
    nameofcollection = "GRAVEL"
  elif noc.name == "Sand":
    nameofcollection = "SAND"
  elif noc.name == "Red Sand":
    nameofcollection = "SAND:1"
  elif noc.name == "Ice":
    nameofcollection = "ICE"
  elif noc.name == "Obsidian":
    nameofcollection = "OBSIDIAN"
  elif noc.name == "Netherrack":
    nameofcollection = "NETHERRACK"
  elif noc.name == "Glowstone Dust":
    nameofcollection = "GLOWSTONE_DUST"
  elif noc.name == "Quartz":
    nameofcollection = "QUARTZ"
  elif noc.name == "Sulphur":
    nameofcollection = "SULPHUR_ORE"
  elif noc.name == "Mycelium":
    nameofcollection = "MYCEL"
  elif noc.name == "End Stone":
    nameofcollection = "ENDER_STONE"
  if member.name == "Bigboy8424":
    
    response = requests.get(urlh)
    data = json.loads(response.content)
    pretty_data = json.dumps(data, indent=2)
    f = open("./json/ccheck/output-ccheck.json", "+w")
    f.write(pretty_data)
    f.close()
    time.sleep(2.5)
    # Load the JSON data from a file
    with open('./json/ccheck/output-ccheck.json', 'r') as file:
      data = json.load(file)
    # Convert the JSON data to a DataFrame
    df = pd.json_normalize(data)
    # Write the DataFrame to a CSV file
    df.to_csv('./csv/ccheck/output-ccheck.csv', index=False)
    dd = pd.read_csv('./csv/ccheck/output-ccheck.csv', nrows=2)
    col = 'profile.members.c3ca1ae1236c45d5922f2b1ec7eca271.collection.' + nameofcollection
    wanted_info = dd[[col]]
    await interaction.response.send_message(wanted_info)
  elif member.name == "Firefox696":
    
    response = requests.get(urlh)
    data = json.loads(response.content)
    pretty_data = json.dumps(data, indent=2)
    f = open("./json/ccheck/output-ccheck.json", "+w")
    f.write(pretty_data)
    f.close()
    time.sleep(2.5)
    # Load the JSON data from a file
    with open('./json/ccheck/output-ccheck.json', 'r') as file:
      data = json.load(file)
    # Convert the JSON data to a DataFrame
    df = pd.json_normalize(data)
    # Write the DataFrame to a CSV file
    df.to_csv('./csv/ccheck/output-ccheck.csv', index=False)
    dd = pd.read_csv('./csv/ccheck/output-ccheck.csv', nrows=2)
    col_f = 'profile.members.6c7cd35c6fe14e82b142f1299a3bb759.collection.' + nameofcollection
    wanted_info_f = dd[[col_f]]
    await interaction.response.send_message(wanted_info_f)
  elif member.name == "Zixy42":
    
    response = requests.get(urlh)
    data = json.loads(response.content)
    pretty_data = json.dumps(data, indent=2)
    f = open("./json/ccheck/output-ccheck.json", "+w")
    f.write(pretty_data)
    f.close()
    time.sleep(2.5)
    # Load the JSON data from a file
    with open('./json/ccheck/output-ccheck.json', 'r') as file:
      data = json.load(file)
    # Convert the JSON data to a DataFrame
    df = pd.json_normalize(data)
    # Write the DataFrame to a CSV file
    df.to_csv('./csv/ccheck/output-ccheck.csv', index=False)
    dd = pd.read_csv('./csv/ccheck/output-ccheck.csv', nrows=2)
    col_z = 'profile.members.677b393621554f62b28cd70c0c7dfa80.collection.' + nameofcollection
    wanted_info_z = dd[[col_z]]
    await interaction.response.send_message(wanted_info_z)


@tree.command(
  name='combatcol',
  guild=discord.Object('1095716776987328574'),
  description=
  'Allows you too view the current number of collection in Hypixel Skyblock for the Selected Member'
)
async def combatcol(interaction: discord.Interaction, member: CoopMembers,
                    noc: CombatItems):
  if noc.name == "Rotten Flesh":
    nameofcollection = "ROTTEN_FLESH"
  elif noc.name == "Bones":
    nameofcollection = "BONE"
  elif noc.name == "Spider Eyes":
    nameofcollection = "SPIDER_EYE"
  elif noc.name == "String":
    nameofcollection = "STRING"
  elif noc.name == "Slime":
    nameofcollection = "SLIME_BALL"
  elif noc.name == "Gunpowder":
    nameofcollection = "SULPHUR"
  elif noc.name == "Blaze Rods":
    nameofcollection = "BLAZE_ROD"
  elif noc.name == "Magma Cream":
    nameofcollection = "MAGMA_CREAM"
  elif noc.name == "Ghast Tears":
    nameofcollection = "GHAST_TEAR"
  elif noc.name == "Chili Peppers":
    nameofcollection = "CHILI_PEPPER"
  elif noc.name == "Ender Pearls":
    nameofcollection = "ENDER_PEARL"
  if member.name == "Bigboy8424":
    
    response = requests.get(urlh)
    data = json.loads(response.content)
    pretty_data = json.dumps(data, indent=2)
    f = open("./json/ccheck/output-ccheck.json", "+w")
    f.write(pretty_data)
    f.close()
    time.sleep(2.5)
    # Load the JSON data from a file
    with open('./json/ccheck/output-ccheck.json', 'r') as file:
      data = json.load(file)
    # Convert the JSON data to a DataFrame
    df = pd.json_normalize(data)
    # Write the DataFrame to a CSV file
    df.to_csv('./csv/ccheck/output-ccheck.csv', index=False)
    dd = pd.read_csv('./csv/ccheck/output-ccheck.csv', nrows=2)
    col = 'profile.members.c3ca1ae1236c45d5922f2b1ec7eca271.collection.' + nameofcollection
    wanted_info = dd[[col]]
    await interaction.response.send_message(wanted_info)
  elif member.name == "Firefox696":
    
    response = requests.get(urlh)
    data = json.loads(response.content)
    pretty_data = json.dumps(data, indent=2)
    f = open("./json/ccheck/output-ccheck.json", "+w")
    f.write(pretty_data)
    f.close()
    time.sleep(2.5)
    # Load the JSON data from a file
    with open('./json/ccheck/output-ccheck.json', 'r') as file:
      data = json.load(file)
    # Convert the JSON data to a DataFrame
    df = pd.json_normalize(data)
    # Write the DataFrame to a CSV file
    df.to_csv('./csv/ccheck/output-ccheck.csv', index=False)
    dd = pd.read_csv('./csv/ccheck/output-ccheck.csv', nrows=2)
    col_f = 'profile.members.6c7cd35c6fe14e82b142f1299a3bb759.collection.' + nameofcollection
    wanted_info_f = dd[[col_f]]
    await interaction.response.send_message(wanted_info_f)
  elif member.name == "Zixy42":
    
    response = requests.get(urlh)
    data = json.loads(response.content)
    pretty_data = json.dumps(data, indent=2)
    f = open("./json/ccheck/output-ccheck.json", "+w")
    f.write(pretty_data)
    f.close()
    time.sleep(2.5)
    # Load the JSON data from a file
    with open('./json/ccheck/output-ccheck.json', 'r') as file:
      data = json.load(file)
    # Convert the JSON data to a DataFrame
    df = pd.json_normalize(data)
    # Write the DataFrame to a CSV file
    df.to_csv('./csv/ccheck/output-ccheck.csv', index=False)
    dd = pd.read_csv('./csv/ccheck/output-ccheck.csv', nrows=2)
    col_z = 'profile.members.677b393621554f62b28cd70c0c7dfa80.collection.' + nameofcollection
    wanted_info_z = dd[[col_z]]
    await interaction.response.send_message(wanted_info_z)


@tree.command(
  name='farmingcol',
  guild=discord.Object('1095716776987328574'),
  description=
  'Allows you too view the current number of collection in Hypixel Skyblock for the Selected Member'
)
async def farmingcol(interaction: discord.Interaction, member: CoopMembers,
                     noc: FarmingItems):
  if noc.name == "Wheat":
    nameofcollection = "WHEAT"
  elif noc.name == "Seeds":
    nameofcollection = "SEEDS"
  elif noc.name == "Potatos":
    nameofcollection = "POTATO_ITEM"
  elif noc.name == "Carrots":
    nameofcollection = "CARROT_ITEM"
  elif noc.name == "Melon":
    nameofcollection = "MELON"
  elif noc.name == "Pumpkin":
    nameofcollection = "PUMPKIN"
  elif noc.name == "Netherwart":
    nameofcollection = "NETHER_STALK"
  elif noc.name == "Cocoa Beans":
    nameofcollection = "INK_SACK:3"
  elif noc.name == "Mushrooms":
    nameofcollection = "MUSHROOM_COLLECTION"
  elif noc.name == "Sugar Cane":
    nameofcollection = "SUGAR_CANE"
  elif noc.name == "Cactus":
    nameofcollection = "CACTUS"
  elif noc.name == "Leather":
    nameofcollection = "LEATHER"
  elif noc.name == "Pork":
    nameofcollection = "PORK"
  elif noc.name == "Feather":
    nameofcollection = "FEATHER"
  elif noc.name == "Raw Chicken":
    nameofcollection = "RAW_CHICKEN"
  elif noc.name == "Mutton":
    nameofcollection = "MUTTON"
  elif noc.name == "Rabbit":
    nameofcollection = "RABBIT"
  if member.name == "Bigboy8424":
    
    response = requests.get(urlh)
    data = json.loads(response.content)
    pretty_data = json.dumps(data, indent=2)
    f = open("./json/ccheck/output-ccheck.json", "+w")
    f.write(pretty_data)
    f.close()
    time.sleep(2.5)
    # Load the JSON data from a file
    with open('./json/ccheck/output-ccheck.json', 'r') as file:
      data = json.load(file)
    # Convert the JSON data to a DataFrame
    df = pd.json_normalize(data)
    # Write the DataFrame to a CSV file
    df.to_csv('./csv/ccheck/output-ccheck.csv', index=False)
    dd = pd.read_csv('./csv/ccheck/output-ccheck.csv', nrows=2)
    col = 'profile.members.c3ca1ae1236c45d5922f2b1ec7eca271.collection.' + nameofcollection
    wanted_info = dd[[col]]
    await interaction.response.send_message(wanted_info)
  elif member.name == "Firefox696":
    
    response = requests.get(urlh)
    data = json.loads(response.content)
    pretty_data = json.dumps(data, indent=2)
    f = open("./json/ccheck/output-ccheck.json", "+w")
    f.write(pretty_data)
    f.close()
    time.sleep(2.5)
    # Load the JSON data from a file
    with open('./json/ccheck/output-ccheck.json', 'r') as file:
      data = json.load(file)
    # Convert the JSON data to a DataFrame
    df = pd.json_normalize(data)
    # Write the DataFrame to a CSV file
    df.to_csv('./csv/ccheck/output-ccheck.csv', index=False)
    dd = pd.read_csv('./csv/ccheck/output-ccheck.csv', nrows=2)
    col_f = 'profile.members.6c7cd35c6fe14e82b142f1299a3bb759.collection.' + nameofcollection
    wanted_info_f = dd[[col_f]]
    await interaction.response.send_message(wanted_info_f)
  elif member.name == "Zixy42":
    
    response = requests.get(urlh)
    data = json.loads(response.content)
    pretty_data = json.dumps(data, indent=2)
    f = open("./json/ccheck/output-ccheck.json", "+w")
    f.write(pretty_data)
    f.close()
    time.sleep(2.5)
    # Load the JSON data from a file
    with open('./json/ccheck/output-ccheck.json', 'r') as file:
      data = json.load(file)
    # Convert the JSON data to a DataFrame
    df = pd.json_normalize(data)
    # Write the DataFrame to a CSV file
    df.to_csv('./csv/ccheck/output-ccheck.csv', index=False)
    dd = pd.read_csv('./csv/ccheck/output-ccheck.csv', nrows=2)
    col_z = 'profile.members.677b393621554f62b28cd70c0c7dfa80.collection.' + nameofcollection
    wanted_info_z = dd[[col_z]]
    await interaction.response.send_message(wanted_info_z)


@tree.command(
  name='fishingcol',
  guild=discord.Object('1095716776987328574'),
  description=
  'Allows you too view the current number of collection in Hypixel Skyblock for the Selected Member'
)
async def fishingcol(interaction: discord.Interaction, member: CoopMembers,
                     noc: FishingItems):
  if noc.name == "Raw Fish":
    nameofcollection = "RAW_FISH"
  elif noc.name == "Raw Salmon":
    nameofcollection = "RAW_FISH:1"
  elif noc.name == "ClownFish":
    nameofcollection = "RAW_FISH:2"
  elif noc.name == "PufferFish":
    nameofcollection = "RAW_FISH:3"
  elif noc.name == "Clay":
    nameofcollection = "CLAY_BALL"
  elif noc.name == "Sponge":
    nameofcollection = "SPONGE"
  elif noc.name == "Prismarine Crystals":
    nameofcollection = "PRISMARINE_CRYSTALS"
  elif noc.name == "Prismarine Shards":
    nameofcollection = "PRISMARINE_SHARD"
  elif noc.name == "Lily Pads":
    nameofcollection = "WATER_LILY"
  elif noc.name == "Ink Sacks":
    nameofcollection = "INK_SACK"
  elif noc.name == "Magma Fish":
    nameofcollection = "MAGMA_FISH"
  if member.name == "Bigboy8424":
    
    response = requests.get(urlh)
    data = json.loads(response.content)
    pretty_data = json.dumps(data, indent=2)
    f = open("./json/ccheck/output-ccheck.json", "+w")
    f.write(pretty_data)
    f.close()
    time.sleep(2.5)
    # Load the JSON data from a file
    with open('./json/ccheck/output-ccheck.json', 'r') as file:
      data = json.load(file)
    # Convert the JSON data to a DataFrame
    df = pd.json_normalize(data)
    # Write the DataFrame to a CSV file
    df.to_csv('./csv/ccheck/output-ccheck.csv', index=False)
    dd = pd.read_csv('./csv/ccheck/output-ccheck.csv', nrows=2)
    col = 'profile.members.c3ca1ae1236c45d5922f2b1ec7eca271.collection.' + nameofcollection
    wanted_info = dd[[col]]
    await interaction.response.send_message(wanted_info)
  elif member.name == "Firefox696":
    
    response = requests.get(urlh)
    data = json.loads(response.content)
    pretty_data = json.dumps(data, indent=2)
    f = open("./json/ccheck/output-ccheck.json", "+w")
    f.write(pretty_data)
    f.close()
    time.sleep(2.5)
    # Load the JSON data from a file
    with open('./json/ccheck/output-ccheck.json', 'r') as file:
      data = json.load(file)
    # Convert the JSON data to a DataFrame
    df = pd.json_normalize(data)
    # Write the DataFrame to a CSV file
    df.to_csv('./csv/ccheck/output-ccheck.csv', index=False)
    dd = pd.read_csv('./csv/ccheck/output-ccheck.csv', nrows=2)
    col_f = 'profile.members.6c7cd35c6fe14e82b142f1299a3bb759.collection.' + nameofcollectioon
    wanted_info_f = dd[[col_f]]
    await interaction.response.send_message(wanted_info_f)
  elif member.name == "Zixy42":
    
    response = requests.get(urlh)
    data = json.loads(response.content)
    pretty_data = json.dumps(data, indent=2)
    f = open("./json/ccheck/output-ccheck.json", "+w")
    f.write(pretty_data)
    f.close()
    time.sleep(2.5)
    # Load the JSON data from a file
    with open('./json/ccheck/output-ccheck.json', 'r') as file:
      data = json.load(file)
    # Convert the JSON data to a DataFrame
    df = pd.json_normalize(data)
    # Write the DataFrame to a CSV file
    df.to_csv('./csv/ccheck/output-ccheck.csv', index=False)
    dd = pd.read_csv('./csv/ccheck/output-ccheck.csv', nrows=2)
    col_z = 'profile.members.677b393621554f62b28cd70c0c7dfa80.collection.' + nameofcollection
    wanted_info_z = dd[[col_z]]
    await interaction.response.send_message(wanted_info_z)


@tree.command(
  name='acolslime',
  guild=discord.Object('1095716776987328574'),
  description='Displays all of the Co-Op Members Slime Collections')
async def acolslime(interaction: discord.Interaction):
  
  response = requests.get(urlh)
  data = json.loads(response.content)
  pretty_data = json.dumps(data, indent=2)
  f = open("./json/ccheck/output-acolslime.json", "+w")
  f.write(pretty_data)
  f.close()
  time.sleep(2.5)
  # Load the JSON data from a file
  with open('./json/ccheck/output-acolslime.json', 'r') as file:
    data = json.load(file)
  # Convert the JSON data to a DataFrame
  df = pd.json_normalize(data)
  # Write the DataFrame to a CSV file
  df.to_csv('./csv/ccheck/output-acolslime.csv', index=False)
  dd = pd.read_csv('./csv/ccheck/output-acolslime.csv', nrows=2)
  col = 'profile.members.c3ca1ae1236c45d5922f2b1ec7eca271.collection.SLIME_BALL'
  wanted_info = dd[[col]]
  await interaction.response.send_message(
    "Bigboy8424's Current Slime Collection >> \n")
  await interaction.response.send_message(wanted_info)
  col_f = 'profile.members.6c7cd35c6fe14e82b142f1299a3bb759.collection.SLIME_BALL'
  wanted_info_f = dd[[col_f]]
  await interaction.response.send_message(
    "Firefox696's Current Slime Collection >> \n")
  await interaction.response.send_message(wanted_info_f)
  col_z = 'profile.members.677b393621554f62b28cd70c0c7dfa80.collection.SLIME_BALL'
  wanted_info_z = dd[[col_z]]
  await interaction.response.send_message(
    "Zixy42's Slime Current Collection >>\n")
  await interaction.response.send_message(wanted_info_z)


@tree.command(
  name='woodacol',
  guild=discord.Object('1095716776987328574'),
  description=
  'Displays the total Co-Ops Colections from the Choice you Selected.')
async def woodacol(interaction: discord.Interaction, noc: ForagingItems):
  if noc.name == "Oak Log":
    nameofcollection = "LOG"
  elif noc.name == "Brich Log":
    nameofcollection = "LOG:2"
  elif noc.name == "Spruce Log":
    nameofcollection = "LOG:1"
  elif noc.name == "Jungle Log":
    nameofcollection = "LOG:3"
  elif noc.name == "Acacia Log":
    nameofcollection = "LOG_2"
  elif noc.name == "Dark Oak Log":
    nameofcollection = "LOG_2:1"
  
  response = requests.get(urlh)
  data = json.loads(response.content)
  pretty_data = json.dumps(data, indent=2)
  f = open("./json/ccheck/output-ccheck.json", "+w")
  f.write(pretty_data)
  f.close()
  time.sleep(2.5)
  # Load the JSON data from a file
  with open('./json/ccheck/output-ccheck.json', 'r') as file:
    data = json.load(file)
  # Convert the JSON data to a DataFrame
  df = pd.json_normalize(data)
  # Write the DataFrame to a CSV file
  df.to_csv('./csv/ccheck/output-ccheck.csv', index=False)
  dd = pd.read_csv('./csv/ccheck/output-ccheck.csv', nrows=2)
  col = 'profile.members.c3ca1ae1236c45d5922f2b1ec7eca271.collection.' + nameofcollection
  wanted_info = dd[[col]]
  await interaction.response.send_message("Bigboy8424's Collection of " +
                                          nameofcollection + " >> \n")
  await interaction.response.send_message(wanted_info)
  col_f = 'profile.members.6c7cd35c6fe14e82b142f1299a3bb759.collection.' + nameofcollection
  wanted_info_f = dd[[col_f]]
  await interaction.response.send_message("Firefox696's Collection of " +
                                          nameofcollection + " >> \n")
  await interaction.response.send_message(wanted_info_f)
  col_z = 'profile.members.677b393621554f62b28cd70c0c7dfa80.collection.' + nameofcollection
  wanted_info_z = dd[[col_z]]
  await interaction.response.send_message("Zixy42's Collection of " +
                                          nameofcollection + " >> \n")
  await interaction.response.send_message(wanted_info_z)


@tree.command(
  name='miningacol',
  guild=discord.Object('1095716776987328574'),
  description=
  'Displays the total Co-Ops Colections from the Choice you Selected.')
async def miningacol(interaction: discord.Interaction, noc: MiningItems):
  if noc.name == "Cobblestone":
    nameofcollection = "COBBLESTONE"
  elif noc.name == "Coal":
    nameofcollection = "COAL"
  elif noc.name == "Iron Ingot":
    nameofcollection = "IRON_INGOT"
  elif noc.name == "Gold Ingot":
    nameofcollection = "GOLD_INGOT"
  elif noc.name == "Lapis Lazuli":
    nameofcollection = "INK_SACK:4"
  elif noc.name == "Redstone":
    nameofcollection = "REDSTONE"
  elif noc.name == "Emerald":
    nameofcollection = "EMERALD"
  elif noc.name == "Diamond":
    nameofcollection = "DIAMOND"
  elif noc.name == "Mithril":
    nameofcollection = "MITHRIL_ORE"
  elif noc.name == "Hard Stone":
    nameofcollection = "HARD_STONE"
  elif noc.name == "Gemstones":
    nameofcollection = "GEMSTONE_COLLECTION"
  elif noc.name == "Gravel":
    nameofcollection = "GRAVEL"
  elif noc.name == "Sand":
    nameofcollection = "SAND"
  elif noc.name == "Red Sand":
    nameofcollection = "SAND:1"
  elif noc.name == "Ice":
    nameofcollection = "ICE"
  elif noc.name == "Obsidian":
    nameofcollection = "OBSIDIAN"
  elif noc.name == "Netherrack":
    nameofcollection = "NETHERRACK"
  elif noc.name == "Glowstone Dust":
    nameofcollection = "GLOWSTONE_DUST"
  elif noc.name == "Quartz":
    nameofcollection = "QUARTZ"
  elif noc.name == "Sulphur":
    nameofcollection = "SULPHUR_ORE"
  elif noc.name == "Mycelium":
    nameofcollection = "MYCEL"
  elif noc.name == "End Stone":
    nameofcollection = "ENDER_STONE"
  
  response = requests.get(urlh)
  data = json.loads(response.content)
  pretty_data = json.dumps(data, indent=2)
  f = open("./json/ccheck/output-ccheck.json", "+w")
  f.write(pretty_data)
  f.close()
  time.sleep(2.5)
  # Load the JSON data from a file
  with open('./json/ccheck/output-ccheck.json', 'r') as file:
    data = json.load(file)
  # Convert the JSON data to a DataFrame
  df = pd.json_normalize(data)
  # Write the DataFrame to a CSV file
  df.to_csv('./csv/ccheck/output-ccheck.csv', index=False)
  dd = pd.read_csv('./csv/ccheck/output-ccheck.csv', nrows=2)
  col = 'profile.members.c3ca1ae1236c45d5922f2b1ec7eca271.collection.' + nameofcollection
  wanted_info = dd[[col]]
  await interaction.response.send_message("Bigboy8424's Collection of " +
                                          nameofcollection + " >> \n")
  await interaction.response.send_message(wanted_info)
  col_f = 'profile.members.6c7cd35c6fe14e82b142f1299a3bb759.collection.' + nameofcollection
  wanted_info_f = dd[[col_f]]
  await interaction.response.send_message("Firefox696's Collection of " +
                                          nameofcollection + " >> \n")
  await interaction.response.send_message(wanted_info_f)
  col_z = 'profile.members.677b393621554f62b28cd70c0c7dfa80.collection.' + nameofcollection
  wanted_info_z = dd[[col_z]]
  await interaction.response.send_message("Zixy42's Collection of " +
                                          nameofcollection + " >> \n")
  await interaction.response.send_message(wanted_info_z)


@tree.command(
  name='combatacol',
  guild=discord.Object('1095716776987328574'),
  description=
  'Displays the total Co-Ops Colections from the Choice you Selected.')
async def comabtacol(interaction: discord.Interaction, noc: CombatItems):
  if noc.name == "Rotten Flesh":
    nameofcollection = "ROTTEN_FLESH"
  elif noc.name == "Bones":
    nameofcollection = "BONE"
  elif noc.name == "Spider Eyes":
    nameofcollection = "SPIDER_EYE"
  elif noc.name == "String":
    nameofcollection = "STRING"
  elif noc.name == "Slime":
    nameofcollection = "SLIME_BALL"
  elif noc.name == "Gunpowder":
    nameofcollection = "SULPHUR"
  elif noc.name == "Blaze Rods":
    nameofcollection = "BLAZE_ROD"
  elif noc.name == "Magma Cream":
    nameofcollection = "MAGMA_CREAM"
  elif noc.name == "Ghast Tears":
    nameofcollection = "GHAST_TEAR"
  elif noc.name == "Chili Peppers":
    nameofcollection = "CHILI_PEPPER"
  elif noc.name == "Ender Pearls":
    nameofcollection = "ENDER_PEARL"
  
  response = requests.get(urlh)
  data = json.loads(response.content)
  pretty_data = json.dumps(data, indent=2)
  f = open("./json/ccheck/output-ccheck.json", "+w")
  f.write(pretty_data)
  f.close()
  time.sleep(2.5)
  # Load the JSON data from a file
  with open('./json/ccheck/output-ccheck.json', 'r') as file:
    data = json.load(file)
  # Convert the JSON data to a DataFrame
  df = pd.json_normalize(data)
  # Write the DataFrame to a CSV file
  df.to_csv('./csv/ccheck/output-ccheck.csv', index=False)
  dd = pd.read_csv('./csv/ccheck/output-ccheck.csv', nrows=2)
  col = 'profile.members.c3ca1ae1236c45d5922f2b1ec7eca271.collection.' + nameofcollection
  wanted_info = dd[[col]]
  await interaction.response.send_message("Bigboy8424's Collection of " +
                                          nameofcollection.name + " >> \n")
  await interaction.response.send_message(wanted_info)
  col_f = 'profile.members.6c7cd35c6fe14e82b142f1299a3bb759.collection.' + nameofcollection
  wanted_info_f = dd[[col_f]]
  await interaction.response.send_message("Firefox696's Collection of " +
                                          nameofcollection.name + " >> \n")
  await interaction.response.send_message(wanted_info_f)
  col_z = 'profile.members.677b393621554f62b28cd70c0c7dfa80.collection.' + nameofcollection
  wanted_info_z = dd[[col_z]]
  await interaction.response.send_message("Zixy42's Collection of " +
                                          nameofcollection.name + " >> \n")
  await interaction.response.send_message(wanted_info_z)


@tree.command(
  name='fishingacol',
  guild=discord.Object('1095716776987328574'),
  description=
  'Displays the total Co-Ops Colections from the Choice you Selected.')
async def fishingacol(interaction: discord.Interaction, noc: FishingItems):
  if noc.name == "Raw Fish":
    nameofcollection = "RAW_FISH"
  elif noc.name == "Raw Salmon":
    nameofcollection = "RAW_FISH:1"
  elif noc.name == "ClownFish":
    nameofcollection = "RAW_FISH:2"
  elif noc.name == "PufferFish":
    nameofcollection = "RAW_FISH:3"
  elif noc.name == "Clay":
    nameofcollection = "CLAY_BALL"
  elif noc.name == "Sponge":
    nameofcollection = "SPONGE"
  elif noc.name == "Prismarine Crystals":
    nameofcollection = "PRISMARINE_CRYSTALS"
  elif noc.name == "Prismarine Shards":
    nameofcollection = "PRISMARINE_SHARD"
  elif noc.name == "Lily Pads":
    nameofcollection = "WATER_LILY"
  elif noc.name == "Ink Sacks":
    nameofcollection = "INK_SACK"
  elif noc.name == "Magma Fish":
    nameofcollection = "MAGMA_FISH"
  
  response = requests.get(urlh)
  data = json.loads(response.content)
  pretty_data = json.dumps(data, indent=2)
  f = open("./json/ccheck/output-ccheck.json", "+w")
  f.write(pretty_data)
  f.close()
  time.sleep(2.5)
  # Load the JSON data from a file
  with open('./json/ccheck/output-ccheck.json', 'r') as file:
    data = json.load(file)
  # Convert the JSON data to a DataFrame
  df = pd.json_normalize(data)
  # Write the DataFrame to a CSV file
  df.to_csv('./csv/ccheck/output-ccheck.csv', index=False)
  dd = pd.read_csv('./csv/ccheck/output-ccheck.csv', nrows=2)
  col = 'profile.members.c3ca1ae1236c45d5922f2b1ec7eca271.collection.' + nameofcollection
  wanted_info = dd[[col]]
  await interaction.response.send_message("Bigboy8424's Collection of " +
                                          nameofcollection + " >> \n")
  await interaction.response.send_message(wanted_info)
  col_f = 'profile.members.6c7cd35c6fe14e82b142f1299a3bb759.collection.' + nameofcollection
  wanted_info_f = dd[[col_f]]
  await interaction.response.send_message("Firefox696's Collection of " +
                                          nameofcollection + " >> \n")
  await interaction.response.send_message(wanted_info_f)
  col_z = 'profile.members.677b393621554f62b28cd70c0c7dfa80.collection.' + nameofcollection
  wanted_info_z = dd[[col_z]]
  await interaction.response.send_message("Zixy42's Collection of " +
                                          nameofcollection + " >> \n")
  await interaction.response.send_message(wanted_info_z)


@tree.command(
  name='farmingacol',
  guild=discord.Object('1095716776987328574'),
  description=
  'Displays the total Co-Ops Colections from the Choice you Selected.')
async def farmingacol(interaction: discord.Interaction, noc: FarmingItems):
  if noc.name == "Wheat":
    nameofcollection = "WHEAT"
    pass
  elif noc.name == "Seeds":
    nameofcollection = "SEEDS"
    pass
  elif noc.name == "Potatos":
    nameofcollection = "POTATO_ITEM"
    pass
  elif noc.name == "Carrots":
    nameofcollection = "CARROT_ITEM"
    pass
  elif noc.name == "Melon":
    nameofcollection = "MELON"
    pass
  elif noc.name == "Pumpkin":
    nameofcollection = "PUMPKIN"
    pass
  elif noc.name == "Netherwart":
    nameofcollection = "NETHER_STALK"
    pass
  elif noc.name == "Cocoa Beans":
    nameofcollection = "INK_SACK:3"
    pass
  elif noc.name == "Mushrooms":
    nameofcollection = "MUSHROOM_COLLECTION"
    pass
  elif noc.name == "Sugar Cane":
    nameofcollection = "SUGAR_CANE"
    pass
  elif noc.name == "Cactus":
    nameofcollection = "CACTUS"
    pass
  elif noc.name == "Leather":
    nameofcollection = "LEATHER"
    pass
  elif noc.name == "Pork":
    nameofcollection = "PORK"
    pass
  elif noc.name == "Feather":
    nameofcollection = "FEATHER"
    pass
  elif noc.name == "Raw Chicken":
    nameofcollection = "RAW_CHICKEN"
    pass
  elif noc.name == "Mutton":
    nameofcollection = "MUTTON"
    pass
  elif noc.name == "Rabbit":
    nameofcollection = "RABBIT"
    pass
  else:
    nameofcollection = "NULL"
    pass
  response = requests.get(urlh)
  data = json.loads(response.content)
  pretty_data = json.dumps(data, indent=2)
  f = open("./json/ccheck/output-ccheck.json", "+w")
  f.write(pretty_data)
  f.close()
  time.sleep(2.5)
  await interaction.response.send_message("before with func")
  # Load the JSON data from a file
  with open('./json/ccheck/output-ccheck.json', 'r') as file:
    data = json.load(file)
    pass
  await interaction.response.is_done()
  # Convert the JSON data to a DataFrame
  df = pd.json_normalize(data)
  # Write the DataFrame to a CSV file
  df.to_csv('./csv/ccheck/output-ccheck.csv', index=False)
  dd = pd.read_csv('./csv/ccheck/output-ccheck.csv', nrows=2)
  col = 'profile.members.c3ca1ae1236c45d5922f2b1ec7eca271.collection.' + nameofcollection
  wanted_info = dd[[col]]
  wantinf = tabulate(wanted_info,
     headers=['Bigboy8424s Collection'])
  col_f = 'profile.members.6c7cd35c6fe14e82b142f1299a3bb759.collection.' + nameofcollection
  wanted_info_f = dd[[col_f]]
  col_z = 'profile.members.677b393621554f62b28cd70c0c7dfa80.collection.' + nameofcollection
  wanted_info_z = dd[[col_z]]
  print(wantinf)
  await interaction.response.send_message("Finished")

# DATA & BOT MANAGEMENT #
# Populates First Scan of Data Required for the above #
@tree.command(name='populate', guild=discord.Object('1095716776987328574'))
async def populate(interaction: discord.Interaction):
  response = requests.get(url)
  data = json.loads(response.content)
  pretty_data = json.dumps(data, indent=2)
  f = open("./json/ccheck/output-ccheck.json", "+w")
  f.write(pretty_data)
  f.close()
  time.sleep(2.5)
  # Load the JSON data from a file
  with open('./json/ccheck/output-ccheck.json', 'r') as file:
    data = json.load(file)
  # Convert the JSON data to a DataFrame
  df = pd.json_normalize(data)
  # Write the DataFrame to a CSV file
  df.to_csv('./csv/ccheck/output-ccheck.csv', index=False)
  time.sleep(0.5)
  
  response = requests.get(url)
  data = json.loads(response.content)
  pretty_data = json.dumps(data, indent=2)
  f = open("./json/ccheck/output-ccheck.json", "+w")
  f.write(pretty_data)
  f.close()
  time.sleep(2.5)
  # Load the JSON data from a file
  with open('./json/ccheck/output-ccheck.json', 'r') as file:
    data = json.load(file)
  # Convert the JSON data to a DataFrame
  df = pd.json_normalize(data)
  # Write the DataFrame to a CSV file
  df.to_csv('./csv/ccheck/output-ccheck.csv', index=False)
  time.sleep(0.5)
  
  response = requests.get(url)
  data = json.loads(response.content)
  pretty_data = json.dumps(data, indent=2)
  f = open("./json/ccheck/output-ccheck.json", "+w")
  f.write(pretty_data)
  f.close()
  time.sleep(2.5)
  # Load the JSON data from a file
  with open('./json/ccheck/output-ccheck.json', 'r') as file:
    data = json.load(file)
  # Convert the JSON data to a DataFrame
  df = pd.json_normalize(data)
  # Write the DataFrame to a CSV file
  df.to_csv('./csv/ccheck/output-ccheck.csv', index=False)
  time.sleep(0.5)
  url = 'https://sky.coflnet.com/api/player/' + Bigboy8424 + '/bids?page=0'
  response = requests.get(url)
  data = json.loads(response.content)
  pretty_data = json.dumps(data, indent=2)
  f = open("./json/inbound/output-inboundah-bigboy8424.json", "+w")
  f.write(pretty_data)
  f.close()
  time.sleep(2.5)
  # Load the JSON data from a file
  with open('./json/inbound/output-inboundah-bigboy8424.json', 'r') as file:
    data = json.load(file)
  # Convert the JSON data to a DataFrame
  df = pd.json_normalize(data)
  # Write the DataFrame to a CSV file
  df.to_csv('./csv/inbound/output-inboundah-bigboy8424.csv', index=False)
  url = 'https://sky.coflnet.com/api/player/' + Firefox696 + '/bids?page=0'
  response = requests.get(url)
  data = json.loads(response.content)
  pretty_data = json.dumps(data, indent=2)
  f = open("./json/inbound/output-inboundah-firefox696.json", "w")
  f.write(pretty_data)
  f.close()
  time.sleep(2.5)
  # Load the JSON data from a file
  with open('./json/inbound/output-inboundah-firefox696.json', 'r') as file:
    data = json.load(file)
  # Convert the JSON data to a DataFrame
  df = pd.json_normalize(data)
  # Write the DataFrame to a CSV file
  df.to_csv('./csv/inbound/output-inboundah-firefox696.csv', index=False)
  url = 'https://sky.coflnet.com/api/player/' + Zixy42 + '/bids?page=0'
  response = requests.get(url)
  data = json.loads(response.content)
  pretty_data = json.dumps(data, indent=2)
  f = open("./json/inbound/output-inboundah-zixy42.json", "+w")
  f.write(pretty_data)
  f.close()
  time.sleep(2.5)
  # Load the JSON data from a file
  with open('./json/inbound/output-inboundah-zixy42.json', 'r') as file:
    data = json.load(file)
  # Convert the JSON data to a DataFrame
  df = pd.json_normalize(data)
  # Write the DataFrame to a CSV file
  df.to_csv('./csv/inbound/output-inboundah-zixy42.csv', index=False)
  url = 'https://sky.coflnet.com/api/player/' + Bigboy8424 + '/auctions?page=0'
  response = requests.get(url)
  data = json.loads(response.content)
  pretty_data = json.dumps(data, indent=2)
  f = open("./json/outbound/output-outboundah-bigboy8424.json", "+w")
  f.write(pretty_data)
  f.close()
  time.sleep(2.5)
  # Load the JSON data from a file
  with open('./json/outbound/output-outboundah-bigboy8424.json', 'r') as file:
    data = json.load(file)
  # Convert the JSON data to a DataFrame
  df = pd.json_normalize(data)
  # Write the DataFrame to a CSV file
  df.to_csv('./csv/outbound/output-outboundah-bigboy8424.csv', index=False)
  url = 'https://sky.coflnet.com/api/player/' + Firefox696 + '/auctions?page=0'
  response = requests.get(url)
  data = json.loads(response.content)
  pretty_data = json.dumps(data, indent=2)
  f = open("./json/outbound/output-outboundah-firefox696.json", "w")
  f.write(pretty_data)
  f.close()
  time.sleep(2.5)
  # Load the JSON data from a file
  with open('./json/outbound/output-outboundah-firefox696.json', 'r') as file:
    data = json.load(file)
  # Convert the JSON data to a DataFrame
  df = pd.json_normalize(data)
  # Write the DataFrame to a CSV file
  df.to_csv('./csv/outbound/output-outboundah-firefox696.csv', index=False)
  url = 'https://sky.coflnet.com/api/player/' + Zixy42 + '/auctions?page=0'
  response = requests.get(url)
  data = json.loads(response.content)
  pretty_data = json.dumps(data, indent=2)
  f = open("./json/outbound/output-outboundah-zixy42.json", "+w")
  f.write(pretty_data)
  f.close()
  time.sleep(2.5)
  # Load the JSON data from a file
  with open('./json/outbound/output-outboundah-zixy42.json', 'r') as file:
    data = json.load(file)
  # Convert the JSON data to a DataFrame
  df = pd.json_normalize(data)
  # Write the DataFrame to a CSV file
  df.to_csv('./csv/outbound/output-outboundah-zixy42.csv', index=False)
  await interaction.response.send_message("POPULATION COMPLETED!!!!")


# Deletes all messages within a channel #
@tree.command(
  name='purge',
  guild=discord.Object('1095716776987328574'),
  description=
  'This will wipe all messages from the channel you are currently in... USE WITH CUATION!!!!'
)
async def purge(interaction: discord.Interaction, purgeamount: PurgeAmount):
  if purgeamount.name == "10":
    amount = 10
    await interaction.channel.purge(limit=amount)
  elif purgeamount.name == "100":
    amount = 100
    await interaction.channel.purge(limit=amount)
  elif purgeamount.name == "1000":
    amount = 1000
    await interaction.channel.purge(limit=amount)
  elif purgeamount.name == "10000":
    amount = 10000
    await interaction.channel.purge(limit=amount)


# Checks and Creates folders for storage of data #
@discord_bot.command(name='fldrload',
                     guild=discord.Object('1095716776987328574'))
async def fldrload(interaction: discord.Interaction):
  if os.path.exists('logged-collection/zixy42') == True and os.path.exists(
      'logged-collection/firefox696') == True and os.path.exists(
        'logged-collection/bigboy8424'
      ) == True and os.path.exists('json/outbound') == True and os.path.exists(
        'json/inbound') == True and os.path.exists(
          'json/ccheck') == True and os.path.exists(
            'csv/outbound') == True and os.path.exists(
              'csv/inbound') == True and os.path.exists('csv/ccheck') == True:
    await interaction.response.send_message("ALL FOLDERS ARE LOCATED!!!")
  if os.path.exists('csv/ccheck') == True:
    await interaction.response.send_message(
      "The Folder '/csv/ccheck' already exists")
    pass
  elif os.path.exists('csv/ccheck') == False:
    os.mkdir('csv/ccheck')
    await interaction.response.send_message(
      "The Folder '/csv/ccheck' was created.")
  if os.path.exists('csv/inbound') == True:
    await interaction.response.send_message(
      "The Folder '/csv/inbound' already exists")
    pass
  elif os.path.exists('csv/inbound') == False:
    os.mkdir('csv/inbound')
    await interaction.response.send_message(
      "The Folder '/csv/inbound' was created.")
  if os.path.exists('csv/outbound') == True:
    await interaction.response.send_message(
      "The Folder '/csv/outbound' already exists")
    pass
  elif os.path.exists('csv/outbound') == False:
    os.mkdir('csv/outbound')
    await interaction.response.send_message(
      "The Folder '/csv/outbound' was created.")
  if os.path.exists('json/ccheck') == True:
    await interaction.response.send_message(
      "The Folder '/json/ccheck' already exists")
    pass
  elif os.path.exists('json/ccheck') == False:
    os.mkdir('json/ccheck')
    await interaction.response.send_message(
      "The Folder '/json/ccheck' was created.")
  if os.path.exists('json/inbound') == True:
    await interaction.response.send_message(
      "The Folder '/json/inbound' already exists")
    pass
  elif os.path.exists('json/inbound') == False:
    os.mkdir('json/inbound')
    await interaction.response.send_message(
      "The Folder '/json/inbound' was created.")
  if os.path.exists('json/outbound') == True:
    await interaction.response.send_message(
      "The Folder '/json/outbound' already exists")
    pass
  elif os.path.exists('json/outbound') == False:
    os.mkdir('json/outbound')
    await interaction.response.send_message(
      "The Folder '/json/outbound' was created.")
  if os.path.exists('logged-collection/bigboy8424') == True:
    await interaction.response.send_message(
      "The Folder '/logged-collection/bigboy8424' already exists")
    pass
  elif os.path.exists('logged-collection/bigboy8424') == False:
    os.mkdir('logged-collection/bigboy8424')
    await interaction.response.send_message(
      "The Folder '/logged-collection/bigboy8424' was created.")
  if os.path.exists('logged-collection/firefox696') == True:
    await interaction.response.send_message(
      "The Folder '/logged-collection/firefox696' already exists")
    pass
  elif os.path.exists('logged-collection/firefox696') == False:
    os.mkdir('logged-collection/firefox696')
    await interaction.response.send_message(
      "The Folder '/logged-collection/firefox696' was created.")
  if os.path.exists('logged-collection/zixy42') == True:
    await interaction.response.send_message(
      "The Folder '/logged-collection/zixy42' already exists")
    pass
  elif os.path.exists('logged-collection/zixy42') == False:
    os.mkdir('logged-collection/zixy42')
    await interaction.response.send_message(
      "The Folder '/logged-collection/zixy42' was created.")
  if os.path.exists('logged-collection/storage') == True:
    await interaction.response.send_message(
      "The Folder '/logged-collection/storage' alread exists")
    pass
  elif os.path.exists('logged-collection/storage') == False:
    os.mkdir('logged-collection/storage')
    await interaction.response.send_message(
      "The Folder '/logged-collection/storage' was created.")
  await interaction.response.send_message("ALL FOLDERS ARE LOCATED!!!")
  time.sleep(3)
  await interaction.channel.purge(limit=11)
  await interaction.response.send_message(
    "All the Folders required have been Located!")


# Stops the bot #
@discord_bot.command(name='stop', guild=discord.Object('1095716776987328574'))
async def stop(interaction: discord.Interaction):
  goodbye = "Goodbye..."
  await interaction.response.send_message(goodbye)
  time.sleep(1)
  exit()


# Updates the bot #
@tree.command(
  name='botupdate',
  guild=discord.Object('1095716776987328574'),
  description=
  'Updates the bot to the latest version of code. Can only be ran by The Creator!'
)
async def botupdate(interaction: discord.Interaction):
  os.system("pgrep -f  \"python keep_alive.py keep_alive\" | xargs kill 1")


# Starts the bot after Update #
@tree.command(
  name='botstart',
  guild=discord.Object('1095716776987328574'),
  description=
  'Starts the Bot Fully after an Update was ran. Can only be ran by The Creator!'
)
async def botstart(interaction: discord.Interaction):
  async with interaction.typing():
    # do expensive stuff here
    await asyncio.sleep(5)
  await interaction.response.send_message("Bot Is Fully Started")


# Starts the Weekly Tracker #
@tree.command(name='wtstart',
              guild=discord.Object('1095716776987328574'),
              description='WIP CANNOT BE RUN BY ANYONE BUT THE CREATOR!')
async def wtstart(interaction: discord.Interaction):
  os.system("python weekly.py")
  time.sleep(1)
  await interaction.response.send_message(
    "Weekly Tracker for SLIME_BALL Collection, Was Successfully Started!")


keep_alive()
client.run(TOKEN)
