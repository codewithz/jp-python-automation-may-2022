from urllib import request
import json

url = "https://api.github.com/users/codewithz"

with request.urlopen(url) as response:
    body = response.read()

print("Response:", body)

details = json.loads(body)
print("---------------------------------")
print(details)
