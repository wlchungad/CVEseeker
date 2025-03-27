import csv
# import json
# import re
from tqdm import tqdm
import requests
import time
# import sys
from . import setting

# we can call API now
def download_problems():
    # ProductList = importList
    temp = []
    alertInfo = []
    rowContent = []
    count = 0
    Initial = "https://api.msrc.microsoft.com/sug/v2.0/en-US/vulnerability/"
    with open("Title.txt", "r") as txt_file:
        for line in txt_file.readlines():
            alertInfo.append(line.replace("\n", ""))
    with open("CVE List.txt", "r") as txt_file:
        for line in txt_file.readlines():
            count += 1
            temp.append(Initial + line.strip())
    # print(temp)
    # to append each big item and sub-item to csv
    with open("output.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile)  # header is generated in setting, we just append to that csv file
        isFirstRow = True
        for each in tqdm(temp, desc="Progress: "):  # progress bar added
            #print(each)
            try:
                page = requests.get(each).json()
                time.sleep(1)
                Code = page["cveNumber"]
                #tqdm.write(f"{Code}")
                Context = page["cveTitle"]
                if "Chromium security severity" in Context:  # Edge specific, else continue
                    Context = str((Context.split(" in Google Chrome prior to"))[0]).strip()
                elif "Chromium: CVE-" in Context:
                    Context = str(Context.replace(f"Chromium: {Code} ", ""))
                #tqdm.write(f"{Context}")
                if (isFirstRow):  # for first row, it's better to mark down how the CVEs are called officially
                    rowContent = [alertInfo[0], alertInfo[1], "Yes", Code, "Yes", Context]
                    isFirstRow = False
                else:
                    rowContent = ["", "", "", Code, "Yes", Context]
                if setting.alertType == "edge":
                    rowContent.append(setting.edgeVersion)
                # print("\n", rowContent, '\n')  # to check rowContent list before writing to csv file
                writer.writerow(rowContent)
            except Exception as e:
                rowContent = ["", "", "", Code, "?", e]
                writer.writerow(rowContent)
                print("Error occurred while writing, probably it is not readable yet")
    return

if __name__ == "__main__":
    print("Downloader Called")