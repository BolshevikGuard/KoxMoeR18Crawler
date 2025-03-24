import re
import json
import pandas as pd

# 读取文件
with open("output.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

data = []

for line in lines:
    line = line.strip()
    # 正则匹配：N 是 1 或 2，mark 是浮点数，url 以 https://kox.moe/c/ 开头并以 .htm 结尾
    match = re.match(r"^(1|2)\s+(.+?)\s+(\d+\.\d)\s+(https://kox\.moe/c/\w+\.htm)$", line)
    
    if match:
        N = int(match.group(1))  # 评级
        title = match.group(2)  # 书名
        mark = float(match.group(3))  # 评分
        url = match.group(4)  # 链接
        
        data.append({"TYPE": N, "TITLE": title, "MARK": mark, "URL": url})

# 打印结果

# with open("output.json", "w", encoding="utf-8") as json_file:
#     json.dump(data, json_file, ensure_ascii=False, indent=4)

# print("数据已保存到 output.json")

df = pd.DataFrame(data)

# 保存到 Excel 文件
df.to_excel("output.xlsx", index=False, engine="openpyxl")

print("数据已成功保存到 output.xlsx")