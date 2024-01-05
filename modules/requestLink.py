from modules import setting
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def process_GOV_Link(weblink):
    CVE_List = []
    page = requests.get(weblink)
    soup = BeautifulSoup(page.text, "html.parser")
    # get title
    pageTitle = soup.select("h3")[0].text.replace("):", "(").split("(", 2)[1:]
    with open("Title.txt", "w+") as txtFile:
        for each in pageTitle:
            txtFile.write(each.strip())
            txtFile.write("\n")

    # identify if it is MS regular patch list
    if "Microsoft Products" in pageTitle[1]:
        setting.alertType = "MS"

    # get links
    link_count = 0
    urlList = [i.text for i in soup.find_all("li") if ("https://cve.mitre.org/" in i.text)]
    for item in urlList:
        if "https://cve.mitre.org/" in item:
            link_count += 1
            for year in [str(x) for x in (range(2022, datetime.now().year+1))]:
                if year in item:
                    itemText = str(item.replace(f"https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-{year}-",""))
                    # print(itemText)
                    if " (to CVE-" in itemText:
                        temp = []
                        temp = itemText.split(f" (to CVE-{year}-")
                        temp[1] = temp[1].replace(")","")
                        for _ in range (int(temp[0]),int(temp[1])+1):
                            placeholder = str(f"CVE-{year}-")+str(_).zfill(4)
                            CVE_List.append(placeholder)
                    else:# Only one CVE
                        CVE_List.append(str(f"CVE-{year}-")+str(itemText))
    
    last_CVE = CVE_List[-1]
    setting.lastCVE = last_CVE
    print(
        f"There are {link_count} links, expanded to {len(CVE_List)} CVEs, the last one is {last_CVE}"
    )
    # output module
    with open("CVE List.txt", "w+") as txt_file:
        for line in CVE_List:
            txt_file.write("".join(line) + "\n")


if __name__ == "__main__":
    print("GOV-CVE Link Processor Called")