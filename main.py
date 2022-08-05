import tensorflow as tf
import os
from dotenv import load_dotenv
import tensorflow_hub as hub
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
print("TensorFlow version:", tf.__version__)
load_dotenv()
key = os.environ.get('API_KEY')
CSV_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&outputsize=full&apikey='+key+'&datatype=csv'
df = pd.read_csv(CSV_URL)
print(df.head())