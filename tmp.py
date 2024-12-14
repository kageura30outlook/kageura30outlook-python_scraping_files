import urllib.request
from bs4 import BeautifulSoup 
import json
import os
#import gmail_send as gmail


# ファイルを比較する関数
def compare_files(prev_file, new_file):
    if prev_file == new_file:
        return True
    else:
        return False



def job():

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
            
    directory = "./prev_spla"

    if not os.path.exists(directory):
        os.makedirs(directory)

    filename = "prev_file.json"
    file_path = os.path.join(directory, filename)

    prev_file_path = "prev_spla/prev_file.json"
    prev_file = ""

    with open(prev_file_path) as prev_f:
        prev_file = json.load(prev_f)


    with open(file_path, "w") as f:
        json.dump(new_file, f,indent=2, ensure_ascii=False)


    if compare_files(prev_file, new_file):
        print("There are no change")
        #gmail.send_test_email("There are no change")
    else:
        print("There is a change")
        #gmail.send_test_email("There is a change")




