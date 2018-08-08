import unittest
import sys
import StringIO
import HTMLTestRunner
import xlrd
setAutoWaitTimeout(10)

class Test_Search_Effects(unittest.TestCase):

    def test_step1_setup(self):       
        type("r", KEY_WIN)
        type("C:\\Users\\nbhushan\\Desktop\\SikuliFramework_PRE2019\\BatFiles\\Clear_PRE_Cache.bat")
        type(Key.ENTER)
        wait(3)
        type("r", KEY_WIN)
        type("C:\Program Files\Adobe\Adobe Premiere Elements 2019\PremiereElementsEditor.exe")
        type(Key.ENTER)
        wait(5)
        wait('BaselineIMG_PREFileMenu.png')
                  
    def test_step2_handleGoalScreen(self):
        wait('Buton_GoalScreen_CloseGoalScreen.png')
        click('Buton_GoalScreen_CloseGoalScreen.png')
        wait('BaselineIMG_PREMenuBar.png')
            
    def test_step3_effects(self):
        click('Button_ExpertRoom.png')         
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
        type("C:\\Users\\nbhushan\\Desktop\\SikuliFramework_PRE2019\\BatFiles\\KillPre_App.bat")
        type(Key.ENTER)     

Settings.ActionLogs = False
Settings.InfoLogs = False
Settings.DebugLogs = False

suite = unittest.TestLoader().loadTestsFromTestCase(Test_Search_Effects)

fp = file('SearchEffects.html', 'wb')
runner = HTMLTestRunner.HTMLTestRunner(
                stream=fp,
                title='Search Effects Test',
                description='Test report for searching all Effects in PRE.'
                )
runner.run(suite)
