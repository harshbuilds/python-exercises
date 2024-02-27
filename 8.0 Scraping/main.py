from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import json
import re
import requests

service = Service(executable_path='./webdriver/chromedriver.exe')
chrome_options = Options()
chrome_options.add_argument("--window-size=1080,720")
chrome_options.add_argument('--no-sandbox')


def parse_page(page_data):
    products = []
    data = BeautifulSoup(page_data, "html.parser")
    for item in data.select('span.productContainer'):
        stats = {
            'rating': item.select_one('div.sc-c99bc871-25.dNFVPe').find('div', {'class': re.compile(r'-2')}),
            'rating_count': item.select_one('div.sc-c99bc871-25.dNFVPe').find('span', {'class': re.compile(r'-5')}),
            'old_price': item.select_one('.oldPrice'),
            'discount': item.select_one('.discount'),
        }
        product = {
            'brand': item.find('div', attrs={"data-qa": "product-name"})['title'].split()[0],
            'title': item.find('div', attrs={"data-qa": "product-name"})['title'],
            'amount': float(item.select_one('.amount').text.replace(',', '')),
            'currency': item.select_one('.currency').text.strip(),
            'url': item.select_one('a[id^=productBox]')['href'],
            'rating': stats['rating'] and float(stats['rating'].text),
            'rating_count': stats['rating_count'] and int(stats['rating_count'].text.replace(',', '')),
            'old_price': stats['old_price'] and int(stats['old_price'].text.replace(',', '')),
            'discount': stats['discount'] and stats['discount'].text,
        }
        products.append(product)
    return products


def scan_page_requests(main_url, todo_pages=1):
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    }
    query_params = "?limit=50page={}"
    items = []
    current_page = 1
    print("Loading: {}".format(main_url + query_params.format(current_page)))
    page_data = requests.get(main_url + query_params.format(current_page), headers=headers)
    data = BeautifulSoup(page_data.text, "html.parser")
    total_pages = int(data.select("div.sc-d0edef12-0.gnckOf>ul>li")[-2].text)
    todo_pages = min(todo_pages, total_pages)
    print("Total pages: {}\nPages todo: {}".format(total_pages, todo_pages))
    while current_page <= todo_pages:
        items.extend(parse_page(page_data.text))
        current_page += 1
        if current_page <= todo_pages:
            print("Loading: {}".format(main_url + query_params.format(current_page)))
            page_data = requests.get(main_url + query_params.format(current_page), headers=headers)
    return items


def scan_page_selenium(main_url, todo_pages=1):
    driver = webdriver.Chrome(service=service, options=chrome_options)
    # query_params = "?limit={}&page={}&searchDebug=false&sort%5Bby%5D=popularity&sort%5Bdir%5D=desc"
    query_params = "?limit=50page={}"
    items = []
    current_page = 1
    print("Loading: {}".format(main_url + query_params.format(current_page)))
    driver.get(main_url + query_params.format(current_page))
    data = BeautifulSoup(driver.page_source, "html.parser")
    total_pages = int(data.select("div.sc-d0edef12-0.gnckOf>ul>li")[-2].text)
    todo_pages = min(todo_pages, total_pages)
    print("Total: {}\nTodo: {}".format(total_pages, todo_pages))
    while current_page <= todo_pages:
        items.extend(parse_page(driver.page_source))
        current_page += 1
        if current_page <= todo_pages:
            print("Loading: {}".format(main_url + query_params.format(current_page)))
            driver.get(main_url + query_params.format(current_page))
    driver.close()
    driver.quit()
    return items


def save_products(filename, data):
    with open("./data/{}.json".format(filename), "w") as f:
        f.write(json.dumps(data, indent=4))
        print('Saved {}.json'.format(filename))


if __name__ == "__main__":
    scrape_url = "https://www.noon.com/uae-en/electronics-and-mobiles/computers-and-accessories/monitor-accessories" \
                 "/monitors-17248/"

    try:
        products_list = scan_page_selenium(scrape_url, 2)
        # products_list = scan_page_requests(scrape_url, 5)
        save_products("Monitors", products_list)
    except Exception as e:
        print(e)
