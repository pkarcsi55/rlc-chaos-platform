# 🔧 Assembly Guide

This guide describes how to assemble the Chaotic RLC demonstration board.

---

## 🧰 Required Tools

- Soldering iron (fine tip recommended)
- Solder wire (0.5–0.7 mm)
- Side cutters
- Multimeter (recommended)
- Optional: oscilloscope or sound card measurement setup

---

## 📦 Components

All required components are listed in the [BOM](BOM.md).

---

## 🪛 Assembly Steps

### 1. Start with Passive Components

Solder the lowest profile components first:

- Resistors (R1–R10)
- Small capacitors (C5, C6, C7, C8, C9)

👉 Tip: Bend leads and place components flat on the PCB before soldering.

---

### 2. Install Larger Capacitors

- C1 (560 nF)
- C2 (4.7 µF)
- C3, C4 (220 µF)

⚠️ Observe polarity for electrolytic capacitors!

---

### 3. Insert Diodes

- D1, D2 (1N4148)

⚠️ Pay attention to polarity (stripe marking).

---

### 4. Install IC Socket / Op-Amp

- TL064 (U4)

👉 Recommended: use a DIP socket instead of soldering directly.

---

### 5. Add Connectors and Headers

- Audio jacks (AUDIOIN, AUDIOOUT)
- Pin headers (J1–J6)

---

### 6. Mount Inductor

- L1 (47 mH)

👉 Ensure stable mechanical placement.

---

### 7. Install Switches

- SW1 (Power)
- SW2 (Chaos ON)
- SW3 (Lx ON/OFF)

---

### 8. Power Section

- TPA4056 module
- DC-DC converter
- Battery holder (14500)

⚠️ Double-check polarity before powering!

---

### 9. LED Indicator

- LED1 + resistor

⚠️ Check LED polarity (long leg = anode).

---

## 🔍 Final Checks

Before powering the board:

- Check for solder bridges
- Verify polarity of:
  - electrolytic capacitors
  - diodes
  - battery
- Measure resistance between VCC and GND (should not be short)

---

## ⚡ First Power-Up

1. Power the board using the battery  
2. Verify LED turns ON  
3. Measure supply voltage from DC-DC converter  

---

## 🔊 Functional Test

1. Connect audio input (phone or PC)
2. Apply sine wave (e.g., 1 kHz)
3. Connect output to sound card
4. Observe signal using:
   - Audacity
   - oscilloscope software

---

## 🧪 Mode Testing

- SW2 OFF → linear oscillation  
- SW2 ON → nonlinear behavior  
- Adjust input amplitude to observe chaotic response  

---

## ⚠️ Safety Notes

- Do not exceed sound card input limits (~±1 V)
- Avoid incorrect battery polarity
- Ensure stable grounding

---

## 🎓 Notes

This board is designed for educational purposes and supports both:

- experimental measurements  
- simulation-based comparison  

---

