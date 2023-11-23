import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_file(url, folder_path):
    response = requests.get(url,verify=False)
    if response.status_code == 200:
        file_name = url.split("/")[-1]
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {file_name}")
        return file_path
    else:
        print(f"Failed to download: {url}")
        return None

def scrape_and_download(url, folder_path):
    grab = requests.get(url,verify=False)
    soup = BeautifulSoup(grab.text, 'html.parser')

    for link in soup.find_all("a"):
        href = link.get("href")
        if href:
            absolute_url = urljoin(url, href)
            lower_url = absolute_url.lower()

            if any(extension in lower_url for extension in ['.pdf', '.docx', '.doc', '.txt', '.ppt', '.pptx']):
                download_file(absolute_url, folder_path)
            else:
                with open("non_downloadable_links.txt", "a") as non_dl_file:
                    non_dl_file.write(absolute_url + "\n")

# Replace 'your_website_url' with the actual URL you want to scrape
website_url = 'http://www.nctb.gov.bd/site/files/e977a7e5-be01-4c42-99ac-bc966d334ae7/-'
output_folder = 'downloaded_files'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Scrape and download files
scrape_and_download(website_url, output_folder)

print("Scraping and downloading complete.")
