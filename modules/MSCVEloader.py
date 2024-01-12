import csv
import json
# import re
from tqdm import tqdm
import requests

# we can call API now
def download_problems():
    # ProductList = importList
    temp = []
    alertInfo = []
    count = 0
    Initial = "https://api.msrc.microsoft.com/sug/v2.0/en-US/vulnerability/"
    with open("Title.txt", "r") as txt_file:
        for line in txt_file.readlines():
            alertInfo.append(line.replace('\n', ''))
    with open("CVE List.txt", "r") as txt_file:
        for line in txt_file.readlines():
            count += 1
            temp.append(Initial +str(line.strip()))
    # to append each big item and sub-item to csv
    with open('output.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile) # header is generated in setting, we just append to that csv file
        isFirstRow = True
        for each in tqdm(temp, desc="Progress: "): # progress bar added
            page = requests.get(each).json()
            Code = page["cveNumber"]
            Context = page["cveTitle"]
            if "Chromium security severity" in Context: # Edge specific, else continue
                Context = str((Context.split(" in Google Chrome prior to"))[0]).strip()
            if isFirstRow: # for first row, it's better to mark down how the CVEs are called officially
                writer.writerow([alertInfo[0],alertInfo[1],'Yes',Code,'Yes',Context])
                isFirstRow = False
            else:
                writer.writerow(['','','',Code,'Yes',Context])
    return
    
if __name__=="__main__": 
    print("Downloader Called")                