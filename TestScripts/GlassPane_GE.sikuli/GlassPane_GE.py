import utils
reload(utils)
from utils import *
import os
import sys
import unittest

class TestGlassPane_GE(unittest.TestCase):

    def setUp(self):       
        cleanCache_And_LaunchPRE()

    def test_UI_GlassPane_GE(self):
        doubleClickElement("Button_GoalScreen_CloseGoalScreen.png")
        findElement("BaselineIMG_PREMenuBar.png")

        clickElement("Button_GuidedRoom.png")
        findElement("Button_GuidedRoom_Active.png")   
        clickElement("Button_Guided_FunEdits.png")
        findElement("BaselineIMG_GlassPane_Placeholder.png")
        clickElement("BaselineIMG_GlassPane_Placeholder.png")
        
        findElement("GlassPane_Step1_GlassPane.png")
        clickElement("Button_GE_Next.png")
        findElement("BaselineIMG_GE_AddMediaHighlighted.png")
        findElement("GlassPane_Step2_GetStarted.png")
        clickElement("Button_GE_Next.png")        
        findElement("GlassPane_Step3_AddMedia.png")       
        findElement("BaselineIMG_AddMediaOptions.png")
        clickElement("Dropdown_AddMedia_FilesAndFolders.png")
        findElement("TextBox_ImportMediaPath.png")               
        clickElement("TextBox_ImportMediaPath.png") 
        typeKeys(Constants.TestDataFile_path)
        type(Key.ENTER)
        findElement("GlassPane_Step4_ProjectAssets.png")       
        dragDropElement("GlassPane_GE_MediaFile_Track1.png", "VideoTrack1.png")
        findElement("GlassPane_Step5_AddMediaToTimeline.png")

        wait(2)
        hoverElement("Button_Timeline_Up.png")
        mouseDown(Button.LEFT)
        mouseMove("Button_Timeline_Up.png")
        wait(5)
        mouseUp()

        dragDropElement("ProjectAssets_MediaFile_active.png", Pattern("VideoTrack2.png").similar(0.99))        
        findElement("GlassPane_Step6_AddOverlay_1.png")
        wait(3)
        clickElement("Button_GE_Next.png")        
        findElement("GlassPane_Step6_AddOverlay_2.png")
        findElement("BaselineIMG_GE_MatteOverlaysHighlighted.png")
        wait(3)
        
        hoverElement("Button_Timeline_Up.png")
        mouseDown(Button.LEFT)
        mouseMove("Button_Timeline_Up.png")
        wait(5)
        mouseUp()

        dragDropElement("MatteOverlay01.png", Pattern("AudioTrack3.png").similar(0.99))
        findElement("BaselineIMG_GE_MatteOverlaysHighlighted.png")
        wait(2)
        findElement("Button_GE_Next.png")
        wait(2)
        clickElement("Button_GE_Next.png")  
        findElement("GlassPane_Step7_TrackMatteEffect_1.png")
        findElement("BaselineIMG_EffectsHighlighted.png")
        clickElement("BaselineIMG_EffectsHighlighted.png")
        findElement("GlassPane_Step7_TrackMatteEffect_2.png")
        findElement("BaselineIMG_TrackMatteEffectHighlighted.png")
        
        wait(2)
        hoverElement("Button_Timeline_Up.png")
        mouseDown(Button.LEFT)
        mouseMove("Button_Timeline_Up.png")
        wait(5)
        mouseUp()

        dragDropElement("BaselineIMG_TrackMatteEffectHighlighted.png", "VideoTrack2_DropAreaForTrackMatte.png")
        findElement("GlassPane_Step7_TrackMatteEffect_3.png")
        findElement("BaselineIMG_TrackMatteKey_paramsHighlighted.png")
        clickElement("DropDown_TrackMatte_None.png")
        clickElement("DropDown_Matte_Video3Option.png")
        findElement("GlassPane_Step7_TrackMatteEffect_3.png")        
        clickElement("DropDown_TrackMatte_ComositeUsing.png")
        clickElement("DropDown_ComositeUsing_MatteLumaOption.png")
        findElement("GlassPane_Step7_TrackMatteEffect_4.png")
        wait(2)
        clickElement("Button_GE_Next.png")
        findElement("GlassPane_Step8_AddBlurEffect_1.png")
        findElement("BaselineIMG_EffectsHighlighted.png")
        clickElement("BaselineIMG_EffectsHighlighted.png")        
        wait(2)
        findElement("GlassPane_Step8_AddBlurEffect_2.png")
        findElement("BaselineIMG_FastBlurHighlighted.png")
        dragDropElement("BaselineIMG_FastBlurHighlighted.png", "BaselineIMG_Media_VideoTrack1.png")
        findElement("GlassPane_Step8_AddBlurEffect_3.png")
        findElement("BaselineIMG_FastBlur_ParamsHighlighted.png")
        wait(2)
        clickElement("Button_GE_Next.png")                
        findElement("GlassPane_Step9_AddAdjustments_1.png")
        findElement("BaselineIMG_AdjustmentHighlighted.png")
        clickElement("BaselineIMG_AdjustmentHighlighted.png")        
        findElement("GlassPane_Step9_AddAdjustments_2.png")
        findElement("BaselineIMG_Temperature-TintHighlighted.png")
        clickElement("BaselineIMG_Temperature-TintHighlighted.png")   
        findElement("BaselineIMG_TemperatureTint_Presets.png")
        findElement("GlassPane_Step9_AddAdjustments_3.png")
        clickElement("Preset_TemperatureTint.png")
        findElement("GlassPane_Step9_AddAdjustments_4.png")
        wait(2)
        clickElement("Button_GE_Next.png")                        
        assertElementExists("GlassPane_Step10_Done.png")
        clickElement("Button_GlassPane_Done.png")
        

    def tearDown(self):
        
        closePRE()     

