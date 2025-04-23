# BIOS & Driver Update Cadence (UK Support) – 2024/25

| System (Support Link) | Cadence | Updates (BIOS / Critical Drivers 12 mo) | Last Firmware Update | Remarks (Security & User Insights) |
|-----------------------|---------|--------------------------------------|----------------------|----------------------------------|
| Minisforum UM890 Pro (Ryzen 9 8945HS) | ❌ Dormant | 0 – No BIOS updates (only initial drivers) | No BIOS posted (as of Apr 2025) | No BIOS patch for AMD's high-severity "SinkClose" firmware flaw (CVE-2023-31315). Uses test Secure Boot keys, raising security concerns. Users report slow or absent support and critical BIOS updates. |
| Beelink GTR7 Pro (Ryzen 9 7940HS) | ⚠️ Moderate | 1 – One BIOS update (Dec 2023) | 19 Dec 2023 | One BIOS (v37→v38) released to fix stability. No further BIOS in 2024/25 – SinkClose vulnerability likely still open. UEFI platform key was left in "TEST" mode; community urged Beelink to update to proper certs. |
| ASUS NUC 14 Pro Kit (Core Ultra 7 165H) | ✅ Active | 5 – ≈5 BIOS releases (since early 2024) | 08 Jan 2025 | Frequent BIOS updates (v0038 → v0047) delivered for Meteor Lake NUC. Last firmware Jan 2025; patches Intel CPU microcode bugs and voltage issues. No known Intel SA advisories left unpatched. |
| HP Elite Mini 800 G9/G10 (Core i7-14700T) | HP Support (UK) | ⚠️ Moderate | 2–3 – BIOS updates via HP SoftPaq/UUP | ~Q4 2024 (via Windows Update) | Business mini-PC gets periodic BIOS/UEFI capsule updates through HP's "Seamless Update" service. Last known firmware late 2024 (Intel Platform Update 2024 IPUs). No user-accessible BIOS posted on support site (updates pushed via Windows/UUP). No unpatched Intel SAs reported. |
| Lenovo ThinkCentre M90q Gen 5 Tiny (Core Ultra 7) | Lenovo Support (UK) | ⚠️ Moderate | 1–2 – ≈1 BIOS + 1 driver | 2024 (BIOS vT0E*) | Latest BIOS (e.g. vT0EA) released for 13th/14th Gen Tiny PCs. Likely includes fixes for UEFI vulnerabilities. Moderate cadence: initial firmware plus occasional driver/firmware updates via Lenovo Vantage. No known open security bulletins. |

---

## Mini-PCs

| System (Support Link) | Cadence | Updates (BIOS / Critical Drivers 12 mo) | Last Firmware Update | Remarks (Security & User Insights) |
|-----------------------|---------|--------------------------------------|----------------------|----------------------------------|
| Minisforum UM890 Pro (Ryzen 9 8945HS) | ❌ Dormant | 0 – No BIOS updates (only initial drivers) | No BIOS posted (as of Apr 2025) | No BIOS patch for AMD's high-severity "SinkClose" firmware flaw (CVE-2023-31315). Uses test Secure Boot keys, raising security concerns. Users report slow or absent support and critical BIOS updates. |
| Beelink GTR7 Pro (Ryzen 9 7940HS) | ⚠️ Moderate | 1 – One BIOS update (Dec 2023) | 19 Dec 2023 | One BIOS (v37→v38) released to fix stability. No further BIOS in 2024/25 – SinkClose vulnerability likely still open. UEFI platform key was left in "TEST" mode; community urged Beelink to update to proper certs. |
| ASUS NUC 14 Pro Kit (Core Ultra 7 165H) | ✅ Active | 5 – ≈5 BIOS releases (since early 2024) | 08 Jan 2025 | Frequent BIOS updates (v0038 → v0047) delivered for Meteor Lake NUC. Last firmware Jan 2025; patches Intel CPU microcode bugs and voltage issues. No known Intel SA advisories left unpatched. |
| HP Elite Mini 800 G9/G10 (Core i7-14700T) | HP Support (UK) | ⚠️ Moderate | 2–3 – BIOS updates via HP SoftPaq/UUP | ~Q4 2024 (via Windows Update) | Business mini-PC gets periodic BIOS/UEFI capsule updates through HP's "Seamless Update" service. Last known firmware late 2024 (Intel Platform Update 2024 IPUs). No user-accessible BIOS posted on support site (updates pushed via Windows/UUP). No unpatched Intel SAs reported. |
| Lenovo ThinkCentre M90q Gen 5 Tiny (Core Ultra 7) | Lenovo Support (UK) | ⚠️ Moderate | 1–2 – ≈1 BIOS + 1 driver | 2024 (BIOS vT0E*) | Latest BIOS (e.g. vT0EA) released for 13th/14th Gen Tiny PCs. Likely includes fixes for UEFI vulnerabilities. Moderate cadence: initial firmware plus occasional driver/firmware updates via Lenovo Vantage. No known open security bulletins. |

