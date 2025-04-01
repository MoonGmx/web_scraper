import requests
from bs4 import BeautifulSoup
import csv

def scrape_website(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    products = []
    for item in soup.find_all("div", class_="product"):  # Change class accordingly
        name = item.find("h2").text.strip()
        price = item.find("span", class_="price").text.strip()
        rating = item.find("span", class_="rating").text.strip()
        products.append([name, price, rating])
    
    with open("products.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Price", "Rating"])
        writer.writerows(products)
    
    print("Data saved to products.csv")

def main():
    url = input("Enter the e-commerce website URL to scrape: ")
    scrape_website(url)

if _name_ == "_main_":
    main()
