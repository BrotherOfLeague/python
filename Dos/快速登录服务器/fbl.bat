@echo off
cd /D D:\SVN\Organization\trunk\Dos\���ٵ�¼������
FOR /F "eol=; tokens=1,2 delims==" %%i in (fbl.ini) do (
if %%i==IP set IP=%%j
if %%i==Username set Username=%%j
if %%i==Password set Password=%%j
)
START putty %Username%@%IP% -pw %Password%