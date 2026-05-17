import requests
from bs4 import BeautifulSoup

# Website URL
url = "http://quotes.toscrape.com"

# Get website data
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Extract quotes
quotes = soup.find_all("span", class_="text")

print("Quotes from website:\n")

# Print quotes
for i, q in enumerate(quotes, start=1):
    print(i, "-", q.text)  

with open("quotes.txt", "w", encoding="utf-8") as file:
    for i, q in enumerate(quotes, start=1):
        file.write(f"{i} - {q.text}\n")    