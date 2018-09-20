from sikuli import *
import os, sys
import traceback
from TestScripts import Constants as Constants
reload(Constants)
import BaselineImages
reload(BaselineImages)

def cleanCache_And_LaunchPRE():
        print "\n~~~~~~~~Cleaning cache files and launching PRE application~~~~~~~~"
        type("r", KEY_WIN)
        type(Constants.RootFolder + "\\BatFiles\\PRE_Clean_Launch.bat")
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
        type(Constants.RootFolder + "\\BatFiles\\Kill_PRE_App.bat")
        type(Key.ENTER)
        wait(3)

def getBaselineImg( img_name ):
        return Constants.BaselineFolder+ img_name
        
def findElement( element ):       
        element_name = getElementNameFromFullPath(element)
        print "Finding element: " + element_name
        try:
                find(element)
        except:
                        stack = traceback.extract_stack(limit = 2)
                        print "Unable to find element: " + element_name + "\nBelow are details:\n" + str(sys.exc_info()[0]) + " -- line no. " + str(stack[0][1])
                        raise

def clickElement( element ):
        element_name = getElementNameFromFullPath(element)
        print "Clicking on element: " + element_name
        try:
                click(element)
        except:
                stack = traceback.extract_stack(limit = 2)
                print "Unable to click element: " + element_name + "\nBelow are details:\n" + str(sys.exc_info()[0]) + " -- line no. " + str(stack[0][1])
                raise

def hoverElement( element ):
        element_name = getElementNameFromFullPath(element)
        print "Hovering on element: " + element_name
        try:
                hover(element)
        except:
                stack = traceback.extract_stack(limit = 2)
                print "Unable to hover on element: " + element_name + "\nBelow are details:\n" + str(sys.exc_info()[0]) + " -- line no. " + str(stack[0][1])
                raise

def assertElementExists( element ):
        element_name = getElementNameFromFullPath(element)
        print "Asserting whether element exists: " + element_name
        try:
                assert(exists(element))
        except AssertionError:
                stack = traceback.extract_stack(limit = 2)
                print "Unable to assert image exists: " + element_name + "\nBelow are details:\n" + str(sys.exc_info()[0]) + " -- line no. " + str(stack[0][1])
                raise

def getElementNameFromFullPath( image_path ):
        element_path_list = image_path.split("\\")
        image_item = element_path_list[len(element_path_list)-1]
        return image_item