---

## Laptops

| System (Support Link) | Cadence | Updates (BIOS / Critical Drivers 12 mo) | Last Firmware Update | Remarks (Security & User Insights) |
|-----------------------|---------|--------------------------------------|----------------------|----------------------------------|
| Dell XPS 14 (9440) (Core Ultra 7 155H) | ✅ Active | 5+ – multiple BIOS & driver updates | 19 Jan 2025 (BIOS 1.11.0) | Very active support – ≈11 BIOS revisions in ≈12 months (v1.0 → 1.11) addressing stability and Intel CPU fixes. Last firmware Jan 2025. No known unpatched CVEs; Dell promptly issued BIOS updates for Intel's voltage flaw late 2024. |
| Lenovo ThinkPad X1 Carbon Gen 13 (Core Ultra 7 258V) | Lenovo Support (UK) | ⚠️ Moderate | 1–2 – BIOS + some drivers | 2025 (BIOS 1.xx) | New 2025 model – initial BIOS and a minor update via Lenovo System Update. Likely up-to-date on Intel firmware advisories. Early adopters noted TPM attestation issues needing firmware tweaks; Lenovo is releasing fixes. Overall support is on track though update count still low. |
| HP EliteBook Ultra 14 G1 (Core Ultra 7 155H) | HP Support (UK) | ⚠️ Moderate | 1–3 – few BIOS/driver updates | 2024 (BIOS 0.x via HPIA) | First-gen "Ultra" EliteBook – periodic HP BIOS updates through Support Assistant. Likely received firmware for Intel IPU 2024.3 (Wi-Fi & CPU fixes). No outstanding HP security bulletin on this model. Users mainly concerned with driver setup; no major complaints on BIOS cadence. |
| ASUS ROG Zephyrus G14 (2024 GA403) (Ryzen AI 9 HX370) | ASUS Support (UK) | ⚠️ Moderate | 1 – one BIOS update | Jul 2024 (BIOS v306) | Moderate support: one BIOS (v306, Jul 2024) via Windows Update, which surprised users when it auto-flashed. No BIOS since; AMD "SinkClose" SMM exploit fix pending. Users waiting on new BIOS to resolve power-management quirks. |
| Razer Blade 14 (2024) (Ryzen 9 8945HS) | Razer Support (UK) | ⚠️ Moderate | 03 Jul 2024 (BIOS v1.06) | Received one BIOS (v1.06) mid-2024 to improve ACPI (audio/Wi-Fi). No further BIOS; Ryzen PSP patches may be outstanding. Razer provides easy BIOS tools, but Linux users note need for newer firmware for stability. |
| Lenovo ThinkPad X1 Extreme Gen 4 (Ryzen 9 7940HS) | Lenovo Support (UK) | ⚠️ Moderate | 1–2 – BIOS + some drivers | 2024 (BIOS vT0E*) | Latest BIOS (e.g. vT0EA) released for 13th/14th Gen Tiny PCs. Likely includes fixes for UEFI vulnerabilities. Moderate cadence: initial firmware plus occasional driver/firmware updates via Lenovo Vantage. No known open security bulletins. |

🔗 Previous: [Why Specs Matter](rationale.md) | Back to [Index](../README.md) | Next: [CPU/GPU Roadmap](cpu_gpu_roadmap.md)
