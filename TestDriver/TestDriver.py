import xlrd
import os
import os
import sys
import time

RootFolder = "C:\\Users\\nbhushan\\Desktop\\SikuliFramework_PRE2019"
Sikuli_Path = "C:\\Users\\nbhushan\\Downloads\\"

if not RootFolder in sys.path: 
    sys.path.append(RootFolder)

workbook = xlrd.open_workbook(RootFolder+"\\TestDriver\\" + "PRE_Test_Area.xls")
worksheet = workbook.sheet_by_index(0)

for row in range(worksheet.nrows):
    area_flag = worksheet.cell(row, 3).value
    if area_flag == 1:
        area_name = worksheet.cell(row, 1).value
        area_script_path = RootFolder + "\\TestScripts\\" + area_name + ".sikuli"
        script_run_command = Sikuli_Path + "runsikulix.cmd -r " + area_script_path 
        print "Running area: " + area_name
        os.system(script_run_command)
        print "Completed execution of: " + area_name + " area."
        time.sleep(5)
    
