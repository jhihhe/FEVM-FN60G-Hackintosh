<!-- readme-visuals:header:start -->
<p align="center"><img src="readme-assets/banner.svg" alt="FEVM FN60G — Hardware configuration and setup documentation" width="100%"></p>

<p align="center">
  <a href="https://github.com/jhihhe/FEVM-FN60G-Hackintosh/commits/main"><img src="https://img.shields.io/github/last-commit/jhihhe/FEVM-FN60G-Hackintosh?style=flat-square&amp;color=38bdf8" alt="Last commit"></a>
  <a href="https://github.com/jhihhe/FEVM-FN60G-Hackintosh/stargazers"><img src="https://img.shields.io/github/stars/jhihhe/FEVM-FN60G-Hackintosh?style=flat-square&amp;color=38bdf8" alt="GitHub stars"></a>
  <a href="https://github.com/jhihhe"><img src="https://img.shields.io/badge/Maintainer-%40Jhih%20he-38bdf8?style=flat-square" alt="Maintainer: @Jhih he"></a>
</p>
<!-- readme-visuals:header:end -->

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

![关于本机](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/%E5%85%B3%E4%BA%8E%E6%9C%AC%E6%9C%BA.png)
![System Overview](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/raw/main/%E7%B3%BB%E7%BB%9F%E6%8A%A5%E5%91%8A.png)

---

<!-- readme-visuals:overview:start -->

## At a glance

<table>
<tr>
<td width="33%"><strong>Machine configuration</strong><br><br>OpenCore configuration for FEVM-FN60G.</td>
<td width="33%"><strong>Hardware notes</strong><br><br>CPU, graphics, networking and USB records.</td>
<td width="33%"><strong>Downloads and checks</strong><br><br>Release links, setup notes and recorded screenshots.</td>
</tr>
</table>

### Workflow overview

```mermaid
flowchart LR
    S0["Review hardware and documentation"] --> S1
    S1["Back up existing EFI"] --> S2
    S2["Get configuration and replace identifiers"] --> S3
    S3["Check boot and hardware behavior"]
```

<!-- readme-visuals:overview:end -->

## 🚀 Quick Start
**Latest Stable EFI Download** →  
[![GitHub Release](https://img.shields.io/github/v/release/jhihhe/FEVM-FN60G-Hackintosh?style=for-the-badge&logo=apple)](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/releases)

> **Important Notice**  
> Before use, please generate and replace the following unique identifiers:
> - Board Serial Number  
> - Serial Number  
> - SmUUID  
>
> Configuration paths:
> - `PlatformInfo → Generic`
> - `NVRAM → RtVariables → MLB & ROM`

---

## 📜 Changelog
**Core Component Updates**  
![OpenCore](https://img.shields.io/badge/OpenCore-1.0.7_MOD-9cf?style=flat-square)  
![Kexts](https://img.shields.io/badge/Kexts-2025.03_Latest-4BC51D?style=flat-square)

- ✅ Official support for macOS Tahoe 26.3
- ✅ Stable Ethernet / Wi-Fi / Audio drivers
- ✅ All core kexts updated with optimized load order for 26.3
- ✅ ACPI and boot arguments fine-tuned for the new macOS release
- ✅ Improved sleep, wake, and network wake reliability

---

## 📌 Project Overview
This project provides a **custom OpenCore EFI solution** specifically designed for  
**FEVM-FN60G (Intel 13th / 14th Gen + AMD RX 6600M)**,  
targeting **macOS Tahoe 26.3** with a strong focus on stability, full hardware acceleration, and daily usability.

### Key Features
- Native-like macOS Tahoe 26.3 experience  
- CPU power management and frequency scaling  
  *(iMacPro1,1 SMBIOS for balanced performance and stability)*  
- Full AMD dGPU acceleration with HiDPI and hardware video decoding  
- Fully functional wired / wireless networking and Bluetooth Continuity  
- Complete audio support with proper volume control  
- Seamless multi-boot coexistence with Windows and Linux  

---

## 📥 Download & Updates
- **Latest Release**: https://github.com/jhihhe/FEVM-FN60G-Hackintosh/releases  
- **Update Highlights**:
  - ✅ OpenCore 1.0.7 MOD core update
  - ✅ All kexts synced to the latest stable versions
  - ✅ ACPI and boot argument adjustments for macOS Tahoe 26.3
  - ✅ Enhanced network and audio driver stability
  - ✅ Continuous optimization of USB mapping and power management

---

## ⚙️ Hardware Configuration
| Component | Model | Notes |
|----------|------|------|
| **CPU** | Intel® Core™ i5-13600T | Supports 12th–14th Gen CPUs |
| **GPU** | AMD Radeon RX 6600M | HDMI / DP, H.264 / HEVC hardware decoding |
| **Storage** | NVMe SSD | TRIM supported |
| **Memory** | DDR5 5600MHz | Mainstream DDR5 compatibility |
| **Ethernet** | Realtek RTL8125B | Stable Gigabit Ethernet |
| **Wi-Fi / BT** | BCM94352Z | Full Wi-Fi and Bluetooth support |

---

## 📸 Functional Validation

| Module | Status | Description |
|------|------|------|
| CPU Power Management | ✅ | Proper frequency scaling |
| GPU Acceleration | ✅ | Hardware decoding & display output |
| USB | ✅ | Fully customized port mapping |
| Sleep / Wake | ✅ | Stable sleep and wake |
| Ethernet | ✅ | RTL8125B operational |
| Wireless | ✅ | Wi-Fi / Bluetooth / Continuity |
| Audio | ✅ | Full audio support with volume control |

---

## 📝 Advanced Configuration
- `ScanPolicy=0` enables multi-OS boot scanning  
- `-v` can be enabled for verbose debugging  

---

## 🙏 Acknowledgements
- OpenCore Legacy Patcher — Broadcom wireless support  
  https://github.com/dortania/OpenCore-Legacy-Patcher
- daliansky/FEVM-FN60G-Hackintosh — EFI reference  
  https://github.com/daliansky/FEVM-FN60G-Hackintosh
- Xmingbai/FEVM-FN60G-Hackintosh — Compatibility solutions  
  https://github.com/Xmingbai/FEVM-FN60G-Hackintosh
- Daliansky Blog — Installation guides and troubleshooting  
  https://blog.daliansky.net/
