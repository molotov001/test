import requests
import random
import socks
import socket

def generate_code():
    return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=16))

def check_code(code):
    url = f'https://discord.gift/redeem/{code}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'
    }
    response = requests.get(url, headers=headers, allow_redirects=False, proxies={'http': f'socks5://{dan_proxy}', 'https': f'socks5://{dan_proxy}'})
    return response.status_code == 302

webhook_url = 'https://discord.com/api/webhooks/1210349485172199424/MGml5bHCoM3exBNgT3-_9DOTPkQ6wOeqSYIXaQn3vgEIvPD9cK65SGkd-JcdDh78-8VI'

dan_proxy = '123.456.789.012:8080'

code = generate_code()
while not check_code(code):
    code = generate_code()

webhook_data = {
    'content': f'Valid Discord Nitro Code: {code}'
}

session = requests.Session()
session.proxies = {'http': f'socks5://{dan_proxy}', 'https': f'socks5://{dan_proxy}'}

response = session.post(webhook_url, json=webhook_data, timeout=5)

if response.status_code == 204:
    print('Code sent successfully!')
else:
    print('Failed to send the code.')