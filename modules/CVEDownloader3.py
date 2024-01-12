from . import setting
import csv
import time
# import re
from tqdm import tqdm
import requests
from bs4 import BeautifulSoup

# omprove performance by calling bs4 instead of pure selenium
def download_problems():
    # ProductList = importList
    temp = []
    alertInfo = []
    count = 0
    # For later changes (if cve.org or Microsoft changes again...)
    oldInitial = "https://cve.mitre.org/cgi-bin/cvename.cgi?name="
    with open("Title.txt", "r") as txt_file:
        for line in txt_file.readlines():
            alertInfo.append(line.replace('\n', ''))
    # some CVE are useless for the system (e.g. Apple/ Android) or unrelated
    if any(item in alertInfo[1] for item in setting.uselessSet) : 
        print(" - not usable for us")
        Code = setting.lastCVE
        MsgUnrelated = "N/A, only related to "
        if "Multiple Vulnerabilities in " in alertInfo[1]:
            MsgUnrelated += str(alertInfo[1].replace("Multiple Vulnerabilities in ",""))
        elif "Vulnerability in " in alertInfo[1]:
            MsgUnrelated += str(alertInfo[1].replace("Vulnerability in ",""))
        with open('output.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            # first row already filled in setting.py
            writer.writerow([alertInfo[0],alertInfo[1],'No',Code,'No',MsgUnrelated.strip()])
        return
    # let's be conservative and assume all other vulnerabilities are related
    else:
        with open("CVE List.txt", "r") as txt_file:
            for line in txt_file.readlines():
                count += 1
                temp.append(oldInitial +str(line.strip()))
        # to append each big item and sub-item to csv
        with open('output.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile) # header is generated in setting, we just append to that csv file
            isFirstRow = True
            for each in tqdm(temp, desc="Progress: "): # progress bar added
                page = requests.get(each)
                soup = BeautifulSoup(page.text, "html.parser")
                Code = soup.find("h2").text.strip()
                Context = soup.find_all("tr")[9].find("td").text.strip()
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