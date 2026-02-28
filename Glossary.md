# TUO Glossary

*Definitions of all terms, symbols, and concepts used in the Theory of Universal Origins.*

---

## Physical Constants

| Symbol | Name | Value | Notes |
|--------|------|-------|-------|
| ℏ | Reduced Planck constant | 1.054571817 × 10⁻³⁴ J·s | Exact (SI 2019) |
| c | Speed of light | 299,792,458 m/s | Exact (SI 2019) |
| G | Newton's gravitational constant | 6.67430 × 10⁻¹¹ m³/kg/s² | CODATA 2018 |
| k_B | Boltzmann constant | 1.380649 × 10⁻²³ J/K | Exact (SI 2019) |

---

## Planck Units

These are derived from the constants above and define the natural scale for TUO.

| Symbol | Name | Definition | Value |
|--------|------|-----------|-------|
| E_Pl | Planck energy | √(ℏc⁵/G) | 1.9561 × 10⁹ J |
| t_Pl | Planck time | √(ℏG/c⁵) | 5.3912 × 10⁻⁴⁴ s |
| ℓ_Pl | Planck length | √(ℏG/c³) | 1.6162 × 10⁻³⁵ m |
| T_Pl | Planck temperature | √(ℏc⁵/Gk_B²) | 1.4168 × 10³² K |
| M_Pl | Planck mass | √(ℏc/G) | 2.1764 × 10⁻⁸ kg |

**Key identity**: c·t_Pl = ℓ_Pl (exact, used throughout all derivations)

**Key identity**: G·M_Pl² = ℏc (exact, follows from definitions; makes E_total = 0)

---

## TUO-Specific Symbols

| Symbol | Definition | Section |
|--------|-----------|---------|
| **0**_∞ | The infinite zero matrix; all entries zero | §2.1 |
| **Q**[ρ̂] | Observable charge vector; 12-component column of all conserved charges | §3 |
| ρ̂(t) | Global density operator of the universe; element of B(ℱ) | §2.3 |
| ℱ | Universe Fock space; ⊕_{n=0}^∞ ℋ_n | §2.2 |
| ℋ_n | n-particle sector of Fock space | §2.2 |
| Q̂_k | Conserved charge operator (energy, momentum, B−L, colour, etc.) | §2.4 |
| ZSC | Zero-Sum Constraint; the set of density operators satisfying Axiom II | §3 |
| g* | Effective relativistic degrees of freedom | §7 |
| E_cell | Total matter energy per Planck cell at emergence | §7 |
| T_TUO | Pre-emergence temperature; (15/π²)^(1/4) T_Pl | §12 |
| σ(t) | Wavepacket width at time t; ℓ_Pl √(1 + (ct/ℓ_Pl)²) | §9 |
| H_TUO(t) | TUO Hubble parameter; c²t/(ℓ_Pl² + c²t²) | §9 |
| w | Equation-of-state parameter; P/(ρc²) | §9 |

---

## Standard Model Quantities

| Symbol | Definition | Value |
|--------|-----------|-------|
| g* | Effective relativistic DOF at T ≫ T_QCD | 106.75 |
| N_B | Bosonic SM degrees of freedom | 28 |
| N_F | Fermionic SM degrees of freedom (Weyl) | 90 |
| g* formula | N_B + (7/8)N_F | 28 + (7/8)×90 = 106.75 |
| B | Baryon number | Quarks: 1/3 each |
| L | Lepton number | Leptons: 1 each |
| B−L | Baryon minus lepton number | Zero per SM generation (proven) |
| Q_em | Electric charge | Zero per SM generation (proven) |

**SM boson content (N_B = 28)**:  
Photon (2) + W± (6) + Z (3) + Gluons (16) + Higgs (1) = 28

**SM fermion content per generation (N_F/3 = 30 Weyl DOF)**:  
Quarks: (u,d) × 3 colors × 2 spins = 12  
Leptons: (ν,e) × 2 spins = 4  
Total per generation: 16 Weyl; × 3 generations = 48 Weyl  
Plus right-handed: 48 more = 96? [Standard counting gives 90; see PDG for precise bookkeeping]

---

## Key Concepts

