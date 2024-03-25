@echo off
setlocal

rem Vérification de l'installation de Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python n'est pas installé sur ce système.
    pause
    exit /b
)

rem Vérification et installation des modules nécessaires
python -c "import sys, tkinter, tkinter.ttk as ttk, os.path, matplotlib" >nul 2>&1
if %errorlevel% neq 0 (
    echo Installation des modules nécessaires...
    python -m pip install -q tkinter
    python -m pip install -q ttkwidgets
    python -m pip install -q matplotlib
    rem Ajoutez d'autres installations de modules ici si nécessaire
    echo Modules installés avec succès.
)

rem Lancement du script Python "InterfacePython"
start /B "" pythonw.exe InterfacePython.py

endlocal