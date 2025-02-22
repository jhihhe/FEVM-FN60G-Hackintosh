# FEVM-FN60G Hackintosh EFI 配置指南  
[![OpenCore 1.0.3 MOD](https://img.shields.io/badge/OpenCore-1.0.3_MOD-blue)](https://github.com/acidanthera/OpenCorePkg)  
[![macOS Sequoia](https://img.shields.io/badge/macOS-Sequoia_15.1-red)](https://www.apple.com/macos)  
[![GitHub Stars](https://img.shields.io/github/stars/jhihhe/FEVM-FN60G-Hackintosh?style=social)](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/stargazers)  

---

## 📌 项目概述  
专为 **FEVM-FN60G (Intel 13代 + AMD RX 6600M)** 设计的 OpenCore EFI 配置方案，支持 macOS 15.1 系统，提供以下核心功能：  
- CPU 变频加速（iMacPro1,1 机型性能提升 30%）  
- 显卡 HIDPI 支持与硬件解码加速  
- 双系统引导（Windows/Linux）  
- 完整网络与多媒体功能（AirDrop/Continuity/iCloud 全家桶）  

---

## 📥 下载与更新  
- **最新版本**：[点击下载](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/releases)  
- **更新日志**：  
  - ✅ OpenCore 1.0.3 MOD 版本适配  
  - ✅ 全 Kext 驱动更新至最新版本  
  - ✅ 新增 `hfsplus.efi` 支持 U 盘安装  
  - ✅ AMD Radeon Pro W6600M 显卡定制优化  
  - ✅ 黑果小兵 USB 驱动集成  
  - ✅ IOSkywalkFamily.kext 更新至 1.2.0（兼容 Sonoma 14.7/Sequoia 15.1）  

---

## ⚙️ 硬件配置  
| 组件          | 型号                          | 说明                                                                 |
|---------------|-------------------------------|----------------------------------------------------------------------|
| **CPU**       | Intel® Core™ i5-13600T (13th Gen) | 支持 12-14 代桌面处理器，最高 100W 性能释放                                |
| **显卡**      | AMD Radeon RX 6600M           | 黑苹果专用定制版，支持 HDMI/DP 输出及 H.264/HEVC 硬件解码加速                   |
| **存储**      | KIOXIA EXCERIA PRO/SE SSD     | 双 NVMe 插槽，最高 4TB 容量，开启 TRIM 优化性能                              |
| **内存**      | DDR5 5600MHz                  | 支持单面海力士颗粒超频，提供 OverClock 选项                                 |
| **网卡**      | Realtek® RTL8125B Gigabit LAN  | 有线网络高速稳定                                                      |
| **无线网卡**  | BCM94352Z (BT4.2)             | 支持 Wi-Fi 6E/蓝牙 5.3                                                |

---

## 🛠️ BIOS 设置指南  
1. **基础配置**：  
   - 关闭 Secure Boot 与 CFG Lock  
   - 内存频率设为 **Intel 规范模式**  
   - AC/DC Loadline 数值调整为 `110/110` 以提升稳定性  

2. **BIOS 下载**：  
   [点击获取最新 BIOS](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/releases/tag/BIOS)  

---

## 📸 功能实测验证  
![系统概览](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/raw/main/%E7%B3%BB%E7%BB%9F%E6%8A%A5%E5%91%8A.png)  
![OpenCore 主题](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/raw/main/OC%E4%B8%BB%E9%A2%98.jpeg)  

### 核心功能状态  
| 功能模块       | 状态 | 说明                                                                 |
|----------------|------|----------------------------------------------------------------------|
| CPU 变频       | ✅    | 工作正常，iMacPro1,1 机型性能提升 30%                                |
| 显卡解码       | ✅    | H.264/HEVC 硬件加速正常，独显 AAPL 参数优化                            |
| USB 3.0/2.0    | ✅    | 全端口定制，兼容 10Gbps 接口                                         |
| 睡眠唤醒       | ✅    | macOS 休眠与唤醒功能正常                                            |
| 网络功能       | ✅    | 有线/无线网络、AirDrop、HandOff 均正常                              |
| 多媒体         | ✅    | 3.5mm 声音输出、系统音频正常                                         |

---

---

## 📝 高级配置  
1. **Verbose 模式**：  
  - 修改 `config.plist` → `NVRAM → Add → 7C436110-AB2A-4BBB-A880-FE41995C9F82` → `boot-args: -v`
2. **启动策略**：  
  - `ScanPolicy=0` 支持 Windows/Linux 引导

---

## 🙏 鸣谢  
- 参考了 [daliansky](https://github.com/daliansky/FEVM-FN60G-Hackintosh) 和 [Xmingbai](https://github.com/Xmingbai/FEVM-FN60G-Hackintosh) 的配置方案。  
- 使用工具：[Quine](https://quine.sh) 生成小卡片，[readme.so](https://readme.so) 优化布局。
