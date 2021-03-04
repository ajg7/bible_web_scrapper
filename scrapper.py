import requests
from bs4 import BeautifulSoup
# The Plan:

# Inspect Bible Hub Text Analysis
# Scrape Bible Hub
    # We want the Hebrew Text, English Text, and Morphology
# Parse the Data
# Create A window, in which you can input a verse, and it then scrapes and parses the data from Bible Hub
# Display it in a similar format

URL = "https://biblehub.com/interlinear/songs/5-1.htm"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

# Grab the div (class = maintext)

results = soup.find(class_="padleft")
# print(results.prettify())

text = []

for result in results:
    hebrewText = result.find("span", class_="hebrew")
    if hebrewText == None:
        continue
    else:
        text.append(hebrewText.text)
    print(hebrewText.text, "Shalom")

print(text, "Hi")