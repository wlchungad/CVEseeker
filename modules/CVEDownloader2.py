from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from . import FirefoxProfile as FP
from . import setting
import csv
import time
# import re
from tqdm import tqdm

# to patch against change in CVE official website and format changes
# Example Link: https://www.cve.org/CVERecord?id=CVE-2023-6346
def download_problems(importList, type = None):
    # ProductList = importList
    temp = []
    alertInfo = []
    count = 0
    # For later changes (if cve.org or Microsoft changes again...)
    MSRC_Initial = "https://msrc.microsoft.com/update-guide/vulnerability/"
    CVE_Initial = "https://www.cve.org/CVERecord?id=" # replaced with newer URL (old one to be phased out from 1/1/2024) 
    with open("CVE List.txt", "r") as txt_file:
        for line in txt_file.readlines():
            count += 1
            if type == "MS":
                temp.append(MSRC_Initial +str(line.strip()))
            else: 
                temp.append(CVE_Initial +str(line.strip()))
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
    elif temp != []:
        driver = FP.FFdriver()
        # to append each big item and sub-item to csv
        with open('output.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile) # header is generated in setting, we just append to that csv file
            isFirstRow = True
            for each in tqdm(temp, desc="Progress: "): # progress bar added
                driver.get(each)
                time.sleep(5)
                if type == "MS": # Better consult official information first, IF they are available
                    retries = 3
                    time.sleep(10)
                    Context = ""
                    Code = str(each.replace("https://msrc.microsoft.com/update-guide/vulnerability/",""))
                    while retries >= 0 :
                        try:
                            Context = str(driver.find_element(By.XPATH, "//h1").text)
                            break
                        except NoSuchElementException: 
                            print ("trying again in 5 seconds ...")
                            time.sleep(5)
                            retries -= 1
                else: # normally, we can just ask cve.org
                    Code = str(driver.find_element(By.XPATH, "//h1[@class='title']").text).strip()
                    Context = str(driver.find_element(By.XPATH, "//div[@id='cve-desciption']/p").text).strip()
                    if "Chromium security severity" in Context: # Edge specific, else continue
                        Context = str((Context.split(" in Google Chrome prior to"))[0]).strip()
                if isFirstRow: # for first row, it's better to mark down how the CVEs are called officially
                    writer.writerow([alertInfo[0],alertInfo[1],'Yes',Code,'Yes',Context])
                    isFirstRow = False
                else:
                    writer.writerow(['','','',Code,'Yes',Context])
        driver.close()
    return
    
if __name__=="__main__": 
    print("Downloader Called")                