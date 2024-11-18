import urllib.request
from bs4 import BeautifulSoup
from threading import *
from time import time, sleep

def parse_weather():
    url = 'https://meteofor.com.ua/'
    req = urllib.request.Request (
        url,
        headers= {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/91.0.4472.124 Safari/537.36'}
    )

    try:
        with urllib.request.urlopen(req) as response:
            html = response.read()
            soup = BeautifulSoup(html, 'html.parser')
        #print(html)
        #temp_elms = soup.find_all('value')
        #temp_elms = soup.find_all('div', class_='temperature')
        temp_elms = soup.find_all('span', {'class': 'temp-value'})


        if not temp_elms:
            print("No temperature data found.")
            return
        for temp in temp_elms:
            temp_val = temp.get('value')
            #temp_txt = temp.text
        print(f"Temperature: {temp_val}")
        return int(temp_val)

    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code}")
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")
    except Exception as e:
        print(f"Error: {e}")


parse_weather()