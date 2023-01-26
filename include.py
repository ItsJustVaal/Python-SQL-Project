import json
from bs4 import BeautifulSoup as bs
import sqlite3 as sql
import django as dj
import requests as rq
import pandas as pd
import scraper as sc
from datetime import datetime as dt
import helpers as help
import database as db
'''
notes for next time:
make a new branch to work on then merge it in after to main

TODO in order:

news command:
    this will use javascript to query the db and
    format the output in a discord embed for the bot

webapp.py:
    this is just for my django practice
'''
