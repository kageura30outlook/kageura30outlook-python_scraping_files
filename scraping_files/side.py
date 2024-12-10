import urllib.request
from bs4 import BeautifulSoup 
import json
import os
import datetime


# ファイルを比較する関数
def compare_files(file1_path, new_file):

    with open(file1_path, "r") as f1:
        data1 = json.load(f1)
 
    if data1 == new_file:
        return True
    else:
        return False




url = "https://game8.jp/splatoon3/480736#hl_9"

res = urllib.request.urlopen(url)

soup = BeautifulSoup(res, "html.parser") 

name = soup.find_all("td")

ret = []
for t in name:
    ret.append(t.text)



new_file = []


for text in ret:
    if "Ver." in text:
        new_file.append(text)
        
directory = "./spla"

if not os.path.exists(directory):
    os.makedirs(directory)

today_d = datetime.date.today()
filename = f"file_{today_d}.json"
file_path = os.path.join(directory, filename)


with open(file_path, "w") as f:
    json.dump(new_file, f,indent=2, ensure_ascii=False)


prev_file_path = "spla/file_2024-04-07.json"




if compare_files(prev_file_path, new_file):
    print("変更点はありません")
else:
    print("変更点があります")




