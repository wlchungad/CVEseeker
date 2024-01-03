import csv

def init():
    # put constants here
    global ProductList 
    ProductList = {"Windows Server 2016", "Windows Server 2016 (Server Core installation)",
                    "Microsoft Excel 2013 Service Pack 1 (64-bit editions)",
                    "Microsoft Outlook 2013 Service Pack 1 (64-bit editions)",
                    "Microsoft Word 2013 Service Pack 1 (64-bit editions)",
                    "Microsoft Publisher 2013 Service Pack 1 (64-bit editions)",
                    "Microsoft Office 2013 Service Pack 1 (64-bit editions)",
                    "Microsoft Edge (Chromium-based)",
                    "Microsoft ODBC Driver 13 for SQL Server on Windows",
                    "Microsoft ODBC Driver 17 for SQL Server on Windows",
                    "Microsoft OLE DB Driver 18 for SQL Server","Microsoft OLE DB Driver 19 for SQL Server",
                    "Microsoft .NET Framework 3.5 AND 4.6.2/4.7/4.7.1/4.7.2",
                    "Microsoft .NET Framework 3.5 AND 4.7.2",
                    "Microsoft .NET Framework 3.5 AND 4.8",
                    "Microsoft .NET Framework 3.5",
                    "System Center Operations Manager (SCOM) 2016"}
    # global variable indicating if the Security Alert is about Monthly update
    global alertType
    alertType = None
    # global variable of downloading directoty
    global downloadFolder
    downloadFolder = "" # default is None, and will be further defined in FirefoxProfile.py
    # global variable indicating set of non-applicable vulnerabilities
    # Note: the selection is just in favor of personal usage, please feel free to change to fit your need
    global uselessSet
    uselessSet = {"Apple iOS and iPadOS",
                  "Android",
                  "Firefox",
                  "QNAP Products",
                  "Drupal",
                  "SonicWall", 
                  "Intel Products", 
                  "Fortinet Products", 
                  "Cisco Products", 
                  "Adobe Reader/Acrobat",
                  "Google Chrome",
                  "Bluetooth devices"}
    # prepare a last CVE Number in case the item is not applicable
    # i.e. cveList[-1]
    global lastCVE
    # prepare the output.csv
    with open('output.csv', 'w+', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Again, the format is personal, but you can can always change that
        writer.writerow(['Security Alert Number',' ','Related to ERKS system?','CVE-ID', 'Required?', 'Justification']) 
        #csvfile.close()
def reset():
    global lastCVE
    lastCVE = ""
    global alertType
    alertType = ""