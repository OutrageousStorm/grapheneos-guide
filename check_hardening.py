#!/usr/bin/env python3
"""Check if device has GrapheneOS hardening features enabled"""
import subprocess

def adb(cmd):
    r = subprocess.run(['adb', 'shell'] + cmd.split(), capture_output=True, text=True)
    return r.stdout.strip()

checks = {
    'SELinux enforcing': ('getenforce', ['Enforcing']),
    'exec-shield': ('cat /proc/sys/kernel/exec-shield', ['1']),
    'ASLR enabled': ('cat /proc/sys/kernel/randomize_va_space', ['2']),
    'dmesg restrictions': ('cat /proc/sys/kernel/dmesg_restrict', ['1']),
}

print("GrapheneOS Security Checks:")
for name, (cmd, expected) in checks.items():
    result = adb(cmd)
    status = '✓' if any(e in result for e in expected) else '✗'
    print(f"  {status} {name}: {result}")
