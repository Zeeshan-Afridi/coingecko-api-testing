import requests
import json
import matplotlib.pyplot as plt
import pandas as pd
import datetime

def column_getter():
    for i in data.keys():
        timestamps, column = list_seperator(data, i)
        df["Date"] = timestamps
        df[i] = column

    return df

def list_seperator(d, c):
    # Unpack the nested list from the dictionary
    load_lists = d[c]

    # Separate timestamps and prices using list comprehension
    timestamps, t_data = zip(*load_lists)

    # Convert them to separate lists
    timestamp_list = list(timestamps)
    t_data = list(t_data)

    return timestamp_list, t_data

def time_converter(unix_time):
    try:
        seconds_timestamp = unix_time / 1000  # Divide by 1000 to convert milliseconds to seconds
        local_datetime = datetime.datetime.fromtimestamp(seconds_timestamp)
        formatted_date = local_datetime.strftime("%Y-%m-%d")
        return formatted_date
    except Exception as e:
        return None  # Handle potential errors gracefully

respone = requests.get("https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range?vs_currency=usd&from=1674552452&to=1706088452")

data = respone.json()

df = pd.DataFrame()

column_getter()

df["Date"] = df["Date"].apply(time_converter)

df