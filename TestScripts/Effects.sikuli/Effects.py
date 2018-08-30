import utils
reload(utils)
from utils import *
import os
import sys

if not utils.RootFolder in sys.path: 
    sys.path.append(utils.RootFolder)

import StringIO

fp = file(os.path.join(utils.OutputFolder, "Test_report_Effects.html"), "wb")

import unittest
import HTMLTestRunner
reload(HTMLTestRunner)
setAutoWaitTimeout(60)
        
class Test_Effects(unittest.TestCase):

    def setUp(self):       
        utils.openPRE()
                  
    def test_UI_Effects(self):
        find(utils.getBaselineImg('Button_GoalScreen_CloseGoalScreen.png'))
        click(utils.getBaselineImg('Button_GoalScreen_CloseGoalScreen.png'))
        find(utils.getBaselineImg('BaselineIMG_PREMenuBar.png'))

        click(utils.getBaselineImg('Button_ExpertRoom.png'))         
        find(utils.getBaselineImg('BaselineIMG_ExportRoomTimeline.png'))
        wait(2)
        find(utils.getBaselineImg('Button_RHSPanels_Effects.png'))
        
        click(utils.getBaselineImg('Button_RHSPanels_Effects.png'))
        find(utils.getBaselineImg('DropDown_EffectsPanel_AllCategories.png'))
        click(utils.getBaselineImg('DropDown_EffectsPanel_AllCategories.png'))
        find(utils.getBaselineImg('BaselineIMG_Effects_AllCategories.png'))

        click(utils.getBaselineImg('Effects_Category_AdvancedAdjustments.png'))
        assert(exists(utils.getBaselineImg('Effects_Category_AdvancedAdjustments_items.png')))
        click(utils.getBaselineImg('Button_EffectCategories_Next.png'))
       
        assert(exists(utils.getBaselineImg('Effects_Category_BlurSharpen_items.png')))   
        click(utils.getBaselineImg('Button_EffectCategories_Next.png'))
        
        assert(exists(utils.getBaselineImg('Effects_Category_Channel_items.png')))
        click(utils.getBaselineImg('Button_EffectCategories_Next.png'))

        assert(exists(utils.getBaselineImg('Effects_Categories_ColorCorrection_items.png')))
        click(utils.getBaselineImg('Button_EffectCategories_Next.png'))

        assert(exists(utils.getBaselineImg('Effects_Categories_Distort_items.png')))
        click(utils.getBaselineImg('Button_EffectCategories_Next.png'))

        assert(exists(utils.getBaselineImg('Effects_Categories_Generate_items.png')))
        click(utils.getBaselineImg('Button_EffectCategories_Next.png'))

        assert(exists(utils.getBaselineImg('Effects_Categories_ImageControl_items.png')))
        click(utils.getBaselineImg('Button_EffectCategories_Next.png'))

        assert(exists(utils.getBaselineImg('Effects_Categories_Keying_items.png')))
        click(utils.getBaselineImg('Button_EffectCategories_Next.png'))

        assert(exists(utils.getBaselineImg('Effects_Categories_NewBlueArtEffects_items.png')))
        click(utils.getBaselineImg('Button_EffectCategories_Next.png'))

        assert(exists(utils.getBaselineImg('Effects_Categories_NewBlueCartoonrPlus_items.png')))
        click(utils.getBaselineImg('Button_EffectCategories_Next.png'))

        assert(exists(utils.getBaselineImg('Effects_Categories_NewBlueFilmLooks_items.png')))
        click(utils.getBaselineImg('Button_EffectCategories_Next.png'))

        assert(exists(utils.getBaselineImg('Effects_Categories_Perspective_items.png')))
        click(utils.getBaselineImg('Button_EffectCategories_Next.png'))

        assert(exists(utils.getBaselineImg('Effects_Categories_Pixelate_items.png')))
        click(utils.getBaselineImg('Button_EffectCategories_Next.png'))

        assert(exists(utils.getBaselineImg('Effects_Categories_Render_items.png')))
        click(utils.getBaselineImg('Button_EffectCategories_Next.png'))

        assert(exists(utils.getBaselineImg('Effects_Categories_Stylize_items.png')))
        click(utils.getBaselineImg('Button_EffectCategories_Next.png'))

        assert(exists(utils.getBaselineImg('Effects_Categories_Time_items.png')))
        click(utils.getBaselineImg('Button_EffectCategories_Next.png'))

        assert(exists(utils.getBaselineImg('Effects_Categories_Transform_items.png')))
        click(utils.getBaselineImg('Button_EffectCategories_Next.png'))

        assert(exists(utils.getBaselineImg('Effects_Categories_VideoMerge_items.png')))
        click(utils.getBaselineImg('Button_EffectCategories_Next.png'))
        
        wait(2)
        click(utils.getBaselineImg('Button_EffectCategories_Next.png'))

        assert(exists(utils.getBaselineImg('Effects_Categories_HollywoodLooks_items.png')))              
    
    def tearDown(self):
       utils.closePRE()         

suite = unittest.TestLoader().loadTestsFromTestCase(Test_Effects)

runner = HTMLTestRunner.HTMLTestRunner(
                stream=fp,
                title='Effects Test',
                description='Test report for viewing all Effects in PRE.'
                )
runner.run(suite)
