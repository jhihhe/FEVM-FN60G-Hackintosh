# 组件清单

Kext 版本读取自本次包内 Info.plist，不表示上游最新版本。OpenCore 为 1.0.9 MOD（BTWISE），版本由机主确认。

| Kext | Version |
| --- | --- |
| Lilu.kext | 1.7.3 |
| VirtualSMC.kext | 1.3.9 |
| NVMeFix.kext | 1.1.4 |
| RestrictEvents.kext | 1.1.7 |
| AMFIPass.kext | 1.4.1 |
| USBPortsMap.kext | 1.0 |
| WhateverGreen.kext | 1.7.2 |
| AppleALC.kext | 1.9.9 |
| SimpleHDA.kext | 1.0.1 |
| SimpleBCM.kext | 1.2.0 |
| HibernationFixup.kext | 1.5.5 |
| SMCProcessor.kext | 1.3.9 |
| SMCSuperIO.kext | 1.3.9 |
| LucyRTL8125Ethernet.kext | 1.2.3 |
| RadeonSensor.kext | 0.3.3 |
| SMCRadeonGPU.kext | 0.3.3 |
| FeatureUnlock.kext | 1.1.9 |
| BlueToolFixup.kext | 2.7.3 |

仅一份 EFI/OC/config.plist。SimpleHDA 与 AppleALC 配合使用；SimpleBCM 自带的嵌入组件不另作独立旧无线驱动注入。
