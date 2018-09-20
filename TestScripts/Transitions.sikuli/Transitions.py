import utils
reload(utils)
from utils import *
import os
import sys

import unittest

class TestTransitions(unittest.TestCase):

    def setUp(self):       
        utils.cleanCache_And_LaunchPRE()
                    
    def test_UI_Transitions(self):
        utils.clickElement(utils.getBaselineImg('Button_GoalScreen_CloseGoalScreen.png'))
        utils.findElement(utils.getBaselineImg('BaselineIMG_PREMenuBar.png'))
        utils.clickElement(utils.getBaselineImg('Button_ExpertRoom.png'))
        utils.findElement(utils.getBaselineImg('BaselineIMG_ExportRoomTimeline.png'))
        wait(2)
        
        utils.clickElement(utils.getBaselineImg('Button_RHSPanels_Transitions.png'))
        utils.assertElementExists(utils.getBaselineImg('DropDown_TransitionssPanel_AllCategories.png'))
        utils.clickElement(utils.getBaselineImg('DropDown_TransitionssPanel_AllCategories.png'))
        utils.assertElementExists(utils.getBaselineImg('BaselineIMG_Transitions_AllCategories.png'))        
        utils.clickElement(utils.getBaselineImg('Transition_Category_3DMotion.png'))       
        utils.assertElementExists(utils.getBaselineImg('Transition_Category_3DMotion_items.png'))
        utils.clickElement(utils.getBaselineImg('Transition_Category_Next.png'))
        utils.hoverElement(utils.getBaselineImg("NonClickable_TransitionsPanelText.png"))
        
        utils.assertElementExists(utils.getBaselineImg('Transition_Category_Dissolve_items.png'))
        utils.clickElement(utils.getBaselineImg('Transition_Category_Next.png'))
        utils.hoverElement(utils.getBaselineImg("NonClickable_TransitionsPanelText.png"))
        
        utils.assertElementExists(utils.getBaselineImg('Transition_Category_Iris_items.png'))
        utils.clickElement(utils.getBaselineImg('Transition_Category_Next.png'))
        utils.hoverElement(utils.getBaselineImg("NonClickable_TransitionsPanelText.png"))
        
        utils.assertElementExists(utils.getBaselineImg('Transition_Category_Map_items.png'))
        utils.clickElement(utils.getBaselineImg('Transition_Category_Next.png'))
        utils.hoverElement(utils.getBaselineImg("NonClickable_TransitionsPanelText.png"))
        
        utils.assertElementExists(utils.getBaselineImg('Transition_Category_NewBlue3DExplosion_items.png'))
        utils.clickElement(utils.getBaselineImg('Transition_Category_Next.png'))
        utils.hoverElement(utils.getBaselineImg("NonClickable_TransitionsPanelText.png"))
        
        utils.assertElementExists(utils.getBaselineImg('Transition_Category_NewBlue3DTransformations_items.png'))
        utils.clickElement(utils.getBaselineImg('Transition_Category_Next.png'))
        utils.hoverElement(utils.getBaselineImg("NonClickable_TransitionsPanelText.png"))
        
        utils.assertElementExists(utils.getBaselineImg('Transition_Category_NewBlue_ArtBlends_items.png'))
        utils.clickElement(utils.getBaselineImg('Transition_Category_Next.png'))
        utils.hoverElement(utils.getBaselineImg("NonClickable_TransitionsPanelText.png"))
        
        utils.assertElementExists(utils.getBaselineImg('Transition_Category_NewBlue_MotionBlends_items.png'))
        utils.clickElement(utils.getBaselineImg('Transition_Category_Next.png'))
        utils.hoverElement(utils.getBaselineImg("NonClickable_TransitionsPanelText.png"))
        
        utils.assertElementExists(utils.getBaselineImg('Transition_Category_PagePeel_items.png'))
                
        utils.clickElement(utils.getBaselineImg('Transition_Category_Next.png'))
        utils.hoverElement(utils.getBaselineImg("NonClickable_TransitionsPanelText.png"))
        
        utils.assertElementExists(utils.getBaselineImg('Transition_Category_PictureWipes_items.png'))
                    
        utils.clickElement(utils.getBaselineImg('Transition_Category_Next.png'))
        utils.hoverElement(utils.getBaselineImg("NonClickable_TransitionsPanelText.png"))
        
        utils.assertElementExists(utils.getBaselineImg('Transition_Category_Slide_items.png'))
                        
        utils.clickElement(utils.getBaselineImg('Transition_Category_Next.png'))
        utils.hoverElement(utils.getBaselineImg("NonClickable_TransitionsPanelText.png"))
        
        utils.assertElementExists(utils.getBaselineImg('Transition_Category_SpecialEffects_items.png'))
        
        utils.clickElement(utils.getBaselineImg('Transition_Category_Next.png'))
        utils.hoverElement(utils.getBaselineImg("NonClickable_TransitionsPanelText.png"))
        
        utils.assertElementExists(utils.getBaselineImg('Transition_Category_Stretch_items.png'))
        
        utils.clickElement(utils.getBaselineImg('Transition_Category_Next.png'))
        utils.hoverElement(utils.getBaselineImg("NonClickable_TransitionsPanelText.png"))
        
        utils.assertElementExists(utils.getBaselineImg('Transition_Category_Wipe_items.png'))
                    
        utils.clickElement(utils.getBaselineImg('Transition_Category_Next.png'))
        utils.hoverElement(utils.getBaselineImg("NonClickable_TransitionsPanelText.png"))
        utils.assertElementExists(utils.getBaselineImg('Transition_Category_Zoom_items.png'))
                                                                                                                                                        
    def tearDown(self):
        utils.closePRE()