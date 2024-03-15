import csv

def init():
    # put constants here
    global ProductList 
    ProductList = set()
    with open(".\\conf\\productlist.conf", "r", encoding='UTF-8') as _:
        for line in _:
            ProductList.add(line.strip())
    # global variable indicating if the Security Alert is about Monthly update
    global alertType
    alertType = None
    # global variable of downloading directoty
    global downloadFolder
    downloadFolder = "" # default is None, and will be further defined in FirefoxProfile.py
    # global variable indicating set of non-applicable vulnerabilities
    # Note: the selection is just in favor of personal usage, please feel free to change to fit your need
    global uselessSet
    uselessSet = set()
    with open(".\\conf\\unused.conf", "r", encoding='UTF-8') as _:
        for line in _:
            uselessSet.add(line.strip())
    # prepare a last CVE Number in case the item is not applicable
    # i.e. cveList[-1]
    global lastCVE
    global govcertLink
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
    global govcertLink
    govcertLink = ""