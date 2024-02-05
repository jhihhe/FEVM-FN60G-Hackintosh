# FEVM-FN60G-Hackintosh-EFI_OpenCore-0.9.7 macOS

# [中文](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/README.md)｜[English](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/README-EN.md)

# 下载点击[releases](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/releases)

# 请自行生成Board Serial Number、序列号、SmUUID，并相应的修改SysPrameter系统参数中的“自定义UUID”，和RtVariables变量设置中的MLB、ROM

## 更新日志：
- [x] 1. 更新 oc 版本到0.9.7正式版
- [x] 2. 更新所有kext内核拓展驱动到最新版本
- [x] 3. 添加hfsplus.efi以支持u盘安装

## 配置
1. 机型: FEVM-FN60G（BIOS Version FN60G-BIOS（B11HF170）
   1.修复博通网卡Windows兼容性。
   2.修正14代部分处理器兼容性问题。
   3.修正部分内存条兼容性问题,支持5600频率内存
   请点击这里[下载BIOS](https://www.lanzouh.com/iHkix1mxk6yh) ）
1. CPU:13th Generation Intel® Core™ i5-13600T Processors
1. 显卡: AMD Radeon RX 6600M
1. 板载网卡: Realtek® RTL8125B Gigabit LAN Controller
1. WiFi/蓝牙: BCM94352Z（BT4.2）
1. 固态硬盘: KIOXIA-EXCERIA G2 SSD RD20-2TB（开启TRIM）

### BIOS设置
1. 关闭secure boot &cfg lock

# **可适用操作系统版本：支持macOS Catalina/Big Sur/macOS Monterey 12.7.3/macOS Ventura 13.6.4**
1. OpenCore版本：0.9.7
![主题](https://tva2.sinaimg.cn/large/cec1774cly8h1g75kzm0vj21hc0u0gmt.jpg)
- [x] 1. CPU变频：工作正常。 
![CPU](https://pic.imgdb.cn/item/65c0b97e9f345e8d033304b3.png)
![CPU1](https://pic.imgdb.cn/item/65c0b97e9f345e8d0333053c.png)
- [x] 2. 显卡：工作正常，开启HIDPI，开启H.264&HEVC硬件解码加速，RX6600M：工作正常，增加独显AAPL,slot-name参数，机型设置imacpro1,1 比macpro7,1增加30%性能
![显卡](https://pic.imgdb.cn/item/65c0bddf9f345e8d033f3cee.png)
![硬件解码加速：H.264&HEVC解码](https://pic.imgdb.cn/item/65c0be559f345e8d03407fce.png)
- [x] 3. 3.5mm声音：工作正常
- [x] 4. USB：工作正常
![USB](https://pic.imgdb.cn/item/65c0bee79f345e8d03421fdf.png)
- [x] 5. 有线网卡：工作正常
![有线网卡](https://pic.imgdb.cn/item/65c0b9789f345e8d0332f49a.png)
- [x] 6. 无线网卡：工作正常 
![Wi-Fi](https://pic.imgdb.cn/item/65c0b97d9f345e8d033301c5.png)
- [x] 7. 睡眠唤醒：工作正常 
- [x] 8. 关机开机：工作正常
- [x] 9. iCloud & App Store & iMessage & FaceTime：正常
- [x] 10. AirDrop & HandOff & Continuity：正常。
![蓝牙](https://pic.imgdb.cn/item/65c0b97d9f345e8d0333030a.png)

### Tips：

1. 该config默认为无verbose模式。如需启用verbose模式，config.plist需要修改以下一项：NVRAM-Add-7C436110-AB2A-4BBB-A880-FE41995C9F82-boot-args，添加-v。
1. 该config启动盘策略 ScanPolicy 值设置为0。可引导Windows或Other OS（Linux、Unix）如需指定搜索分区类型，可参考OC配置手册。

# 鸣谢 
# 使用了daliansky大佬和Xmingbai大佬的配置文件,如果需其他版本可点击大佬链接查看
# https://github.com/daliansky/FEVM-FN60G-Hackintosh

# https://github.com/Xmingbai/FEVM-FN60G-Hackintosh

