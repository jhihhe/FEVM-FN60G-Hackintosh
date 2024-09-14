# FEVM-FN60G-Hackintosh-EFI_OpenCore-macOS

# [中文](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/README.md)｜[English](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/README-EN.md)

# 下载点击[releases](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/releases)

# 请自行生成Board Serial Number、序列号、SmUUID，并相应的修改SysPrameter系统参数中的“自定义UUID”，和RtVariables变量设置中的MLB、ROM

## 更新日志：
- [x] 1. 更新 oc 版本到1.0.2 MOD版
- [x] 2. 更新所有kext内核拓展驱动到最新版本
- [x] 3. 添加hfsplus.efi以支持u盘安装
- [x] 4. 显卡定制为AMD Radeon Pro W6600以增强性能
- [x] 5. USB驱动更换为daliansky黑果小兵最新定制版本
- [x] 6. 更新IOSkywalkFamily.kext到1.1.0版本,以支持macOS Sonoma 14.6.1


![系统报告](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/%E7%B3%BB%E7%BB%9F%E6%8A%A5%E5%91%8A.png)

## 配置
1. 机型: FEVM-FN60G（BIOS Version FN60G-BIOS（B11HF210）
   
   1.修复博通网卡Windows兼容性。
   
   2.修正14代部分处理器兼容性问题。
   
   3.修正部分内存条兼容性问题,支持5600频率内存
   
   4.为兼容更多类型的处理器提高稳定性，修正AC/DC loadline数值为110/110
   
   5.内存频率修改为遵循intel处理器支持的频率和规范（默认不做内存超频），加入OverClock超频选项代替之前默认超频设置（单面海力士颗粒内存可选）
   
   请点击这里[下载BIOS](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/releases/tag/BIOS)

1. CPU:13th Generation Intel® Core™ i5-13600T Processors
1. 显卡: AMD Radeon RX 6600M
1. 板载网卡: Realtek® RTL8125B Gigabit LAN Controller
1. WiFi/蓝牙: BCM94352Z（BT4.2）
1. 固态硬盘: 1.KIOXIA-EXCERIA PRO SSD SE10-2TB（开启TRIM）2.KIOXIA-EXCERIA G2 SSD RD20-2TB
                      

### BIOS设置
1. 关闭secure boot &cfg lock

# **可适用操作系统版本：支持macOS Catalina/Big Sur/macOS Monterey/macOS Ventura/macOS Sonoma **
1. OpenCore版本：1.0.0
![主题](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/OC%E4%B8%BB%E9%A2%98.jpeg)
- [x] 1. CPU变频：工作正常，机型设置imacpro1,1 比macpro7,1增加30%性能
![CPU](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/CPU%E6%B5%8B%E8%AF%95.png)
![CPU1](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/CPU.png)
![CPU2](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/CPU%E7%9B%91%E6%B5%8B.png)
![CPU3](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/CPU%E7%9B%91%E6%B5%8B1.png)
- [x] 2. 显卡：工作正常，开启HIDPI，开启H.264&HEVC硬件解码加速，RX6600M：工作正常，增加独显AAPL,slot-name参数
![显卡](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/%E6%98%BE%E5%8D%A1.png)
![显卡1](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/GPU%E6%B5%8B%E8%AF%951.png)
![硬件解码加速：H.264&HEVC解码](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/%E7%A1%AC%E8%A7%A3%E7%A0%81.png)
- [x] 3. 3.5mm声音：工作正常
- [x] 4. USB：工作正常
![USB](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/USB.png)
- [x] 5. 有线网卡：工作正常
![有线网卡](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/%E6%9C%89%E7%BA%BF%E7%BD%91%E5%8D%A1.png)
- [x] 6. 无线网卡：工作正常

![Wi-Fi](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/%E6%97%A0%E7%BA%BF%E7%BD%91.png)
- [x] 7. 睡眠唤醒：工作正常 
- [x] 8. 关机开机：工作正常
- [x] 9. iCloud & App Store & iMessage & FaceTime：正常
- [x] 10. AirDrop & HandOff & Continuity：正常。
![蓝牙](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/%E8%93%9D%E7%89%99.png)

### Tips：

1. 该config默认为无verbose模式。如需启用verbose模式，config.plist需要修改以下一项：NVRAM-Add-7C436110-AB2A-4BBB-A880-FE41995C9F82-boot-args，添加-v。
1. 该config启动盘策略 ScanPolicy 值设置为0。可引导Windows或Other OS（Linux、Unix）如需指定搜索分区类型，可参考OC配置手册。

# 鸣谢 
# 参考了daliansky大佬和Xmingbai大佬的配置文件,如果需其他版本可点击大佬链接查看
# https://github.com/daliansky/FEVM-FN60G-Hackintosh

# https://github.com/Xmingbai/FEVM-FN60G-Hackintosh

