from . import setting
import csv
# import time
# import re
from tqdm import tqdm
import requests
from bs4 import BeautifulSoup
import time
import urllib.request, json 
# improve performance by calling bs4 instead of pure selenium
def download_problems():
    # ProductList = importList
    temp = []
    alertInfo = []
    count = 0
    # For later changes (if cve.org or Microsoft changes again...)
    oldInitial = "https://cveawg.mitre.org/api/cve/"
    # oldInitial = "https://cve.circl.lu/api/cve/" # replaced with newer URL (old one to be phased out from 1/1/2024)
    # oldInitial = "https://cve.mitre.org/cgi-bin/cvename.cgi?name="
    with open("Title.txt", "r") as txt_file:
        for line in txt_file.readlines():
            alertInfo.append(line.replace("\n", ""))
    # some CVE are useless for the system (e.g. Apple/ Android) or unrelated
    if any(item in alertInfo[1] for item in setting.uselessSet):
        local_flag = False
        Code = setting.lastCVE
        MsgUnrelated = "N/A, only related to "
        if "VMware Products" in alertInfo[1]:
            # get product list of vmware, if VMTools update is needed
            print("VMware: re-checking...")
            page = requests.get(setting.govcertLink)
            soup = BeautifulSoup(page.text, "html.parser")
            ProductList = [x.get_text() for x in soup.find_all("li")[3:]]
            for each in ProductList:
                match each:
                    case str(x) if "VMware Tools" in x:
                        local_flag = True
                        break
                    case str(x) if "VMware" in x:
                        MsgUnrelated += each + ", "
                    case _:
                        continue
            MsgUnrelated = MsgUnrelated.rstrip()[:-1]
        else:
            if "Multiple Vulnerabilities in " in alertInfo[1]:
                MsgUnrelated += str(
                    alertInfo[1].replace("Multiple Vulnerabilities in ", "")
                )
            elif "Vulnerability in " in alertInfo[1]:
                MsgUnrelated += str(alertInfo[1].replace("Vulnerability in ", ""))
        if not local_flag:
            print(" - not usable for us")
            with open("output.csv", "a", newline="") as csvfile:
                writer = csv.writer(csvfile)
                # first row already filled in setting.py
                writer.writerow(
                    [alertInfo[0], alertInfo[1], "No", Code, "No", MsgUnrelated.strip()]
                )
            return
    # let's be conservative and assume all other vulnerabilities are related
    with open("CVE List.txt", "r") as txt_file:
        for line in txt_file.readlines():
            count += 1
            temp.append(oldInitial + str(line.strip()))
            # print (temp)
    # to append each big item and sub-item to csv
    with open("output.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile)  # header is generated in setting, we just append to that csv file
        isFirstRow = True
        for each in tqdm(temp, desc="Progress: "):  # progress bar added
            try:
                with urllib.request.urlopen(each) as url:    
                    data = json.load(url)
                    # print (data)
                    Code = data['cveMetadata']['cveId']
                    Context = data['containers']['cna']['descriptions'][0]['value']
                    if "Chromium security severity" in Context:  # Edge specific, else continue
                        Context = str((Context.split(" in Google Chrome prior to"))[0]).strip()
                    if (isFirstRow):  # for first row, it's better to mark down how the CVEs are called officially
                        writer.writerow([alertInfo[0], alertInfo[1], "Yes", Code, "Yes", Context])
                        isFirstRow = False
                    else:
                        writer.writerow(["", "", "", Code, "Yes", Context])            
            except (AttributeError, requests.exceptions.RequestException) as e: # NoneType and Timeout means API is unavailable for webscrapping
                #print(e)
                # print ("Error getting content: API is unavailable")
                Code = setting.lastCVE
                writer.writerow(["", "", "", Code, "", "Error getting content: API is unavailable"])
                break
    return

if __name__ == "__main__":
    print("Downloader Called")