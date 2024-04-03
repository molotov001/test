import random
import requests
import string
from urllib.parse import urljoin

def generate_gift_link():
    username_characters = string.ascii_lowercase + string.digits
    username = ''.join(random.choices(username_characters, k=10))
    code = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=16))
    return urljoin('https://discord.gift/', f'{username}-{code}')

webhook_url = 'https://discord.com/api/webhooks/1210349485172199424/MGml5bHCoM3exBNgT3-_9DOTPkQ6wOeqSYIXaQn3vgEIvPD9cK65SGkd-JcdDh78-8VI'

gift_link = generate_gift_link()

webhook_data = {
    'content': f'Valid Discord Nitro Gift Link: {gift_link}'
}

response = requests.post(webhook_url, json=webhook_data, timeout=5)

if response.status_code == 204:
    print('Gift link sent successfully!')
else:
    print('Failed to send the gift link.')