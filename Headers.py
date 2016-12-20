# A program designed to pull JSON headers from the web, written in Python 3.5.2.

import requests
import simplejson as json

url = "https://www.googleapis.com/urlshortener/v1/url"
payload = {"longUrl": "http://example.com/"}
headers = {"Content-Type": "application/json"}
r = requests.post(url, json=payload, headers=headers)

print(r.headers)
