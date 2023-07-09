import requests

url = 'http://localhost:8887'

res = requests.get(
    url,
    headers={
        'content-type': 'text/html',
        'accept': 'application/json',
    },
)
if res.status_code != 200:
    print('error')
else:
    print(res.headers)
    print(res.text)
