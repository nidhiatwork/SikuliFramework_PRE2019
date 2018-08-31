import utils
reload(utils)
from utils import *
import os
import sys

if not utils.RootFolder in sys.path: 
    sys.path.append(utils.RootFolder)

import unittest
setAutoWaitTimeout(60)

class TestGlassPane_GE(unittest.TestCase):

    def setUp(self):       
        utils.cleanCache_And_LaunchPRE()

    def test_UI_GlassPane_GE(self):
        find(utils.getBaselineImg('Button_GoalScreen_CloseGoalScreen.png'))
        click(utils.getBaselineImg('Button_GoalScreen_CloseGoalScreen.png'))
        find(utils.getBaselineImg('BaselineIMG_PREMenuBar.png'))


        click(utils.getBaselineImg('Button_GuidedRoom.png'))
        find(utils.getBaselineImg('Button_GuidedRoom_Active.png'))   
        click(utils.getBaselineImg('Button_Guided_FunEdits.png'))
        find(utils.getBaselineImg('BaselineIMG_GlassPane_Placeholder.png'))
        click(utils.getBaselineImg('BaselineIMG_GlassPane_Placeholder.png'))
        

        find(utils.getBaselineImg('GlassPane_Step1_GlassPane.png'))
        click(utils.getBaselineImg('Button_GE_Next.png'))
        find(utils.getBaselineImg('BaselineIMG_GE_AddMediaHighlighted.png'))
        find(utils.getBaselineImg('GlassPane_Step2_GetStarted.png'))
        click(utils.getBaselineImg('Button_GE_Next.png'))        
        find(utils.getBaselineImg('GlassPane_Step3_AddMedia.png'))       
        find(utils.getBaselineImg('BaselineIMG_AddMediaOptions.png'))
        click(utils.getBaselineImg('Dropdown_AddMedia_FilesAndFolders.png'))
        find(utils.getBaselineImg('TextBox_ImportMediaPath.png'))               
        click(utils.getBaselineImg('TextBox_ImportMediaPath.png')) 
        type(utils.TestDataFile_path)
        type(Key.ENTER)
        find(utils.getBaselineImg('GlassPane_Step4_ProjectAssets.png'))       
        dragDrop(utils.getBaselineImg('GlassPane_GE_MediaFile_Track1.png'), utils.getBaselineImg('VideoTrack1.png'))
        find(utils.getBaselineImg('GlassPane_Step5_AddMediaToTimeline.png'))        
        dragDrop(utils.getBaselineImg('ProjectAssets_MediaFile_active.png'), utils.getBaselineImg('VideoTrack2.png'))        
        find(utils.getBaselineImg('GlassPane_Step6_AddOverlay_1.png'))
        wait(3)
        click(utils.getBaselineImg('Button_GE_Next.png'))        
        find(utils.getBaselineImg('GlassPane_Step6_AddOverlay_2.png'))
        find(utils.getBaselineImg('BaselineIMG_GE_MatteOverlaysHighlighted.png'))
        wait(3)
        dragDrop(utils.getBaselineImg('MatteOverlay01.png'), utils.getBaselineImg('AudioTrack3.png'))
        find(utils.getBaselineImg('BaselineIMG_GE_MatteOverlaysHighlighted.png'))
        wait(2)
        find(utils.getBaselineImg('Button_GE_Next.png'))
        wait(2)
        click(utils.getBaselineImg('Button_GE_Next.png'))  
        find(utils.getBaselineImg('GlassPane_Step7_TrackMatteEffect_1.png'))
        find(utils.getBaselineImg('BaselineIMG_EffectsHighlighted.png'))
        click(utils.getBaselineImg('BaselineIMG_EffectsHighlighted.png'))
        find(utils.getBaselineImg('GlassPane_Step7_TrackMatteEffect_2.png'))
        find(utils.getBaselineImg('BaselineIMG_TrackMatteEffectHighlighted.png'))
        dragDrop(utils.getBaselineImg('BaselineIMG_TrackMatteEffectHighlighted.png'), utils.getBaselineImg('VideoTrack2_DropAreaForTrackMatte.png'))
        find(utils.getBaselineImg('GlassPane_Step7_TrackMatteEffect_3.png'))
        find(utils.getBaselineImg('BaselineIMG_TrackMatteKey_paramsHighlighted.png'))
        click(utils.getBaselineImg('DropDown_TrackMatte_None.png'))
        click(utils.getBaselineImg('DropDown_Matte_Video3Option.png'))
        find(utils.getBaselineImg('GlassPane_Step7_TrackMatteEffect_3.png'))        
        click(utils.getBaselineImg('DropDown_TrackMatte_ComositeUsing.png'))
        click(utils.getBaselineImg('DropDown_ComositeUsing_MatteLumaOption.png'))
        find(utils.getBaselineImg('GlassPane_Step7_TrackMatteEffect_4.png'))
        wait(2)
        click(utils.getBaselineImg('Button_GE_Next.png'))
        find(utils.getBaselineImg('GlassPane_Step8_AddBlurEffect_1.png'))
        find(utils.getBaselineImg('BaselineIMG_EffectsHighlighted.png'))
        click(utils.getBaselineImg('BaselineIMG_EffectsHighlighted.png'))        
        wait(2)
        find(utils.getBaselineImg('GlassPane_Step8_AddBlurEffect_2.png'))
        find(utils.getBaselineImg('BaselineIMG_FastBlurHighlighted.png'))
        dragDrop(utils.getBaselineImg('BaselineIMG_FastBlurHighlighted.png'), utils.getBaselineImg('BaselineIMG_Media_VideoTrack1.png'))
        find(utils.getBaselineImg('GlassPane_Step8_AddBlurEffect_3.png'))
        find(utils.getBaselineImg('BaselineIMG_FastBlur_ParamsHighlighted.png'))
        wait(2)
        click(utils.getBaselineImg('Button_GE_Next.png'))                
        find(utils.getBaselineImg('GlassPane_Step9_AddAdjustments_1.png'))
        find(utils.getBaselineImg('BaselineIMG_AdjustmentHighlighted.png'))
        click(utils.getBaselineImg('BaselineIMG_AdjustmentHighlighted.png'))        
        find(utils.getBaselineImg('GlassPane_Step9_AddAdjustments_2.png'))
        find(utils.getBaselineImg('BaselineIMG_Temperature-TintHighlighted.png'))
        click(utils.getBaselineImg('BaselineIMG_Temperature-TintHighlighted.png'))   
        find(utils.getBaselineImg('BaselineIMG_TemperatureTint_Presets.png'))
        find(utils.getBaselineImg('GlassPane_Step9_AddAdjustments_3.png'))
        click(utils.getBaselineImg('Preset_TemperatureTint.png'))
        find(utils.getBaselineImg('GlassPane_Step9_AddAdjustments_4.png'))
        wait(2)
        click(utils.getBaselineImg('Button_GE_Next.png'))                        
        assert(exists(utils.getBaselineImg('GlassPane_Step10_Done.png')))
        click(utils.getBaselineImg('Button_GlassPane_Done.png'))
        

    def tearDown(self):
       utils.closePRE()     

