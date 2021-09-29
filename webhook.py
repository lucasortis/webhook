import requests
import json

#pip install requests

webhook_url = 'http://127.0.0.1:5000/webhook'

data = { 'Name': 'Lucas Ortis',
          'Github' : 'https://github.com/lucasortis'}

r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type' : 'application/json'})