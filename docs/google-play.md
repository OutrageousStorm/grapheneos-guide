# Sandboxed Google Play on GrapheneOS

GrapheneOS lets you run Google Play apps in a sandboxed environment — completely isolated from your main OS.

---

## What is Sandboxed Google Play?

Traditional Google Play Services has deep system access — it can track location, access contacts, run background, and communicate with Google servers.

GrapheneOS's implementation runs Google Play as a **regular app with no special privileges**. It can't access system APIs it shouldn't. It's isolated from your data.

---

## Install in a separate profile (recommended)

The safest setup: install Google Play in a **work profile** or **secondary user**, keeping your main profile Google-free.

1. Settings → System → Multiple users → Add user
2. Log into new user
3. Follow install steps below inside that user
4. Your main profile stays completely Google-free

---

## Install steps

1. Settings → Apps → tap ⋮ menu → **Install Google Play**
2. Follow prompts to install Google Play Services + Play Store
3. Open Play Store, sign in (optional — can use anonymously via Aurora Store)
4. Install your apps

---

## What works

✅ Most apps — banking, streaming, games  
✅ Google Maps, Gmail, YouTube  
✅ Push notifications (via Firebase Cloud Messaging in sandbox)  
✅ In-app purchases  
✅ Google Pay (on some devices — depends on Play Integrity)  

---

## What's limited

⚠️ Play Integrity / SafetyNet — some banking apps check this. GrapheneOS passes Basic integrity but not Device integrity on some versions. Check https://grapheneos.org/usage#banking-apps for the current status.

---

## Network isolation

With Sandboxed Play, you can revoke network access from individual Google Play components:

Settings → Apps → Google Play Services → Permissions → Network → Block

This stops telemetry while keeping core app functionality.

---

## Aurora Store (alternative)

Download Play Store apps **without a Google account**:

- Install Aurora Store from F-Droid
- Sign in anonymously
- Browse and install Play Store apps
- No Google account, no tracking

**Aurora Store:** https://auroraoss.com
