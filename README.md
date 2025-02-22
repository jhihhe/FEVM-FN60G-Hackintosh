# 🍎 FEVM-FN60G-Hackintosh-EFI_OpenCore-macOS

[![OpenCore 1.0.3](https://img.shields.io/badge/OpenCore-1.0.3_MOD-1575F9?logo=opencontainersinitiative&logoColor=fff)](https://github.com/acidanthera/OpenCorePkg)
[![macOS Sequoia](https://img.shields.io/badge/macOS-Sequoia_15.1-FF2D55?logo=apple)](https://www.apple.com/macos)
[![最新版本](https://img.shields.io/github/v/release/jhihhe/FEVM-FN60G-Hackintosh?label=下载&color=28a745&logo=github)](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/releases)
[![License](https://img.shields.io/badge/License-MIT-4DA1F2)](https://choosealicense.com/licenses/mit/)

[中文](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/README.md) | [English](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/README-EN.md)

## 📖 目录
- [⚠️ 重要提示](#-重要提示)
- [🛠️ 硬件配置](#️-硬件配置)
- [📜 更新日志](#-更新日志)
- [⚙️ BIOS 设置](#️-bios-设置)
- [🖥️ 功能状态](#️-功能状态)
- [📸 系统截图](#-系统截图)
- [🔧 高级设置](#-高级设置)
- [🙏 鸣谢](#-鸣谢)

## ⚠️ 重要提示
> **警告**  
> 必须自行生成以下参数并修改对应配置：
> - `Board Serial Number`
> - `序列号`
> - `SmUUID`
> - `SysParameter` 系统参数中的 "自定义UUID"
> - `RtVariables` 变量设置中的 `MLB`、`ROM`

## 🛠️ 硬件配置
| 组件类别       | 型号                                   |
|----------------|----------------------------------------|
| **机型**       | FEVM-FN60G (BIOS Version B11HF210)     |
| **CPU**        | Intel® Core™ i5-13600T (13th Gen)      |
| **显卡**       | AMD Radeon RX 6600M                    |
| **板载网卡**   | Realtek® RTL8125B Gigabit LAN          |
| **无线网卡**   | BCM94352Z (BT4.2)                      |
| **存储方案**   | KIOXIA EXCERIA PRO SSD SE10-2TB
KIOXIA EXCERIA G2 SSD RD20-2TB |

## 📜 更新日志 (2025.02.22)
- 🚀 **核心更新**
  - ✅ OpenCore 1.0.3 MOD 版
  - ✅ 全量更新 Kext 驱动
  - ✅ 新增 hfsplus.efi 支持 U 盘安装

- 🎮 **显卡优化**
  - ✅ AMD Radeon Pro W6600 显卡定制
  - ✅ 黑果小兵最新 USB 定制驱动
  - ✅ IOSkywalkFamily.kext 1.2.0 支持 macOS 14.7/15.1

## ⚙️ BIOS 设置
1. `关闭 Secure Boot`
2. `禁用 CFG Lock`
3. `内存频率遵循 Intel 规范`
4. `AC/DC Loadline 设为 110/110`

[![BIOS下载指南](https://img.shields.io/badge/BIOS_下载-图文教程-FFD33D?logo=biometrics-institute)](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/releases/tag/BIOS)

## 🖥️ 功能状态
<details>
<summary>📌 点击展开功能详情</summary>

### 🎯 核心功能
- [x] CPU 变频 (iMacPro1,1 机型提升30%性能)
- [x] 显卡 HIDPI + 硬件解码加速
- [x] USB 3.0/2.0 全端口定制
- [x] 双系统引导支持 (Windows/Linux)

### 🌐 网络功能
- [x] 有线/无线网络
- [x] AirDrop & HandOff
- [x] iCloud 全家桶

### ⚡ 系统功能
- [x] 睡眠/唤醒
- [x] 音频输出
- [x] 硬件监控
</details>

## 📸 系统截图
<details>
<summary>🖼️ 点击查看系统截图</summary>

| 系统概览 | OpenCore 主题 | 硬件解码 |
|----------|---------------|----------|
| ![系统概览](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/%E7%B3%BB%E7%BB%9F%E6%8A%A5%E5%91%8A.png) | ![OpenCore主题](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/OC%E4%B8%BB%E9%A2%98.jpeg) | ![硬件解码](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/%E7%A1%AC%E8%A7%A3%E7%A0%81.png) |
</details>

## 🔧 高级设置
```markdown
# 启用 Verbose 模式
1. 修改 NVRAM → Add → 7C436110-AB2A-4BBB-A880-FE41995C9F82
2. 在 boot-args 中添加 `-v` 参数

# 启动策略配置
- ScanPolicy=0 (支持 Windows/Linux 引导)
- 自定义策略参考 [OpenCore 官方文档](https://dortania.github.io/OpenCore-Post-Install/)
