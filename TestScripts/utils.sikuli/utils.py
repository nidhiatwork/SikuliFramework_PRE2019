from sikuli import *
import os, sys
import traceback
from TestScripts import Constants as Constants
reload(Constants)
import BaselineImages
reload(BaselineImages)

def cleanCache_And_LaunchPRE():
        print "\n~~~~~~~~Cleaning cache files and launching PRE application~~~~~~~~"
        os.system(Constants.RootFolder + "\\BatFiles\\PRE_Clean_Launch.bat")       
        openApp('C:\Program Files\Adobe\Adobe Premiere Elements 2019\PremiereElementsEditor.exe') 
        setAutoWaitTimeout(240)

        try:
                setBundlePath(Constants.BaselineFolder)
                find("Button_GoalScreen_CloseGoalScreen.png")
        except:
                print("Unable to launch PRE application after waiting for 60 seconds. End of execution.")
                closePRE()
                sys.exit(0)

        setAutoWaitTimeout(30)      

def closePRE():
        print "~~~~~~~~Closing any open instance of PRE application~~~~~~~~"
        os.system(Constants.RootFolder + "\\BatFiles\\Kill_PRE_App.bat")       
        wait(3)

        
def findElement( element ):       
        print "Finding element: " + element
        try:
                find(element)
        except:
                        stack = traceback.extract_stack(limit = 2)
                        print "Unable to find element: " + Constants.BaselineFolder + element + "\nBelow are details:\n" + str(sys.exc_info()[0]) + " -- line no. " + str(stack[0][1])
                        raise

def clickElement( element ):
        print "Clicking on element: " + element
        try:
                click(element)
        except:
                stack = traceback.extract_stack(limit = 2)
                print "Unable to click element: " + Constants.BaselineFolder + element + "\nBelow are details:\n" + str(sys.exc_info()[0]) + " -- line no. " + str(stack[0][1])
                raise

def hoverElement( element ):
        print "Hovering on element: " + element
        try:
                hover(element)
        except:
                stack = traceback.extract_stack(limit = 2)
                print "Unable to hover on element: " + Constants.BaselineFolder + element + "\nBelow are details:\n" + str(sys.exc_info()[0]) + " -- line no. " + str(stack[0][1])
                raise

def assertElementExists( element ):
        print "Asserting whether element exists: " + element
        try:
                assert(exists(element))
        except AssertionError:
                stack = traceback.extract_stack(limit = 2)
                print "Unable to assert image exists: " + Constants.BaselineFolder + element + "\nBelow are details:\n" + str(sys.exc_info()[0]) + " -- line no. " + str(stack[0][1])
                raise

def typeKeys( data ):
        print "Typing: " + data
        try:
                type(data)
        except:
                stack = traceback.extract_stack(limit = 2)
                print "Unable to type: " + data + "\nBelow are exception details:\n" + str(sys.exc_info()[0]) + " -- line no. " + str(stack[0][1])
                raise

def dragDropElement(sourceImg, destImg):
        print "Dragging and dropping: " + sourceImg + " to " + destImg
        try:
                dragDrop(sourceImg, destImg)
        except:
                stack = traceback.extract_stack(limit = 2)
                print "Unable to drag and drop: " + Constants.BaselineFolder + sourceImg + "to " + Constants.BaselineFolder + sourceImg + "\nBelow are exception details:\n" + str(sys.exc_info()[0]) + " -- line no. " + str(stack[0][1])
                raise

def pressAndHoldElement( element, seconds ):       
        print "Pressing and holding on element: " + element + "for " + str(seconds) + "seconds"
        try:
                
                hoverElement(element)
                mouseDown(Button.LEFT)
                mouseMove(element)
                wait(seconds)
                mouseUp()
        except:
                stack = traceback.extract_stack(limit = 2)
                print "Unable to press and hold on element: " + Constants.BaselineFolder + element + "\nBelow are exception details:\n" + str(sys.exc_info()[0]) + " -- line no. " + str(stack[0][1])
                raise