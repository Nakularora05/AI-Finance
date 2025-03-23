import pandas as pd
import json
from datetime import datetime
import pytz
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.widgets as widgets
import requests

import pandas as pd
import json
from datetime import datetime
import pytz
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.widgets as widgets
import requests

class StockAPI:
    def __init__(self, alpha_api_key, gemini_api_key):
        self.alpha_api_key = "1UJ6ACYM0P4MHORZ"

        self.gemini_api_key = "AIzaSyAVi1v80vt41mTjZED6BaMs5-74HKFkSk0"


    def get_stock_info(self, stock, market):
        if market == 'NASDAQ':
            url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock}&outputsize=compact&apikey={self.alpha_api_key}'
        else:
            url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock}.{market}&outputsize=compact&apikey={self.alpha_api_key}'
        response = requests.get(url)
        return response.json()

    def get_gemini_insights(self, stock):
        url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={self.gemini_api_key}'
        headers = {'Content-Type': 'application/json'}
        payload = {
            "contents": [{"parts": [{"text": f"Analyze recent performance and predict future trends for {stock} stock."}]}]
        }
        response = requests.post(url, headers=headers, json=payload)
        return response.json()


    def get_stock_info(self, stock, market):
        if market == 'NASDAQ':
            url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock}&outputsize=compact&apikey={self.alpha_api_key}'
        else:
            url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock}.{market}&outputsize=compact&apikey={self.alpha_api_key}'
        response = requests.get(url)
        return response.json()

    def get_gemini_insights(self, stock):
        url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={self.gemini_api_key}'
        headers = {'Content-Type': 'application/json'}
        payload = {
            "contents": [{"parts": [{"text": f"Analyze recent performance and predict future trends for {stock} stock."}]}]
        }
        response = requests.post(url, headers=headers, json=payload)
        return response.json()
