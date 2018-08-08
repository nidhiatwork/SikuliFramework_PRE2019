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

        click('Effects_Category_AdvancedAdjustments.png')
        assert(exists('Effects_Category_AdvancedAdjustments_items.png'))
        click('Button_EffectCategories_Next.png')
       
        assert(exists('Effects_Category_BlurSharpen_items.png'))   
        click('Button_EffectCategories_Next.png')
        
        assert(exists('Effects_Category_Channel_items.png'))
        click('Button_EffectCategories_Next.png')

        assert(exists('Effects_Categories_ColorCorrection_items.png'))
        click('Button_EffectCategories_Next.png')

        assert(exists('Effects_Categories_Distort_items.png'))
        click('Button_EffectCategories_Next.png')

        assert(exists('Effects_Categories_Generate_items.png'))
        click('Button_EffectCategories_Next.png')

        assert(exists('Effects_Categories_ImageControl_items.png'))
        click('Button_EffectCategories_Next.png')

        assert(exists('Effects_Categories_Keying_items.png'))
        click('Button_EffectCategories_Next.png')

        assert(exists('Effects_Categories_NewBlueArtEffects_items.png'))
        click('Button_EffectCategories_Next.png')

        assert(exists('Effects_Categories_NewBlueCartoonrPlus_items.png'))
        click('Button_EffectCategories_Next.png')

        assert(exists('Effects_Categories_NewBlueFilmLooks_items.png'))
        click('Button_EffectCategories_Next.png')

        assert(exists('Effects_Categories_Perspective_items.png'))
        click('Button_EffectCategories_Next.png')

        assert(exists('Effects_Categories_Pixelate_items.png'))
        click('Button_EffectCategories_Next.png')

        assert(exists('Effects_Categories_Render_items.png'))
        click('Button_EffectCategories_Next.png')

        assert(exists('Effects_Categories_Stylize_items.png'))
        click('Button_EffectCategories_Next.png')

        assert(exists('Effects_Categories_Time_items.png'))
        click('Button_EffectCategories_Next.png')

        assert(exists('Effects_Categories_Transform_items.png'))
        click('Button_EffectCategories_Next.png')

        assert(exists('Effects_Categories_VideoMerge_items.png'))
        click('Button_EffectCategories_Next.png')
        wait(1)
        click('Button_EffectCategories_Next.png')

        assert(exists('Effects_Categories_HollywoodLooks_items.png'))     
        
    
 #   def test_step4_teardown(self):
  #      type("r", KEY_WIN)
 #       type("C:\\Users\\nbhushan\\Desktop\\SikuliFramework_PRE2019\\BatFiles\\KillPre_App.bat")
  #      type(Key.ENTER)     

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
