import unittest
import sys
import StringIO
import HTMLTestRunner
import xlrd
setAutoWaitTimeout(20)

class Test_Search_Transitions(unittest.TestCase):

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
               
    def test_step3_transitions(self):
        click('Button_ExpertRoom.png')         
        wait('BaselineIMG_ExportButtonInExpert.png')   
        wait(2)        
        click('Button_RHSPanels_Transitions.png')               
        assert(exists('DropDown_TransitionssPanel_AllCategories.png'))
        click('DropDown_TransitionssPanel_AllCategories.png')
        assert(exists('BaselineIMG_Transitions_AllCategories.png'))        
        click('Transition_Category_3DMotion.png')       
        assert(exists('Transition_Category_3DMotion_items.png'))
        click('Transition_Category_Next.png')
        click('NonClickable_TransitionsPanel_EffectsText.png')
        assert(exists('Transition_Category_Dissolve_items.png'))
        click('Transition_Category_Next.png')
        click('NonClickable_TransitionsPanel_EffectsText.png')        
        assert(exists('Transition_Category_Iris_items.png'))
        click('Transition_Category_Next.png')
        click('NonClickable_TransitionsPanel_EffectsText.png')   
        assert(exists('Transition_Category_Map_items.png'))
        click('Transition_Category_Next.png')
        click('NonClickable_TransitionsPanel_EffectsText.png')
        assert(exists('Transition_Category_NewBlue3DExplosion_items.png'))
        click('Transition_Category_Next.png')
        click('NonClickable_TransitionsPanel_EffectsText.png')
        assert(exists('Transition_Category_NewBlue3DTransformations_items.png'))
        click('Transition_Category_Next.png')
        click('NonClickable_TransitionsPanel_EffectsText.png')
        assert(exists('Transition_Category_NewBlue_ArtBlends_items.png'))
        click('Transition_Category_Next.png')
        click('NonClickable_TransitionsPanel_EffectsText.png')
        assert(exists('Transition_Category_NewBlue_MotionBlends_items.png'))
        click('Transition_Category_Next.png')
        click('NonClickable_TransitionsPanel_EffectsText.png')
        assert(exists('Transition_Category_PagePeel_items.png'))
                
        click('Transition_Category_Next.png')
        click('NonClickable_TransitionsPanel_EffectsText.png')
        assert(exists('Transition_Category_PictureWipes_items.png'))
                    
        click('Transition_Category_Next.png')
        click('NonClickable_TransitionsPanel_EffectsText.png')
        assert(exists('Transition_Category_Slide_items.png'))
                        
        click('Transition_Category_Next.png')
        click('NonClickable_TransitionsPanel_EffectsText.png')
        assert(exists('Transition_Category_SpecialEffects_items.png'))
        
        click('Transition_Category_Next.png')
        click('NonClickable_TransitionsPanel_EffectsText.png')              
        assert(exists('Transition_Category_Stretch_items.png'))
        
        click('Transition_Category_Next.png')
        click('NonClickable_TransitionsPanel_EffectsText.png')   
        assert(exists('Transition_Category_Wipe_items.png'))
                    
        click('Transition_Category_Next.png')
        click('NonClickable_TransitionsPanel_EffectsText.png')
        assert(exists('Transition_Category_Zoom_items.png'))
                                                                                                                                                        
    def test_step4_teardown(self):
        type("r", KEY_WIN)
        type("C:\\Users\\nbhushan\\Desktop\\SikuliFramework_PRE2019\\BatFiles\\KillPre_App.bat")
        type(Key.ENTER)     

Settings.ActionLogs = False
Settings.InfoLogs = False
Settings.DebugLogs = False

suite = unittest.TestLoader().loadTestsFromTestCase(Test_Search_Transitions)

fp = file('SearchTransitions.html', 'wb')
runner = HTMLTestRunner.HTMLTestRunner(
                stream=fp,
                title='Search Transitions Test',
                description='Test report for searching all Transitions in PRE.'
                )
runner.run(suite)
