from sikuli import*
import HTMLTestRunner 
reload(HTMLTestRunner)
import unittest
import os,sys
import xlrd

RootFolder = "C:\\Users\\nbhushan\\Desktop\\SikuliFramework_PRE2019"

if not RootFolder in sys.path: 
    sys.path.append(RootFolder)
 
from  Effects import *
from  Transitions import *
from  GlassPane_GE import *

print "Starting execution of UI tests for PRE application."

workbook = xlrd.open_workbook(RootFolder+"\\TestData\\" + "PRE_Test_Execution_Data.xls")
worksheet = workbook.sheet_by_index(0)

testcase_list = []
for row in range(worksheet.nrows):
    area_flag = worksheet.cell(row, 3).value
    if area_flag == 1:
        testcase_list.append(worksheet.cell(row, 1).value)

print testcase_list

suite = unittest.TestSuite()

for testcase in testcase_list:
    if testcase == "Effects":
        suite.addTest(Effects("test_UI_Effects"))
    elif testcase == "Transitions":
        suite.addTest(Transitions("test_UI_Transitions"))
    elif testcase == "GlassPane_GE":
        suite.addTest(GlassPane_GE("test_UI_GlassPane_GE"))

outfile = file("C:\\Users\\nbhushan\\Desktop\\SikuliFramework_PRE2019\\Output\\TestReport.html", "wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='PRE UI Tests Execution Report', description='This is test report for test execution of UI tests for Premiere Elements application.' )
runner.run(suite)