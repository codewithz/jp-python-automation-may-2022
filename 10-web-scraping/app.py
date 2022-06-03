import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/questions"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

questions = soup.select(".s-post-summary")
# print(questions[0])
# print(questions[0].get("id", 0))

for question in questions:
    print("---------------------------------------------")

    print(question.
          select_one(".s-post-summary--content-excerpt")
          .getText())

    print(question.select(
        ".s-post-summary--stats-item-number")[0].getText(), "Votes")
    print("---------------------------------------------")
