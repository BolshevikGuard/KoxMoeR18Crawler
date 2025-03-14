import requests
from bs4 import BeautifulSoup
import re
import time
import sys

def progress_bar(page, cnt):    
    print('\r', end='')
    print(f'Page {page} progress {cnt}/21', '*'*cnt, end='')
    sys.stdout.flush()
    time.sleep(0.05)

base_url = "https://kox.moe/l/--/{page}.htm"

f = open('url_list.txt', 'a+')

# 遍历所有列表页，从1到932
for page in range(1, 1000):
    url = base_url.format(page=page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # 找到所有的 <script> 标签，里面包含漫画的网址
    scripts = soup.find_all("script", string=re.compile("https://kox.moe/c/"))
    pattern = re.compile(r'disp_divinfo\s*\(.*?"(https://kox\.moe/c/[\w-]+\.htm)"', re.DOTALL)

    if not scripts:
        break
    
    book_cnt = 0
    for script in scripts:
        # 提取漫画网址
        match = pattern.search(script.string)
        if match:
            manga_url = match.group(1)  # 漫画详情页URL
            book_cnt += 1
            progress_bar(page=page, cnt=book_cnt)
            f.write(manga_url+'\n')
    print('\n', end='')
    time.sleep(1)

f.close()
