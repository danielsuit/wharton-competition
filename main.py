import tensorflow as tf
import requests
import csv
import tensorflow_hub as hub
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
print("TensorFlow version:", tf.__version__)

CSV_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=IBM&interval=15min&slice=year1month1&apikey=APXD3W7Z5ODR41O4'

with requests.Session() as s:
    download = s.get(CSV_URL)
    decoded_content = download.content.decode('utf-8')
    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    print(my_list)
   #  for row in my_list:
      #   print(row)