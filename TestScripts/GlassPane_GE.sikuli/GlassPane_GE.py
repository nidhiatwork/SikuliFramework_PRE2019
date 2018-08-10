import utils
reload(utils)
from utils import *
import os
import sys

if not utils.RootFolder in sys.path: 
    sys.path.append(utils.RootFolder)

import StringIO

fp = file(os.path.join(utils.OutputFolder, "Test_report_GlassPane_GE.html"), "wb")

import unittest
import HTMLTestRunner
reload(HTMLTestRunner)
setAutoWaitTimeout(20)

class Test_GlassPane_GE(unittest.TestCase):

    def setUp(self):       
        utils.openPRE()

    def test_UI_GlassPane_GE(self):
        wait(utils.getBaselineImg('Button_GoalScreen_CloseGoalScreen.png'))
        click(utils.getBaselineImg('Button_GoalScreen_CloseGoalScreen.png'))
        wait(utils.getBaselineImg('BaselineIMG_PREMenuBar.png'))


        click(utils.getBaselineImg('Button_GuidedRoom.png'))
        wait(utils.getBaselineImg('Button_GuidedRoom_Active.png'))   
        click(utils.getBaselineImg('Button_Guided_FunEdits.png'))
        wait(utils.getBaselineImg('BaselineIMG_GlassPane_Placeholder.png'))
        click(utils.getBaselineImg('BaselineIMG_GlassPane_Placeholder.png'))
        

        wait(utils.getBaselineImg('GlassPane_Step1_GlassPane.png'))
        click(utils.getBaselineImg('Button_GE_Next.png'))
        wait(utils.getBaselineImg('BaselineIMG_GE_AddMediaHighlighted.png'))
        wait(utils.getBaselineImg('GlassPane_Step2_GetStarted.png'))
        click(utils.getBaselineImg('Button_GE_Next.png'))        
        wait(utils.getBaselineImg('GlassPane_Step3_AddMedia.png'))       
        wait(utils.getBaselineImg('BaselineIMG_AddMediaOptions.png'))
        click(utils.getBaselineImg('Dropdown_AddMedia_FilesAndFolders.png'))
        wait(utils.getBaselineImg('TextBox_ImportMediaPath.png'))               
        click(utils.getBaselineImg('TextBox_ImportMediaPath.png')) 
        type(utils.TestDataFile_path)
        type(Key.ENTER)
        wait(utils.getBaselineImg('GlassPane_Step4_ProjectAssets.png'))       
        dragDrop(utils.getBaselineImg('GlassPane_GE_MediaFile_Track1.png'), utils.getBaselineImg('VideoTrack1.png'))
        wait(utils.getBaselineImg('GlassPane_Step5_AddMediaToTimeline.png'))        
        dragDrop(utils.getBaselineImg('ProjectAssets_MediaFile_active.png'), utils.getBaselineImg('VideoTrack2.png'))        
        wait(utils.getBaselineImg('GlassPane_Step6_AddOverlay_1.png'))
        wait(3)
        click(utils.getBaselineImg('Button_GE_Next.png'))        
        wait(utils.getBaselineImg('GlassPane_Step6_AddOverlay_2.png'))
        wait(utils.getBaselineImg('BaselineIMG_GE_MatteOverlaysHighlighted.png'))
        wait(3)
        dragDrop(utils.getBaselineImg('MatteOverlay01.png'), utils.getBaselineImg('AudioTrack3.png'))
        wait(utils.getBaselineImg('BaselineIMG_GE_MatteOverlaysHighlighted.png'))
        wait(utils.getBaselineImg('Button_GE_Next.png'))
        click(utils.getBaselineImg('Button_GE_Next.png'))  
        wait(utils.getBaselineImg('GlassPane_Step7_TrackMatteEffect_1.png'))
        wait(utils.getBaselineImg('BaselineIMG_EffectsHighlighted.png'))
        click(utils.getBaselineImg('BaselineIMG_EffectsHighlighted.png'))
        wait(utils.getBaselineImg('GlassPane_Step7_TrackMatteEffect_2.png'))
        wait(utils.getBaselineImg('BaselineIMG_TrackMatteEffectHighlighted.png'))
        dragDrop(utils.getBaselineImg('BaselineIMG_TrackMatteEffectHighlighted.png'), utils.getBaselineImg('VideoTrack2_DropAreaForTrackMatte.png'))
        wait(utils.getBaselineImg('GlassPane_Step7_TrackMatteEffect_3.png'))
        wait(utils.getBaselineImg('BaselineIMG_TrackMatteKey_paramsHighlighted.png'))
        click(utils.getBaselineImg('DropDown_TrackMatte_None.png'))
        click(utils.getBaselineImg('DropDown_Matte_Video3Option.png'))
        wait(utils.getBaselineImg('GlassPane_Step7_TrackMatteEffect_3.png'))        
        click(utils.getBaselineImg('DropDown_TrackMatte_ComositeUsing.png'))
        click(utils.getBaselineImg('DropDown_ComositeUsing_MatteLumaOption.png'))
        wait(utils.getBaselineImg('GlassPane_Step7_TrackMatteEffect_4.png'))
        wait(2)
        click(utils.getBaselineImg('Button_GE_Next.png'))
        wait(utils.getBaselineImg('GlassPane_Step8_AddBlurEffect_1.png'))
        wait(utils.getBaselineImg('BaselineIMG_EffectsHighlighted.png'))
        click(utils.getBaselineImg('BaselineIMG_EffectsHighlighted.png'))        
        wait(2)
        wait(utils.getBaselineImg('GlassPane_Step8_AddBlurEffect_2.png'))
        wait(utils.getBaselineImg('BaselineIMG_FastBlurHighlighted.png'))
        dragDrop(utils.getBaselineImg('BaselineIMG_FastBlurHighlighted.png'), utils.getBaselineImg('BaselineIMG_Media_VideoTrack1.png'))
        wait(utils.getBaselineImg('GlassPane_Step8_AddBlurEffect_3.png'))
        wait(utils.getBaselineImg('BaselineIMG_FastBlur_ParamsHighlighted.png'))
        wait(2)
        click(utils.getBaselineImg('Button_GE_Next.png'))                
        wait(utils.getBaselineImg('GlassPane_Step9_AddAdjustments_1.png'))
        wait(utils.getBaselineImg('BaselineIMG_AdjustmentHighlighted.png'))
        click(utils.getBaselineImg('BaselineIMG_AdjustmentHighlighted.png'))        
        wait(utils.getBaselineImg('GlassPane_Step9_AddAdjustments_2.png'))
        wait(utils.getBaselineImg('BaselineIMG_Temperature-TintHighlighted.png'))
        click(utils.getBaselineImg('BaselineIMG_Temperature-TintHighlighted.png'))   
        wait(utils.getBaselineImg('BaselineIMG_TemperatureTint_Presets.png'))
        wait(utils.getBaselineImg('GlassPane_Step9_AddAdjustments_3.png'))
        click(utils.getBaselineImg('Preset_TemperatureTint.png'))
        wait(utils.getBaselineImg('GlassPane_Step9_AddAdjustments_4.png'))
        wait(2)
        click(utils.getBaselineImg('Button_GE_Next.png'))                        
        assert(exists(utils.getBaselineImg('GlassPane_Step10_Done.png')))
        click(utils.getBaselineImg('Button_GlassPane_Done.png'))
        

    def tearDown(self):
       utils.closePRE()     

suite = unittest.TestLoader().loadTestsFromTestCase(Test_GlassPane_GE)

runner = HTMLTestRunner.HTMLTestRunner(
                stream=fp,
                title='Glass Pane GE Test',
                description='Test report Glass Pane Guided Edit in PRE.'
                )
runner.run(suite)