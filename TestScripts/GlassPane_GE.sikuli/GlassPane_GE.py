import utils
reload(utils)
from utils import *
import os
import sys
import unittest
setAutoWaitTimeout(60)

class TestGlassPane_GE(unittest.TestCase):

    def setUp(self):       
        utils.cleanCache_And_LaunchPRE()

    def test_UI_GlassPane_GE(self):
        utils.clickElement(utils.getBaselineImg('Button_GoalScreen_CloseGoalScreen.png'))
        utils.findElement(utils.getBaselineImg('BaselineIMG_PREMenuBar.png'))


        utils.clickElement(utils.getBaselineImg('Button_GuidedRoom.png'))
        utils.findElement(utils.getBaselineImg('Button_GuidedRoom_Active.png'))   
        utils.clickElement(utils.getBaselineImg('Button_Guided_FunEdits.png'))
        utils.findElement(utils.getBaselineImg('BaselineIMG_GlassPane_Placeholder.png'))
        utils.clickElement(utils.getBaselineImg('BaselineIMG_GlassPane_Placeholder.png'))
        

        utils.findElement(utils.getBaselineImg('GlassPane_Step1_GlassPane.png'))
        utils.clickElement(utils.getBaselineImg('Button_GE_Next.png'))
        utils.findElement(utils.getBaselineImg('BaselineIMG_GE_AddMediaHighlighted.png'))
        utils.findElement(utils.getBaselineImg('GlassPane_Step2_GetStarted.png'))
        utils.clickElement(utils.getBaselineImg('Button_GE_Next.png'))        
        utils.findElement(utils.getBaselineImg('GlassPane_Step3_AddMedia.png'))       
        utils.findElement(utils.getBaselineImg('BaselineIMG_AddMediaOptions.png'))
        utils.clickElement(utils.getBaselineImg('Dropdown_AddMedia_FilesAndFolders.png'))
        utils.findElement(utils.getBaselineImg('TextBox_ImportMediaPath.png'))               
        utils.clickElement(utils.getBaselineImg('TextBox_ImportMediaPath.png')) 
        type(utils.TestDataFile_path)
        type(Key.ENTER)
        utils.findElement(utils.getBaselineImg('GlassPane_Step4_ProjectAssets.png'))       
        dragDrop(utils.getBaselineImg('GlassPane_GE_MediaFile_Track1.png'), utils.getBaselineImg('VideoTrack1.png'))
        utils.findElement(utils.getBaselineImg('GlassPane_Step5_AddMediaToTimeline.png'))        
        dragDrop(utils.getBaselineImg('ProjectAssets_MediaFile_active.png'), utils.getBaselineImg('VideoTrack2.png'))        
        utils.findElement(utils.getBaselineImg('GlassPane_Step6_AddOverlay_1.png'))
        wait(3)
        utils.clickElement(utils.getBaselineImg('Button_GE_Next.png'))        
        utils.findElement(utils.getBaselineImg('GlassPane_Step6_AddOverlay_2.png'))
        utils.findElement(utils.getBaselineImg('BaselineIMG_GE_MatteOverlaysHighlighted.png'))
        wait(3)
        dragDrop(utils.getBaselineImg('MatteOverlay01.png'), utils.getBaselineImg('AudioTrack3.png'))
        utils.findElement(utils.getBaselineImg('BaselineIMG_GE_MatteOverlaysHighlighted.png'))
        wait(2)
        utils.findElement(utils.getBaselineImg('Button_GE_Next.png'))
        wait(2)
        utils.clickElement(utils.getBaselineImg('Button_GE_Next.png'))  
        utils.findElement(utils.getBaselineImg('GlassPane_Step7_TrackMatteEffect_1.png'))
        utils.findElement(utils.getBaselineImg('BaselineIMG_EffectsHighlighted.png'))
        utils.clickElement(utils.getBaselineImg('BaselineIMG_EffectsHighlighted.png'))
        utils.findElement(utils.getBaselineImg('GlassPane_Step7_TrackMatteEffect_2.png'))
        utils.findElement(utils.getBaselineImg('BaselineIMG_TrackMatteEffectHighlighted.png'))
        dragDrop(utils.getBaselineImg('BaselineIMG_TrackMatteEffectHighlighted.png'), utils.getBaselineImg('VideoTrack2_DropAreaForTrackMatte.png'))
        utils.findElement(utils.getBaselineImg('GlassPane_Step7_TrackMatteEffect_3.png'))
        utils.findElement(utils.getBaselineImg('BaselineIMG_TrackMatteKey_paramsHighlighted.png'))
        utils.clickElement(utils.getBaselineImg('DropDown_TrackMatte_None.png'))
        utils.clickElement(utils.getBaselineImg('DropDown_Matte_Video3Option.png'))
        utils.findElement(utils.getBaselineImg('GlassPane_Step7_TrackMatteEffect_3.png'))        
        utils.clickElement(utils.getBaselineImg('DropDown_TrackMatte_ComositeUsing.png'))
        utils.clickElement(utils.getBaselineImg('DropDown_ComositeUsing_MatteLumaOption.png'))
        utils.findElement(utils.getBaselineImg('GlassPane_Step7_TrackMatteEffect_4.png'))
        wait(2)
        utils.clickElement(utils.getBaselineImg('Button_GE_Next.png'))
        utils.findElement(utils.getBaselineImg('GlassPane_Step8_AddBlurEffect_1.png'))
        utils.findElement(utils.getBaselineImg('BaselineIMG_EffectsHighlighted.png'))
        utils.clickElement(utils.getBaselineImg('BaselineIMG_EffectsHighlighted.png'))        
        wait(2)
        utils.findElement(utils.getBaselineImg('GlassPane_Step8_AddBlurEffect_2.png'))
        utils.findElement(utils.getBaselineImg('BaselineIMG_FastBlurHighlighted.png'))
        dragDrop(utils.getBaselineImg('BaselineIMG_FastBlurHighlighted.png'), utils.getBaselineImg('BaselineIMG_Media_VideoTrack1.png'))
        utils.findElement(utils.getBaselineImg('GlassPane_Step8_AddBlurEffect_3.png'))
        utils.findElement(utils.getBaselineImg('BaselineIMG_FastBlur_ParamsHighlighted.png'))
        wait(2)
        utils.clickElement(utils.getBaselineImg('Button_GE_Next.png'))                
        utils.findElement(utils.getBaselineImg('GlassPane_Step9_AddAdjustments_1.png'))
        utils.findElement(utils.getBaselineImg('BaselineIMG_AdjustmentHighlighted.png'))
        utils.clickElement(utils.getBaselineImg('BaselineIMG_AdjustmentHighlighted.png'))        
        utils.findElement(utils.getBaselineImg('GlassPane_Step9_AddAdjustments_2.png'))
        utils.findElement(utils.getBaselineImg('BaselineIMG_Temperature-TintHighlighted.png'))
        utils.clickElement(utils.getBaselineImg('BaselineIMG_Temperature-TintHighlighted.png'))   
        utils.findElement(utils.getBaselineImg('BaselineIMG_TemperatureTint_Presets.png'))
        utils.findElement(utils.getBaselineImg('GlassPane_Step9_AddAdjustments_3.png'))
        utils.clickElement(utils.getBaselineImg('Preset_TemperatureTint.png'))
        utils.findElement(utils.getBaselineImg('GlassPane_Step9_AddAdjustments_4.png'))
        wait(2)
        utils.clickElement(utils.getBaselineImg('Button_GE_Next.png'))                        
        utils.assertElementExists(utils.getBaselineImg('GlassPane_Step10_Done.png'))
        utils.clickElement(utils.getBaselineImg('Button_GlassPane_Done.png'))
        

    def tearDown(self):
        
        utils.closePRE()     

