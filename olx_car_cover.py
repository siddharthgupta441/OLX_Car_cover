import requests
from bs4 import BeautifulSoup
import csv

def olx_car_covers():
    url = 'https://www.olx.in/items/q-car-cover'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f'Failed to retrieve data: Status {response.status_code}')
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    listings = soup.find_all('li', {'class': 'EIR5N'})

    with open('olx_car_covers.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Price', 'Location', 'Link'])


    print('The search result are availbale in CSV file.')
olx_car_covers()