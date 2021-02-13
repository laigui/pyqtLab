@echo off
setlocal

set NAME=myapp

cd %~dp0\..
cd %NAME%
pyinstaller.exe %NAME%.py --onefile --noconsole --clean --add-data data;data
move dist\%NAME%.exe %~dp0\
rmdir /S /Q build dist
del %NAME%.spec
cd %~dp0
