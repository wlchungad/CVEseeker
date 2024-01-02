from modules import setting
import requests
from bs4 import BeautifulSoup


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
    for item in soup.select("ul>li")[1:]:
        if "https://cve.mitre.org/" in item.text:
            # print (item.text)
            link_count += 1
            itemText = str(
                item.text.replace(
                    "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-", ""
                )
            )
            if " (to CVE-2023-" in itemText:
                temp = []
                temp = itemText.split(" (to CVE-2023-")
                temp[1] = temp[1].replace(")", "")
                for _ in range(int(temp[0]), int(temp[1]) + 1):
                    placeholder = str("CVE-2023-") + str(_)
                    CVE_List.append(placeholder)
            else:  # Only one CVE
                CVE_List.append(str("CVE-2023-") + str(itemText))
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
