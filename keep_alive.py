from flask import Flask, request, jsonify
from threading import Thread
import threading
import time
import datetime as dt
import os
import requests

pingc = str(dt.datetime.now())

app = Flask('')


@app.route('/')
def home():
  return "Hello. I am alive!"
  

def run():
    app.run(host='0.0.0.0', port=8080)


def keep_alive():
  t = Thread(target=run)
  t.start()