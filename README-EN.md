# FEVM-FN60G-Hackintosh-EFI_OpenCore-0.9.7 macOS

# [Chinese](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/blob/main/README.md)｜[English](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/ blob/main/README-EN.md)

# Download click [releases](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/releases)

# Please generate the Board Serial Number, serial number, and SmUUID by yourself, and modify the "custom UUID" in the SysPrameter system parameters accordingly, and the MLB and ROM in the RtVariables variable settings.

## Update log:
- [x] 1. Update oc version to official version 0.9.7
- [x] 2. Update all kext kernel extension drivers to the latest version
- [x] 3. Add hfsplus.efi to support USB disk installation

## Configuration
1. Model: FEVM-FN60G (BIOS Version FN60G-BIOS (B11HF170) Please click here [Download BIOS](https://www.lanzouh.com/iHkix1mxk6yh))
1. CPU:13th Generation Intel® Core™ i5-13600T Processors
1. Graphics card: AMD Radeon RX 6600M
1. Onboard network card: Realtek® RTL8125B Gigabit LAN Controller
1. WiFi/Bluetooth: BCM94352Z (BT4.2)
1. Solid state drive: Media name: KIOXIA-EXCERIA G2 SSD RD20-2TB (TRIM enabled)

### BIOS settings
1. Turn off secure boot &cfg lock

# **Applicable operating system versions: support macOS Catalina/Big Sur/macOS Monterey 12.7.3/macOS Ventura 13.6.4**
1. OpenCore version: 0.9.7
![Topic](https://tva2.sinaimg.cn/large/cec1774cly8h1g75kzm0vj21hc0u0gmt.jpg)
- [x] 1. CPU frequency conversion: working normally.
![CPU](https://pic.imgdb.cn/item/65c0b97e9f345e8d033304b3.png)
![CPU1](https://pic.imgdb.cn/item/65c0b97e9f345e8d0333053c.png)
- [x] 2. Graphics card: works normally, turns on HIDPI, turns on H.264&HEVC hardware decoding acceleration, RX6600M: works normally, adds independent display AAPL, slot-name parameters, model setting imacpro1,1 is 30% higher than macpro7,1 performance
![Graphics card](https://pic.imgdb.cn/item/65c0bddf9f345e8d033f3cee.png)
![Hardware decoding acceleration: H.264&HEVC decoding](https://pic.imgdb.cn/item/65c0be559f345e8d03407fce.png)
- [x] 3. 3.5mm sound: working fine
- [x] 4. USB: working fine
![USB](https://pic.imgdb.cn/item/65c0bee79f345e8d03421fdf.png)
- [x] 5. Wired network card: working normally, using RealtekRTL8111.kext
![Cable network card](https://pic.imgdb.cn/item/65c0b9789f345e8d0332f49a.png)
- [x] 6. Wireless network card: working normally
![Wi-Fi](https://pic.imgdb.cn/item/65c0b97d9f345e8d033301c5.png)
- [x] 7. Sleep wake-up: works fine
- [x] 8. Turn off and on: working normally
- [x] 9. iCloud & App Store & iMessage & FaceTime: Normal
- [x] 10. AirDrop & HandOff & Continuity: Normal.
![Bluetooth](https://pic.imgdb.cn/item/65c0b97d9f345e8d0333030a.png)

### Tips:

1. This config defaults to no verbose mode. To enable verbose mode, config.plist needs to modify the following item: NVRAM-Add-7C436110-AB2A-4BBB-A880-FE41995C9F82-boot-args, add -v.
1. The config startup disk policy ScanPolicy value is set to 0. Can boot Windows or Other OS (Linux, Unix). If you need to specify the search partition type, please refer to the OC configuration manual.

# Acknowledgments
# The configuration files of daliansky boss and Xmingbai boss are used. If you need other versions, please click the boss link to view
https://github.com/Xmingbai/FEVM-FN60G-Hackintosh
https://github.com/daliansky/FEVM-FN60G-Hackintosh
