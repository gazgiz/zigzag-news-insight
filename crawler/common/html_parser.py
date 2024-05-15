
import requests
from bs4 import BeautifulSoup


# 공통으로 사용 할 수가 없어서
def make_file_path(url):
    file_path = ""
    items = url.split("/")
    file_name = items.pop()
    return f"html_storage/{file_name[:8]}/{file_name}"


def html_parser(url):
    # 웹 페이지 가져오기
    response = requests.get(url)
    response.encoding = 'euc-kr'

    # BeautifulSoup을 사용하여 HTML 파싱
    soup = BeautifulSoup(response.text, 'html.parser')

    f = open('html_storage/20240514/2024051302109931065006.html', 'w', encoding='utf-8')
    f.write(str(soup))

    # 제목 가져오기
    if soup.find(class_='title') is not None:
        title = soup.find(class_='title').text.strip()
    else:
        title = ""

    # 내용 가져오기
    content = soup.text

    # 파일에 저장
    with open('file_storage/20240514/2024051302109931065006.txt', 'w', encoding='utf-8') as file:
        file.write(title + '\n\n')
        file.write(content)

    print("기사가 저장되었습니다.")


if __name__ == '__main__':
    url = "https://health.chosun.com/site/data/html_dir/2024/05/13/2024051301680.html"
    make_file_path(url)