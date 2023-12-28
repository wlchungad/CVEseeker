from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from . import setting
import os

def GCDriver(download_dir=None):
    option = Options()
    if (download_dir != None):
        setting.downloadFolder = download_dir
    else: # default = temp folderList
        final_directory = os.path.join(os.getcwd(), r'temp')
        if not os.path.exists(final_directory):
            os.makedirs(final_directory)
        setting.downloadFolder = final_directory
    option.add_argument("--headless=new")
    option.add_argument("--disable-extensions")
    prefs={"intl.accept_languages":"en-GB, en-US, en",
          "browser.download.folderList": 2,
          "browser.helperApps.alwaysAsk.force": False,
          "browser.download.manager.showWhenStarting": False,
          "browser.download.manager.showAlertOnComplete": False,
          "browser.helperApps.neverAsk.saveToDisk": 'application/zip,application/octet-stream,application/x-zip-compressed,multipart/x-zip,application/x-rar-compressed, application/octet-stream,application/msword,application/vnd.ms-word.document.macroEnabled.12,application/vnd.openxmlformats-officedocument.wordprocessingml.document,application/vnd.ms-excel,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/vnd.openxmlformats-officedocument.wordprocessingml.document,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/rtf,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/vnd.ms-excel,application/vnd.ms-word.document.macroEnabled.12,application/vnd.openxmlformats-officedocument.wordprocessingml.document,application/xls,application/msword,text/csv,application/vnd.ms-excel.sheet.binary.macroEnabled.12,text/plain,text/csv/xls/xlsb/xlsx,application/csv,application/download,application/vnd.openxmlformats-officedocument.presentationml.presentation,application/octet-stream',
          "browser.download.dir": setting.downloadFolder
          }
    option.add_experimental_option("prefs", prefs)
    return webdriver.Chrome(options=option)