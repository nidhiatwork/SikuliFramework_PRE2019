from sikuli import *
import os, sys
import traceback

AppPath_PRE = "C:\Program Files\Adobe\Adobe Premiere Elements 2019\PremiereElementsEditor.exe"
Sikuli_Path = "C:\Users\nbhushan\Downloads"


userdir = os.path.expanduser('~')
userdir.replace("\\", "\\\\")

RootFolder = userdir + "\\Desktop\\SikuliFramework_PRE2019"
BaselineFolder = RootFolder + "\\BaselineImages\\"
OutputFolder = RootFolder + "\\Output\\"
TestDataFile_path = RootFolder + "\\TestData\\test.mp4"

setAutoWaitTimeout(15)

def cleanCache_And_LaunchPRE():
        print "\n~~~~~~~~Cleaning cache files and launching PRE application~~~~~~~~"
        type("r", KEY_WIN)
        type(RootFolder + "\\BatFiles\\PRE_Clean_Launch.bat")
        type(Key.ENTER) 
        
        setAutoWaitTimeout(60)
        try:
                find(getBaselineImg('Button_GoalScreen_CloseGoalScreen.png'))
        except:
                print("Unable to launch PRE application after waiting for 60 seconds. End of execution.")
                closePRE()
                sys.exit(0)
        setAutoWaitTimeout(15)
       
      
def closePRE():
        print "~~~~~~~~Closing any open instance of PRE application~~~~~~~~"
        type("r", KEY_WIN)
        type(RootFolder + "\\BatFiles\\Kill_PRE_App.bat")
        type(Key.ENTER)
        wait(3)

def getBaselineImg( img_name ):
        return BaselineFolder+ img_name
        
def findElement( element ):
       try:
               find(element)
       except:
                stack = traceback.extract_stack(limit = 2)
                print "Unable to find element: " + getImageNameFromFullPath(element) + "\nBelow are details:\n" + str(sys.exc_info()[0]) + " -- line no. " + str(stack[0][1])
                #raise

def clickElement( element ):
        try:
                click(element)
        except:
                stack = traceback.extract_stack(limit = 2)
                print "Unable to click element: " + getImageNameFromFullPath(element) + "\nBelow are details:\n" + str(sys.exc_info()[0]) + " -- line no. " + str(stack[0][1])
                #raise

def assertElementExists( element ):
        try:
                assert(exists(element))
        except:
                stack = traceback.extract_stack(limit = 2)
                print "Unable to assert image exists: " + getImageNameFromFullPath(element) + "\nBelow are details:\n" + str(sys.exc_info()[0]) + " -- line no. " + str(stack[0][1])
                #raise

def getImageNameFromFullPath( image_path ):
        element_path_list = image_path.split("\\")
        image_item = element_path_list[len(element_path_list)-1]
        return image_item
        



