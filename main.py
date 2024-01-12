# custom library
from modules import requestLink as LinkProcessor
from modules import CVEDownloader5 as CVEDownloader
from modules import PatchListProcessor
from modules import ClearFile
from modules import setting
from modules import MSRC
from modules import MSCVEloader
allowedYes = {"Yes", "yes", "Y", "y"}
allowedNo = {"No", "no", "n", "N"}
exitSign = {"Exit", "exit", "EXIT"}
linkProcessedCount = 0
exited = False

import re
from urllib.parse import urlparse

def getLink(hintMsg):
    while True:
        try:
            value = str(input(hintMsg)).strip()
        except ValueError:
            print("Sorry, I don't understand that.")
            continue
        if value in exitSign:
            return "kill"
        elif not re.search("www.govcert.gov.hk", value):  # not following the format
            print("The link does not follows the format.")
            print("Example link:")
            print("https://www.govcert.gov.hk/en/alerts_detail.php?id=1154")
            continue
        else:
            parsed_url = urlparse(value)
            if parsed_url.scheme and parsed_url.netloc:
                print("Valid URL.")
                break
            else:
                print("Invalid URL!")
                continue
    return value

def run(linkProcessedCount):
    # Step 1: Get the list of CVE and expand for Excel (i.e. CVE-2023-xxxx to xxxx)
    print("****************************************")
    print(f"Link count: {linkProcessedCount}")
    print("****************************************")
    setting.alertType == ""
    _ = getLink("Please enter the link: ")
    if _ != "kill":
        LinkProcessor.process_GOV_Link(_)
    else: 
        print("Exiting...")
        global exited
        exited = True
        ClearFile.ClearTemp()
        print("Files are moved and deleted.")
        print("==================END===================")
        return
    print("Getting CVEs from GovCERT...")
    if setting.alertType == "MS":
        print("Downloading MSRC...")
        # Step 2: highlight related items for easier reading
        MSRC.downloadFile()  # Step 2.1: get raw file
        PatchListProcessor.process_patchlist(
            MSRC.patchName, setting.ProductList
        )  # Step 2.2: process file
    else:
        print(" - No need to download MSRC files.")
        pass
    if setting.alertType == "edge" or setting.alertType == "MS":
        print("Calling MS API ...")
        MSCVEloader.download_problems() # Step 2.3: download problems with specific module
    else:
        print("Copying CVEs and their info from cve.org ...")
        CVEDownloader.download_problems() # step 3: download from cve.org
    print("Done, returning...")
    return

def main():
    # Step 0: Initialize global variable
    setting.init()
    print("=================START==================")
    while exited == False:
        global linkProcessedCount
        linkProcessedCount += 1
        run(linkProcessedCount)
        setting.reset()
    return

if __name__ == "__main__":
    main()
