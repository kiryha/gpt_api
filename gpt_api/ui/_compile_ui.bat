set UIFILE=%1
set UIDIR=%~dp$PATH:1
set FILENAME=%~n1
set SNAME=%UIDIR%%FILENAME%.py

CALL C:\Users\kko8\AppData\Local\Programs\Python\Python310\Scripts\pyside2-uic.exe %UIFILE% -o %SNAME%