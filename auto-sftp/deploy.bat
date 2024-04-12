@echo off
setlocal enabledelayedexpansion

rem Read the password from the file 
set /p PASSWORD=<password.txt

rem set PrivateKey Path
set /p PPK=<ppk.txt

rem Use WinSCP with the password
"C:\Program Files (x86)\WinSCP\WinSCP.com" /script=C:\auto-sftp\download_script.txt /parameter !PASSWORD!,!PPK!