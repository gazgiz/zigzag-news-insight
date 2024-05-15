import os

import requests
from bs4 import BeautifulSoup

def url_crawler():
    # 웹 페이지의 URL
    page_size = 15
    start_offset = 0

    for i in range(10):
        url = f"https://www.ibric.org/bric/trend/bio-news.do?mode=list&&articleLimit={page_size}&article.offset={start_offset}"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

        response = requests.get(url, headers=headers)
        # response.encoding = 'euc-kr'

        soup = BeautifulSoup(response.text, 'html.parser')

        f = open(f'url_storage/page_{page_size}_{start_offset}.html', 'w', encoding='utf-8')
        f.write(str(soup))

        html_new_infos = []
        if soup.findAll(class_="b-box02") is not None:
            html_new_infos = soup.findAll(class_="b-box02")

        index = 0
        for html_new_info in html_new_infos:
            html_url = html_new_info.find(class_="b-title news-link-url")
            if html_url is None:
                html_url = html_new_info.find(class_="b-title")
                link = f"https://www.ibric.org/bric/trend/bio-news.do{html_url.attrs['href']}"
            else:
                link = html_url.attrs['href']
            article_info = html_new_info.find(class_="b-article-info")

            news_host = html_new_info.find('span').text
            date = html_new_info.find_all('span')[1].text

            directory = f"url_storage/{date.replace('.', '')}"
            if not os.path.exists(directory):
                os.makedirs(directory)
                print(f"'{directory}' 디렉토리가 생성되었습니다.")
            else:
                print(f"'{directory}' 디렉토리가 이미 존재합니다.")

            url_file = open(f"url_storage/{date.replace('.', '')}/urls.txt", 'a', encoding='utf-8')
            url_file.write(f"{link},{news_host},{date}\n")

        start_offset = start_offset + page_size

    print("저장되었습니다.")