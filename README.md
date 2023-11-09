# 2023.11.6
## 一些linux脚本命令
#### rustdesk远程桌面自建服务器     输入,回车,一路yes,全部安装,dns,输入域名,然后完成后直接在手机上中继服务器输入域名,无需端口就能用,别的都不用搞    
wget https://raw.githubusercontent.com/techahold/rustdeskinstall/master/install.sh      
chmod +x install.sh      
./install.sh       
#### xui科学上网
bash <(curl -Ls https://raw.githubusercontent.com/FranzKafkaYu/x-ui/956bf85bbac978d56c0e319c5fac2d6db7df9564/install.sh) 0.3.4.4
#### aws 的ec2开root
https://blog.csdn.net/u014756339/article/details/120801927          ,5步搞完不要第六步直接重启,就能root,同时普通账户失效
# 2023.10.16
## 禁用移动鼠标唤醒电脑
打开设备管理器,拔掉键盘,将键盘,鼠标和其他指针设备里面所有设备的属性,电源管理,允许此设备唤醒计算机,关了!,别问为什么要拔键盘
![image](https://github.com/cancundeyingzi/rizhi/assets/73635883/a4428bdc-ce75-4b3e-ad3b-3053eec669bb)

# 2023.7.23
## 删除虚拟摄像头
电脑按win+r输入regedit       
搜索摄像头名称,删除    

# 2023.7.21
折腾了好久,发现mpv的qsv-copy解码不兼容RTXvsr视频超分辨率,开启后者,mpv就会闪退.........

# 2023.5.26
## edge观看b站HDR视频
在地址栏输入edge://flags/   
页面搜索force color profile   
改为HDR10![image](https://github.com/cancundeyingzi/rizhi/assets/73635883/715d5630-0655-4446-b6b4-f27062c0eb7c)



# 2023.4.15
## ios端视频播放软件:    
alook,操作手势舒服,自定义多,不支持HDR等        
nplayer,在线视频加载迅速,手势操作还行         
infuse,格式支持全面,字幕适配极好,手势操作是屎,天天误触/触发不动             
# 2023.4.14
## win11笔记本电池健康度
Win+R，输入CMD。在CMD里面输入“powercfg /batteryreport”。然后打开个人文件夹，查看生成的电池报告文件   

![image](https://user-images.githubusercontent.com/73635883/231927237-68016fb6-149d-4a77-8592-901de2249e0b.png)
## win11ldac蓝牙音频
下载软件Alternative A2DP Driver,需要付费20一个设备   

![image](https://user-images.githubusercontent.com/73635883/231927465-ae0863b0-be1f-4d90-ba73-78e385f80876.png)
## 注册表清理软件Wise Registry Cleaner
感觉还行,挺好用的,免费
## FontCreator 14字体设计软件,改字体名
放在私人网盘
## mkv内嵌字幕  
注意修改字体名称,部分字体有中英文两个名字,全要改   
 ![image](https://user-images.githubusercontent.com/73635883/231929603-b64abdfe-dd52-4296-9a2e-24c3b2687a1e.png)
