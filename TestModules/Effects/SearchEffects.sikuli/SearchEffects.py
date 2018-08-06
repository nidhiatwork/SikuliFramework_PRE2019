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
        
        
    def test_step3_effects(self):
        if not exists('Button_ExpertRoom_Active.png'):
            click('Button_ExpertRoom.png')  
        if exists('Button_RoomSwitch_Continue.png'):
            click('Button_RoomSwitch_Continue.png')
        wait('BaselineIMG_ExportButtonInExpert.png')   
        wait(2) 
        
        wait('Button_RHSPanels_Effects.png')
        
        click('Button_RHSPanels_Effects.png')
        wait('DropDown_EffectsPanel_AllCategories.png')
        click('DropDown_EffectsPanel_AllCategories.png')
        wait('BaselineIMG_Effects_AllCategories.png')
        click('NonClickable_EffectsPanel_EffectsText.png')
        hover('Button_EffectsPanel_SearchEffect.png')
        
        workbook = xlrd.open_workbook('C:\\Users\\nbhushan\\Downloads\\SikuliFramework_PRE2019\\TestData\\PRE_Effects.xls')
        worksheet = workbook.sheet_by_index(0)
        effects_list = worksheet.col_values(0)
        for i in range (1, len(effects_list)):
            effect = worksheet.cell(i, 0).value
            wait('Button_EffectsPanel_SearchEffect_active.png')
            click('Button_EffectsPanel_SearchEffect_active.png')
            
            type(effect)
            if exists('BaselineIMG_EffectsPanel_SearchedEffect.png'):
                print(effect + " effect appeared.")
            else:
                print(effect + " effect did not appear!")
            
            click('Button_EffectsPanel_ClearEffectSearch.png')           
    
    def test_step4_teardown(self):
        type("r", KEY_WIN)
        type("C:\\Users\\nbhushan\\Desktop\\KillPre_App.bat")
        type(Key.ENTER)     
        
suite = unittest.TestLoader().loadTestsFromTestCase(TestUM)

fp = file('my_report.html', 'wb')
runner = HTMLTestRunner.HTMLTestRunner(
                stream=fp,
                title='My unit test',
                description='Test report for searching all Effects in PRE.'
                )
runner.run(suite)
