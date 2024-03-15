import requests
from bs4 import BeautifulSoup
import csv
from pdf import scrape_and_download
import os
from tqdm import tqdm

csv_file_path = "links.csv"



with open(csv_file_path, newline="", encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in tqdm(csv_reader, desc="Crawling BDEBOOKS", unit="websites"):


        website=row[0].strip("/")
        name = website.split("/")[-1]
        
        scrape_and_download(website,name)