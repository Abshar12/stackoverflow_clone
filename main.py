import requests
from bs4 import BeautifulSoup
import json

url = "https://stackoverflow.com/questions"

r = requests.get(url)
#print (r.text)

soup = BeautifulSoup (r.text , "html.parser")
#print (soup)
questions_data = {"questions" : []}

questions = soup.select(".s-post-summary--content")

for i in questions:
    q = i.select_one(".s-link").getText()
    questions_data['questions'].append({"questions":q})
json_data = json.dumps(questions_data)
print (json_data)
   
