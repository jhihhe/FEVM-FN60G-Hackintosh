# FEVM-FN60G Hackintosh EFI 配置指南  
[![OpenCore 1.0.3 MOD](https://img.shields.io/badge/OpenCore-1.0.3_MOD-blue)](https://github.com/acidanthera/OpenCorePkg)  
[![macOS 15.1](https://img.shields.io/badge/macOS-Sequoia_15.1-red)](https://www.apple.com/macos)  
[![GitHub Stars](https://img.shields.io/github/stars/jhihhe/FEVM-FN60G-Hackintosh?style=social)](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/stargazers)  

---

## 🚀 项目概述  
专为 **FEVM-FN60G (Intel 13代 + AMD RX 6600M)** 设计的 OpenCore EFI 配置方案，支持 macOS 15.1 系统，提供以下核心功能：  
- CPU 变频加速  
- 显卡 HIDPI 支持  
- 双系统引导 (Windows/Linux)  
- 完整网络与多媒体功能  

---

## 📦 硬件配置  
| 组件          | 型号                          |  
|---------------|-------------------------------|  
| **CPU**       | Intel® Core™ i5-13600T (13th Gen) |  
| **显卡**      | AMD Radeon RX 6600M           |  
| **存储**      | KIOXIA EXCERIA PRO/SE SSD     |  

---

## 📌 更新日志 (2025.02.22)  
- 🛠️ 全面适配 OpenCore 1.0.3 MOD 版  
- 🔄 更新所有 Kext 驱动至最新版本  
- 📱 新增 U 盘安装支持 (hfsplus.efi)  
- 🖥️ 优化 AMD Radeon Pro W6600 显卡配置  
- 🔋 集成黑果小兵 USB 定制驱动  

---

## ⚠️ 注意事项  
1. **必填参数**：需自行生成并修改 `Board Serial Number`、`SmUUID`、`SysParameter` 中的 "自定义UUID" 等关键配置[1](@ref)。  
2. **BIOS 设置**：  
  - 关闭 Secure Boot  
  - 禁用 CFG Lock  
  - 内存频率设为 **Intel 规范模式**  

---

## 📸 系统实测  
![系统概览](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/raw/main/%E7%B3%BB%E7%BB%9F%E6%8A%A5%E5%91%8A.png)  
![OpenCore 主题](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/raw/main/OC%E4%B8%BB%E9%A2%98.jpeg)  

---

## 📝 高级配置  
1. **Verbose 模式**：  
  - 修改 NVRAM → 添加 `boot-args: -v`  
2. **启动策略**：  
  - 设置 `ScanPolicy=0` 支持多系统引导  

---

## 🙏 鸣谢  
- 参考了 [daliansky](https://github.com/daliansky/FEVM-FN60G-Hackintosh) 和 [Xmingbai](https://github.com/Xmingbai/FEVM-FN60G-Hackintosh) 的配置方案[5](@ref)。  
- 使用工具：[Quine](https://quine.sh) 生成小卡片[2,6](@ref)，[readme.so](https://readme.so) 优化布局[3](@ref)。  

---
