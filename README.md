# 🛡️ GrapheneOS Guide

The most complete GrapheneOS setup reference — install, harden, and configure for daily use.

**Official site:** https://grapheneos.org  
**Subreddit:** https://reddit.com/r/GrapheneOS

---

## Why GrapheneOS?

GrapheneOS is a privacy-focused Android fork developed by Daniel Micay and contributors. It is the gold standard for mobile security:

- **Hardened memory allocator** — catches use-after-free, heap overflows
- **Verified boot with locked bootloader** — even after flashing
- **Per-app network/sensor/storage permissions** — beyond what stock Android offers
- **Sandboxed Google Play** — use Play Store apps in complete isolation
- **Automatic reboot** — configurable lock after inactivity
- **Exploit mitigations** — PAC, shadow call stack, CFI, RELRO, PIE by default

**Pixel-only.** GrapheneOS only supports Google Pixel devices.

---

## Supported devices (2026)

| Device | Codename | Status |
|--------|----------|--------|
| Pixel 6 | oriole | ✅ Supported |
| Pixel 6 Pro | raven | ✅ Supported |
| Pixel 6a | bluejay | ✅ Supported |
| Pixel 7 | panther | ✅ Supported |
| Pixel 7 Pro | cheetah | ✅ Supported |
| Pixel 7a | lynx | ✅ Supported |
| Pixel 8 | shiba | ✅ Supported |
| Pixel 8 Pro | husky | ✅ Supported |
| Pixel 8a | akita | ✅ Supported |
| Pixel 9 | tokay | ✅ Supported |
| Pixel 9 Pro | caiman | ✅ Supported |
| Pixel 9 Pro XL | komodo | ✅ Supported |
| Pixel 9 Pro Fold | comet | ✅ Supported |
| Pixel Fold | felix | ✅ Supported |
| Pixel Tablet | tangorpro | ✅ Supported |

---

## Installation

### Easiest: Web installer (recommended)

1. Use **Chrome or Chromium** on desktop
2. Go to https://grapheneos.org/install/web
3. Enable **OEM Unlocking** in Developer Options first
4. Follow the on-screen steps — it handles everything

### CLI install

```bash
# 1. Enable OEM Unlocking (Settings → Developer Options)
adb reboot bootloader
fastboot flashing unlock

# 2. Flash GrapheneOS
fastboot flash bootloader bootloader.img
fastboot reboot bootloader
fastboot flash radio radio.img
fastboot reboot bootloader
fastboot -w update image-<device>-<version>.zip

# 3. IMPORTANT: lock bootloader again
fastboot flashing lock
```

---

## Sections

- [Initial Setup](docs/initial-setup.md) — First boot configuration
- [Sandboxed Google Play](docs/google-play.md) — Using Google apps in isolation
- [App Recommendations](docs/apps.md) — Best apps for GrapheneOS
- [Hardening Tips](docs/hardening.md) — Advanced security configuration
- [Network Privacy](docs/network.md) — DNS, VPN, Tor on GrapheneOS

---

*See also: [custom-rom-notes](https://github.com/OutrageousStorm/custom-rom-notes)*
