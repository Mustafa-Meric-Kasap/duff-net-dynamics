# duff-net-dynamics

## Branch Naming Convention

To keep the project clean and organized, we follow a structured branch naming system:

### Prefixes

| Prefix         | Purpose                                                   | Example                           |
|----------------|-----------------------------------------------------------|-----------------------------------|
| `math/`        | Analytical derivations, theory, and LaTeX math writing    | `math/duffing-derivation`         |
| `sim/`         | Numerical simulation work (e.g., Duffing integration)     | `sim/phase-space-batch`           |
| `nn/`          | Neural network models and training                        | `nn/lstm-predictor`               |
| `viz/`         | Plotting, figure generation, and visual tuning            | `viz/animated-trajectories`       |
| `paper/`       | Work on the LaTeX or .docx draft of the term paper        | `paper/methods-section`           |
| `slides/`      | Presentation slide preparation                            | `slides/final-layout`             |
| `doc/`         | README updates, project setup, or documentation tweaks    | `doc/add-branch-guide`            |

### Multi-Scope Branches
If your work involves more than one scope, combine prefixes:
- `math-sim/chaos-analysis`
- `sim-nn/generate-training-data`
- `viz-paper/figure-exports`

### Best Practices
- Use `kebab-case` for descriptions (e.g., `no_spaces_orCamelCase`)
- Keep `main` clean and production-ready — only merge tested code