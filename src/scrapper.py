import requests
from bs4 import BeautifulSoup

def scrapper(lookup):
    URL = f"https://biblehub.com/interlinear/{lookup.book}/{lookup.verse}.htm"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    hebrew_text_containers = soup.find_all("table", class_="tablefloatheb")
    greek_text_containers = soup.find_all("table", class_="tablefloat")
    
    hebrew_text = []
    english_text = []
    greek_text = []

    if lookup.testament == "old":
        for table in hebrew_text_containers:
            hebrew = table.find("span", class_="hebrew")
            english = table.find("span", class_="eng")
            if None in (hebrew, english):
                continue
            hebrew_text.append(hebrew.text.strip())
            english_text.append(english.text.strip())
    else:
        for table in greek_text_containers:
            greek = table.find("span", class_="greek")
            english = table.find("span", class_="eng")
            if None in (greek, english):
                continue
            greek_text.append(greek.text.strip())
            english_text.append(english.text.strip())


    return [english_text, greek_text, hebrew_text]
