'''  
real world example : multithreading for i/o bound tasks
scenario : web scraping
web scraping often involves making numerous network request to fetch web pages. These taske are i/o bound because they spend a lot of time waiting for  responses from servers. Multithreading can significantly improve the performance by allowing by multiple web pages to be fetched concurrently.
'''


'''
https://docs.langchain.com/oss/python/deepagents/overview

https://docs.langchain.com/oss/python/deepagents/customization
'''

import threading
import requests
from bs4 import BeautifulSoup

urls = [
    'https://docs.langchain.com/oss/python/deepagents/overview',
    'https://docs.langchain.com/oss/python/deepagents/customization'
]

def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f'Fetched {len(soup.text)} characters from {url}')

threads = []

for url in urls:
    thread = threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All web pages fetched")
        
        
    
    