from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from . import setting

import os

def FFdriver(download_dir=None):
    option = Options()
    option.set_preference('intl.accept_languages', 'en-GB, en-US, en')
    option.set_preference("browser.download.folderList", 2)
    option.set_preference("browser.helperApps.alwaysAsk.force", False)
    option.set_preference("browser.download.manager.showWhenStarting", False)
    option.set_preference("browser.download.manager.showAlertOnComplete", False)
    option.set_preference('browser.helperApps.neverAsk.saveToDisk','application/zip,application/octet-stream,application/x-zip-compressed,multipart/x-zip,application/x-rar-compressed, application/octet-stream,application/msword,application/vnd.ms-word.document.macroEnabled.12,application/vnd.openxmlformats-officedocument.wordprocessingml.document,application/vnd.ms-excel,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/vnd.openxmlformats-officedocument.wordprocessingml.document,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/rtf,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/vnd.ms-excel,application/vnd.ms-word.document.macroEnabled.12,application/vnd.openxmlformats-officedocument.wordprocessingml.document,application/xls,application/msword,text/csv,application/vnd.ms-excel.sheet.binary.macroEnabled.12,text/plain,text/csv/xls/xlsb/xlsx,application/csv,application/download,application/vnd.openxmlformats-officedocument.presentationml.presentation,application/octet-stream')
    if (download_dir != None):
        option.set_preference("browser.download.dir", download_dir)
        setting.downloadFolder = download_dir
    else: # default = temp folderList
        current_directory = os.getcwd()
        final_directory = os.path.join(current_directory, r'temp')
        if not os.path.exists(final_directory):
            os.makedirs(final_directory)
        option.set_preference("browser.download.dir", final_directory)
        setting.downloadFolder = final_directory
    return webdriver.Firefox(options=option)