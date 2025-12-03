# Pico Connector  
### A Reliable Lutron Pico → Home Assistant Light Controller  
[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://hacs.xyz)  
![GitHub release (latest by date)](https://img.shields.io/github/v/release/smartqasa/pico-connector)  
![GitHub License](https://img.shields.io/github/license/smartqasa/pico-connector)  

---

## 🌟 Overview

**Pico Connector** is a lightweight, reliable, non-polling Home Assistant integration that turns **Lutron Caseta Pico remotes** into powerful light controllers.

It listens directly to `lutron_caseta_button_event` and applies intuitive dimming behavior:

### ✔ Paddle Pico Behavior  
- **Short Press ON** → Sets configurable brightness (default: 100%)  
- **Short Press OFF** → Turns off  
- **Long Press ON** → Ramps up brightness  
- **Long Press OFF** → Ramps down brightness  
- Automatically stops when max/min brightness is reached  

### ✔ 5-Button Pico Behavior (Pico3RaiseLower & true 5-button models)  
- **ON** → immediate brightness_on_pct  
- **OFF** → immediate off  
- **STOP** → halts ramping  
- **RAISE / LOWER** → ramps immediately (no hold timer)  

This integration requires **no polling**, uses **async**, and is extremely responsive.

---

## 🚀 Installation

### 📦 HACS (Recommended)

1. Go to **HACS → Integrations**
2. Click **⋮ → Custom Repositories**
3. Add repository URL:

