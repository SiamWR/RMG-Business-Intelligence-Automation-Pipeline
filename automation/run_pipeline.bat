@echo off

REM ==================================================
REM RMG BI AUTOMATION PIPELINE
REM ==================================================

cd /d D:\Projects\RMG_BI_Automation_Project

echo ======================================== >> automation\pipeline_log.txt
echo RMG BI PIPELINE STARTED >> automation\pipeline_log.txt
echo Date: %date% Time: %time% >> automation\pipeline_log.txt
echo ======================================== >> automation\pipeline_log.txt

call venv\Scripts\activate.bat

python python\pipeline.py >> automation\pipeline_log.txt 2>&1

IF %ERRORLEVEL% EQU 0 (
    echo RMG BI PIPELINE COMPLETED SUCCESSFULLY >> automation\pipeline_log.txt
) ELSE (
    echo RMG BI PIPELINE FAILED - ERROR CODE %ERRORLEVEL% >> automation\pipeline_log.txt
)

echo ======================================== >> automation\pipeline_log.txt
echo RMG BI PIPELINE FINISHED >> automation\pipeline_log.txt
echo ======================================== >> automation\pipeline_log.txt

exit /b %ERRORLEVEL%