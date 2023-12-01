# pip install xlrd

# custom library
from modules import LinkProcessor
# from modules import CVEDownloader
from modules import CVEDownloader2 as CVEDownloader
from modules import PatchListProcessor
from modules import ClearFile
from modules import setting
from modules import MSRC

from datetime import datetime
import fnmatch, os, re, validators


def getLink(prompt):
    while True:
        try:
            value = str(input(prompt)).strip()
        except ValueError:
            print("Sorry, I don't understand that.")
            continue
        if not re.search("www.govcert.gov.hk", value): # not following the format
            print ("The link does not follows the format.")
            print ("Example link:") 
            print ("https://www.govcert.gov.hk/en/alerts_detail.php?id=1154")
            continue
        else:
            if not validators.url(value):
                print ("The link did not pass validation.")
                continue
            else: 
                print("The link passed checking.")
                break
    return value
    

if __name__=="__main__": 
    # Step 0: Initialize global variable
    setting.init()
    # Step 1: Get the list of CVE and expand for Excel (i.e. CVE-2023-xxxx to xxxx)
    # GOVLink = "https://www.govcert.gov.hk/en/alerts_detail.php?id=1154"
    # LinkProcessor.process_GOV_Link(GOVLink)
    print("=================START==================")
    LinkProcessor.process_GOV_Link(getLink("Please enter the link: "))
    print("Getting CVEs from GovCERT... Done.")
    
    if setting.alertType == "MS":
        print("Downloading MSRC...")
        # Step 2: highlight related items for easier reading
        # Step 2.1: get raw file
        MSRC.downloadFile()
        # Step 2.1: process file
        PatchListProcessor.process_patchlist(MSRC.patchName, setting.ProductList)
    else:
        print("No need to download MSRC files.")
        pass
    # Step 3: Download the Justification for each Known CVE
    print("Reading CVEs from MITRE...")
    CVEDownloader.download_problems(setting.ProductList, setting.alertType)
    # Sweep files to output folder
    ClearFile.ClearTemp()
    print("Files are moved and deleted, exiting...")
    print("==================END===================")
