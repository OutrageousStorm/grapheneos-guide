# GrapheneOS — Initial Setup

Steps to take after first boot.

---

## First boot checklist

### 1. Lock the bootloader
If you used the web installer, this was done automatically. If not:
```bash
fastboot flashing lock
```
GrapheneOS is one of the few ROMs that supports verified boot with a locked bootloader.

### 2. Set a strong PIN / password
Settings → Security → Screen lock. Use a 6+ digit PIN or alphanumeric password.

### 3. Configure Auto-Reboot
Settings → Security → Auto-reboot. Set to 8–24 hours. Device reboots if not unlocked within that window, forcing full disk decryption on next unlock.

### 4. Enable Duress PIN (optional)
Settings → Security → Duress password. Entering this PIN wipes the device — useful for border crossings.

### 5. Set up network privacy
Settings → Network & internet → Private DNS → set to `dns.quad9.net` or your preferred encrypted DNS.

### 6. Review app permissions
GrapheneOS adds extra permissions beyond stock:
- **Network** — per-app toggle to completely block internet
- **Sensors** — block accelerometer/gyroscope access
- **Nearby Wi-Fi networks** — separate from location

Revoke anything unnecessary.

### 7. Configure Storage Scopes
Instead of granting broad storage access, Storage Scopes lets apps only see specific files/folders they need.

Settings → Apps → [app] → Permissions → Storage → Configure Storage Scopes

---

## Recommended first apps

```
F-Droid          → https://f-droid.org (open source app store)
Vanadium         → built-in hardened browser (use this over Chrome)
Obtainium        → install apps directly from GitHub releases
Orbot            → Tor proxy for Android
Molly            → hardened Signal fork
```

---

## What NOT to do

- ❌ Don't install Play Store on your main profile — use a separate profile
- ❌ Don't grant "All files access" to any app that doesn't strictly need it
- ❌ Don't enable USB debugging permanently — only when needed
- ❌ Don't use SMS 2FA — prefer TOTP (Aegis authenticator)
