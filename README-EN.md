<p align="center">
  <img src="https://img.shields.io/badge/OpenCore-1.0.5_MOD-9cf?style=flat-square&logo=apple" />    
  <img src="https://img.shields.io/badge/macOS-Sequoia_15.4-success?style=flat-square&logo=apple" />    
  <img src="https://img.shields.io/badge/BIOS-FN60G_B11HF210-blue?style=flat-square" />  
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-green" />    

</p>

<h1 align="center">FEVM-FN60G Hackintosh EFI for OpenCore</h1>  
<div align="center">
  <a href="https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/README.md">中文</a>｜    
  <a href="https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/README-EN.md">English</a>      
</div>

---

## 🚀 Quick Start
**Latest stable version EFI download** → [![GitHub Release](https://img.shields.io/github/v/release/jhihhe/FEVM-FN60G-Hackintosh?style=for-the-badge&logo=apple)](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/releases)

> **Important tips**
> Please generate the following three codes and modify the corresponding configuration before use:
> - Board Serial Number
> - Serial Number
> - SmUUID
>
> File location to be modified:
> - SysParameter → Custom UUID  
> - RtVariables → MLB & ROM

---

## 📜 Update log
**Core component upgrade**
![OpenCore](https://img.shields.io/badge/OpenCore-1.0.5_MOD-9cf?style=flat-square)    
![Kexts](https://img.shields.io/badge/Kexts-2025.03_Latest-4BC51D?style=flat-square)  

---
## 📌 Project Overview
OpenCore EFI configuration solution designed for **FEVM-FN60G (Intel 13/14th generation + AMD RX 6600M)**, supports macOS 15.4 system, and provides the following core functions:    
- CPU frequency conversion acceleration (iMacPro1,1 model performance increased by 30%)    
- Graphics card HIDPI support and hardware decoding acceleration    
- Dual system boot (Windows/Linux)
- Complete network and multimedia functions (AirDrop/Continuity/iCloud family bucket)

---

## 📥 Download and update
- **Latest version**: [Click to download](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/releases)  
- **Update log**:
- ✅ OpenCore 1.0.5 MOD version adaptation  
- ✅ All Kext drivers updated to the latest version
- ✅ Add `hfsplus.efi` to support USB installation
- ✅ AMD Radeon Pro W6600M graphics card customization optimization  
- ✅ Black Fruit Soldier USB driver integration
- ✅ IOSkywalkFamily.kext Updated to 1.2.0 (compatible with Sonoma/Sequoia)  

---

## ⚙️ Hardware Configuration
| Components | Model | Description |
|---------------|-------------------------------|----------------------------------------------------------------------|
| **CPU** | Intel® Core™ i5-13600T (13th Gen) | Supports 12th-14th generation desktop processors, up to 100W performance release |
| **Graphics** | AMD Radeon RX 6600M | Black Apple customized version, supports HDMI/DP output and H.264/HEVC hardware decoding acceleration |
| **Storage** | KIOXIA EXCERIA PRO/SE SSD | Dual NVMe slots, up to 4TB capacity, turn on TRIM to optimize performance |
| **Memory** | DDR5 5600MHz | Supports single-sided Hynix chip overclocking, provides OverClock option   |
| **Network card** | Realtek® RTL8125B Gigabit LAN | High-speed and stable wired network |
| **Wireless network card** | BCM94352Z (BT4.2) | Supports Wi-Fi 6E/Bluetooth 5.3 |

---

## 🛠️ BIOS setup guide
1. **Basic configuration**:
- Turn off Secure Boot and CFG Lock
- Set memory frequency to **Intel standard mode**
- Adjust AC/DC Loadline value to `110/110` to improve stability  

2. **BIOS download**:
[Click to get the latest BIOS](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/releases/tag/BIOS)

---

## 📸 Function test verification
![System Overview](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/raw/main/%E7%B3%BB%E7%BB%9F%E6%8A%A5%E5%91%8A.png)
![OpenCore Theme](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/raw/main/OC%E4%B8%BB%E9%A2%98.jpeg)

### Core Function Status
| Functional Module | Status | Description |
|----------------|------|----------------------------------------------------------------------|
| CPU Frequency Conversion | ✅ | Working Normally, iMacPro1,1 Model Performance Improved by 30% |
| Graphics Card Decoding | ✅ | H.264/HEVC Hardware Acceleration Normal, Independent Display AAPL Parameters Optimized |
| USB 3.0/2.0 | ✅ | Full port customization, compatible with 10Gbps interface |
| Sleep wakeup | ✅ | macOS sleep and wakeup functions are normal |
| Network function | ✅ | Wired/wireless network, AirDrop, HandOff are all normal |
| Multimedia | ✅ | 3.5mm sound output, system audio are normal |

---

---

## 📝 Advanced configuration
1. **Verbose mode**:
- Modify `config.plist` → `NVRAM → Add → 7C436110-AB2A-4BBB-A880-FE41995C9F82` → `boot-args: -v`
2. **Boot policy**:
- `ScanPolicy=0` supports Windows/Linux booting

---

## 🙏 Acknowledgements
The realization of this project is inseparable from the following open source projects and technical support:
- [OpenCore Legacy Patcher](https://github.com/dortania/OpenCore-Legacy-Patcher) - Broadcom NIC driver support
- [daliansky/FEVM-FN60G-Hackintosh](https://github.com/daliansky/FEVM-FN60G-Hackintosh) - EFI configuration reference
- [Xmingbai/FEVM-FN60G-Hackintosh](https://github.com/Xmingbai/FEVM-FN60G-Hackintosh) - Hardware compatibility solution
- [Black Fruit Little Soldier Blog](https://blog.daliansky.net/) - Installation tutorial and troubleshooting
