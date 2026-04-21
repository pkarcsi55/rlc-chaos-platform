# An Experimental Platform for Exploring Resonance, Nonlinear Dynamics, and Chaos in RLC Circuits
A compact, low-cost, audio-based hardware platform for hands-on experiments in linear and nonlinear physics.  
The system allows students and researchers to explore resonance phenomena, nonlinear effects, and chaotic dynamics using a simple RLC circuit and a standard computer sound card.
---
## 🎯 Project Overview
This project presents a portable experimental platform designed for:
- Investigating **classical RLC circuits** (resonance, damping, phase shift)
- Exploring **nonlinear behavior** using diode-based elements
- Demonstrating **chaotic oscillations** in an intuitive, hands-on way
A key feature of the system is that it uses:
- a **mobile phone or PC audio signal** as excitation  
- a **sound card** as a measurement interface  
This makes the setup extremely accessible and reproducible in educational environments.
---
## ⚡ Key Features
- 🔊 Audio-based excitation (phone / PC signal generator)
- 📈 Direct measurement via sound card (Digital Audio Analyzer and Oscilloscope software, Audacity)
- 🔁 Switchable linear → nonlinear → chaotic behavior
- 🔋 Fully portable (Li-ion powered)
- 🧠 Supports both **experimental and simulation-based learning**
---
## 🧩 System Architecture
The circuit is composed of the following functional blocks:
### 1. Power Supply
- 14500 Li-ion battery (3.7 V)
- TPA4056 charging module
- DC-DC converter (adjustable output)
### 2. Signal Input
- 3.5 mm audio jack (AUDIO IN)
- Accepts sine or square wave excitation
### 3. Built-in RLC resonant circuit
- Inductor: 47 mH (≈52 Ω internal resistance)
- Capacitor: 560 nF
- 0-50 Ohm series resistance for damping control
### 4. Nonlinear Element
- Antiparallel diodes (1N4148)
- Switchable via **SW2 (Chaos ON)**
### 5. Measurement Stage
- TL064 quad operational amplifier
- Signal conditioning and buffering
- Dual output:
  - CH1 → capacitor voltage (Uc)
  - CH2 → current-related signal (Ic)
### 6. Output
- 3.5 mm audio jack (AUDIO OUT)
- Compatible with PC sound card input
---

## 🧪 Operating Modes

| Mode | Configuration | Observed Behavior |
|------|-------------|------------------|
| Linear | SW2 OFF | Classical RLC oscillations |
| Nonlinear | SW2 ON | Distorted oscillations |
| Chaotic | SW2 ON + proper excitation | Chaotic dynamics |

---

## 📐 Hardware Files

All hardware design files are available in the repository:

