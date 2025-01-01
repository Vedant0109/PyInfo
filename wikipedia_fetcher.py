import requests

title = input("Enter your title: ")
title = title.replace(" ", "_")

url = "https://en.wikipedia.org/w/api.php"

params = {
    'action': 'query',
    'format': 'json',
    'prop': 'extracts',
    'exintro': True,
    'titles': title
}

data = requests.get(url, params=params)

info = data.json()

pages = info["query"]["pages"]

if "-1" in pages:
    print("Page not found.")
elif "missing" in pages:
    print("Page missing.")
else:
    page_info = list(pages.values())[0]
    
    if "extract" in page_info:
        output = page_info["extract"]
        print(output)
    else:
        print("No extract available for this page.")