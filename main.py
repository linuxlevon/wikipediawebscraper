import bs4
import requests
import csv

response = requests.get(input("Link:"))

if response is not None:
    page = bs4.BeautifulSoup(response.text, "html.parser")

title = page.select("#hproduct").reverse()

title = page.select("#mw-headline").reverse()

title = page.select("#mv-redirect").reverse()

paragraphs = page.select("td")

paragraphs_2 = page.select("td")

into = '| \n '.join(para.text for para in paragraphs[0:32])

print(into)

file1 = open("myfile12.csv", "a")  # append mode

# price = soup.find_all("div",{"class":"property-card-price-container"})

# daddress = soup.find_all("div",{"class":"property-card-subtitle"})


file1.write(into)

file1.writerows(print("row2"))

file1.close()
