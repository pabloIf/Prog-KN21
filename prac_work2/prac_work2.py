import urllib.request
from bs4 import BeautifulSoup
from threading import *
from time import time, sleep


def weather():
    url = 'https://meteofor.com.ua/'
    req = urllib.request.Request (
        url,
        headers= {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/91.0.4472.124 Safari/537.36'}
    )
    with urllib.request.urlopen(req) as file:
        src = file.read()
    
    soup = BeautifulSoup(src, 'html.parser')
    
    temperature_cont = soup.find("div", class_="temperature")
    if temperature_cont:
        temperature = temperature_cont.find("temperature-value")
        if temperature:
            value = temperature.get("value")
            print(f"Temperature: {value}°C")
        else:
            print("teg temperature-value not found")
    else:
        print("not fount el with class temperature")


def usd():
    url = "https://minfin.com.ua/ua/currency/"
    req = urllib.request.Request(
        url,
        headers= {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/91.0.4472.124 Safari/537.36'}
    )
    with urllib.request.urlopen(req) as file:
        src = file.read()

    soup = BeautifulSoup(src, "html.parser")

    usd = soup.find("div", class_="sc-1x32wa2-9 bKmKjX")
    if usd:
        print(f"Dollar exchange rate: {usd.text[:5]}")
    else:
        print("Dollar exchange rate not found")
    
def Gwei():
    url = "https://etherscan.io/gastracker"
    req = urllib.request.Request(
        url,
        headers= {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/91.0.4472.124 Safari/537.36'}
    )
    with urllib.request.urlopen(req) as file:
        src = file.read()

    soup = BeautifulSoup(src, "html.parser")

    gwei = soup.find("div", class_="h4 text-danger mb-0").find("span")
    if gwei:
        print(f"Gwei in ETH: {gwei.text.strip()}")
    else:
        print("Gwei in ETH not found")


def avr_time(function, repeats = 5):
    in_all_time = 0
    for i in range(repeats):
        start_time = time()
        function()
        end_time = time()
        in_all_time += (end_time - start_time)
    return in_all_time / repeats


print("Sequential execution:")
gwei_time = avr_time(Gwei)
usd_time = avr_time(usd)
weather_time = avr_time(weather)
print(f"Average gwei time: {gwei_time} sec")
print(f"Average weather time: {weather_time} sec")
print(f"Average usd time: {usd_time} sec")


print("\n\nParallel execution:")
