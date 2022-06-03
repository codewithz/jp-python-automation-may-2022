import requests


url = "https://jsonplaceholder.typicode.com/todos"

response = requests.get(url)

print(response)

data = response.json()

print(type(data))

for todo in data:
    print(todo)
    print("------------------------")
