from bs4 import BeautifulSoup
import requests 
import csv
from datetime import datetime  

page_to_scrape = requests.get("https://quotes.toscrape.com/")
soup = BeautifulSoup(page_to_scrape.text, 'html.parser')
quotes = soup.find_all("span", attrs={"class": "text"})
authors = soup.find_all("small", attrs={"class": "author"})

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"scraped_quotes_{timestamp}.csv"


with open(filename, "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author"]) 

    for quote, author in zip(quotes, authors):
        print(f"{quote.text} - {author.text}")
        writer.writerow([quote.text, author.text])

print(f"CVS file been saved as {filename}")