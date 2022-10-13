from bs4 import BeautifulSoup as BS
from dotenv import load_dotenv
from matplotlib import pyplot as plt
import requests, csv, pandas as pd, lxml, os, numpy as np
import re, json
from io import StringIO
from lxml import html
headers = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}

