import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import warnings

# Suppress the warning
warnings.filterwarnings("ignore", message="Unverified HTTPS request")

def download_file(url, folder_path):
    response = requests.get(url,verify=False)
    if response.status_code == 200:
        file_name = url.split("/")[-1]
        file_path = os.path.join(folder_path, file_name)
        try:
            with open(file_path, 'wb') as f:
                f.write(response.content)
        except OSError as oserr:
            print("error in downloading file")




        print(f"Downloaded: {file_name}")
        return file_path
    else:
        print(f"Failed to download: {url}")
        return None
def download_file_no_extension(url, folder_path,name):
    response = requests.get(url,verify=False)
    if response.status_code == 200:
        file_name = f"{name}.pdf"
        file_path = os.path.join(folder_path, file_name)
        try:
            with open(file_path, 'wb') as f:
                f.write(response.content)
        except OSError as oserr:
            print("error in downloading file")




        print(f"Downloaded: {file_name}")
        return file_path
    else:
        print(f"Failed to download: {url}")
        return None

def scrape_and_download(url, folder_path):
    try:
        name=url.strip("/").split("/")[-1]
        grab = requests.get(url,verify=False)
        soup = BeautifulSoup(grab.text, 'html.parser')

        for link in soup.find_all("a"):
            href = link.get("href")
            if href:
                absolute_url = urljoin(url, href)
                lower_url = absolute_url.lower()

                if any(extension in lower_url for extension in ['.pdf', '.docx', '.doc', '.txt', '.ppt', '.pptx']):
                    with open("downloadable_links.txt", "a") as dl_file:
                        dl_file.write(f"{absolute_url} == {name}\n")
        
                elif "storage" in absolute_url:
                    with open("downloadable_links.txt", "a") as dl_file:
                        dl_file.write(f"{absolute_url} == {name}\n")
                else:
                    
                    with open("non_downloadable_links.txt", "a") as non_dl_file:
                        non_dl_file.write(absolute_url + "\n")
    except requests.exceptions.RequestException as e:
        print('error in ',url)

# # # Replace 'your_website_url' with the actual URL you want to scrape
# website_url = 'https://bdebooks.com/books/101-madani-phool-by-muhammad-ilyas-attar-qadri-razavi/'
# output_folder = 'downloaded_files'

# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)

# # # Scrape and download files
# scrape_and_download(website_url, output_folder)

# print("Scraping and downloading complete.")
