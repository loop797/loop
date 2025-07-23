@echo off
title 🔨 تحويل LoopApp.exe - النسخة العربية
echo.
echo ==========================================
echo 🔁 جاري التأكد من وجود LoopApp.py
echo ==========================================
echo.

if not exist "LoopApp.py" (
    echo ❌ الملف LoopApp.py غير موجود.
    pause
    exit
)

echo ✅ جاري تحويل التطبيق...
pip show pyinstaller >nul 2>&1
if %errorlevel% neq 0 (
    echo ⏳ تثبيت pyinstaller...
    pip install pyinstaller
)

pyinstaller --noconsole --onefile ^
--add-data "loop_music.wav;." ^
--add-data "LOGO.png;." ^
--add-data "snow_background.gif;." ^
--icon=loop_icon.ico ^
--hidden-import=pygame ^
LoopApp.py

echo.
echo ✅ تم إنشاء LoopApp.exe داخل مجلد dist
pause
