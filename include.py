# This file is just to import everything into every file easily (and my notes)

from datetime import datetime as dt
from bs4 import BeautifulSoup as bs
import json
import sqlite3 as sql
import django as dj
import requests as rq
import scraper as sc
import helpers as help
import database as db
import os

path = "C:\Temp\Code\Learn\Practice\Scraper"
os.chdir(path)
'''

TODO in order:

news command:
    this will use javascript to query the db and
    format the output in a discord embed for the bot

webapp.py:
    this is just for my django practice
'''
