import unittest
import sys
import StringIO
import HTMLTestRunner
import xlrd
setAutoWaitTimeout(20)

class Test_GlassPane_GE(unittest.TestCase):

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

    def test_step3_startGE(self):
        click('Button_GuidedRoom.png')
        wait('Button_GuidedRoom_Active.png')   
        click('Button_Guided_FunEdits.png')
        wait('BaselineIMG_GlassPane_Placeholder.png')
        click('BaselineIMG_GlassPane_Placeholder.png')
        
    def test_step4_verifyGESteps(self):    
        wait('GlassPane_Step1_GlassPane.png')
        click('Button_GE_Next.png')
        wait('BaselineIMG_GE_AddMediaHighlighted.png')
        wait('GlassPane_Step2_GetStarted.png')
        click('Button_GE_Next.png')        
        wait('GlassPane_Step3_AddMedia.png')       
        wait('BaselineIMG_AddMediaOptions.png')
        click('Dropdown_AddMedia_FilesAndFolders.png')
        wait('Dropdown_MediaPath.png')               
        click('Dropdown_MediaPath.png') 
        type("C:\\Users\\nbhushan\\Desktop")
        type(Key.ENTER)
        doubleClick('Media_FileName.png')
        wait('GlassPane_Step4_ProjectAssets.png')        
        dragDrop('GlassPane_GE_MediaFile_Track1.png', 'VideoTrack1.png')
        wait('GlassPane_Step5_AddMediaToTimeline.png')        
        dragDrop('ProjectAssets_MediaFile_active.png', 'VideoTrack2.png')        
        wait('GlassPane_Step6_AddOverlay_1.png')
        wait(3)
        click('Button_GE_Next.png')        
        wait('GlassPane_Step6_AddOverlay_2.png')
        wait('BaselineIMG_GE_MatteOverlaysHighlighted.png')
        wait(3)
        dragDrop('MatteOverlay01.png','AudioTrack3.png')
        wait('BaselineIMG_GE_MatteOverlaysHighlighted.png')
        wait('Button_GE_Next.png')
        click('Button_GE_Next.png')  
        wait('GlassPane_Step7_TrackMatteEffect_1.png')
        wait('BaselineIMG_EffectsHighlighted.png')
        click('BaselineIMG_EffectsHighlighted.png')
        wait('GlassPane_Step7_TrackMatteEffect_2.png')
        wait('BaselineIMG_TrackMatteEffectHighlighted.png')
        dragDrop('BaselineIMG_TrackMatteEffectHighlighted.png', 'VideoTrack2_DropAreaForTrackMatte.png')
        wait('GlassPane_Step7_TrackMatteEffect_3.png')
        wait('BaselineIMG_TrackMatteKey_paramsHighlighted.png')
        click('DropDown_TrackMatte_None.png')
        click('DropDown_Matte_Video3Option.png')
        click('DropDown_TrackMatte_ComositeUsing.png')
        click('DropDown_ComositeUsing_MatteLumaOption.png')
        wait('GlassPane_Step7_TrackMatteEffect_4.png')
        wait(2)
        click('Button_GE_Next.png')
        wait('GlassPane_Step8_AddBlurEffect_1.png')
        wait('BaselineIMG_EffectsHighlighted.png')
        click('BaselineIMG_EffectsHighlighted.png')        
        wait(2)
        wait('GlassPane_Step8_AddBlurEffect_2.png')
        wait('BaselineIMG_FastBlurHighlighted.png')
        dragDrop('BaselineIMG_FastBlurHighlighted.png', 'BaselineIMG_Media_VideoTrack1.png')
        wait('GlassPane_Step8_AddBlurEffect_3.png')
        wait('BaselineIMG_FastBlur_ParamsHighlighted.png')
        wait(2)
        click('Button_GE_Next.png')                
        wait('GlassPane_Step9_AddAdjustments_1.png')
        wait('BaselineIMG_AdjustmentHighlighted.png')
        click('BaselineIMG_AdjustmentHighlighted.png')        
        wait('GlassPane_Step9_AddAdjustments_2.png')
        wait('BaselineIMG_Temperature-TintHighlighted.png')
        click('BaselineIMG_Temperature-TintHighlighted.png')   
        wait('BaselineIMG_TemperatureTint_Presets.png')
        wait('GlassPane_Step9_AddAdjustments_3.png')
        click('Preset_TemperatureTint.png')
        wait('GlassPane_Step9_AddAdjustments_4.png')
        wait(2)
        click('Button_GE_Next.png')                        
        wait('GlassPane_Step10_Done.png')
        click('Button_GlassPane_Done.png')
        
    def test_step5_teardown(self):
        type("r", KEY_WIN)
        type("C:\\Users\\nbhushan\\Desktop\\SikuliFramework_PRE2019\\BatFiles\\KillPre_App.bat")
        type(Key.ENTER)     

Settings.ActionLogs = False
Settings.InfoLogs = False
Settings.DebugLogs = False

suite = unittest.TestLoader().loadTestsFromTestCase(Test_GlassPane_GE)

fp = file('GlassPaneGE.html', 'wb')
runner = HTMLTestRunner.HTMLTestRunner(
                stream=fp,
                title='Glass Pane GE Test',
                description='Test report Glass Pane Guided Edit in PRE.'
                )
runner.run(suite)
        

        
        