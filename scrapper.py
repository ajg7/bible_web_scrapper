import requests
from bs4 import BeautifulSoup
from input import User_Input
# The Plan:

# Inspect Bible Hub Text Analysis
# Scrape Bible Hub
    # We want the Hebrew Text, English Text, and Morphology
# Parse the Data
# Create A window, in which you can input a verse, and it then scrapes and parses the data from Bible Hub
# Display it in a similar format

lookup = User_Input("john", "3-16", "new")

URL = f"https://biblehub.com/interlinear/{lookup.book}/{lookup.verse}.htm"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

hebrewTextContainers = soup.find_all("table", class_="tablefloatheb")
greekTextContainers = soup.find_all("table", class_="tablefloat")

hebrewText = []
englishText = []
greekText = []

if lookup.testament == "old":
    for table in hebrewTextContainers:
        hebrew = table.find("span", class_="hebrew")
        english = table.find("span", class_="eng")
        if None in (hebrew, english):
            continue
        hebrewText.append(hebrew.text.strip())
        englishText.append(english.text.strip())
else:
    for table in greekTextContainers:
        greek = table.find("span", class_="greek")
        english = table.find("span", class_="eng")
        if None in (greek, english):
            continue
        hebrewText.append(greek.text.strip())
        englishText.append(english.text.strip())


print(hebrewText, englishText, greekText)
