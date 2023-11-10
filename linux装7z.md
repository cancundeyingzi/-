先在win下载,解压,发送到linux:https://github.com/p7zip-project/p7zip/releases/download/v17.05/linux-cmake-p7zip.7z            
正常情况cd到目录./7za就行了       
如果version `GLIBC_2.34’ not found            
检查版本          
strings /lib/x86_64-linux-gnu/libc.so.6 |grep GLIBC_         
看看有没有对应版本,如果没有,拿root
vim /etc/apt/sources.list
deb http://th.archive.ubuntu.com/ubuntu jammy main    #添加该行到文件
然后再检查版本看看,有了就cd到目录./7za就行了
