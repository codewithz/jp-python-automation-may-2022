import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    'title': 'Post Title',
    'body': 'Post Body',
    'userId': 100
}

response = requests.post(url=url, data=data)
print(response)
print(response.text)

from bs4 import BeautifulSoup
