import os, sys, platform


if platform.system()=='Windows':
    AppPath_PRE = "C:\Program Files\Adobe\Adobe Premiere Elements 2019\PremiereElementsEditor.exe"
    userdir = os.path.expanduser('~')
    userdir.replace("\\", "\\\\")

    RootFolder = userdir + "\\Desktop\\SikuliFramework_PRE2019"
    BaselineFolder = RootFolder + "\\BaselineImages\\"
    OutputFolder = RootFolder + "\\Output\\"
    TestDataFile_path = RootFolder + "\\TestData\\test.mp4"
    Sikuli_Path = userdir + "\\Downloads"

elif platform.system()=='Darwin':
    AppPath_PRE = "/Applications/Adobe Premiere Elements 2019/Support Files/Adobe Premiere Elements.app"
    userdir = os.path.expanduser('~')

    RootFolder = userdir + "/Desktop/SikuliFramework_PRE2019"
    BaselineFolder = RootFolder + "/BaselineImages/"
    OutputFolder = RootFolder + "/Output/"
    TestDataFile_path = RootFolder + "/TestData/test.mp4"
    Sikuli_Path = userdir + "/Downloads"