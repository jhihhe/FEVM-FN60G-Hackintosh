# 上游与许可

第一方配置整理、文档和脚本维护：@Jhih he。原项目涉及的 dailiansky、Xmingbai 及各上游作者署名保留；这不是从零编写的引导器或驱动。

- [OpenCore MOD / BTWISE](https://github.com/BTwise/OpenCorePkg)，基于 [Acidanthera OpenCorePkg](https://github.com/acidanthera/OpenCorePkg)。本包保留现有可用 MOD 二进制，并未自行构建。
- [SimpleBCM](https://github.com/laobamac/SimpleBCM) 及 [SimpleHDA](https://github.com/laobamac/SimpleHDA)：laobamac，保留其版权和第三方声明。详见 `Licenses/` 中随发行包提供的原始 NOTICE 与许可证。两者包含 Apple 驱动组件，Apple 的专有条款仍然适用。
- [Lilu](https://github.com/acidanthera/Lilu)、[VirtualSMC](https://github.com/acidanthera/VirtualSMC)、[WhateverGreen](https://github.com/acidanthera/WhateverGreen)、[AppleALC](https://github.com/acidanthera/AppleALC)、[NVMeFix](https://github.com/acidanthera/NVMeFix)、[RestrictEvents](https://github.com/acidanthera/RestrictEvents)、[HibernationFixup](https://github.com/acidanthera/HibernationFixup)、[BrcmPatchRAM / BlueToolFixup](https://github.com/acidanthera/BrcmPatchRAM)：各上游作者。
- [AMFIPass](https://github.com/dortania/OpenCore-Legacy-Patcher)、[FeatureUnlock](https://github.com/acidanthera/FeatureUnlock)、[LucyRTL8125Ethernet](https://github.com/Mieze/LucyRTL8125Ethernet)、[RadeonSensor / SMCRadeonGPU](https://github.com/aluveitie/RadeonSensor)：各上游作者；保留包内标识及原版权。
- USBPortsMap 是随现有配置保留的本机定制，包内标识为 cn.laobamac.USBPortsMap；不要直接当成其他机器的通用映射。

本仓库的 MIT 文件仅覆盖第一方配置、文档和脚本，不为任何第三方程序重新授权，也不表示 Apple 组件开放源代码。分发和使用第三方部分时请同时遵守对应上游及 Apple 条款。
