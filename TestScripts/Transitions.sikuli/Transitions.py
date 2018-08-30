import utils
reload(utils)
from utils import *
import os
import sys

if not utils.RootFolder in sys.path: 
    sys.path.append(utils.RootFolder)

import StringIO

fp = file(os.path.join(utils.OutputFolder, "Test_report_Transitions.html"), "wb")

import unittest
import HTMLTestRunner
reload(HTMLTestRunner)
setAutoWaitTimeout(60)

class Test_Transitions(unittest.TestCase):

    def setUp(self):       
        utils.openPRE()
                    
    def test_UI_Transitions(self):
        find(utils.getBaselineImg('Button_GoalScreen_CloseGoalScreen.png'))
        click(utils.getBaselineImg('Button_GoalScreen_CloseGoalScreen.png'))
        find(utils.getBaselineImg('BaselineIMG_PREMenuBar.png'))
        click(utils.getBaselineImg('Button_ExpertRoom.png'))
        find(utils.getBaselineImg('BaselineIMG_ExportRoomTimeline.png'))
        wait(2)
        
        click(utils.getBaselineImg('Button_RHSPanels_Transitions.png'))
        assert(exists(utils.getBaselineImg('DropDown_TransitionssPanel_AllCategories.png')))
        click(utils.getBaselineImg('DropDown_TransitionssPanel_AllCategories.png'))
        assert(exists(utils.getBaselineImg('BaselineIMG_Transitions_AllCategories.png')))        
        click(utils.getBaselineImg('Transition_Category_3DMotion.png'))       
        assert(exists(utils.getBaselineImg('Transition_Category_3DMotion_items.png')))
        click(utils.getBaselineImg('Transition_Category_Next.png'))
        click(utils.getBaselineImg('NonClickable_TransitionsPanel_EffectsText.png'))
        assert(exists(utils.getBaselineImg('Transition_Category_Dissolve_items.png')))
        click(utils.getBaselineImg('Transition_Category_Next.png'))
        click(utils.getBaselineImg('NonClickable_TransitionsPanel_EffectsText.png'))        
        assert(exists(utils.getBaselineImg('Transition_Category_Iris_items.png')))
        click(utils.getBaselineImg('Transition_Category_Next.png'))
        click(utils.getBaselineImg('NonClickable_TransitionsPanel_EffectsText.png'))   
        assert(exists(utils.getBaselineImg('Transition_Category_Map_items.png')))
        click(utils.getBaselineImg('Transition_Category_Next.png'))
        click(utils.getBaselineImg('NonClickable_TransitionsPanel_EffectsText.png'))
        assert(exists(utils.getBaselineImg('Transition_Category_NewBlue3DExplosion_items.png')))
        click(utils.getBaselineImg('Transition_Category_Next.png'))
        click(utils.getBaselineImg('NonClickable_TransitionsPanel_EffectsText.png'))
        assert(exists(utils.getBaselineImg('Transition_Category_NewBlue3DTransformations_items.png')))
        click(utils.getBaselineImg('Transition_Category_Next.png'))
        click(utils.getBaselineImg('NonClickable_TransitionsPanel_EffectsText.png'))
        assert(exists(utils.getBaselineImg('Transition_Category_NewBlue_ArtBlends_items.png')))
        click(utils.getBaselineImg('Transition_Category_Next.png'))
        click(utils.getBaselineImg('NonClickable_TransitionsPanel_EffectsText.png'))
        assert(exists(utils.getBaselineImg('Transition_Category_NewBlue_MotionBlends_items.png')))
        click(utils.getBaselineImg('Transition_Category_Next.png'))
        click(utils.getBaselineImg('NonClickable_TransitionsPanel_EffectsText.png'))
        assert(exists(utils.getBaselineImg('Transition_Category_PagePeel_items.png')))
                
        click(utils.getBaselineImg('Transition_Category_Next.png'))
        click(utils.getBaselineImg('NonClickable_TransitionsPanel_EffectsText.png'))
        assert(exists(utils.getBaselineImg('Transition_Category_PictureWipes_items.png')))
                    
        click(utils.getBaselineImg('Transition_Category_Next.png'))
        click(utils.getBaselineImg('NonClickable_TransitionsPanel_EffectsText.png'))
        assert(exists(utils.getBaselineImg('Transition_Category_Slide_items.png')))
                        
        click(utils.getBaselineImg('Transition_Category_Next.png'))
        click(utils.getBaselineImg('NonClickable_TransitionsPanel_EffectsText.png'))
        assert(exists(utils.getBaselineImg('Transition_Category_SpecialEffects_items.png')))
        
        click(utils.getBaselineImg('Transition_Category_Next.png'))
        click(utils.getBaselineImg('NonClickable_TransitionsPanel_EffectsText.png'))              
        assert(exists(utils.getBaselineImg('Transition_Category_Stretch_items.png')))
        
        click(utils.getBaselineImg('Transition_Category_Next.png'))
        click(utils.getBaselineImg('NonClickable_TransitionsPanel_EffectsText.png'))   
        assert(exists(utils.getBaselineImg('Transition_Category_Wipe_items.png')))
                    
        click(utils.getBaselineImg('Transition_Category_Next.png'))
        click(utils.getBaselineImg('NonClickable_TransitionsPanel_EffectsText.png'))
        assert(exists(utils.getBaselineImg('Transition_Category_Zoom_items.png')))
                                                                                                                                                        
    def tearDown(self):
        utils.closePRE()              

suite = unittest.TestLoader().loadTestsFromTestCase(Test_Transitions)

runner = HTMLTestRunner.HTMLTestRunner(
                stream=fp,
                title='Search Transitions Test',
                description='Test report for searching all Transitions in PRE.'
                )
runner.run(suite)
