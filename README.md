<p align="center">
  <img src="https://img.shields.io/badge/OpenCore-1.0.7_MOD-9cf?style=flat-square&logo=apple" />    
  <img src="https://img.shields.io/badge/macOS-Tahoe_26.3-success?style=flat-square&logo=apple" />    
  <img src="https://img.shields.io/badge/BIOS-FN60G_B11HF210-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-green" />    
</p>

<h1 align="center">FEVM-FN60G Hackintosh EFI for OpenCore</h1>  
<div align="center">
  <a href="https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/README.md">中文</a>｜    
  <a href="https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/README-EN.md">English</a>    
</div>

![系统概览](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/raw/main/%E7%B3%BB%E7%BB%9F%E6%8A%A5%E5%91%8A.png)

---

## 🚀 快速开始
**最新稳定版 EFI 下载** →  
[![GitHub Release](https://img.shields.io/github/v/release/jhihhe/FEVM-FN60G-Hackintosh?style=for-the-badge&logo=apple)](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/releases)

> **重要提示**  
> 使用前请自行生成并替换以下三码：
> - Board Serial Number  
> - Serial Number  
> - SmUUID  
>
> 修改位置：
> - `PlatformInfo → Generic`
> - `NVRAM → RtVariables → MLB & ROM`

---

## 📜 更新日志
**核心组件升级**  
![OpenCore](https://img.shields.io/badge/OpenCore-1.0.7_MOD-9cf?style=flat-square)  
![Kexts](https://img.shields.io/badge/Kexts-2025.03_Latest-4BC51D?style=flat-square)

- ✅ 正式支持 macOS Tahoe 26.3
- ✅ 有线网卡 / 无线网卡 / 声卡全部实现稳定驱动
- ✅ 核心 Kext 全面升级并针对 26.3 优化加载顺序
- ✅ ACPI 与引导参数针对新系统版本微调
- ✅ 提升睡眠唤醒与网络唤醒稳定性

---

## 📌 项目概述  
本项目是专为 **FEVM-FN60G（Intel 13 / 14 代 + AMD RX 6600M）** 打造的 **OpenCore EFI 解决方案**，  
面向 **macOS Tahoe 26.3**，在保证系统稳定性的前提下，实现硬件完整驱动与日常可用性：

- macOS Tahoe 26.3 原生级运行体验  
- CPU 变频加速（iMacPro1,1 机型，性能与稳定性平衡）  
- AMD 独显 HIDPI 与完整硬件解码  
- 有线 / 无线网络与蓝牙连续互通功能正常  
- 声卡完整驱动，系统音量与多应用音频输出正常  
- Windows / Linux 多系统引导共存  

---

## 📥 下载与更新  
- **最新版本**：[点击下载](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/releases)  
- **更新内容摘要**：
  - ✅ OpenCore 1.0.7 MOD 核心更新
  - ✅ 全量 Kext 同步最新稳定版本
  - ✅ 针对 macOS Tahoe 26.3 的 ACPI / 引导参数调整
  - ✅ 网络与音频相关驱动稳定性增强
  - ✅ USB 映射与电源管理持续优化

---

## ⚙️ 硬件配置  
| 组件 | 型号 | 说明 |
|------|------|------|
| **CPU** | Intel® Core™ i5-13600T | 支持 12–14 代处理器，功耗与性能平衡 |
| **显卡** | AMD Radeon RX 6600M | HDMI / DP 输出，H.264 / HEVC 硬解 |
| **存储** | NVMe SSD | 支持 TRIM，系统运行稳定 |
| **内存** | DDR5 5600MHz | 兼容主流 DDR5 模组 |
| **有线网卡** | Realtek RTL8125B | 千兆有线网络稳定驱动 |
| **无线网卡** | BCM94352Z | Wi-Fi / 蓝牙功能完整 |

---

## 📸 功能实测验证

### 核心功能状态  
| 功能模块 | 状态 | 说明 |
|---------|------|------|
| CPU 变频 | ✅ | 变频与功耗管理正常 |
| 显卡加速 | ✅ | 硬件解码与显示输出正常 |
| USB | ✅ | 全端口定制 |
| 睡眠唤醒 | ✅ | 睡眠 / 唤醒稳定 |
| 有线网络 | ✅ | RTL8125B 正常工作 |
| 无线网络 | ✅ | Wi-Fi / 蓝牙 / 连续互通 |
| 声音 | ✅ | 声卡完整驱动，音量控制正常 |

---

## 📝 高级配置
- `ScanPolicy=0` 支持多系统引导  
- 可按需开启 `-v` Verbose 调试模式  
  
---

## 🙏 鸣谢
本项目的实现离不开以下开源项目和技术支持：
- [OpenCore Legacy Patcher](https://github.com/dortania/OpenCore-Legacy-Patcher) - 博通网卡驱动支持
- [daliansky/FEVM-FN60G-Hackintosh](https://github.com/daliansky/FEVM-FN60G-Hackintosh) - EFI配置参考
- [Xmingbai/FEVM-FN60G-Hackintosh](https://github.com/Xmingbai/FEVM-FN60G-Hackintosh) - 硬件兼容性方案
- [黑果小兵部落阁](https://blog.daliansky.net/) - 安装教程与疑难解答
