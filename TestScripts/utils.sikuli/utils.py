from sikuli import *
import os

AppPath_PRE = "C:\Program Files\Adobe\Adobe Premiere Elements 2019\PremiereElementsEditor.exe"
Sikuli_Path = "C:\Users\nbhushan\Downloads"


userdir = os.path.expanduser('~')
userdir.replace("\\", "\\\\")

RootFolder = userdir + "\\Desktop\\SikuliFramework_PRE2019"
BaselineFolder = RootFolder + "\\BaselineImages\\"
OutputFolder = RootFolder + "\\Output\\"
TestDataFile_path = RootFolder + "\\TestData\\test.mp4"

def openPRE():
        type("r", KEY_WIN)
        type(RootFolder + "\\BatFiles\\Clear_PRE_Cache.bat")
        type(Key.ENTER)
        wait(3)
        type("r", KEY_WIN)
        type(AppPath_PRE)
        type(Key.ENTER) 
        wait(10)
        
def closePRE():
        type("r", KEY_WIN)
        type(RootFolder + "\\BatFiles\\Kill_PRE_App.bat")
        type(Key.ENTER)

def getBaselineImg( str ):
        return BaselineFolder+ str