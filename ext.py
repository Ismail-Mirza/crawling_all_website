import os
import requests

def download_file(url, folder_path):
    # Send an HTTP GET request to the URL
    response = requests.get(url, stream=True)

    if response.status_code == 200:
        # Extract the filename from the URL
        file_name = url.split("/")[-1]

        # If the file name is empty or doesn't contain an extension, you can specify one manually
        if not file_name or '.' not in file_name:
            file_name = "downloaded_file.pdf"

        # Construct the file path
        file_path = os.path.join(folder_path, file_name)

        # Save the response content to a file
        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        print(f"Downloaded: {file_name}")
        return file_path
    else:
        print(f"Failed to download: {url}")
        return None

# URL of the file to download
url = "https://storage2.bdebooks.com/fa61871c25843b02"
# Folder path to save the downloaded file
output_folder = "extension"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Download the file
download_file(url, output_folder)
