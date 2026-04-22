**Luca Major¹, Károly Piláth²**  

¹ Svetits Catholic School, Hungary  
² ELTE Trefort Ágoston Practice Secondary School, Budapest, Hungary


# An Experimental Platform for Exploring Resonance, Nonlinear Dynamics, and Chaos in RLC Circuits

A compact, low-cost experimental system for studying linear, nonlinear, and chaotic oscillations.

<div align="center">
  <img src="images/panel1.jpg" width="650">
</div>

<p align="center">
  <i>Figure 1 – Chaotic RLC demonstration board</i>
</p>

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

## Operating Modes

| Mode | Configuration | Observed Behavior |
|------|---------------|------------------|
| Linear | SW2 OFF | Classical RLC oscillations |
| Nonlinear | SW2 ON | Distorted oscillations |
| Chaotic | SW2 ON + proper excitation | Chaotic dynamics |
---

## 📐 Hardware Files

All hardware design files are available in the repository:

- 📄 Schematic: [schematic.pdf](hardware/Schematic_chaos_RLC.pdf)
- 📄 Schematic EasyEda: [SCH_chaotic.json](hardware/SCH_chaotic.json)
- 📋 Bill of Materials: [BOM.md](hardware/BOM.md)
- 🧩 PCB Layout: [board.png](hardware/PCB/board.png)
- 🏭 Gerber Files: [gerber.zip](hardware/PCB/Gerber_chaotic_2025_0807.zip)
- 🔧 Assembly Guide: [assembly.md](hardware/ASSEMBLY.md)
# RLC Chaos Platform

This repository presents an educational and experimental framework for exploring
linear and nonlinear dynamics in RLC circuits using:

- interactive simulation (Falstad)
- numerical modelling (Python / Google Colab)
- real-world measurements (sound card-based acquisition)

---

## 🔬 Project overview

The system is based on a driven RLC circuit that can exhibit complex dynamics,
including nonlinear behaviour and phase-space structures.

Students can explore the same physical system through three complementary approaches:

1. **Interactive simulation** (Falstad)
2. **Numerical model** (Duffing-type equation)
3. **Real measurement** (audio interface)
---
## ⚡ Falstad simulation

This circuit can be explored using the Falstad Circuit Simulator.
1. Open https://falstad.com/circuit/
2. File → Import From Text
3. Paste the contents of:
   simulations/rlc_series_falstad.txt
   
simulations: [rlc_series_falstad.txt](simulations/rlc_series_falstad.txt)

screenshote: [rlc_series_falstad.png](simulations/rlc_series_falsta.png)

### Clab Features
Colab script: [duffing_rlc_colab.py](notebooks/duffing_rlc_colab.py)
Screenshat: [colab_chaotic.png](notebooks/colab_chaotic.png)
- Time-domain analysis: \( V_C(t) \)
- Phase-space trajectories: \( V_C \) vs \( I_L \)
- Poincaré section (periodic sampling)

---

## 📊 Physical interpretation

The model describes a driven nonlinear RLC system:

- \( x \) → capacitor voltage (dimensionless)
- \( y \) → inductor current (dimensionless)

The scaling to physical units is performed using:

- characteristic impedance:  
  \[
  \rho = \sqrt{\frac{L}{C}}
  \]

- voltage scaling based on diode threshold

This allows direct comparison with experimental measurements.

---





