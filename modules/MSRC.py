from . import FirefoxProfile as FP
from . import setting
#from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
import time, os, shutil, fnmatch
#from pathlib import Path

def downloadFile():
    # call pre-defined driver (see FirefoxProfile)
    driver = FP.FFdriver()
    driver.get("https://msrc.microsoft.com/update-guide/")
    time.sleep(5)    
    try: # auto select and download
       time.sleep(1)
       print ("-> Opening option")
       driver.execute_script("document.querySelector('[title=\"Select a different date range\"]').click()")
       time.sleep(1)
       # selecting month
       print ("-> Select current month option")
       driver.execute_script("document.querySelectorAll('[class^=\"ms-Dropdown-title\"]')[2].click()")
       time.sleep(1)
       command = "document.querySelectorAll('[role=\"listbox\"] > * > [data-automationid=\"splitbuttonprimary\"]')["+str(datetime.now().month-1)+"].click()" # month button
       driver.execute_script(command)
       time.sleep(1)
       # select year
       print ("-> Select current year option")
       driver.execute_script(f"document.querySelectorAll('[role=\"spinbutton\"]')[0].value={datetime.now().year}")
       time.sleep(1)
       driver.execute_script("document.querySelectorAll('[class^=\"ms-Dropdown-title\"]')[2].click()")
       time.sleep(1)
       # select today
       print ("-> Save options")
       driver.execute_script("document.querySelector('[title=\"Save and use your new date selections\"]').click()")
       time.sleep(5)
    except: # manual
        print("You have 20 seconds to change date...")
        time.sleep(20)

    # call all elements out (for xlsx output)
    while True:
        try:
            driver.find_element(By.XPATH, "//span[contains(text(),'Load')]/ancestor::button").click()
        except NoSuchElementException:
            # print("We reached the end!")
            break
    
    # output: download file
    try:
        driver.find_element(By.XPATH, "//span[contains(text(),'Download')]/ancestor::button").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//span[contains(text(),'Start')]/ancestor::button").click()
        while True:
            try:
                _ = driver.find_element(By.XPATH,"//span[text()='Download complete!']")
                print ("Download completed!")
                break
            except:
                print ("...Waiting for 5 seconds...")
                time.sleep(5)
                continue
    except: # if selenium fails (again)...
        print ("Selenium cannot click, please download manually to continue...(Timeout: {}s)".format(60))
        time.sleep(60)
    driver.close() # close driver to free resources
    
    # after output: rename file
    month = ("0" + str(datetime.now().month)) if int(datetime.now().month) < 10 else datetime.now().month
    day = ("0" + str(datetime.now().day)) if int(datetime.now().day) < 10 else datetime.now().day
    startDate = str(datetime.now().year) + "-" + month + "-" + "01"
    endDate   = str(datetime.now().year) + "-" + month + "-" + day
    filename  = str("Microsoft Patch List ("+ startDate +" to "+ endDate +").xlsx")
    
    # output filename for other functions 
    global patchName 
    patchName = filename
    searchField = 'Security Updates {}-{}-{}*.xlsx'.format(datetime.now().year, month, day)
    downloadFolder = setting.downloadFolder
    for file in os.listdir(downloadFolder):
        #print("In folder: {}".format(file))
        #print(f"Searching: {searchField}")
        if fnmatch.fnmatch(file, searchField):
            #print("New: {}".format(filename))
            oldPath = downloadFolder + "\\" + file
            newPath = ".\\" + filename
            try:
                os.remove(newPath)
                print(" - Old file found & removed.")
            except OSError: # OSError means no file found -> should be safe
                print(" - Safe - No old file found.")
                pass
            shutil.move(oldPath, newPath)
           