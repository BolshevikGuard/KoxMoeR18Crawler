import requests
from bs4 import BeautifulSoup
import re

# 目标网址（示例）
url = "https://kox.moe/c/2144de.htm"

# 发送请求
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # 提取评分
    score_tag = soup.find("table", class_="book_score")
    score = None
    if score_tag:
        font_tag = score_tag.find("font", style=re.compile("font-size"))
        if font_tag:
            score = font_tag.text.strip()

    # 提取漫画名称
    title = None
    meta_tag = soup.find("meta", {"name": "keywords"})
    if meta_tag:
        title = meta_tag["content"].split(",")[0]  # 取第一个关键词作为名称

    # 提取 R15 / R18 分类
    script_tag = soup.find("script", string=re.compile(r"var is_r18\s*=\s*parseInt"))
    category = None
    if script_tag:
        match = re.search(r"var is_r18\s*=\s*parseInt\(\s*\"(\d+)\"\s*\)", script_tag.text)
        if match:
            category = int(match.group(1))

    # 只保留 R15 (1) 和 R18 (2) 的漫画
    if category in [1, 2]:
        print(f"名称: {title}")
        print(f"评分: {score}")
        print(f"类别: {'R15' if category == 1 else 'R18'}")
