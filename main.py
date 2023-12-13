# custom library
from modules import LinkProcessor
from modules import CVEDownloader2 as CVEDownloader
from modules import PatchListProcessor
from modules import ClearFile
from modules import setting
from modules import MSRC

allowedYes = {"Yes", "yes", "Y", "y"}
allowedNo = {"No", "no", "n", "N"}

import re
from urllib.parse import urlparse


def getLink(hintMsg):
    while True:
        try:
            value = str(input(hintMsg)).strip()
        except ValueError:
            print("Sorry, I don't understand that.")
            continue
        if not re.search("www.govcert.gov.hk", value):  # not following the format
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


def main():
    # Step 0: Initialize global variable
    setting.init()
    exited = False
    print("=================START==================")
    while exited == False:
        while True:
            answer = input("Do you need the service? [Y/N]")
            if answer in allowedNo:
                # Sweep files to output folder
                ClearFile.ClearTemp()
                print("Files are moved and deleted.")
                print("==================END===================")
                print("bye")
                exited = True
                break
            elif answer in allowedYes or answer == "":
                # Step 1: Get the list of CVE and expand for Excel (i.e. CVE-2023-xxxx to xxxx)
                print("----------------------------------------")
                setting.alertType == ""
                LinkProcessor.process_GOV_Link(getLink("Please enter the link: "))
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
                # Step 3: Download the Justification for each Known CVE
                print("Copying CVEs and their info...")
                CVEDownloader.download_problems(setting.ProductList, setting.alertType)
                continue
            else:
                print("Invalid input")
                continue
    return


if __name__ == "__main__":
    main()
