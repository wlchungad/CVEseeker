from selenium import webdriver
from selenium.webdriver.common.by import By
from modules import setting
import csv
import time
import re

def process_GOV_Link(weblink):
    CVE_List = []
    driver = webdriver.Firefox()
    driver.get(weblink) 
    # get title 
    pageTitle = driver.find_element(By.XPATH, "//h3[@id='doc_title']").text
    pageTitle = pageTitle.replace("):", "(").split("(",1)
    del pageTitle[0]
    with open("Title.txt", "w+") as txtFile:
        for each in pageTitle:
            txtFile.write(each.strip())
            txtFile.write('\n')
    # identify if it is MS regular patch list
    if ("Microsoft Products" in pageTitle[1]):
        setting.alertType = "MS"
    # get links
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    li_xpath = "//h4[text()='More Information:']/following-sibling::ul[1]/li"
    links = driver.find_elements(By.XPATH, li_xpath)
    linkCount = 0
    for item in links: # for each link
        itemText = item.text.strip()
        if "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE" in itemText:
            itemText = str(itemText.replace("https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-",""))
            if " (to CVE-2023-" in itemText:
                temp = []
                temp = itemText.split(" (to CVE-2023-")
                temp[1] = temp[1].replace(")","")
                for _ in range (int(temp[0]),int(temp[1])+1):
                    placeholder = str("CVE-2023-")+str(_)
                    CVE_List.append(placeholder)
            else:# Only one CVE
                CVE_List.append( str("CVE-2023-")+str(itemText))
        else: continue # do not treat non-MITRE links
    # output module
    with open("CVE List.txt", "w+") as txt_file:
        for line in CVE_List:
            txt_file.write("".join(line) + "\n")
    setting.lastCVE = driver.find_element(By.XPATH,"//h4[text()='More Information:']/following-sibling::ul[1]/li[last()]/a").text.replace("https://cve.mitre.org/cgi-bin/cvename.cgi?name=","")
    driver.quit()

if __name__=="__main__": 
    print("GOV-CVE Link Processor Called")