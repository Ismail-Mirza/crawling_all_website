import requests
from bs4 import BeautifulSoup
import csv
from pdf import scrape_and_download
import os

csv_file_path = "links.csv"



with open(csv_file_path, newline="", encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        website=row[0].strip("/")
        if website.startswith("http://") or website.startswith("www.") or website.startswith("https://"):
            # print(website)

            # pass
            try:
                grab = requests.get(website,verify=False)
                soup = BeautifulSoup(grab.text, 'html.parser')

                # Extract all links
            except requests.exceptions.RequestException as e:
                print('error in ',website)
            links = [link.get('href') for link in soup.find_all("a")]



            for link in links:
                if link and not link.startswith("#") and not link.startswith("http://") and not link.startswith("https://")  and not link.startswith("mailto:"):
                    root_folder = 'downloaded_files'
                   
                    if not os.path.exists(root_folder):
                        os.makedirs(root_folder)

                    website_url = website +'/'+ link.strip("/")
                    print('crawling...',website_url)
                    
                    scrape_and_download(website_url, root_folder)

                    
                    
                    
                    
        else:
            print("website not in ",website)
    