# Theory of Universal Origins (TUO)

**A Matrix-Algebraic Framework for Cosmogenesis**  
*Romeo Matshaba · University of South Africa · 2026*

---

## The Central Idea in One Sentence

The universe is a non-trivial rearrangement of nothing — a configuration of matter and fields whose total observable content, when assembled as an infinite column vector and evaluated against every conserved charge operator, equals the infinite zero matrix.

---

## The Two Axioms

Everything in TUO follows from exactly two postulates.

**Axiom I — Flat Background**  
The pre-emergence arena is (3+1)-dimensional Minkowski spacetime.  
No curvature. No preferred time. No pre-existing matter.

**Axiom II — Global Zero-Sum Constraint**  
For every conserved charge operator Q̂_k and all times t:

```
Tr[ρ̂(t) Q̂_k] = 0    ∀k, ∀t
```

Written as an infinite column vector — **the universe's full observable content equals the zero matrix at every instant**:

```
⎡ Tr[ρ̂ Ĥ]         ⎤   ⎡ 0 ⎤
⎢ Tr[ρ̂ P̂^μ]      ⎥   ⎢ 0 ⎥
⎢ Tr[ρ̂ Ĵ]         ⎥   ⎢ 0 ⎥
⎢ Tr[ρ̂ Q̂_em]     ⎥ = ⎢ 0 ⎥ = Ξ
⎢ Tr[ρ̂ Q̂_{B-L}]  ⎥   ⎢ 0 ⎥
⎣ Tr[ρ̂ Q̂_colour] ⎦   ⎣ 0 ⎦
```

This is not an approximation. It is exact, and it holds at every instant.

---

## Mathematical Language: Infinite-Dimensional Linear Algebra

The universe state lives in Fock space `𝓕 = ⊕_{n=0}^∞ ℋ_n`. The density operator is an infinite matrix:

```
      ⎛ ρ₀₀  ρ₀₁  ρ₀₂  ··· ⎞
ρ̂ =  ⎜ ρ₁₀  ρ₁₁  ρ₁₂  ··· ⎟
      ⎜ ρ₂₀  ρ₂₁  ρ₂₂  ··· ⎟
      ⎝  ·    ·    ·   ·    ⎠
```

Each conserved charge Q̂_k is diagonal in its eigenbasis:

```
         ⎛ q_{k0}    0      0    ··· ⎞
Q̂_k =   ⎜   0    q_{k1}   0    ··· ⎟
         ⎜   0      0    q_{k2} ··· ⎟
         ⎝   ·      ·      ·    ·   ⎠
```

The constraint `Tr[ρ̂ Q̂_k] = Σ_{n} ρ_{nn} · q_{kn} = 0` is an **infinite linear equation** on the occupation probabilities. The set of physically allowed density operators is the intersection of these hyperplanes — a highly constrained, discrete manifold. There is no continuous dial to tune: the universe either satisfies Axiom II or it does not.

---

## All Scales Are SM-Derived — Not Assumed

A key principle: Planck units (t_Pl, l_Pl, T_Pl) are phenomenological combinations of G, ℏ, c. TUO derives its natural scales from the SM particle content.

Setting the SM thermal energy density equal to the Planck energy density:

```
ρ_SM(T) = (π²/30) g* T⁴/(ℏc)³  =  ρ_Pl

→  T* = (30/(π² g*))^(1/4) × T_Pl  =  0.411 T_Pl   [SM thermal scale]

E_cell = (g*/2) E_Pl  →  T_TUO = (15/π²)^(1/4) × T_Pl  =  1.1103 T_Pl

→  t* = (T_TUO/T*)² × t_Pl  =  7.31 × t_Pl            [SM-derived emergence time]
```

The emergence timescale is **7.31 t_Pl**, not t_Pl by assumption. The Fermi-Dirac mode occupation at T_TUO peaks at k = 35, not k = 33.

---

## What TUO Derives (Standard BB Assumes as Inputs)

| Quantity | TUO Result | How |
|---|---|---|
| Equation of state w | = 1/3 | p = E/3 from v = c at emergence |
| Hubble H(t_Pl) | = 1/(2t_Pl) exact | Wavepacket spreading formula |
| Spatial flatness Ω | = 1 exactly | Axiom I (flat background) |
| Total energy E_tot | = 0 exactly | Axiom II (zero-sum) |
| Expansion law V(t) | (4π/3)l_Pl³[1+(ct/l_Pl)²]^(3/2) | Quantum wavepacket σ(t) |
| Stability | No annihilation channel | No antiparticles → no pair to annihilate |

---

## The Inflationary Structure

The wavepacket σ(t) = l_Pl√(1+(ct/l_Pl)²) implies an effective equation of state:

```
w_eff(x) = -(1 + 2/x²)/3     where  x = ct/l_Pl
```

| x = ct/l_Pl | w_eff | Phase |
|---|---|---|
| → 0 | → −∞ | Super-inflationary |
| 1 (t = t_Pl) | **−1.000 exactly** | **de Sitter — without inflaton** |
| 2 | −0.500 | |
| 10 | −0.340 | |
| → ∞ | → −1/3 | Radiation (FRW) |

