import requests

URL = "https://mail.google.com/mail/u/0/#inbox"
page = requests.get(URL)

print(page.text)
