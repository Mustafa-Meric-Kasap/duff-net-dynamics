# duff-net-dynamics

**Modeling the Dynamics of the Duffing Oscillator Using Neural Networks**  
Mustafa Meriç Kasap, PHYS201, Koç University – Spring 2025

## Overview

This project investigates the use of Recurrent Neural Networks, specifically LSTM architectures, to model the behavior of the Duffing oscillator, a nonlinear dynamical system known for its chaotic properties. We simulate hundreds of trajectories, train two different forecasting models (recursive and multi-step), and evaluate their ability to capture the oscillator's physical and dynamical properties.

---

##  Key Features

-  **Simulates Duffing oscillator** dynamics under a range of damping, forcing, and frequency conditions.
-  Includes both **chaotic and regular regimes**.
-  **Numerical integration** using SciPy's RK45 via `solve_ivp`.
-  **Neural network forecasting** using:
    - Recursive (step-by-step) LSTM
    - Multi-step (direct sequence prediction) LSTM
-  Visual and quantitative comparisons using MSE, MAE, R², and phase space plots.

---

## Project Structure

```
duff-net-dynamics-main/
├── data/
│   ├── raw/           # Raw simulation trajectories (filtered)
│   └── processed/     # Preprocessed datasets for training
├── notebooks/
│   ├── simulation.ipynb              # RK45 Duffing simulation and data generation
│   ├── nn_modeling.ipynb             # General modeling overview
│   ├── nn_modeling_recursive.ipynb   # Recursive LSTM implementation and plots
│   ├── nn_modeling_multi_step.ipynb  # Multi-step LSTM implementation and plots
│   └── math_analysis.ipynb		# Mathematical analysis
├── src/
│   ├── model.py       # LSTM model definitions
│   ├── simulate.py    # ODE integration utilities
│   └── utils.py       # Normalization, plotting, helpers
├── LICENSE
├── pyproject.toml     # Dependencies and build metadata
├── uv.lock
└── README.md          # Project documentation (this file)
```

---

##  Setup

### Requirements

- Python ≥ 3.13
- `torch`, `scikit-learn`, `matplotlib`, `scipy`, `pandas`, `numpy`, `notebook`

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Mustafa-Meric-Kasap/duff-net-dynamics.git
   cd duff-net-dynamics
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt  # Or use pyproject.toml with poetry/uv
   ```

---

## How to Run

1. **Generate data**:
	Run `src/simulate.py`

2. **Train models**:
   - `notebooks/nn_modeling_recursive.ipynb`
   - `notebooks/nn_modeling_multi_step.ipynb`

3. **Visualize results**:
   - Use `math_analysis.ipynb` to compare true vs predicted trajectories
   - Inspect phase space plots and error growth over time

---

##  Key Parameters

- Forcing amplitudes: `F = [0.3, 0.7, 1.0]`
- Damping coefficients: `δ = [0.1, 0.2]`
- Driving frequencies: `ω = [1.0, 1.2, 1.4]`
- Time span: `0 to 100 s`, with `dt = 0.01`

---

## References

- Kovacic, I., & Brennan, M. J. (2011). *The Duffing Equation: Nonlinear Oscillators and their Behaviour*.
- Strogatz, S. H. (2018). *Nonlinear Dynamics and Chaos*.

---
## Branch Naming Convention

To keep the project clean and organized, we follow a structured branch naming system:

### Prefixes

| Prefix         | Purpose                                                   | Example                           |
|----------------|-----------------------------------------------------------|-----------------------------------|
| `math/`        | Analytical derivations, theory, and LaTeX math writing    | `math/duffing-derivation`         |
| `sim/`         | Numerical simulation work (e.g., Duffing integration)     | `sim/phase-space-batch`           |
| `nn/`          | Neural network models and training                        | `nn/lstm-predictor`               |
| `viz/`         | Plotting, figure generation, and visual tuning            | `viz/animated-trajectories`       |
| `doc/`         | README updates, project setup, or documentation tweaks    | `doc/add-branch-guide`            |

### Multi-Scope Branches
If your work involves more than one scope, combine prefixes:
- `math-sim/chaos-analysis`
- `sim-nn/generate-training-data`
- `viz-paper/figure-exports`

### Best Practices
- Use `kebab-case` for descriptions (e.g., `no_spaces_orCamelCase`)
- Keep `main` clean and production-ready, only merge tested code

---


## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
