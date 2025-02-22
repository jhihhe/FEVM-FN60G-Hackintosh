# FEVM-FN60G Hackintosh EFI 配置指南  
[![OpenCore 1.0.3 MOD](https://img.shields.io/badge/OpenCore-1.0.3_MOD-blue)](https://github.com/acidanthera/OpenCorePkg)  
[![macOS Sequoia](https://img.shields.io/badge/macOS-Sequoia_15.1-red)](https://www.apple.com/macos)  
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
| 组件          | 型号                          | 说明                                                                 |  
|---------------|-------------------------------|----------------------------------------------------------------------|  
| **CPU**       | Intel® Core™ i5-13600T (13th Gen) | 12-14代桌面处理器自由更换，最高100W性能释放[2,4](@ref)|  
| **显卡**      | AMD Radeon RX 6600M           | 黑苹果专用定制版本，支持HDMI/DP输出及硬件解码加速[1,4](@ref)|  
| **存储**      | KIOXIA EXCERIA PRO/SE SSD     | 双NVMe插槽，最高支持4TB容量，开启TRIM优化性能[2,4](@ref)|  
| **内存**      | DDR5 5600MHz                  | 支持单面海力士颗粒超频，提供OverClock选项[1,4](@ref)|  

---

## 📌 更新日志 (2025.02.22)  
1. 全面适配 OpenCore 1.0.3 MOD 版  
2. 更新所有 Kext 驱动至最新版本  
3. 新增 hfsplus.efi 支持 U 盘安装  
4. 优化 AMD Radeon Pro W6600 显卡配置  
5. 集成黑果小兵最新 USB 定制驱动  
6. 更新 IOSkywalkFamily.kext 至 1.2.0 版本  

---

## ⚠️ 注意事项  
1. **必填参数**：需自行生成并修改 `Board Serial Number`、`SmUUID`、`SysParameter` 中的 "自定义UUID" 等关键配置[1](@ref)。  
2. **BIOS 设置**：  
  - 关闭 Secure Boot & CFG Lock  
  - 内存频率设为 **Intel 规范模式**  
  - AC/DC Loadline 数值设为 `110/110` 提升稳定性[1,4](@ref)。  

---

## 📸 系统实测  
![系统概览](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/raw/main/%E7%B3%BB%E7%BB%9F%E6%8A%A5%E5%91%8A.png)  
![OpenCore 主题](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/raw/main/OC%E4%B8%BB%E9%A2%98.jpeg)  

---

## 📝 功能状态  
| 功能模块       | 状态 | 说明                                                                 |  
|----------------|------|----------------------------------------------------------------------|  
| CPU 变频       | ✅    | 支持 `imacpro1,1` 机型性能提升 30%[1](@ref)|  
| 显卡解码       | ✅    | 支持 H.264/HEVC 硬件加速，独显 AAPL 参数优化[1,4](@ref)|  
| USB 3.0/2.0    | ✅    | 全端口定制，兼容 10Gbps 接口[2,4](@ref)|  
| 睡眠唤醒       | ✅    | 支持 macOS 休眠与唤醒[1](@ref)|  

---

## 📝 高级配置  
1. **Verbose 模式**：  
  - 修改 `config.plist` → `NVRAM → Add → 7C436110-AB2A-4BBB-A880-FE41995C9F82` → `boot-args: -v`[1](@ref)。  
2. **启动策略**：  
  - `ScanPolicy=0` 支持 Windows/Linux 引导[1](@ref)。  

---

## 🙏 鸣谢  
- 参考了 [daliansky](https://github.com/daliansky/FEVM-FN60G-Hackintosh) 和 [Xmingbai](https://github.com/Xmingbai/FEVM-FN60G-Hackintosh) 的配置方案。  
- 使用工具：[Quine](https://quine.sh) 生成小卡片，[readme.so](https://readme.so) 优化布局。
