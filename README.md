# FEVM FN60G Hackintosh

[English](README-EN.md) · [下载最新发行版](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/releases/latest)

这是我自己在用的 FN60G 日用 EFI。现在回到一份配置：**RX 6600M 负责画面输出和显卡加速，SimpleBCM 管无线网卡，SimpleHDA 配合 AppleALC 管声音。** 不再折腾 UHD 770，也不再提供核显测试配置。

2026-11-10，机主反馈这份日用 EFI 已完成完整回归，可以正常使用。这个结论针对下面这台机器；公开包额外做了脱敏和无效监控驱动清理，发布前通过静态检查，尚未用公开包重新启动验证。

## 这次用的机器

| 项目 | 配置 |
| --- | --- |
| 机器 | FEVM FN60G |
| CPU | Intel Core i5-13600T |
| 显卡 | AMD Radeon RX 6600M，沿用可用的 W6600 名称注入 |
| 无线 | Broadcom，PCI ID 14e4:43a0 |
| 有线 | Realtek RTL8125 |
| 系统 | macOS 26.7.1，构建号 25G313 |
| SMBIOS | MacPro7,1 |
| 引导 | OpenCore MOD（BTWISE），保留现有可用二进制；版本字符串未标明具体版本号 |

这份配置含本机的 USB 定制和 6600M 属性、功耗表。别把它当成所有 FN60G、所有 12–14 代 CPU 或所有 AMD 显卡的通用包。系统里的 W6600 名称是注入显示名，实际硬件仍是 6600M。

## 怎么用

1. 先备份现有 EFI，准备一个能启动的备用 U 盘。下载发行版 ZIP，解压后使用其中的 `EFI` 文件夹。
2. **先填自己的机器信息。** 在 `EFI/OC/config.plist → PlatformInfo → Generic` 中填写自己生成的 `SystemSerialNumber`、`MLB`、`SystemUUID` 和 `ROM`。公开包前三项为空，ROM 为六字节零；不要直接拿这个模板登录 Apple 服务，也不要照抄别人的四码。
3. 保持 `MacPro7,1` 机型，先从 U 盘试启动，再替换硬盘 ESP 里的 EFI。已有 Windows 的机器只更新 `BOOT` 和 `OC`，保留自己的 `Microsoft` 目录。
4. 有 Python 3 时可运行 `python3 tools/verify_efi.py` 检查文件引用。填好四码后运行 `python3 tools/verify_efi.py --personalized`；脚本只校验结构，不验证 Apple 服务资格。
5. 第一次启动后自行检查声音、无线、有线、显示输出、USB、睡眠唤醒和常用应用，再决定是否长期使用。

## 从 OCLP 根补丁迁移

当前声卡和无线方案从 EFI 加载，不需要继续保留对应的 OCLP Wi-Fi / AppleHDA 根补丁。已经正常迁移的机器不用重复操作。

如果系统还装着旧补丁，先备份系统和 EFI，保留原来的 OCLP 版本与恢复网络的办法；用 OCLP 查看实际补丁状态，再撤销旧的声卡、无线根补丁并按其提示重启。OCLP 的撤销可能影响整组根补丁：**还有其他必须依赖的补丁时，先确认其恢复方案**，不要把“撤销全部”当成只卸载声卡网卡。随后切换本 EFI 测试，避免新旧两套方案叠加。

声音沿用 `alcid=98`。显卡保留 WhateverGreen 与 `agdpmod=pikera -wegnoigpu`，不加载 WhateverXe，也不附带 Intel TGL 系统驱动。SIP 沿用原日用配置，没有在本次公开化时提高安全设置；不要把此包理解成默认安全策略。

## 出问题怎么退

从备用 U 盘启动，恢复你自己备份的整份 EFI。若迁移前依赖 OCLP 根补丁，还要用原来的 OCLP 恢复对应系统补丁；仅换回 EFI 不会自动还原系统卷。如果此前装过 WhateverXe 系统驱动，请按其原安装包的卸载说明处理，单独删除 EFI 里的 kext 不等于卸载系统驱动。

## 版本与来源

[更新记录](CHANGELOG.md) · [组件清单](docs/COMPONENTS.md) · [隐私说明](docs/PRIVACY.md) · [上游与许可](THIRD_PARTY.md)

维护：**@Jhih he**。保留原项目对 dailiansky、Xmingbai 及各驱动作者的感谢。仓库开放的是配置、文档和辅助脚本；第三方二进制和其中的 Apple 组件分别遵守原作者及 Apple 的条款，不会因为放进此仓库就变成 MIT 许可。
