#!/usr/bin/env python3
"""Validate the shipped EFI structure. Author: @Jhih he."""
import argparse
import plistlib
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--personalized', action='store_true')
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
oc = root / 'EFI/OC'
configs = list(oc.glob('config*.plist'))
assert len(configs) == 1, 'Expected one config'
c = plistlib.loads(configs[0].read_bytes())
assert (root / 'EFI/BOOT/BOOTx64.efi').is_file()
ids = set()
for item in c['Kernel']['Add']:
    if not item['Enabled']:
        continue
    bundle = oc / 'Kexts' / item['BundlePath']
    info = plistlib.loads((bundle / item['PlistPath']).read_bytes())
    identifier = info['CFBundleIdentifier']
    assert identifier not in ids, 'Duplicate kext: ' + identifier
    ids.add(identifier)
    if item['ExecutablePath']:
        assert (bundle / item['ExecutablePath']).is_file(), item['BundlePath']
    assert not any(x.lower() in item['BundlePath'].lower() for x in ['WhateverXe', 'PcmMsrDriver', 'AMFIPassMod', 'IOSkywalkFamily', 'IO80211FamilyLegacy'])
for section, directory in [('ACPI', 'ACPI'), ('UEFI', 'Drivers')]:
    for item in c[section]['Add' if section == 'ACPI' else 'Drivers']:
        if item['Enabled']:
            assert (oc / directory / item['Path']).is_file(), item['Path']
generic = c['PlatformInfo']['Generic']
if args.personalized:
    import uuid
    assert all(generic[k] for k in ['MLB', 'SystemSerialNumber', 'SystemUUID'])
    assert uuid.UUID(generic['SystemUUID']).int != 0
    assert isinstance(generic['ROM'], bytes) and len(generic['ROM']) == 6 and any(generic['ROM'])
else:
    assert all(generic[k] == '' for k in ['MLB', 'SystemSerialNumber', 'SystemUUID'])
    assert generic['ROM'] == bytes(6)
assert {p.name for p in (root / 'EFI').iterdir()} == {'BOOT', 'OC'}
for p in (root / 'EFI').rglob('*'):
    assert p.name not in ['.DS_Store', 'nvram.plist'] and not p.name.startswith(('._', 'opencore-')), str(p)
print('PASS: plist, active file references, unique kexts, excluded experiments and identity fields')
