
# cc Major Piláth 2015
# Interactive Duffing-type nonlinear RLC simulation (Colab version)

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from ipywidgets import interact, FloatSlider, IntSlider

# --- Nonlinearity definition (three-segment piecewise linear function) ---
def FE(x):
    if x < -0.5:
        return -(x + 1)
    elif x > 0.5:
        return -(x - 1)
    else:
        return x

# --- Duffing-Holmes equation in first-order form ---
def duffing(t, z, a, b, omega):
    x, y = z
    dxdt = y
    dydt = FE(x) - b*y + a*np.sin(omega * t)
    return [dxdt, dydt]

# --- Main simulation function ---
def run_simulation(a=0.4, omega=1.3, b=0.1, L_mH=19.0, C_uF=0.47, t_max=300):
    
    dt = 0.001  # simulation time step
    t_eval = np.arange(0, t_max, dt)  # evaluation time points
    z0 = [0.1, 0.0]  # initial conditions: x=0.1, y=0

    # --- Convert circuit parameters to SI units ---
    L = L_mH * 1e-3         # mH → H
    C = C_uF * 1e-6         # µF → F
    V_star = 0.5            # typical diode threshold voltage (V)
    rho = np.sqrt(L / C)    # characteristic impedance (Ohm)

    # Scaling factor to convert dimensionless current to physical current
    current_scale = (2 * V_star) / rho

    # --- Numerical integration (Runge-Kutta method) ---
    sol = solve_ivp(
        lambda t, z: duffing(t, z, a, b, omega),
        [0, t_max],
        z0,
        t_eval=t_eval,
        method='RK45',
        rtol=1e-8
    )

    # --- Extract solution ---
    x = sol.y[0]  # dimensionless voltage
    y = sol.y[1]  # dimensionless current
    t = sol.t     # time vector

    # --- Poincaré section (sampling once per driving period) ---
    T_drive = 2 * np.pi / omega
    t_poincare = np.arange(50 * T_drive, t_max, T_drive)  # discard transient
    poincare_x = np.interp(t_poincare, t, x)
    poincare_y = np.interp(t_poincare, t, y)

    # --- Plotting ---
    plt.figure(figsize=(16, 10))

    # 1. Time evolution of capacitor voltage
    plt.subplot(3, 1, 1)
    plt.plot(t, x * 2 * V_star, lw=0.8)
    plt.title(f"Capacitor voltage V_C(t) | a={a}, ω={omega}, L={L_mH} mH, C={C_uF} µF")
    plt.xlabel("t [s]")
    plt.ylabel("V_C [V]")

    # 2. Phase space (V_C vs I_L)
    plt.subplot(3, 1, 2)
    plt.plot(x * 2 * V_star, y * current_scale, lw=0.7)
    plt.title("Phase space: V_C [V] vs I_L [A]")
    plt.xlabel("V_C [V]")
    plt.ylabel("I_L [A]")

    # 3. Poincaré section
    plt.subplot(3, 1, 3)
    plt.plot(poincare_x * 2 * V_star, poincare_y * current_scale, 'o', markersize=2)
    plt.title("Poincaré section")
    plt.xlabel("V_C [V]")
    plt.ylabel("I_L [A]")

    plt.tight_layout()
    plt.show()

# --- Interactive controls ---
interact(
    run_simulation,
    a=FloatSlider(value=0.6, min=0.0, max=1.0, step=0.01, description='Amplitude a'),
    omega=FloatSlider(value=1.25, min=0.1, max=5.0, step=0.05, description='Frequency ω'),
    b=FloatSlider(value=0.1, min=0.0, max=1.0, step=0.01, description='Damping b'),
    L_mH=FloatSlider(value=47.0, min=1.0, max=100.0, step=1.0, description='L [mH]'),
    C_uF=FloatSlider(value=0.56, min=0.01, max=10.0, step=0.01, description='C [µF]'),
    t_max=IntSlider(value=300, min=50, max=1000, step=10, description='Duration [s]')
)
