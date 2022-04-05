#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import logging
from datetime import datetime
import os
from twilio.rest import Client
logging.basicConfig(filename='out.log', format='%(levelname)s:%(message)s', level=logging.INFO)

def send_email(url : str):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    twlo_phone = os.environ['TWILIO_PHONE_NO']
    my_phone = os.environ['MY_PHONE_NO']
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="Yay! GPU on your shortlist is available\n" + url,
                        from_='+15407248561',
                        to='+19208830984'
                    )
    return

def check_inventory(url : str, store_id : str):
    url = url + "?storeid=" + store_id
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
        'Content-Type': 'text/html',
    }

    response = requests.get(url, headers=headers)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    in_stock = soup.find_all(class_="msgInStock")

    if not in_stock:
        logging.info("TIMESTAMP: " + str(datetime.now()))
        logging.info("Sorry, but the GPU at \n" + url + "\nis not available")
    else:
        send_email(url)
        logging.info("TIMESTAMP: " + str(datetime.now()))
        logging.info("GPU FOUND! URL: " + url)


if __name__ == "__main__":
    urls = [
        "https://www.microcenter.com/product/639244/asus-nvidia-geforce-rtx-3070-tuf-gaming-v2-overclocked-triple-fan-8gb-gddr6-pcie-40-graphics-card",
        "https://www.microcenter.com/product/638234/asus-nvidia-geforce-rtx-3070-ti-tuf-gaming-overclocked-triple-fan-8gb-gddr6x-pcie-40-graphics-card",
        "https://www.microcenter.com/product/640222/asus-nvidia-geforce-rtx-3070-ko-v2-lhr-overclocked-dual-fan-8gb-gddr6-pcie-40-graphics-card"
    ]
    for url in urls:
        check_inventory(url,store_id='045')