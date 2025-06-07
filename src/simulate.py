"""
Simulate Duffing Oscillator for multiple initial conditions
and save the results to data/raw/ directory.

Mathematical Background:
------------------------
Duffing equation (second-order nonlinear ODE with physical form):
    m x'' + δ x' + k x + α x³ = F cos(ω t)

Converted to a first-order system:
    Let x₁ = x           → position
        x₂ = x'          → velocity
    Then:
        dx₁/dt = x₂
        dx₂/dt = (1/m) [ -δ x₂ - k x₁ - α x₁³ + F cos(ω t) ]

This script uses `solve_ivp` to integrate the system over time for
multiple initial conditions and stores the output as CSV files.
"""

import numpy as np
from scipy.integrate import solve_ivp
import os

# --------------------------------
# Duffing Oscillator Parameters
# --------------------------------
m = 1.0          # Mass
delta = 0.2      # Damping coefficient
k = -1.0         # Linear spring stiffness
alpha = 1.0      # Nonlinear stiffness
F = 0.3          # Forcing amplitude
omega = 1.2      # Driving frequency

# --------------------------------
# Time settings
# --------------------------------
t_start = 0.0
t_end = 100.0
dt = 0.01
t_eval = np.arange(t_start, t_end, dt)

# --------------------------------
# Output directory setup
# --------------------------------
output_dir = "../data/raw/"
os.makedirs(output_dir, exist_ok=True)

# --------------------------------
# Duffing system in first-order form
# --------------------------------
def duffing(t, y):
    """
    Duffing oscillator first-order system:
    dy₁/dt = y₂
    dy₂/dt = (1/m)(-δ y₂ - k y₁ - α y₁³ + F cos(ω t))
    """
    x, v = y
    dxdt = v
    dvdt = (1 / m) * (-delta * v - k * x - alpha * x**3 + F * np.cos(omega * t))
    return [dxdt, dvdt]

# --------------------------------
# Initial condition grid
# --------------------------------
x0_vals = np.linspace(-2, 2, 5)
v0_vals = np.linspace(-2, 2, 5)

sim_id = 0

# --------------------------------
# Run simulation for each (x₀, v₀)
# --------------------------------
for x0 in x0_vals:
    for v0 in v0_vals:
        y0 = [x0, v0]

        solution = solve_ivp(
            duffing,
            t_span=(t_start, t_end),
            y0=y0,
            t_eval=t_eval,
            method="RK45",
            rtol=1e-6,
            atol=1e-9
        )

        # Stack [t, x(t), v(t)] into a single array
        data = np.vstack((solution.t, solution.y[0], solution.y[1])).T

        # Save to CSV
        filename = os.path.join(output_dir, f"sim_{sim_id:03d}.csv")
        np.savetxt(filename, data, delimiter=",", header="t,x,v", comments="")
        print(f"Saved: {filename}")
        sim_id += 1