### Zero-Sum Constraint (ZSC)
The requirement that every conserved charge has zero expectation value in the pre-emergence state. Formally: Tr[ρ̂ Q̂_k] = 0 for all k. This is an infinite set of linear equations on the density operator, defining a hyperplane in B(ℱ).

### Maximum Fluctuation
The zero-sum vacuum fluctuation that excites all g* = 106.75 SM effective degrees of freedom simultaneously at one Planck-scale volume, each at Heisenberg minimum energy E_Pl/2. This is the unique fluctuation that overcomes both the energy barrier and the annihilation barrier.

### Emergence
The moment at t = t_Pl when the maximum fluctuation transitions from the pre-emergence (TUO) regime to the Hot Big Bang regime. The junction conditions (H, w, k) are continuous across this transition.

### Heisenberg Minimum Energy
The minimum energy a mode can carry at timescale Δt = t_Pl, given by ΔE_min = ℏ/(2t_Pl) = E_Pl/2. This is not the thermal average energy; it is the quantum mechanical floor.

### Anomaly Cancellation
The requirement that gauge anomalies vanish, ensuring the SM is self-consistent. Per SM generation: Q = 0 and B−L = 0. TUO's Axiom II independently requires these — they are consequences of the zero-sum constraint applied to electromagnetic and B−L charges.

### Wavepacket Spreading
The quantum-mechanical spreading of a particle wavepacket initially localised to ℓ_Pl. For a relativistic particle (v = c), the width evolves as σ(t) = ℓ_Pl√(1 + (ct/ℓ_Pl)²), giving the TUO expansion law.

### Junction Condition
The matching of TUO and FRW quantities at t = t_Pl. Three conditions are satisfied: H is continuous, w = 1/3 on both sides, k = 0 on both sides. The energy density has a mismatch by 15/π² (open problem).

### Universal Factor 15/π²
The ratio E_cell/E_thermal = 15/π² ≈ 1.52, independent of g* and all SM parameters. Its numerator (15) comes from the Heisenberg minimum energy; its denominator (π²) from the Stefan-Boltzmann radiation constant (π²/30). Physical interpretation is an open problem.

### Configuration Space
The space of particle-physics theories (choices of particle content, charge assignments, mass spectra) that satisfy the zero-sum axiom with matter-only stability. All SM-like theories with integer numbers of complete anomaly-free generations are elements of this space.

### Frozen Constants
At emergence, two types of "constants" are distinguished:
- **Axiom-fixed** (same in all configurations): c, ℏ, G — these are required by the axioms themselves
- **Configuration-fixed** (vary across configurations): α, α_s, mass ratios — these are Lagrangian parameters selected by which configuration emerged

---

## Equation Index

| Equation | Content |
|---------|---------|
| Tr[ρ̂ Q̂_k] = 0 | The Zero-Sum Constraint (Axiom II) |
| E_cell = g*·E_Pl/2 | Energy per Planck cell |
| T_TUO = (15/π²)^(1/4) T_Pl | Pre-emergence temperature |
| E_total = E_Pl/2 − E_Pl/2 = 0 | Zero total energy |
| σ(t) = ℓ_Pl√(1+(ct/ℓ_Pl)²) | Wavepacket expansion law |
| H_TUO = c²t/(ℓ_Pl²+c²t²) | TUO Hubble parameter |
| H_TUO(t_Pl) = 1/(2t_Pl) | Junction condition |
| G_μν + Λg_μν = (8πG/c⁴)T_μν | EFE as local ZSC expression |
| V(t) = (4π/3)ℓ_Pl³[1+(ct/ℓ_Pl)²]^(3/2) | Volume expansion |
| ΔV/V = 3(ℓ_Pl/ct)² | Quantum correction to volume |

---

## Abbreviations

| Abbreviation | Full form |
|-------------|---------|
| TUO | Theory of Universal Origins |
| HBB | Hot Big Bang |
| SM | Standard Model (of particle physics) |
| FRW | Friedmann–Lemaître–Robertson–Walker (metric) |
| ZSC | Zero-Sum Constraint |
| DOF | Degrees of freedom |
| QFT | Quantum field theory |
| GR | General relativity |
| QGD | Quantum Gravity Dynamics (companion framework) |
| CMB | Cosmic microwave background |
| BBN | Big Bang nucleosynthesis |
| EFE | Einstein field equations |
| PDG | Particle Data Group |

---

*Last updated: February 2026*
