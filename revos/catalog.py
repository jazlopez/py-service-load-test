# REVOS device catalog
# Jaziel Lopez

chars = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J"
]

activity = [
    "OS Cursor - Successful - OS_Cursor_Initialize - 93",
    "Sound - Successful - OS_Sound_Initialize - 152",
    "Script - Successful - OS_Script_Initialize - 105",
    "Time - Successful - OS_Time_Initialize - 132",
    "OS Device - Successful - OS_Device_Initialize - 177",
    "OS Font - Successful - OS_Font_Initialize - 131",
    "OS Bitmap - Successful - OS_Bitmap_Initialize - 126",
    "OS Graphics - Successful - OS_Graphics_Initialize - 174",
    "OS Locale - Successful - OS_Locale_Initialize - 91",
    "OS Network - Successful - OS_Network_Initialize - 111",
    "OS Keyboard - Successful - OS_Keyboard_Initialize - 102",
    "OS Touch - Successful - OS_Touch_Initialize - 184",
    "**** OS modules successfully initialized ****",
    "IF Log - Successful - IF_Log_Initialize - 203",
    "OS Update - Successful - OS_Update_Initialize - 138",
    "IF Datastore - Successful - IF_Datastore_Initialize - 243",
    "Diagnostics Emulator - Successful - Diagnostics_Emulator_Initialise - 216",
    "Diagnostics Datastore - Successful - Diagnostics_Datastore_Initialize - 518",
    "IF Datastore Reset Level - Successful - IF_Datastore_ResetLevel_Initialize - 84",
    "**** Diagnostics modules successfully initialized",
    "IF Hardware - Successful - IF_Hardware_Initialize - 255",
    "IF Alarms - Successful - IF_Alarms_Initialize - 249",
    "IF Diagnostics - Successful - IF_Diagnostics_Initialize - 228",
    "IF Battery - Successful - IF_Battery_Initialize - 109",
    "IF Heater - Successful - IF_Heater_Initialize - 105",
    "IF Level - Successful - IF_Level_Initialize - 75",
    "IF Fan - Successful - IF_Fan_Initialize - 100",
    "IF Link - Successful - IF_Link_Initialize - 75",
    "IF Pump - Successful - IF_Pump_Initialize - 107",
    "IF Relay - Successful - IF_Relay_Initialize - 78",
    "IF Pressure - Successful - IF_Pressure_Initialize - 101",
    "IF Reports - Successful - IF_Reports_Initialize - 843",
    "IF Sensor - Successful - IF_Sensor_Initialize - 75",
    "IF Serial - Successful - IF_Serial_Initialize - 87",
    "IF Script - Successful - IF_Script_Initialize - 344",
    "IF Specific Gravity - Successful - IF_SG_Initialize - 127",
    "IF Solenoid - Successful - IF_Solenoid_Initialize - 75",
    "IF Sound - Successful - IF_Sound_Initialize - 79",
    "IF SoftwareReset - Successful - IF_SoftwareReset_Initialize - 82",
    "IF Transfer Flushes - Successful - IF_TransferFlushes_Initialize - 196",
    "IF Transfer Programs - Successful - IF_TransferPrograms_Initialize - 197",
    "IF Transfer Setup - Successful - IF_TransferSetup_Initialize - 175",
    "IF Transfer Logs - Successful - IF_TransferLogs_Initialize - 157",
    "IF Switch - Successful - IF_Switch_Initialize - 75",
    "Media IF Video - Successful - Media_IF_Video_Initialize - 127",
    "IF Video - Successful - IF_Video_Initialize - 107",
    "IF Update - Successful - IF_Update_Initialize - 129",
    "IF Voltage - Successful - IF_Voltage_Initialize - 101",
    "IF Netmon - Successful - IF_Netmon_Initialize - 173",
    "**** IF modules successfully initialized ****",
    "IF Engine - Successful - IF_Engine_Initialize - 175",
    "Control Agitate - Successful - Control_Agitate_Initialize - 144",
    "Control DownDraft - Successful - Control_DownDraft_Initialize - 107",
    "Control Extractor - Successful - Control_Extractor_Initialize - 104",
    "Control BackBottle - Successful - Control_BackBottle_Initialize - 109",
    "Control Filter - Successful - Control_Filter_Initialize - 105",
    "Control Monitor - Successful - Control_Monitor_Initialize - 122",
    "Control Network - Error Failed - Control_Network_Registry_Get_Value - 334",
    "Control Heater - Successful - Control_Heater_Initialize - 262",
    "Control Network - Error Failed - Control_Network_Registry_Get_Value - 334",
    "Control Network - Error Failed - Control_Network_Registry_Get_Value - 334",
    "Control Network - Error Failed - Control_Network_Registry_Get_Value - 334",
    "Control Network - Error Failed - Control_Network_Registry_Get_Value - 334",
    "Control Network - Successful - Control_Network_Initialize - 112",
    "Control Power - Successful - Control_Power_Initialize - 120",
    "Control Pressure - Successful - Control_Pressure_Initialize - 131",
    "Control OnHold - Successful - Control_OnHold_Initialize - 136",
    "Control Reagent - Successful - Control_Reagent_Initialize - 104",
    "Control Service - Successful - Control_Service_Initialize - 101",
    "Control Specific Gravity - Successful - Control_SG_Initialize - 117",
    "Control Rotation - Successful - Control_Rotation_Initialize - 101",
    "Control Valve - Successful - Control_Valve_Initialize - 155",
    "**** Control modules successfully initialized ****",
    "XML Date Import - Successful - XML_DateImport_Initialize - 132",
    "Control Waste Management - Successful - Control_WM_Initialize - 174",
    "XML Diagnostics Import - Successful - XML_DiagnosticsImport_Initialize - 159",
    "XML Flushes Import - Successful - XML_FlushesImport_Initialize - 167",
    "XML Programs Export - Successful - XML_ProgramsExport_Initialize - 166",
    "XML Flushes Export - Successful - XML_FlushesExport_Initialize - 157",
    "XML Programs Import - Successful - XML_ProgramsImport_Initialize - 174",
    "XML Scripts Import - Successful - XML_ScriptsImport_Initialize - 136",
    "XML Settings Export - Successful - XML_SettingsExport_Initialize - 299",
    "XML Reagents Import - Successful - XML_ReagentsImport_Initialize - 128",
    "XML Settings Import - Successful - XML_SettingsImport_Initialize - 492",
    "**** XML modules successfully initialized ****",
    "UI Access Codes - Successful - UI_AccessCodes_Initialize - 195",
    "XML Control - Successful - XML_Control_Initialize - 105",
    "UI Add/Edit User - Successful - UI_AddEditUser_Initialize - 195",
    "UI Chamber Available - Successful - UI_ChamberAvailable_Initialize - 289",
    "UI Chamber NotAvailable - Successful - UI_ChamberNotAvailable_Initialize - 135",
    "UI Alarms - Successful - UI_Alarms_Initialize - 185",
    "UI ConceptDemo - Successful - UI_ConceptDemo_Initialize - 148",
    "UI Customer Services - Successful - UI_CustomerServices_Initialize - 165",
    "UI Customisation - Successful - UI_Customisation_Initialize - 179",
    "UI Confirm - Successful - UI_Confirm_Initialize - 134",
    "UI DeepLASER Link Account - Successful - UI_DeeplaserLinkAccount_Initialize - 177",
    "UI Disable Pipes - Successful - UI_DisablePipes_Initialize - 140",
    "UI Edit Flush - Successful - UI_EditFlush_Initialize - 224",
    "UI Detailed Information - Successful - UI_DetailedInformation_Initialize - 260",
    "UI Edit Program - Successful - UI_EditProgram_Initialize - 239",
    "UI Edit Select Program - Successful - UI_EditSelectProgram_Initialize - 154",
    "UI Faults - Successful - UI_Faults_Initialize - 156",
    "UI Edit Select Flush - Successful - UI_EditSelectFlush_Initialize - 153",
    "UI FaultsInformation - Successful - UI_FaultsInformation_Initialize - 162",
    "UI File Operations - Successful - UI_FileOperations_Initialize - 151",
    "UI Flush - Successful - UI_Flush_Initialize - 172",
    "UI FaultDiagnostics - Successful - UI_FaultDiagnostics_Initialize - 186",
    "UI Flush Complete - Successful - UI_FlushComplete_Initialize - 145",
    "UI Keyboard - Successful - UI_Keyboard_Initialize - 200",
    "UI Lid Open - Successful - UI_LidOpen_Initialize - 132",
    "UI Invalidate Warranty - Successful - UI_InvalidateWarranty_Initialize - 153",
    "UI Lims - Successful - UI_Lims_Initialize - 162",
    "UI LoadPrograms - Successful - UI_LoadPrograms_Initialize - 190",
    "UI Load Reagents - Successful - UI_LoadReagents_Initialize - 290",
    "UI LoadFlushes - Successful - UI_LoadFlushes_Initialize - 190",
    "UI Load Setup - Successful - UI_LoadSetup_Initialize - 154",
    "UI Main - Successful - UI_Main_Initialize - 462",
    "UI Netmon - Successful - UI_Netmon_Initialize - 161",
    "UI Log In - Successful - UI_LogIn_Initialize - 167",
    "UI Number Pad - Successful - UI_NumberPad_Initialize - 258",
    "UI Network Configuration - Successful - UI_NetworkConfiguration_Initialize - 218",
    "UI Options - Successful - UI_Options_Initialize - 193",
    "UI Number Pad - Successful - UI_NumberPad_Initialize - 258",
    "UI Process Complete - Successful - UI_ProcessComplete_Initialize - 151",
    "UI Production Services (Heaters) - Successful - UI_ProductionServices_Heaters_Initialize - 199",
    "UI Production Services (Power) - Successful - UI_ProductionServices_Power_Initialize - 203",
    "UI Production Services - Successful - UI_ProductionServices_Initialize - 370",
    "UI Power Down - Successful - UI_PowerDown_Initialize - 134",
    "UI Reagent Names - Successful - UI_ReagentNames_Initialize - 193",
    "UI Reports - Successful - UI_Reports_Initialize - 282",
    "UI QualityControl - Successful - UI_QualityControl_Initialize - 330",
    "UI Reports View - Successful - UI_Reports_View_Initialize - 183",
    "UI Rotation Management - Successful - UI_RotationManagement_Initialize - 294",
    "UI Save Flushes - Successful - UI_SaveFlushes_Initialize - 180",
    "UI Reset Level - Successful - UI_ResetLevel_Initialize - 200",
    "UI Save Logs - Successful - UI_SaveLogs_Initialize - 157",
    "UI Save Setup - Successful - UI_SaveSetup_Initialize - 152",
    "UI Script List Production - Successful - UI_ScriptList_Production_Initialize - 175",
    "UI Save Programs - Successful - UI_SavePrograms_Initialize - 180",
    "UI Script List Service - Successful - UI_ScriptList_Service_Initialize - 175",
    "UI Select Flush - Successful - UI_SelectFlush_Initialize - 160",
    "UI Select Language - Successful - UI_SelectLanguage_Initialize - 157",
    "UI Script Run - Successful - UI_ScriptRun_Initialize - 210",
    "UI Select Program - Successful - UI_SelectProgram_Initialize - 159",
    "UI Services - Successful - UI_Services_Initialize - 229",
    "UI Set Date - Successful - UI_SetDate_Initialize - 228",
    "UI Serial Number - Successful - UI_SerialNumber_Initialize - 157",
    "UI Set Time - Successful - UI_SetTime_Initialize - 213",
    "UI Splash - Successful - UI_Splash_Initialize - 136",
    "UI Status Bar - Successful - UI_StatusBar_Initialize - 220",
    "UI Software Update - Successful - UI_SoftwareUpdate_Initialize - 162",
    "UI Storage Temperatures - Successful - UI_StorageTemperatures_Initialize - 158",
    "UI Use Limits - Successful - UI_UseLimits_Initialize - 194",
    "UI WM Warning - Successful - UI_WMWarning_Initialize - 179",
    "UI Unload Reagents - Successful - UI_UnloadReagents_Initialize - 263",
    "UI Workflow Setup - Successful - UI_WorkflowSetup_Initialize - 271",
    "**** UI modules successfully initialized ****",
    "**** System Start ****",
    "UI Control - Successful - UI_Control_Initialize - 90",
    "IF Datastore - Datastore Loaded",
    "M1_IDLE       1",
    "PT0_STANDBY_ATMOSPHERE    9",
    "IF Diagnostics Datastore - Loaded",
    "LS 0  0  0  R: 0  0  0  [L: 0.00 RAW: 0.00]",
    "IPC Received, NetmonStarted(0:'c3649e8468c6dad714242731852e043a530ec6f9' )",
    "[DL    ] Starting Deeplaser",
    "FPGA: 0.0.0  NIOS: 0.0.0  SOFTWARE: TFC Test 2018-05-16  SNo.: RS19191919",
    "[Netmon] Ready",
    "UI Main - Options",
    "[DL    ] MemLoad = 43% TotalPhys = 4194303 KiB AvailPhys = 4194303 KiB",
    "UI Select Language - OK",
    "UI Options - Back",
    "Log - Successful - OS_Log_Initialize - 183",
    "Message Queue - Successful - OS_MessageQueue_Initialize - 123",
    "POWER ON",
    "Resource - Successful - OS_Resource_Initialize - 105",
    "Cursor - Successful - OS_Cursor_Initialize - 93",
    "Sound - Successful - OS_Sound_Initialize - 152",
    "Script - Successful - OS_Script_Initialize - 105",
    "Time - Successful - OS_Time_Initialize - 132",
    "OS Device - Successful - OS_Device_Initialize - 177",
    "OS Font - Successful - OS_Font_Initialize - 131",
    "OS Bitmap - Successful - OS_Bitmap_Initialize - 126",
    "OS Graphics - Successful - OS_Graphics_Initialize - 174"
]