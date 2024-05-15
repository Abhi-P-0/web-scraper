import requests
from bs4 import BeautifulSoup
import json
import time
import csv


def main():
    url = 'https://www.bbcgoodfoodme.com/collections/quick-and-healthy/'
    
    extract(url)

def extract(url):
    request = requests.get(url)

    soup = BeautifulSoup(request.content, 'lxml')

    print(soup)

if __name__ == '__main__':
    main()