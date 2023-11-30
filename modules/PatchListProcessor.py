import openpyxl
from openpyxl.styles import PatternFill
from openpyxl import Workbook, load_workbook
import shutil
from datetime import datetime
import os

def process_patchlist(filename, importList):
    ProductList = importList
    wb = load_workbook(filename) 
    sheet = wb['Security Updates'] 
    # sheet = wb['To Edit'] 
    
    CVEList = []
    with open("CVE List.txt", "r") as txt_file:
        lines = [line.strip() for line in txt_file]
        for _ in lines:
            CVEList.append(_)
            
    for row in range(2, sheet.max_row + 1): 
        Product = sheet.cell(row, 2).value
        #print(Product)
        CVE_code = sheet.cell(row, 9).value
        if (CVE_code in CVEList):
            if (Product in ProductList): 
                sheet.cell(row, 2).fill = PatternFill("solid", start_color="FFa500")
            elif ("Microsoft .NET Framework" in Product) and (sheet.cell(row, 3).value == "Windows Server 2016"):
                sheet.cell(row, 2).fill = PatternFill("solid", start_color="FFa500")
            else: 
                sheet.cell(row, 2).fill = PatternFill("solid", start_color="c6efce")
        else:
             sheet.cell(row, 9).fill = PatternFill("solid", start_color="dcdcdc")
    wb.save(filename)
    fileOut = str("Processed_Patch_List_{}.xlsx".format(datetime.now().date()))
    os.rename(filename, fileOut)
    # print ("Checking Completed")
    
if __name__=="__main__": 
    print("Patch List Processor Called")