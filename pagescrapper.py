import requests
import os

def download_pdf(url, page_num, directory):
    try:
        page_url = f"{url}{page_num}.pdf"
        response = requests.get(page_url)
        if response.status_code == 200:
            file_name = f"{directory}/DL-002-Page-{page_num}.pdf"
            with open(file_name, 'wb') as f:
                f.write(response.content)
            print(f"Page {page_num} downloaded successfully as {file_name}")
        else:
            print(f"Failed to download page {page_num}. Status code:", response.status_code)
    except Exception as e:
        print("An error occurred:", str(e))

def download_all_pages(url, start_page, end_page, directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    for page_num in range(start_page, end_page + 1):
        download_pdf(url, page_num, directory)

url = "https://mva.maryland.gov/drivers/Documents/tutorial/new/DL-002-Page-"
start_page = 1
end_page = 54
directory = "downloaded_pages"

download_all_pages(url, start_page, end_page, directory)
