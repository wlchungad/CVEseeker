from modules import setting
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
def remove_prefix_list(list_prefix, url_item):
    for prefix in list_prefix:
        if url_item.startswith(prefix):
            return url_item.removeprefix(prefix)
    return url_item

def process_GOV_Link(weblink):
    CVE_List = []
    page = requests.get(weblink)
    soup = BeautifulSoup(page.text, "html.parser")
    # get title 
    pageTitle = soup.find("h1").text.replace("):", "(").split("(",2)[1:]
    with open("Title.txt", "w+") as txtFile:
        for each in pageTitle:
            txtFile.write(each.strip())
            txtFile.write('\n')
    # identify if it is MS regular patch list
    if ("Microsoft Products" in pageTitle[1]):
        setting.alertType = "MS"
    elif ("Microsoft Edge" in pageTitle[1]):
        setting.alertType = "edge"
        setting.edgeVersion = str(soup(text=lambda t: "Microsoft Edge prior to version " in t.text)[0]).replace("Microsoft Edge prior to version ",'')
        print(str(soup(text=lambda t: "Microsoft Edge prior to version " in t.text)[0]).replace("Microsoft Edge prior to version ",'Edge Version: '))
    elif ("Microsoft Windows" in pageTitle[1]):
        setting.alertType = "windows"
    # get links
    """
        20250801: Now the gov staff are "smart" to use cve.org instead of cve.mitre.org, but WITHOUT ANY NOTICE
        so I need to add compatibility to it. THANKS
    """
    link_count = 0
    localFlag = False
    urlList = [i.text for i in soup.find_all("li") if ("//cve.mitre.org/" in i.text) or ("//www.cve.org/" in i.text)]
    # print (urlList)
    if not urlList:
        localFlag = True
        urlList = [i.text for i in soup.find_all("li") if ("//cve.mitre.org/" in i.text) or ("//www.cve.org/" in i.text)]
    urlList = [url.replace("http://", "https://") for url in urlList]
    if not localFlag:
        list_prefix = ["https://cve.mitre.org/cgi-bin/cvename.cgi?name=", "https://www.cve.org/CVERecord?id="]
    else:
        list_prefix = ["https://msrc.microsoft.com/update-guide/vulnerability/"]
    # print(list_prefix)
    for item in urlList:
        # print(item)
        # if any(list_prefix) in item:
        if item.startswith(tuple(list_prefix)):
            link_count += 1
            pattern = re.compile(r"CVE-([0-9]{4})-*")
            # print (re.search(pattern, item))
            year = re.search(pattern, item).group(1)
            # for year in [str(x) for x in (range(2022, datetime.now().year+1))]:
            if re.search(pattern, item):
                itemText = remove_prefix_list(list_prefix, item)
                itemText = str(re.sub(r'CVE-([0-9]{4})-','',itemText))
                # print (itemText)
                if " (to" in itemText:
                    temp = []
                    temp = re.split(r" \(to", itemText)
                    temp[1] = temp[1].replace(")","")
                    """
                        2025-06-11 : because of the stupidity of the government staff, the CVE number can be wrong and malformatted
                        Cant they read and proofread???
                        we need to fix it before processing the lists of CVEs
                        Example: CVE-2025-33052 (to CVE-33053)
                    """
                    print(temp)
                    try:
                        int(temp[1])
                    except Exception as e:
                        print(f"Error: {temp[1]} is not a valid CVE number") # it looks something like "CVE-33053"
                        temp[1] = temp[1].replace("CVE-","").strip()
                    for _ in range (int(temp[0]),int(temp[1])+1):
                        placeholder = str(f"CVE-{year}-")+str(_).zfill(4)
                        CVE_List.append(placeholder)
                else:# Only one CVE
                    CVE_List.append(str(f"CVE-{year}-")+str(itemText))
    if urlList != []:
        setting.lastCVE = remove_prefix_list(list_prefix, urlList[-1])
        print(f"There are {link_count} links, expanded to {len(CVE_List)} CVEs, the last one is {CVE_List[-1]}")    
    else:
        setting.lastCVE = "ERROR"
        print(f"There are {link_count} links, expanded to {len(CVE_List)} CVEs.\nHowever, the last CVE format is abnormal, and it will not be marked on CSV!")
    # output module
    with open("CVE List.txt", "w+") as txt_file:
        for line in CVE_List:
            txt_file.write("".join(line) + "\n")
    
if __name__=="__main__": 
    print("GOV-CVE Link Processor Called")