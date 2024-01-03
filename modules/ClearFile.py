import os
import shutil
from datetime import datetime
from . import setting

def ClearTemp():
    fileList = ["CVE List.txt", "output.csv", "Title.txt"]
    fileOut = str("Processed_Patch_List_{}.xlsx".format(datetime.now().date()))
    # if setting.alertType == "MS": # special case: MSRC (only delete if MS is triggered)
    #     fileList.append(fileOut)
    # else:
    #     print("Note: {} is not downloaded.".format(fileOut))
    fileList.append(fileOut) # as the last one might not be MSRC-related, now I include the file to avoid missing it 
    folderPath = './output/' + str(datetime.now().date())
    # move and delete
    if not os.path.exists(folderPath): # create output sotrage folder
        os.makedirs(folderPath)
    for item in fileList:
        if os.path.exists(item): # use copy and remove to "move" safely
          shutil.copy2(item, folderPath)
          os.remove(item)
        else:
          print(" - Exception: {} does not exist.".format(item))

    # remove temp dir
    current_directory = os.getcwd()
    tempDir = os.path.join(current_directory, r'temp') # previously set temp folder is in the same folder of execution
    if os.path.exists(tempDir):
        os.rmdir(tempDir)
