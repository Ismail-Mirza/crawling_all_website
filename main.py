import requests
from bs4 import BeautifulSoup
import csv
csv_file_path = "links.csv"
for page in [1]:

    url = f'http://www.nctb.gov.bd/'
    grab = requests.get(url,verify=False)
    soup = BeautifulSoup(grab.text, 'html.parser')

    # Extract all links
    links = []
    for link in soup.find_all("a"):
        links.append(link)

    # Write links to CSV file

    with open(csv_file_path, "a", newline="", encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)

        # Check if the link is not None and is not a relative path
        for link in links:
            if link and not link.startswith("#") and not link.startswith("mailto:"):
                print(link)
                csv_writer.writerow([link])

print(f"All links have been appended to {csv_file_path}")
