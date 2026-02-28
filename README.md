# Theory of Universal Origins (TUO)

**A pre-Big-Bang framework derived from a single algebraic constraint**
---

## What TUO Is

TUO proposes that the universe emerged from a quantum vacuum constrained by one requirement: **every conserved charge must sum to exactly zero**. From this single axiom — applied to the Standard Model's particle content in an infinite-dimensional Fock space — the initial conditions of the Hot Big Bang follow without free parameters.

TUO ends precisely where the Hot Big Bang begins.

---

## Two Axioms

| Axiom | Statement |
|-------|-----------|
| **I. Flat Background** | The pre-emergence spacetime is (3+1)-dimensional Minkowski space with metric η_μν = diag(−1,+1,+1,+1). No curvature, no preferred time. |
| **II. Zero-Sum Constraint** | For every conserved charge Q̂_k and all times t: Tr[ρ̂(t) Q̂_k] = 0. The full charge vector equals the infinite zero matrix: **Q**[ρ̂] = **0**_∞ |

These are the **only** postulates. Everything else is derived.

---

## What Is Proven (from axioms alone)

| Result | Significance |
|--------|-------------|
| **E_total = 0** exactly | The universe has zero net energy — a consequence of G·M_Pl² = ℏc, pure Planck algebra |
| **w = 1/3** (derived) | The radiation equation of state — HBB assumes this; TUO derives it from v₀ = c |
| **H(t_Pl) = 1/(2t_Pl)** | The Planck-era Hubble rate — HBB assumes this; TUO derives it from wavepacket spreading |
| **Ω = 1** exactly | Spatial flatness — forced by Axiom I |
| **E_cell = (g*/2) E_Pl** | All SM modes at Heisenberg minimum; equals 1.04 × 10¹¹ J per Planck cell |
| **T_TUO = (15/π²)^(1/4) T_Pl** | Pre-emergence temperature, **independent of g*** — a non-trivial cancellation |
| **B−L = 0, Q = 0** per generation | SM anomaly cancellation as a consequence of Axiom II |
| **No-annihilation theorem** | Matter-only configurations have no kinematic annihilation channel |
| **V(t) ∝ t³, v < c always** | Expansion law with quantum correction ΔV/V = 3(ℓ_Pl/ct)² |
| **All 5 HBB initial conditions** | Seamless handoff to standard cosmology at t = t_Pl |

---

## The Core Physical Argument

Generic vacuum fluctuations cannot become a universe. Two barriers prevent it:

1. **Energy gap**: A typical electron-positron pair carries ~10⁻¹³ J. The energy needed for a Planck cell is ~10¹¹ J. That is a factor of 10²⁴. No accumulation mechanism bridges this gap in one Planck time.

2. **Annihilation timescale**: At Planck energies, Δt ~ t_Pl ~ 5.4 × 10⁻⁴⁴ s. Any particle-antiparticle content collapses back to vacuum before structure forms.

**The resolution** is the most extreme fluctuation consistent with the zero-sum axiom: *all Standard Model degrees of freedom — quarks, leptons, gauge bosons, Higgs — emerging simultaneously, co-located at a single Planck-scale volume, with no antiparticles.*

This configuration:
- Satisfies zero-sum (B−L = 0, Q = 0 per generation, E_grav = −E_matter)
- Carries sufficient energy (10²⁴× more than a generic pair)
- Is **kinematically stable** — no antiparticles means no annihilation channel

The number g* = 106.75 is not a parameter of TUO. It is the count of all SM degrees of freedom, and it appears in E_cell because **all of them must emerge together** for either barrier to be overcome.

---

## The TUO–HBB Junction

```
TUO regime (t < t_Pl)          at t = t_Pl          Hot Big Bang (t > t_Pl)
─────────────────────          ────────────          ─────────────────────────
Zero-sum pre-emergence    ←→   HANDOFF POINT   ←→   Radiation domination
Wavepacket σ(t), v < c                              a(t) ∝ t^(1/2)
w = 1/3  [derived]             w = 1/3              w = 1/3  [assumed by HBB]
H = 1/(2t_Pl) [derived]        H continuous          H = 1/(2t) [assumed by HBB]
k = 0 [Axiom I]                Ω = 1                Ω = 1 [assumed by HBB]
g* = 106.75 [all SM]           plasma formed         Standard thermodynamics
```

---

## What TUO Does NOT Claim

TUO does not derive or predict:
- Dark matter (open problem)
- Dark energy / cosmological constant (open problem)
- The number of fermion generations N_gen = 3 (open problem)
- The baryon asymmetry η ≈ 6.1 × 10⁻¹⁰ (open problem)
- The CMB power spectrum amplitude (open problem)
- The SM gauge group or coupling constants

Stating this explicitly is not weakness. It is the precondition for trusting what *is* derived.

---

## Repository Structure

```
TUO/
├── README.md                    # This file
├── paper/
│   ├── tuo_paper.tex            # Full LaTeX source
│   └── tuo_paper.pdf            # Compiled paper (27 pages)
├── code/
│   ├── tuo_theory.py            # All physics: constants, theorems, predictions
│   └── tuo_simulation.py        # Emergence event simulation & particle cascade
├── docs/
│   ├── insights.md              # Deep analysis of TUO's novel contributions
│   ├── glossary.md              # Definitions of all terms and symbols
│   └── citations.bib            # Full BibTeX reference file
└── notebooks/
    └── tuo_verification.ipynb   # (optional) interactive verification
```

---

## Quick Start

```bash
git clone https://github.com/matshaba/TUO.git
cd TUO

# Run theory verification
python code/tuo_theory.py

# Run emergence simulation
python code/tuo_simulation.py
```

Requirements: Python ≥ 3.9, NumPy, SciPy, Matplotlib

---

## Key Numbers

| Quantity | Value | Source |
|---------|-------|--------|
| E_cell | 1.044 × 10¹¹ J = 53.375 E_Pl | Axioms + g* |
| T_TUO | 1.573 × 10³² K = 1.110 T_Pl | Axioms (g*-independent) |
| E_total | 0 (exact) | G·M_Pl² = ℏc identity |
| 15/π² | 1.5198... | Heisenberg/Stefan-Boltzmann ratio |
| g* | 106.75 | Standard Model (28 bosons + 90×7/8 fermions) |
| t_Pl | 5.391 × 10⁻⁴⁴ s | Planck units |

---

## Citation

```bibtex
@article{Matshaba2026_TUO,
  author  = {Matshaba, Romeo},
  title   = {Universal Origins: The Zero-Sum Constraint ---
             Matrix Formulation of Cosmogenesis},
  year    = {2026},
  school  = {University of South Africa},
  note    = {Preprint}
}
```

---

## Author

Romeo Matshaba  
Department of Physics, University of South Africa (UNISA)  
Pretoria, South Africa

---

## License

This work is made available under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
You are free to share and adapt the material with appropriate attribution.
