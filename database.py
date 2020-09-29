import requests

url = 'https://microsoft.com'
myobj = {'somekey': 'somevalue'}

x = requests.post(url, data = myobj)

print(x.text)