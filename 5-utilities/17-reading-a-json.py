import json
from pathlib import Path

data = Path("movies.json").read_text()
print(data)
print(type(data))

print(30*'-')

movies = json.loads(data)
print(movies)
print(type(movies))
