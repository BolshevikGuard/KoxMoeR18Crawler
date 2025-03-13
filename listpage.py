import requests
from bs4 import BeautifulSoup
import re

base_url = "https://kox.moe/l/--/{page}.htm"
manga_list = []

# 遍历所有列表页，从1到932
for page in range(1, 2):
    url = base_url.format(page=page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # 找到所有的 <script> 标签，里面包含漫画的网址
    scripts = soup.find_all("script", string=re.compile("https://kox.moe/c/"))
    pattern = re.compile(r'disp_divinfo\s*\(.*?"(https://kox\.moe/c/[\w-]+\.htm)"', re.DOTALL)

    for script in scripts:
        # 提取漫画网址
        match = pattern.search(script.string)
        if match:
            manga_url = match.group(1)  # 漫画详情页URL
            manga_list.append(manga_url)

# 输出所有爬取的漫画名称和评分
for manga in manga_list:
    print(manga)
