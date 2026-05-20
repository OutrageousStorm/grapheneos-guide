#!/usr/bin/env python3
"""Verify GrapheneOS security hardening is active"""
import subprocess, re

def adb(cmd):
    r = subprocess.run(['adb', 'shell'] + cmd.split(), capture_output=True, text=True)
    return r.stdout.strip()

checks = [
    ("SELinux enforcing", "getenforce", "Enforcing"),
    ("MTE enabled", "cat /proc/cpuinfo | grep mte", "mte"),
    ("Exploit mitigations", "cat /proc/sys/kernel/unprivileged_userns_clone", "0"),
    ("SMACK LSM", "cat /proc/lsm", "smack"),
]

for label, cmd, expect in checks:
    out = adb(cmd)
    ok = expect.lower() in out.lower()
    print(f"{'✅' if ok else '❌'} {label}: {out[:40]}")
