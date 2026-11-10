# FEVM FN60G Hackintosh

[中文说明](README.md) · [Latest release](https://github.com/jhihhe/FEVM-FN60G-Hackintosh/releases/latest)

A single daily-use EFI for the FEVM FN60G: RX 6600M handles display and graphics acceleration; SimpleBCM handles Wi-Fi; SimpleHDA and AppleALC handle audio. UHD 770 / WhateverXe experiments are no longer included.

On November 10, 2026, the owner reported that the daily EFI passed a full regression and works normally on their machine. The public package has additional identity sanitization and removal of a nonworking monitoring helper. It passed static checks but has not been boot-tested again after those packaging changes.

## Reference machine

- Intel Core i5-13600T; AMD RX 6600M (the injected W6600 name is cosmetic).
- Broadcom PCI 14e4:43a0; Realtek RTL8125; machine-specific USB mapping.
- macOS 26.7.1, build 25G313; SMBIOS MacPro7,1.
- Existing working OpenCore MOD (BTWISE). Its embedded version string does not identify a numerical version.

The GPU properties and power table are specific to this working profile. Compatibility with other CPUs, FN60G revisions, wireless cards or GPUs is not implied.

## Installation and rollback

1. Back up the current EFI and keep a bootable recovery USB.
2. Generate your own identity and fill `SystemSerialNumber`, `MLB`, `SystemUUID` and `ROM` in `EFI/OC/config.plist → PlatformInfo → Generic`. The public template has empty identity strings and a zero ROM. Keep MacPro7,1 and do not sign into Apple services with placeholders or someone else's identity.
3. Test from USB first. On the internal ESP, preserve your own Windows `Microsoft` folder; this release only supplies BOOT and OC.
4. With Python 3, run `python3 tools/verify_efi.py`; after personalization use `--personalized`. This checks structure, not Apple service eligibility.
5. Check your audio, networking, display, USB, sleep/wake and daily apps before adopting it.

This setup loads audio and Wi-Fi support from EFI. If old OCLP Wi-Fi / AppleHDA root patches are still installed, back up the system and inspect OCLP's actual patch state before reverting them. OCLP may revert the whole patch set: plan recovery for any other required patches first. Keep your previous OCLP and an offline networking recovery option. Already migrated systems do not need another revert.

Audio uses `alcid=98`. Graphics retain WhateverGreen and `agdpmod=pikera -wegnoigpu`. No WhateverXe or Intel TGL system drivers are supplied. Existing SIP settings are preserved rather than hardened for this release.

For rollback, boot the recovery USB and restore your own EFI backup. Reinstall the previous root patches if the old configuration requires them; restoring EFI alone does not restore the system volume. Any previously installed WhateverXe system drivers need the original installer's uninstall procedure.

[Components](docs/COMPONENTS.md) · [Privacy](docs/PRIVACY.md) · [Changes](CHANGELOG.md) · [Third-party terms](THIRD_PARTY.md)

Maintained by **@Jhih he**. Thanks to dailiansky, Xmingbai and the upstream authors. The first-party configuration, documentation and helper scripts are MIT licensed; bundled third-party binaries and Apple components keep their own terms.
