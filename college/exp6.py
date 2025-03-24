from bs4 import BeautifulSoup
import requests

url = "https://edition.cnn.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

headlines = soup.find_all('span', class_='container__headline-text')  

if not headlines:
    print("No headlines found. The class might have changed.")
else:
    for headline in headlines:
        print(headline.get_text(strip=True))  
