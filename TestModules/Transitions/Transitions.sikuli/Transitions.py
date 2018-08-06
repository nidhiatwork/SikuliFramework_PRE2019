import unittest
import sys
import StringIO
import HTMLTestRunner
import xlrd
setAutoWaitTimeout(10)

class TestUM(unittest.TestCase):

    def test_step1_setup(self):       
        type("r", KEY_WIN)
        type("C:\Program Files\Adobe\Adobe Premiere Elements 2019\PremiereElementsEditor.exe")
        type(Key.ENTER)
        wait('BaselineIMG_PREFileMenu.png')
              
       
    def test_step2_handleGoalScreen(self):
        if exists('BaselineIMG_GoalScreen.png'):
            click('Buton_GoalScreen_CloseGoalScreen.png')
            wait('BaselineIMG_PREMenuBar.png')
        
        
    def test_step3_transitions(self):
        if not exists('Button_ExpertRoom_Active.png'):
            click('Button_ExpertRoom.png')   

        if exists('Button_RoomSwitch_Continue.png'):
            click('Button_RoomSwitch_Continue.png')
        wait('BaselineIMG_ExportButtonInExpert.png')   
        wait(2)
        
        click('Button_RHSPanels_Transitions.png')       
        
        wait('DropDown_TransitionssPanel_AllCategories.png')
        click('DropDown_TransitionssPanel_AllCategories.png')
        wait('BaselineIMG_Transitions_AllCategories.png')
        
        click('NonClickable_TransitionsPanel_EffectsText.png')
        hover('Button_TransitonPanel_SearchTransition.png')      
        
        workbook = xlrd.open_workbook('C:\\Users\\nbhushan\\Downloads\\SikuliFramework_PRE2019\\TestData\\PRE_Transitions.xls')
        worksheet = workbook.sheet_by_index(0)
        transitions_list = worksheet.col_values(0)
        for i in range (1, len(transitions_list)):
            transition = worksheet.cell(i, 0).value
            wait('Button_TransitionPanel_SearchTransition_active.png')
            click('Button_TransitionPanel_SearchTransition_active.png')
            type(transition)         
            wait('BaselineIMG_TransitionPanel_SearchedTransition.png') 
            
            if exists('BaselineIMG_TransitionPanel_SearchedTransition.png'):
                print(transition + " transition appeared.")
            else:
                print(transition + " transition did not appear!")
            
            click('Button_TransitionPanel_ClearTransitionSearch.png')           
    
    def test_step4_teardown(self):
        type("r", KEY_WIN)
        type("C:\\Users\\nbhushan\\Desktop\\KillPre_App.bat")
        type(Key.ENTER)     
        
suite = unittest.TestLoader().loadTestsFromTestCase(TestUM)

fp = file('my_report.html', 'wb')
runner = HTMLTestRunner.HTMLTestRunner(
                stream=fp,
                title='My unit test',
                description='Test report for searching all Transitions in PRE.'
                )
runner.run(suite)
