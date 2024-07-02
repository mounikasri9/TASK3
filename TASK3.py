import requests
from bs4 import BeautifulSoup
url="https://realpython.com/beautiful-soup-web-scraper-python/"
response=requests.get(url)
if response.status_code == 200:
    soup=BeautifulSoup(response.text,'html.parser')
    page_text=soup.get_text()
    links=[a['href'] for a in soup.find_all('a',href=True)]
    images=[img['src'] for img in soup.find_all('img',src=True)]
    print("page text:")
    print(page_text)
    print("\nLinks:")
    for link in links:
        print(link)
    print("\nimages:")
    for image in images:
        print(image)
else:
    print(f"failed to retrive the web page.status code:{response.staus_code}")
    