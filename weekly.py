import pandas as pd
import json
import time
import datetime
import requests
import os
import schedule
import shutil

base_url = 'https://api.hypixel.net/skyblock/profile?key=a735f459-9e7d-4775-bfb4-726478b947a1&profile=b44178d3-75ec-4f4e-8134-12ac93989fed'
Bigboy8424 = os.getenv("BIGBOY_UUID")
Firefox696 = os.getenv("FIREFOX_UUID")
Zixy42 = os.getenv("ZIXY_UUID")
today = datetime.date.today()
week_start = datetime.datetime.now() - datetime.timedelta(days=6)


def job_bb():
  response = requests.get(base_url)
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
    'profile.members.' + Bigboy8424 + '.collection.SLIME_BALL'
  ]]
  fi = open('logged-collection/bigboy8424/slime-collection.txt', '+a')
  fi.write(today + "\t>>\n" + wanted_info_f)
  fi.close()


def job_ff():
  response = requests.get(base_url)
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
    'profile.members.' + Firefox696 + '.collection.SLIME_BALL'
  ]]
  fi = open('logged-collection/firefox696/slime-collection.txt', '+a')
  fi.write(today + "\t>>\n" + wanted_info_f)
  fi.close()


def job_zx():
  response = requests.get(base_url)
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
  wanted_info_f = dd[['profile.members.' + Zixy42 + '.collection.SLIME_BALL']]
  fi = open('logged-collection/zixy42/slime-collection.txt', '+a')
  fi.write(today + "\t>>\n" + wanted_info_f)
  fi.close()


def job_stor():
  os.mkdir('logged-collection/storage/' + week_start)
  source_path = os.path.join(
    'logged-collection/bigboy8424/',
    'logged-collection/bigboy8424/slime-collection.txt')
  destination_path = os.path.join(
    'logged-collection/storage/' + week_start,
    'logged-collection/bigboy8424/slime-collection.txt')
  shutil.move(source_path, destination_path)
  os.rename(
    os.path.join('logged-collection/storage/' + week_start,
                 'slime-collection.txt'),
    os.path.join('logged-collection/storage/' + week_start,
                 'bigboy8424-slime-collection.txt'))
  ff_source_path = os.path.join(
    'logged-collection/firefox696/',
    'logged-collection/firefox696/slime-collection.txt')
  ff_destination_path = os.path.join(
    'logged-collection/storage/' + week_start,
    'logged-collection/firefox696/slime-collection.txt')
  shutil.move(ff_source_path, ff_destination_path)
  os.rename(
    os.path.join('logged-collection/storage/' + week_start,
                 'slime-collection.txt'),
    os.path.join('logged-collection/storage/' + week_start,
                 'firefox696-slime-collection.txt'))
  zx_source_path = os.path.join(
    'logged-collection/bigboy8424/',
    'logged-collection/zixy42/slime-collection.txt')
  zx_destination_path = os.path.join(
    'logged-collection/storage/' + week_start,
    'logged-collection/zixy42/slime-collection.txt')
  shutil.move(zx_source_path, zx_destination_path)
  os.rename(
    os.path.join('logged-collection/storage/' + week_start,
                 'slime-collection.txt'),
    os.path.join('logged-collection/storage/' + week_start,
                 'zixy42-slime-collection.txt'))



while True:
  schedule.every().day.at("23:59").do(job_bb)
  schedule.every().day.at("23:59").do(job_ff)
  schedule.every().day.at("23:59").do(job_zx)
  schedule.every().day.at("12:00").do(job_bb)
  schedule.every().day.at("12:00").do(job_ff)
  schedule.every().day.at("12:00").do(job_zx)
  schedule.every().sunday.at("23:59").do(job_stor)
  time.sleep(60)
