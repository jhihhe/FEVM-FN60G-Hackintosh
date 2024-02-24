# FEVM-FN60G-Hackintosh-EFI_OpenCore-macOS

# [Chinese](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/README.md)｜[English](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/README-EN.md)

# Download click [releases](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/releases)

# Please generate the Board Serial Number, serial number, and SmUUID by yourself, and modify the "custom UUID" in the SysPrameter system parameters accordingly, and the MLB and ROM in the RtVariables variable settings.

## Update log:
- [x] 1. Update oc version to official version 0.9.9
- [x] 2. Update all kext kernel extension drivers to the latest version
- [x] 3. Add hfsplus.efi to support USB disk installation

![System Report](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/%E7%B3%BB%E7%BB%9F%E6%8A%A5%E5%91%8A.png)

## Configuration
1. Model: FEVM-FN60G (BIOS Version FN60G-BIOS (B11HF170)
   
    1. Fix Windows compatibility of Broadcom network card.
   
    2. Fixed compatibility issues with some 14th generation processors.
   
    3. Fixed some memory module compatibility issues and supports 5600 frequency memory
   
    Please click here [Download BIOS](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/releases/tag/BIOS)

1. CPU:13th Generation Intel® Core™ i5-13600T Processors
1. Graphics card: AMD Radeon RX 6600M
1. Onboard network card: Realtek® RTL8125B Gigabit LAN Controller
1. WiFi/Bluetooth: BCM94352Z (BT4.2)
1. Solid state drive: KIOXIA-EXCERIA G2 SSD RD20-2TB (TRIM enabled)

### BIOS settings
1. Turn off secure boot &cfg lock

# **Applicable operating system versions: support macOS Catalina/Big Sur/macOS Monterey 12.7.3/macOS Ventura 13.6.5**
1. OpenCore version: 0.9.9
![Topic](https://tva2.sinaimg.cn/large/cec1774cly8h1g75kzm0vj21hc0u0gmt.jpg)
- [x] 1. CPU frequency conversion: working fine, model setting imacpro1,1 increases performance by 30% compared to macpro7,1
![CPU](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/CPU%E6%B5%8B%E8%AF%95.png)
![CPU1](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/CPU.png)
![CPU2](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/CPU%E7%9B%91%E6%B5%8B.png)
![CPU3](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/CPU%E7%9B%91%E6%B5%8B1.png)
- [x] 2. Graphics card: working fine, turns on HIDPI, turns on H.264&HEVC hardware decoding acceleration, RX6600M: works normally, adds independent graphics AAPL, slot-name parameters
![Graphics card](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/%E6%98%BE%E5%8D%A1.png)
![Graphics card 1](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/GPU%E6%B5%8B%E8%AF%951.png)
![Hardware decoding](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/%E7%A1%AC%E8%A7%A3%E7%A0%81.png)
- [x] 3. 3.5mm sound: working fine
- [x] 4. USB: working fine
![USB](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/USB.png)
- [x] 5. Wired network card: working fine
![Wired network card](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/%E6%9C%89%E7%BA%BF%E7%BD%91%E5%8D%A1.png)
- [x] 6. Wireless network card: working fine

![Wi-Fi](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/%E6%97%A0%E7%BA%BF%E7%BD%91.png)
- [x] 7. Sleep wake-up: works fine
- [x] 8. Turn off and on: working fine
- [x] 9. iCloud & App Store & iMessage & FaceTime: working fine
- [x] 10. AirDrop & HandOff & Continuity: working fine
![Bluetooth](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/%E8%93%9D%E7%89%99.png)

### Tips:

1. This config defaults to no verbose mode. To enable verbose mode, config.plist needs to modify the following item: NVRAM-Add-7C436110-AB2A-4BBB-A880-FE41995C9F82-boot-args, add -v.
1. The config startup disk policy ScanPolicy value is set to 0. Can boot Windows or Other OS (Linux, Unix). If you need to specify the search partition type, please refer to the OC configuration manual.

# Acknowledgments
# Refer to the configuration files of daliansky boss and Xmingbai boss. If you need other versions, you can click the boss link to view
# https://github.com/daliansky/FEVM-FN60G-Hackintosh

# https://github.com/Xmingbai/FEVM-FN60G-Hackintosh