**The expansion is always accelerated** (σ̈ > 0, deceleration parameter q = −1/x² < 0 always) and **always sub-luminal** (v < c always, proven). From the SM-derived emergence time t* to the electroweak scale:

```
N_efolds(t* → T_EW) ≈ 76.4 e-folds
```

Standard inflation requires N ≥ 60. **TUO delivers 76 without an inflaton field, without a slow-roll potential, without super-luminal expansion.**

---

## Key Numerical Results

| Quantity | TUO value | Status |
|---|---|---|
| T_TUO | (15/π²)^(1/4) T_Pl = 1.1103 T_Pl | SM-derived |
| t* (emergence) | 7.31 t_Pl | SM-derived |
| E_cell | (g*/2) E_Pl = 1.04×10¹¹ J | Factor 15/π²=1.52 vs standard |
| H(t_Pl) | 1/(2t_Pl) = 9.27×10⁴² s⁻¹ | Exact match FRW |
| w_eff at t_Pl | −1.000 (de Sitter) | Derived |
| N_efolds to EW | 76.4 | Exceeds inflation minimum |
| v_max | < c (always) | Theorem |
| ΔV/V | 3(l_Pl/ct)² | New prediction |
| N_cells | ~8.8×10⁹² | Observable universe |
| Saddle-point ratio | e^(8.8×10⁹²) | Simultaneous emergence dominance |

---

## Why Physical Laws Are Equalities

The zero-sum constraint (Axiom II) explains why fundamental equations are *equalities* rather than inequalities:

- **G_μν = (8πG/c⁴) T_μν** — any inequality would imply net non-zero energy, violating Axiom II. The EFE are the local form of the zero-sum constraint for energy-momentum.
- **iℏ ∂ψ/∂t = Ĥψ** — unitary evolution is the unique dynamics preserving ∫|ψ|² dx = 1 (probability zero-sum).
- **Quantum entanglement** — the singlet state is required by the angular-momentum zero-sum. Bell inequality violations are direct measurements of Axiom II.

---

## Backward Calculations from Observations

| Observation | TUO reading |
|---|---|
| Ω = 1.0007 ± 0.0037 | TUO predicts Ω = 1 exact. Precision will converge to TUO's prediction. |
| H₀ = 67.4 km/s/Mpc | Back-extrapolation gives H(t_Pl) = 1/(2t_Pl). TUO derives this independently. |
| Y_p = 0.245 ± 0.003 | Same g*=106.75 → Y_p ≈ 0.247. Consistent. |
| η = 6.12×10⁻¹⁰ | B−L=0: matter-only allowed; target n_B/s ≈ 1.03×10⁻¹¹ (open calculation). |
| ΔT/T ~ 10⁻⁵ | Within-cell ΔE/E ~ 9.7%; needs ~4 decades GR suppression (highest-priority open problem). |

---

## Open Problems

| Problem | Status |
|---|---|
| Baryon asymmetry η = 6.12×10⁻¹⁰ | Qualitative only. Target: n_B/s ≈ 1.03×10⁻¹¹. Needs Planck-scale QFT. |
| CMB power spectrum ΔT/T ~ 10⁻⁵ | Within-cell fluctuation calculation — highest priority. |
| Dark energy Λ ~ 10⁻¹²² E_Pl⁴ | Zero-sum predicts Λ=0 at leading order. Residual needs QGD. |
| SM particle content g*=106.75 | Used from experiment. Not yet derived from axioms. |
| GR recovery | EFE structure consistent with Axiom II. Full derivation needs companion QGD. |

---

## Repository Contents

| File | Description |
|---|---|
| `tuo_v3.pdf` | 18-page paper (full matrix formalism, inflation section, ranked results, open problems) |
| `tuo_complete_theory.py` | Canonical Python reference — all derivations with numbers |
| `tuo_sim_v2.py` | 14-panel simulation (SM-derived scales, w_eff, e-folds, backward calculations) |
| `tuo_evolution_v2.png` | Simulation output |
| `TUO_INSIGHTS_v2.md` | Full physical interpretation of every result |

---

## Run It

```bash
# Print the complete theory with all SM-derived numerical verifications
python tuo_complete_theory.py

# Generate the 14-panel evolution simulation
python tuo_sim_v2.py
# Outputs: tuo_evolution_v2.png

# Requirements
pip install numpy matplotlib scipy
```

---

## Citation

```bibtex
@article{matshaba2026tuo,
  title   = {Universal Origins: The Zero-Sum Constraint —
             Matrix Formulation of Cosmogenesis},
  author  = {Matshaba, Romeo},
  year    = {2026},
  note    = {University of South Africa, Pretoria}
}
```

---

*TUO does not replace the Big Bang. It precedes it — and it delivers every initial condition the Big Bang needs, derived from two axioms and the Standard Model, with no free parameters.*
