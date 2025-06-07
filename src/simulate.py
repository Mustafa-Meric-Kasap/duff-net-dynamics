"""
Simulate Duffing Oscillator across a grid of initial conditions
and parameter combinations (F, delta, omega), saving only
trajectories with dynamic behavior to ../data/raw/.

Mathematical Model:
-------------------
Duffing Equation (2nd-order nonlinear ODE):
    m * x'' + δ * x' + k * x + α * x³ = F * cos(ω t)

Converted to 1st-order system:
    Let x₁ = x → position
        x₂ = x' → velocity
    Then:
        dx₁/dt = x₂
        dx₂/dt = (1/m)(-δ * x₂ - k * x₁ - α * x₁³ + F * cos(ω t))
"""

import numpy as np
from scipy.integrate import solve_ivp
import os

# --------------------------------
# Base Duffing parameters (fixed)
# --------------------------------
m = 1.0        # Mass of oscillator
k = -1.0       # Linear stiffness (negative: double-well potential)
alpha = 1.0    # Nonlinear stiffness (cubic term)

# --------------------------------
# Parameter ranges to sweep (exploration)
# --------------------------------
F_values = [0.3, 0.7, 1.0]         # Forcing amplitudes (chaos increases with F)
delta_values = [0.1, 0.2]          # Damping coefficients (lower δ = more persistent motion)
omega_values = [1.0, 1.2, 1.4]     # Driving frequencies (chaos depends on resonance)

# --------------------------------
# Time integration settings
# --------------------------------
t_start = 0.0
t_end = 100.0
dt = 0.01
t_eval = np.arange(t_start, t_end, dt)  # output time points

# --------------------------------
# Output folder
# --------------------------------
output_dir = "../data/raw/"
os.makedirs(output_dir, exist_ok=True)

# --------------------------------
# Initial conditions (x₀, v₀) grid
# --------------------------------
x0_vals = np.linspace(-2, 2, 5)  # 5 values from -2 to 2
v0_vals = np.linspace(-2, 2, 5)  # same for velocity
sim_id = 0                       # file counter

# --------------------------------
# Simulation loop over parameter combinations and ICs
# --------------------------------
for F in F_values:
    for delta in delta_values:
        for omega in omega_values:

            # Define Duffing system for current (F, delta, omega)
            def duffing(t, y):
                x, v = y
                dxdt = v
                dvdt = (1 / m) * (-delta * v - k * x - alpha * x**3 + F * np.cos(omega * t))
                return [dxdt, dvdt]

            # Loop over all initial conditions
            for x0 in x0_vals:
                for v0 in v0_vals:
                    y0 = [x0, v0]  # initial state [position, velocity]

                    # Numerically integrate the ODE using solve_ivp
                    sol = solve_ivp(
                        duffing,
                        t_span=(t_start, t_end),
                        y0=y0,
                        t_eval=t_eval,
                        method="RK45",       # Runge-Kutta 4(5)
                        rtol=1e-6,
                        atol=1e-9
                    )

                    # Extract solution components
                    x = sol.y[0]
                    v = sol.y[1]
                    x_std = np.std(x)
                    v_std = np.std(v)

                    # Only save simulations with meaningful dynamics
                    if x_std > 0.05 or v_std > 0.05:
                        data = np.vstack((sol.t, x, v)).T  # shape: [timesteps, 3]

                        # Build filename with all parameters
                        filename = os.path.join(
                            output_dir,
                            f"F{F:.1f}_d{delta:.2f}_w{omega:.1f}_sim_{sim_id:03d}.csv"
                        )

                        # Save to CSV: columns = [t, x, v]
                        np.savetxt(filename, data, delimiter=",", header="t,x,v", comments="")
                        print(f"✅ Saved: {filename} (std_x={x_std:.3f}, std_v={v_std:.3f})")
                        sim_id += 1
                    else:
                        # Skip if the trajectory is too static (no useful learning signal)
                        print(f"⏩ Skipped sim_{sim_id:03d} (std_x={x_std:.3f}, std_v={v_std:.3f})")