import requests
import os

url = os.getenv('DATA_URL')
response = requests.get(url)
if response.status_code == 200:
    with open('vpn-Ha.txt', 'w') as file:
        file.write(response.text)
else:
    print(f'Failed to fetch data. Status code: {response.status_code}')
