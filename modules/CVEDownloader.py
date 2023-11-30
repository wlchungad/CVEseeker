from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import csv
import time
import re

def download_problems(importList, type = None):
    ProductList = importList
    temp = []
    alertInfo = []
    count = 0
    with open("CVE List.txt", "r") as txt_file:
        for line in txt_file.readlines():
            count += 1
            # print("Line{}: {}".format(count, line.strip()))
            if type == "MS":
                temp.append("https://msrc.microsoft.com/update-guide/vulnerability/"+str(line.strip()))
            else: 
                temp.append("https://cve.mitre.org/cgi-bin/cvename.cgi?name="+str(line.strip()))
    with open("Title.txt", "r") as txt_file:
        for line in txt_file.readlines():
            alertInfo.append(line.replace('\n', ''))
    if temp != []:
        option = Options()
        option.set_preference('intl.accept_languages', 'en-US, en')
        driver = webdriver.Firefox(options=option)
        with open('output.csv', 'w+', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Security Alert Number',' ','Related to ERKS system?','CVE-ID', 'Required?', 'Justification'])
            isFirstRow = True
            for each in temp:
                driver.get(each)
                time.sleep(5)
                if type == "MS":
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
                else:
                    Code = str(each.replace("https://cve.mitre.org/cgi-bin/cvename.cgi?name=",""))
                    Context = str(driver.find_element(By.XPATH, "//tr[4]/td").text)
                    if "Chromium security severity" in Context: # Edge specific, else continue
                        Context = str((Context.split(" in Google Chrome prior to"))[0])
                if isFirstRow:
                    writer.writerow([alertInfo[0],alertInfo[1],'Yes',Code,'Yes',Context])
                    isFirstRow = False
                else:
                    writer.writerow(['','','',Code,'Yes',Context])
        driver.quit()
    
if __name__=="__main__": 
    print("Downloader Called")                
    
    
# SoftwareList=[]
# if any( item in Context for item in SoftwareList):
#   if "Chromium security severity" in Context: # Edge specific, else continue
#     Context = str((Context.split(" in Google Chrome prior to"))[0])
#   writer.writerow([Code,'Yes',Context])
# else:
#   Current = driver.find_element(By.XPATH, "...").text #current software/system scanning
#   Context = "N/A, only related to " + Current
#   writer.writerow([Code,'No',Context])
#