from sikuli import*
import HTMLTestRunner 
reload(HTMLTestRunner)
import unittest
import os,sys
import xlrd
import datetime

now = datetime.datetime.now()
userdir = os.path.expanduser('~')
userdir.replace("\\", "\\\\")

if not userdir + "\\Desktop\\SikuliFramework_PRE2019\\TestScripts" in sys.path: 
    sys.path.append(userdir + "\\Desktop\\SikuliFramework_PRE2019\\TestScripts")

import Constants
from  Effects import *
from  Transitions import *
from  GlassPane_GE import *

workbook = xlrd.open_workbook(Constants.TestExecution_DataFile)
worksheet = workbook.sheet_by_index(0)

testcase_list = []
for row in range(worksheet.nrows):
    area_flag = worksheet.cell(row, 4).value
    if area_flag == 1:
        testcase_list.append((str(worksheet.cell(row, 1).value)) + ',' + (str(worksheet.cell(row, 2).value)))

suite = unittest.TestSuite()

for testcase in testcase_list:
    testCase = testcase.split(",")
    className = testCase[0]
    functionName = testCase[1]
    suite.addTest(eval(className)(functionName))
    
outputfilename = Constants.RootFolder + "\\Output\\TestReport_" + str(now.day) + str(now.month) + str(now.year) + "_" + str(now.hour) + str(now.minute) + str(now.second) + ".html"
outfile = file(outputfilename, "wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='PRE UI Tests Execution Report', verbosity=3, dirTestScreenshots = Constants.ScreenshotsFolder, description='This is test report for test execution of UI tests for Premiere Elements application.' )
runner.run(suite)