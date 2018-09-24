import utils
reload(utils)
from utils import *
import os
import sys

import unittest

class TestTransitions(unittest.TestCase):

    def setUp(self):       
        cleanCache_And_LaunchPRE()
                    
    def test_UI_Transitions(self):
        clickElement("Button_GoalScreen_CloseGoalScreen.png")
        findElement("BaselineIMG_PREMenuBar.png")
        clickElement("Button_ExpertRoom.png")
        findElement("BaselineIMG_ExportRoomTimeline.png")
        wait(2)
        
        clickElement("Button_RHSPanels_Transitions.png")
        assertElementExists("DropDown_TransitionssPanel_AllCategories.png")
        wait(2)
        clickElement("DropDown_TransitionssPanel_AllCategories.png")
        assertElementExists("BaselineIMG_Transitions_AllCategories.png")        
        clickElement("Transition_Category_3DMotion.png")       
        assertElementExists("Transition_Category_3DMotion_items.png")
        clickElement("Transition_Category_Next.png")
        hoverElement("NonClickable_TransitionsPanelText.png")
        
        assertElementExists("Transition_Category_Dissolve_items.png")
        clickElement("Transition_Category_Next.png")
        hoverElement("NonClickable_TransitionsPanelText.png")
        
        assertElementExists("Transition_Category_Iris_items.png")
        clickElement("Transition_Category_Next.png")
        hoverElement("NonClickable_TransitionsPanelText.png")
        
        assertElementExists("Transition_Category_Map_items.png")
        clickElement("Transition_Category_Next.png")
        hoverElement("NonClickable_TransitionsPanelText.png")
        
        assertElementExists("Transition_Category_NewBlue3DExplosion_items.png")
        clickElement("Transition_Category_Next.png")
        hoverElement("NonClickable_TransitionsPanelText.png")
        
        assertElementExists("Transition_Category_NewBlue3DTransformations_items.png")
        clickElement("Transition_Category_Next.png")
        hoverElement("NonClickable_TransitionsPanelText.png")
        
        assertElementExists("Transition_Category_NewBlue_ArtBlends_items.png")
        clickElement("Transition_Category_Next.png")
        hoverElement("NonClickable_TransitionsPanelText.png")
        
        assertElementExists("Transition_Category_NewBlue_MotionBlends_items.png")
        clickElement("Transition_Category_Next.png")
        hoverElement("NonClickable_TransitionsPanelText.png")
        
        assertElementExists("Transition_Category_PagePeel_items.png")
                
        clickElement("Transition_Category_Next.png")
        hoverElement("NonClickable_TransitionsPanelText.png")
        
        assertElementExists("Transition_Category_PictureWipes_items.png")
                    
        clickElement("Transition_Category_Next.png")
        hoverElement("NonClickable_TransitionsPanelText.png")
        
        assertElementExists("Transition_Category_Slide_items.png")
                        
        clickElement("Transition_Category_Next.png")
        hoverElement("NonClickable_TransitionsPanelText.png")
        
        assertElementExists("Transition_Category_SpecialEffects_items.png")
        
        clickElement("Transition_Category_Next.png")
        hoverElement("NonClickable_TransitionsPanelText.png")
        
        assertElementExists("Transition_Category_Stretch_items.png")
        
        clickElement("Transition_Category_Next.png")
        hoverElement("NonClickable_TransitionsPanelText.png")
        
        assertElementExists("Transition_Category_Wipe_items.png")
                    
        clickElement("Transition_Category_Next.png")
        hoverElement("NonClickable_TransitionsPanelText.png")
        assertElementExists("Transition_Category_Zoom_items.png")
                                                                                                                                                        
    def tearDown(self):
        closePRE()