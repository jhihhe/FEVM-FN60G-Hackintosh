# 🚀 FEVM-FN60G-Hackintosh-EFI_OpenCore-macOS  
[![OpenCore 1.0.3](https://img.shields.io/badge/OpenCore-1.0.3_MOD-blue)](https://github.com/acidanthera/OpenCorePkg)  
[![macOS Sequoia](https://img.shields.io/badge/macOS-Sequoia_15.1-red)](https://www.apple.com/macos)  

[中文](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/README.md) | [English](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/README-EN.md)  

---

## 📥 下载  
[![最新版本](https://img.shields.io/badge/下载-Releases-green)](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/releases)  

---

## ⚠️ 重要提示  
**必须自行生成以下参数并修改对应配置**：  
- Board Serial Number  
- 序列号  
- SmUUID  
- SysParameter 系统参数中的"自定义UUID"  
- RtVariables 变量设置中的 MLB、ROM  

---

## 🛠️ 硬件配置  
| 组件        | 型号                                   |  
|-------------|----------------------------------------|  
| **机型**    | FEVM-FN60G (BIOS Version B11HF210)     |  
| **CPU**     | Intel® Core™ i5-13600T (13th Gen)      |  
| **显卡**    | AMD Radeon RX 6600M                    |  
| **板载网卡**| Realtek® RTL8125B Gigabit LAN          |  
| **无线网卡**| BCM94352Z (BT4.2)                      |  
| **存储**    | KIOXIA EXCERIA PRO SSD SE10-2TB
KIOXIA EXCERIA G2 SSD RD20-2TB |  

---

## 📜 更新日志 (2025.02.22)  
- ✅ OpenCore 1.0.3 MOD 版  
- ✅ 全量更新 Kext 驱动  
- ✅ 新增 hfsplus.efi 支持 U 盘安装  
- ✅ AMD Radeon Pro W6600 显卡定制  
- ✅ 黑果小兵最新 USB 定制驱动  
- ✅ IOSkywalkFamily.kext 1.2.0 支持 macOS 14.7/15.1  

---

## ⚙️ BIOS 设置  
1. 关闭 Secure Boot  
2. 禁用 CFG Lock  
3. 内存频率遵循 Intel 规范  
4. AC/DC Loadline 设为 110/110  

[![BIOS下载](https://img.shields.io/badge/BIOS-下载指南-yellow)](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/releases/tag/BIOS)  

---

## 🖥️ 功能状态  
<details><summary>点击查看详细功能状态</summary>  

### 核心功能  
- [x] CPU 变频 (iMacPro1,1 机型提升30%性能)  
- [x] 显卡 HIDPI + 硬件解码加速  
- [x] USB 3.0/2.0 全端口定制  
- [x] 双系统引导支持 (Windows/Linux)  

### 网络功能  
- [x] 有线/无线网络  
- [x] AirDrop & HandOff  
- [x] iCloud 全家桶  

### 系统功能  
- [x] 睡眠/唤醒  
- [x] 音频输出  
- [x] 硬件监控  

</details>  

---

## 📸 系统截图  
<details><summary>点击展开系统截图</summary>  

![系统概览](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/%E7%B3%BB%E7%BB%9F%E6%8A%A5%E5%91%8A.png)  
![OpenCore主题](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/OC%E4%B8%BB%E9%A2%98.jpeg)  
![硬件解码](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/%E7%A1%AC%E8%A7%A3%E7%A0%81.png)  

</details>  

---

## 🚀 高级设置  
1. 启用 Verbose 模式：  
   - 修改 NVRAM → Add → `7C436110-AB2A-4BBB-A880-FE41995C9F82` → `boot-args` 添加 `-v`  
2. 启动策略：  
   - `ScanPolicy=0` (支持 Windows/Linux 引导)  
   - 自定义搜索策略参考 [OpenCore 官方网页](https://dortania.github.io/OpenCore-Post-Install/)  

---

## 🙏 鸣谢  
参考了 [daliansky](https://github.com/daliansky/FEVM-FN60G-Hackintosh) 和 [Xmingbai](https://github.com/Xmingbai/FEVM-FN60G-Hackintosh) 的配置文件[5](@ref)。 
