pip_string = "pip install requests beautifulsoup4"
import sys, subprocess
subprocess.check_call([sys.executable, "-m", "pip", "install", *pip_string.split()[2:]])

import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

download_dir = sys.argv[1] if len(sys.argv) > 1 else input("folder name: ")
url = sys.argv[2] if len(sys.argv) > 2 else input("url: ")

os.makedirs(download_dir, exist_ok=True)
visited_pages = set()
base_domain = urlparse(url).netloc

def get_local_filepath(target_url, is_page=False):
    parsed = urlparse(target_url)
    path = parsed.path.lstrip('/')
    
    if not path:
        return os.path.join(download_dir, "index.html")
        
    if is_page and "." not in path.split("/")[-1]:
        return os.path.join(download_dir, path, "index.html")
         
    return os.path.join(download_dir, path)

def scrape_page(current_url):
    if current_url in visited_pages or urlparse(current_url).netloc != base_domain:
        return
    
    visited_pages.add(current_url)

    try:
        response = requests.get(current_url)
    except Exception as e:
        print(f"Failed to access {current_url}: {e}")
        return

    # Generate the sub-directory path for the page
    page_filepath = get_local_filepath(current_url, is_page=True)
    os.makedirs(os.path.dirname(page_filepath), exist_ok=True)
        
    with open(page_filepath, "w", encoding="utf-8") as f:
        f.write(response.text)
    print(f"Scraped page: {page_filepath}")

    soup = BeautifulSoup(response.text, "html.parser")

    for tag in soup.find_all(['script', 'link', 'img', 'a']):
        file_url = tag.get('src') or tag.get('href')
        
        if file_url:
            full_url = urljoin(current_url, file_url)
            
            if tag.name == 'a':
                scrape_page(full_url)
            else:
                # Generate the sub-directory path for assets (images, css, js)
                asset_filepath = get_local_filepath(full_url, is_page=False)
                os.makedirs(os.path.dirname(asset_filepath), exist_ok=True)
                
                if not os.path.exists(asset_filepath): 
                    try:
                        with open(asset_filepath, 'wb') as f:
                            f.write(requests.get(full_url).content)
                        print(f"Downloaded asset: {asset_filepath}")
                    except Exception as e:
                        print(f"Failed to download asset {asset_filepath}: {e}")

scrape_page(url)