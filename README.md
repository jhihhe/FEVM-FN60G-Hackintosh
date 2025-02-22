# 🌟 FEVM-FN60G-Hackintosh-EFI_OpenCore-macOS 🌟  
**多语言支持** | [中文](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/README.md) | [English](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/README-EN.md)  

---

## 🚀 快速开始  
**最新版本下载** → [前往 Releases 页面](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/releases)  

⚠️ **重要提示**  
使用前请自行生成以下信息并修改对应配置：  
- `Board Serial Number`  
- `序列号`  
- `SmUUID`  
- 修改 `SysPrameter` 中的“自定义UUID”  
- 更新 `RtVariables` 中的 `MLB` 和 `ROM`  

---

## 📜 更新日志  
- ✔️ **OpenCore 升级至 1.0.3 MOD 版**  
- ✔️ **所有 Kext 驱动更新至最新版本**  
- ✔️ **新增 `hfsplus.efi` 支持 U 盘安装**  
- ✔️ **显卡定制为 AMD Radeon Pro W6600（性能增强）**  
- ✔️ **USB 驱动更换为黑果小兵最新定制版**  
- ✔️ **IOSkywalkFamily.kext 更新至 1.2.0，支持 macOS Sonoma 14.7 及 Sequoia 15.1**  

---

## 🖥️ 硬件配置  
| **组件**       | **型号**                                   |
|----------------|-------------------------------------------|
| **机型**       | FEVM-FN60G（BIOS 版本 FN60G-BIOS B11HF210） |
| **CPU**        | 第 13 代 Intel® Core™ i5-13600T            |
| **显卡**       | AMD Radeon RX 6600M                       |
| **板载网卡**   | Realtek® RTL8125B 千兆网卡                |
| **WiFi/蓝牙**  | BCM94352Z（蓝牙 4.2）                     |
| **固态硬盘**   | KIOXIA-EXCERIA PRO SSD SE10-2TB（TRIM 开启）<br>KIOXIA-EXCERIA G2 SSD RD20-2TB |

---

## ⚙️ BIOS 设置  
- **关键修改项**：  
  - 关闭 `Secure Boot`  
  - 关闭 `CFG Lock`  
- **优化项**：  
  - 支持 5600 MHz 内存频率  
  - AC/DC Loadline 设置为 110/110  
  - 内存超频选项移至 `OverClock` 菜单  

📥 **BIOS 下载** → [点击此处](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/releases/tag/BIOS)  

---

## ✅ 功能状态  
### **核心组件**  
- **CPU 变频**：  
  ![CPU 测试](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/CPU%E6%B5%8B%E8%AF%95.png)  
  ![CPU 监测](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/CPU%E7%9B%91%E6%B5%8B.png)  
  - 机型设置为 `iMacPro1,1`，性能提升 30%  

- **显卡与解码**：  
  ![显卡信息](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/%E6%98%BE%E5%8D%A1.png)  
  - 支持 HIDPI & H.264/HEVC 硬解  
  - 独显参数优化（AAPL,slot-name）  

- **网络与连接**：  
  - 有线网卡：正常  
    ![有线网卡状态](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/%E6%9C%89%E7%BA%BF%E7%BD%91%E5%8D%A1.png)  
  - 无线/蓝牙：AirDrop & HandOff 正常  
    ![Wi-Fi 状态](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/%E6%97%A0%E7%BA%BF%E7%BD%91.png)  
    ![蓝牙状态](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/%E8%93%9D%E7%89%99.png)  

- **系统功能**：  
  - USB 全端口定制  
    ![USB 映射](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/USB.png)  
  - 睡眠唤醒 & 开关机：正常  
  - iCloud 服务（App Store/iMessage/FaceTime）：正常  

---

## 💡 使用提示  
1. **Verbose 模式**：  
   - 修改 `config.plist → NVRAM → boot-args` 添加 `-v` 参数。  
2. **多系统引导**：  
   - `ScanPolicy` 默认设为 `0`，可搜索所有分区。按需调整以限制搜索类型。  

---

## 🙏 鸣谢  
本 EFI 参考以下项目优化：  
- [daliansky/FEVM-FN60G-Hackintosh](https://github.com/daliansky/FEVM-FN60G-Hackintosh)  
- [Xmingbai/FEVM-FN60G-Hackintosh](https://github.com/Xmingbai/FEVM-FN60G-Hackintosh)  

---

**兼容系统**：  
macOS Catalina ~ macOS Sequoia  
**OpenCore 版本**：1.0.3  

![系统概览](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/%E7%B3%BB%E7%BB%9F%E6%8A%A5%E5%91%8A.png)  
![OpenCore 主题](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/OC%E4%B8%BB%E9%A2%98.jpeg)
