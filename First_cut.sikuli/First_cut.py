import unittest
import sys
import StringIO
import HTMLTestRunner
import xlrd
setAutoWaitTimeout(10)

class TestUM(unittest.TestCase):

    def test_setUp(self):
        pass
 
    def test_effects(self):
        wait('AddMedia.png')
        click('AddMedia.png')
        wait('DropDown_FilesAndFolders.png')
        click('DropDown_FilesAndFolders.png')
        
        wait('Button_MediaPathWindow.png')
        click('Button_MediaPathWindow.png')
        type("C:\\Users\\nbhushan\\Desktop\\"+Key.ENTER)
        wait('MediaFileName.png')
        doubleClick('Media_FileName.png')
        wait('Button_ExpertRoom.png')
        click('Button_ExpertRoom.png')
        if exists('Button_RoomSwitch_Continue.png'):
            click('Button_RoomSwitch_Continue.png')
        wait(3)
        wait('BaselineIMG_ExpertRoomSwitch.png')
            
        wait('Button_RHSPanels_Effects.png')
        click('Button_RHSPanels_Effects.png')
        wait('DropDown_EffectsPanel_AllCategories.png')
        click('DropDown_EffectsPanel_AllCategories.png')
        wait('BaselineIMG_Effects_AllCategories.png')
        click('NonClickable_EffectsPanel_EffectsText.png')
        
        
        workbook = xlrd.open_workbook('C:\\Users\\nbhushan\\Desktop\\filters.xls')
        worksheet = workbook.sheet_by_index(0)
        hover('Button_EffectsPanel_SearchEffect.png')
        for i in range (1,8):
            filter = worksheet.cell(i, 0).value

            wait('Button_EffectsPanel_SearchEffect_active.png')
            click('Button_EffectsPanel_SearchEffect_active.png')
            
            type(filter)
            if exists('BaselineIMG_EffectsPanel_SearchedEffect.png'):
                print(filter + " effect appeared.")
            else:
                print(filter + " effect did not appear!")
            wait(3)
            click('Button_EffectsPanel_ClearEffectSearch.png')
            wait(3)           
    def test_teardown(self):
        pass

suite = unittest.TestLoader().loadTestsFromTestCase(TestUM)

fp = file('my_report.html', 'wb')
runner = HTMLTestRunner.HTMLTestRunner(
                stream=fp,
                title='My unit test',
                description='This demonstrates the report output by HTMLTestRunner.'
                )
runner.run(suite)




