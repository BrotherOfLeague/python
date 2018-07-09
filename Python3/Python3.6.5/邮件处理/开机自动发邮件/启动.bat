@echo off
cd /d D:\SVN\Organization\trunk\Python3\Python3.6.5\邮件处理\开机自动发邮件
cd /d D:\SVN\Organization\trunk\Python3\Python3.6.5\邮件处理\开机自动发邮件

ping 47.91.232.233 -n 3 >test.txt
for /f "skip=8 takens=2,* delims== " %%i in (test.txt) do @echo %%i