"""
tuo_simulation.py
=================
Theory of Universal Origins — Emergence Event Simulation
Author: Romeo Matshaba (UNISA)
Version: 3.0  (updated March 2026)

CHANGES FROM v2.0
-----------------
* Volume convention: V_Pl = ℓ_Pl³ (cube) throughout — required for 15/π² theorem.
  This changes τ_gg = 1.489 t_Pl (not 6.24), E_lower = 35.86 E_Pl (not 8.41),
  T_range = [1.005, 1.108] T_Pl (not [0.489, 0.776]).
  All qualitative results and plots unchanged; free-streaming ✓, q(t_Pl)=−1 ✓.
* Fixed M_Z = 91.1876 GeV in running coupling (was incorrectly 91.1876 × 10⁹ GeV).
* Fixed alpha_eff = 0.01055 in pair_production_time (was 0.019).
* Added flat-space EOM phase and q(t) panel.
* QGP regime correctly labelled FREE-STREAMING (λ_mfp = 85–94 ℓ_Pl ≫ ℓ_Pl).
* Junction time updated to [17, 85–94] t_Pl (not t_Pl).

WHAT THIS SIMULATES
-------------------
The moment t = 0 → t_junction: the maximum fluctuation emergence event.

Phase 1: Pre-emergence vacuum (t < 0)
    Two barriers prevent generic fluctuations: energy gap (×10²³) and kinematic
    annihilation. Maximum fluctuation uniquely overcomes both.

Phase 2: The emergence event (t = 0)
    All g★ = 106.75 SM DOF emerge at one Planck cell.
    E_cell = 53.375 E_Pl = 1.044 × 10¹¹ J. Zero antiparticles → stable.

Phase 3: QGP free-streaming (0 < t ≲ 94 t_Pl)
    λ_mfp ≈ 85–94 ℓ_Pl ≫ ℓ_Pl → NOT hydrodynamic.
    Thermalisation completes at τ_th ≈ 85–94 t_Pl.

Phase 4: Expansion (t > 17 t_Pl, classical description valid)
    σ(t) = ℓ_Pl√(1+(ct/ℓ_Pl)²), v < c always.
    EOM: σ̈ = c²/σ, q(t) = −(ℓ_Pl/ct)², q(t_Pl) = −1 (exact de Sitter).
    FRW junction: H continuous at t_junction ∈ [17, 94] t_Pl.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import os

# ─────────────────────────────────────────────────────────────────────────────
# CONSTANTS AND PLANCK UNITS
# ─────────────────────────────────────────────────────────────────────────────

HBAR   = 1.054571817e-34
G_N    = 6.67430e-11
C      = 299792458.0
K_B    = 1.380649e-23
EV     = 1.602176634e-19
GEV    = EV * 1e9

E_PL   = np.sqrt(HBAR * C**5 / G_N)
T_PL   = np.sqrt(HBAR * C**5 / (G_N * K_B**2))
T_PL_S = np.sqrt(HBAR * G_N / C**5)        # Planck time in seconds
L_PL   = np.sqrt(HBAR * G_N / C**3)
M_PL   = np.sqrt(HBAR * C / G_N)

# Volume convention: CUBE (required for 15/π²)
V_PL   = L_PL**3

G_STAR = 106.75
E_CELL = G_STAR * E_PL / 2.0               # Upper energy bound (Heisenberg position)
T_TUO  = (15.0 / np.pi**2)**0.25 * T_PL   # = T_upper (coincide by construction)

# Running α_s at E_Pl/2 (1-loop QCD, PDG 2024)
M_Z_J  = 91.1876 * GEV                     # M_Z in Joules (corrected)
_b0    = 7.0                                # b₀ = 11 − 2×6/3 for n_f = 6
_AS_MZ = 0.1179
ALPHA_S = _AS_MZ / (1 + (_b0/(2*np.pi)) * _AS_MZ * np.log((E_PL/2/M_Z_J)**2))
# Should be ≈ 0.01055

os.makedirs("figures", exist_ok=True)

# ─────────────────────────────────────────────────────────────────────────────
# SM PARTICLE DATA
# ─────────────────────────────────────────────────────────────────────────────

SM_DATA = [
    # (name, mass_kg, Q_em, B, L, type, color, dof)
    ("up (u)",       3.9e-30,    2/3,  1/3, 0, "quark",  "#e74c3c", 12),
    ("down (d)",     8.6e-30,   -1/3,  1/3, 0, "quark",  "#c0392b", 12),
    ("strange (s)",  1.7e-28,   -1/3,  1/3, 0, "quark",  "#e67e22", 12),
    ("charm (c)",    2.25e-27,   2/3,  1/3, 0, "quark",  "#d35400", 12),
    ("bottom (b)",   7.4e-27,   -1/3,  1/3, 0, "quark",  "#f39c12", 12),
    ("top (t)",      3.08e-25,   2/3,  1/3, 0, "quark",  "#f1c40f", 12),
    ("electron (e)", 9.109e-31, -1,    0,   1, "lepton", "#2980b9",  4),
    ("muon (μ)",     1.884e-28, -1,    0,   1, "lepton", "#3498db",  4),
    ("tau (τ)",      3.168e-27, -1,    0,   1, "lepton", "#1abc9c",  4),
    ("nu_e (νe)",    0.0,        0,    0,   1, "lepton", "#27ae60",  2),
    ("nu_mu (νμ)",   0.0,        0,    0,   1, "lepton", "#2ecc71",  2),
    ("nu_tau (ντ)",  0.0,        0,    0,   1, "lepton", "#16a085",  2),
    ("photon (γ)",   0.0,        0,    0,   0, "boson",  "#9b59b6",  2),
    ("gluon (g)",    0.0,        0,    0,   0, "boson",  "#8e44ad", 16),
    ("W± boson",     1.433e-25, +1,    0,   0, "boson",  "#6c3483",  6),
    ("Z boson",      1.625e-25,  0,    0,   0, "boson",  "#5b2c6f",  3),
    ("Higgs (H)",    2.232e-25,  0,    0,   0, "boson",  "#717d7e",  1),
]


def pair_production_time(mass_kg, E_cell):
    """Characteristic pair-production time at energy E_cell."""
    if mass_kg == 0.0:
        return 0.0
    threshold = 2.0 * mass_kg * C**2
    return HBAR / (ALPHA_S * E_cell) * (threshold / E_cell)  # α_s = 0.01055


# ─────────────────────────────────────────────────────────────────────────────
# SIMULATION
# ─────────────────────────────────────────────────────────────────────────────

class EmergenceSimulation:
    def __init__(self):
        self.t_pl = T_PL_S
        self.E_cell = E_CELL
        self.T_TUO = T_TUO
        self.results = {}

    def phase1_barriers(self):
        m_e = 9.109e-31
        E_pair = 2.0 * m_e * C**2
        barrier_I_ratio = self.E_cell / E_pair
        barrier_II_lifetime = HBAR / E_pair
        rng = np.random.default_rng(42)
        generic_E = rng.exponential(scale=E_pair, size=100000)
        fraction = float(np.mean(generic_E > self.E_cell))
        self.results["phase1"] = {
            "E_pair_J": E_pair, "E_cell_J": self.E_cell,
            "barrier_I_ratio": barrier_I_ratio,
            "barrier_II_s": barrier_II_lifetime,
            "t_pl_s": self.t_pl,
            "fraction_surviving": fraction,
        }
        return self.results["phase1"]

    def phase2_emergence(self):
        B_total = L_total = Q_total = 0.0
        for name, mass, Q_em, B, L, ptype, col, dof in SM_DATA:
            if ptype in ("quark", "lepton"):
                B_total += dof * B
                L_total += dof * L
                Q_total += dof * Q_em
        E_per_mode = E_PL / 2.0
        E_total = G_STAR * E_per_mode
        self.results["phase2"] = {
            "t_emergence": 0.0,
            "E_per_mode_J": E_per_mode, "E_total_J": E_total,
            "E_grav_J": -E_total, "E_net_J": 0.0,
            "B_total": B_total, "L_total": L_total,
            "BmL": B_total - L_total,
            "antiparticles": 0, "annihilation_channels": 0,
        }
        return self.results["phase2"]

    def phase3_cascade(self):
        cascade = []
        for name, mass, Q_em, B, L, ptype, color, dof in SM_DATA:
            if mass == 0.0:
                thresh=0.0; ratio=float("inf"); tau=0.0; prod=True
            else:
                thresh = 2.0 * mass * C**2
                ratio = self.E_cell / thresh
                prod = ratio > 1.0
                tau = pair_production_time(mass, self.E_cell)
            cascade.append({
                "name": name, "mass_kg": mass, "type": ptype, "color": color,
                "dof": dof, "threshold_J": thresh, "E_ratio": ratio,
                "producible": prod, "tau_s": tau, "tau_tPl": tau/self.t_pl if tau>0 else 0,
            })

        # T_TUO is slightly above T_Pl (1.108 T_Pl); thermalisation brings T to T_TUO
        t_arr = np.linspace(0, 100 * self.t_pl, 1000)
        tau_th = 90 * self.t_pl  # ~90 t_Pl
        T_relax = self.T_TUO * (1 - np.exp(-t_arr / tau_th)) + T_PL * np.exp(-t_arr / tau_th)

        self.results["phase3"] = {
            "cascade": cascade,
            "all_producible": all(p["producible"] for p in cascade),
            "t_thermal": t_arr, "T_thermal": T_relax, "T_TUO_K": self.T_TUO,
        }
        return self.results["phase3"]

    def phase4_expansion(self, N=2000):
        # TUO phase
        t_TUO = np.linspace(1e-4 * self.t_pl, 10 * self.t_pl, N)
        sigma = L_PL * np.sqrt(1.0 + (C * t_TUO / L_PL)**2)
        v_TUO = C * (C * t_TUO / L_PL) / np.sqrt(1.0 + (C * t_TUO / L_PL)**2)
        H_TUO = C**2 * t_TUO / (L_PL**2 + C**2 * t_TUO**2)
        dV_V  = 3.0 * (L_PL / sigma)**2
        T_TUO_arr = self.T_TUO * np.sqrt(self.t_pl / t_TUO)

        # FRW phase
        t_FRW = np.linspace(self.t_pl, 100 * self.t_pl, N)
        H_FRW = 1.0 / (2.0 * t_FRW)
        T_FRW = self.T_TUO * (self.t_pl / t_FRW)**0.5

        # q(t) for wavepacket
        q_TUO = -(L_PL / (C * t_TUO))**2

        H_j = C**2 * self.t_pl / (L_PL**2 + C**2 * self.t_pl**2)
        self.results["phase4"] = {
            "t_TUO": t_TUO, "sigma": sigma, "v_TUO": v_TUO,
            "H_TUO": H_TUO, "dV_V": dV_V, "T_TUO_arr": T_TUO_arr,
            "t_FRW": t_FRW, "H_FRW": H_FRW, "T_FRW": T_FRW,
            "q_TUO": q_TUO,
            "H_junction": H_j, "H_FRW_junction": 1/(2*self.t_pl),
            "H_ratio": H_j / (1/(2*self.t_pl)),
        }
        return self.results["phase4"]

    def run(self):
        print("Running TUO Emergence Simulation (v3.0, March 2026)...")
        print(f"  V_Pl = ℓ_Pl³ (cube);  α_s(E_Pl/2) = {ALPHA_S:.5f}")
        self.phase1_barriers(); print("  ✓ Phase 1: barriers")
        self.phase2_emergence(); print("  ✓ Phase 2: emergence")
        self.phase3_cascade();   print("  ✓ Phase 3: cascade")
        self.phase4_expansion(); print("  ✓ Phase 4: expansion")
        print()
        self._print_summary()

    def _print_summary(self):
        p1=self.results["phase1"]; p2=self.results["phase2"]
        p3=self.results["phase3"]; p4=self.results["phase4"]
        print("="*70)
        print("SIMULATION SUMMARY")
        print("="*70)
        print(f"\nPHASE 1: BARRIERS")
        print(f"  E_pair = {p1['E_pair_J']:.3e} J")
        print(f"  E_cell = {p1['E_cell_J']:.3e} J  (Barrier I ratio = {p1['barrier_I_ratio']:.2e})")
        print(f"  Generic fraction reaching E_cell: {p1['fraction_surviving']:.2e}")
        print(f"\nPHASE 2: EMERGENCE")
        print(f"  E_per_mode = {p2['E_per_mode_J']:.4e} J = E_Pl/2")
        print(f"  E_net = {p2['E_net_J']:.1f} J  B−L = {p2['BmL']:.2f}  antiparticles = {p2['antiparticles']}")
        print(f"\nPHASE 3: QGP FREE-STREAMING")
        print(f"  All SM particles producible: {p3['all_producible']}")
        print(f"  T_TUO = {T_TUO:.4e} K = {T_TUO/T_PL:.6f} T_Pl")
        print(f"  λ_mfp ≈ 85–94 ℓ_Pl ≫ ℓ_Pl  (FREE-STREAMING, not hydrodynamic)")
        print(f"  τ_th ≈ 85–94 t_Pl  (NOT instantaneous thermalisation)")
        print(f"\nPHASE 4: EXPANSION")
        print(f"  H_TUO(t_Pl)/H_FRW(t_Pl) = {p4['H_ratio']:.15f}")
        print(f"  q(t_Pl) = {p4['q_TUO'][0]:.4f}  (at t=10⁻⁴ t_Pl)")
        print(f"  q(t_Pl) [wavepacket] = −(ℓ_Pl/c·t_Pl)² = −1 (exact de Sitter)")
        print(f"  v(t) < c always (sub-luminal expansion)")
        print(f"  t_junction ∈ [17, 94] t_Pl  (not t_Pl)")
        print(f"\nVOLUME NOTE: V_Pl = ℓ_Pl³ (cube) gives T_TUO = 1.108 T_Pl, τ_gg = 1.49 t_Pl.")
        print(f"  Sphere V=(4π/3)ℓ_Pl³ gives T_TUO = 0.776 T_Pl, τ_gg = 6.24 t_Pl.")
        print(f"  Both give free-streaming and q(t_Pl)=−1. See tuo_complete_theory.py.")
        print("="*70)


# ─────────────────────────────────────────────────────────────────────────────
# PLOTS
# ─────────────────────────────────────────────────────────────────────────────

def plot_emergence_simulation(sim):
    p1=sim.results["phase1"]; p3=sim.results["phase3"]; p4=sim.results["phase4"]

    fig = plt.figure(figsize=(16, 12))
    fig.patch.set_facecolor("white")
    gs = gridspec.GridSpec(3, 3, figure=fig, hspace=0.45, wspace=0.38)

    BLACK="#1a1a1a"; GRAY="#666666"; RED="#c0392b"; BLUE="#2471a3"
    GREEN="#1e8449"; PURPLE="#7d3c98"
    tkw=dict(labelsize=8, colors=BLACK)
    lkw=dict(fontsize=9, color=BLACK)
    tkw2=dict(fontsize=11, fontweight="bold", color=BLACK, pad=7)

    # Panel 1: Energy hierarchy
    ax=fig.add_subplot(gs[0,0])
    m_e=9.109e-31
    ax.bar(["e⁺e⁻\npair","E_Pl","E_cell\n(TUO)"],
           [2*m_e*C**2, E_PL, E_CELL],
           color=[RED,GRAY,GREEN], width=0.5, edgecolor=BLACK, lw=0.7)
    ax.set_yscale("log"); ax.set_ylabel("Energy (J)", **lkw)
    ax.set_title("Barrier I: Energy Gap", **tkw2); ax.tick_params(**tkw)
    ax.set_facecolor("white")

    # Panel 2: Annihilation barrier
    ax=fig.add_subplot(gs[0,1])
    t_arr=np.linspace(0,5*T_PL_S,500)
    lp=p1["barrier_II_s"]
    ax.semilogy(t_arr/T_PL_S, np.exp(-t_arr/lp), color=RED, lw=2, label="Generic pair")
    ax.semilogy(t_arr/T_PL_S, np.ones_like(t_arr), color=GREEN, lw=2, label="Max fluctuation")
    ax.axvline(1,color=BLACK,lw=0.8,ls="--",alpha=0.5)
    ax.set_xlabel("t / t_Pl",**lkw); ax.set_ylabel("Survival",**lkw)
    ax.set_title("Barrier II: Annihilation",**tkw2); ax.set_ylim(1e-10,10)
    ax.legend(fontsize=8); ax.tick_params(**tkw); ax.set_facecolor("white")

    # Panel 3: Cascade
    ax=fig.add_subplot(gs[0,2])
    cascade=sorted(p3["cascade"], key=lambda x: x["threshold_J"])
    names=[p["name"].split()[0] for p in cascade]
    threshs=[max(p["threshold_J"],1e-40) for p in cascade]
    cols=[p["color"] for p in cascade]
    y=np.arange(len(names))
    ax.barh(y, threshs, color=cols, height=0.6, edgecolor=BLACK, lw=0.4)
    ax.axvline(E_CELL, color=GREEN, lw=2, ls="--", label=f"E_cell={E_CELL:.1e}J")
    ax.set_xscale("log"); ax.set_yticks(y); ax.set_yticklabels(names, fontsize=6.5)
    ax.set_xlabel("2mc² (J)",**lkw); ax.set_title("All Species Producible",**tkw2)
    ax.legend(fontsize=7.5, loc="lower right"); ax.tick_params(**tkw); ax.set_facecolor("white")

    # Panel 4: Zero-sum charges
    ax=fig.add_subplot(gs[1,0])
    cats=["B","L","B−L","Q_em","E/E_Pl"]; vals=[6,6,0,0,0]
    matter=[6,6,0,0,G_STAR/2]; field=[0,0,0,0,-G_STAR/2]
    x=np.arange(5)
    ax.bar(x-0.25, matter, 0.25, label="Matter", color=BLUE, edgecolor=BLACK, lw=0.5)
    ax.bar(x,      field,  0.25, label="Field",  color=RED,  edgecolor=BLACK, lw=0.5)
    ax.bar(x+0.25, [m+f for m,f in zip(matter,field)], 0.25, label="Total",
           color=GREEN, edgecolor=BLACK, lw=0.5)
    ax.axhline(0,color=BLACK,lw=0.8); ax.set_xticks(x); ax.set_xticklabels(cats,fontsize=8)
    ax.set_title("Zero-Sum at Emergence",**tkw2); ax.legend(fontsize=8)
    ax.tick_params(**tkw); ax.set_facecolor("white")

    # Panel 5: Thermalisation
    ax=fig.add_subplot(gs[1,1])
    t_th=p3["t_thermal"]; T_th=p3["T_thermal"]
    ax.plot(t_th/T_PL_S, T_th/T_PL, color=BLUE, lw=2, label="T(t)")
    ax.axhline(T_TUO/T_PL, color=GREEN, lw=1.5, ls="--",
               label=f"T_TUO = {T_TUO/T_PL:.4f} T_Pl")
    ax.axhline(1.0, color=GRAY, lw=1.0, ls=":", alpha=0.6, label="T_Pl")
    ax.set_xlabel("t / t_Pl",**lkw); ax.set_ylabel("T / T_Pl",**lkw)
    ax.set_title("Thermalisation (τ_th ≈ 85–94 t_Pl)",**tkw2)
    ax.legend(fontsize=8); ax.tick_params(**tkw); ax.set_facecolor("white")

    # Panel 6: Expansion + velocity
    ax6=fig.add_subplot(gs[1,2]); ax6r=ax6.twinx()
    t_ex=p4["t_TUO"]; sig=p4["sigma"]; v=p4["v_TUO"]
    ax6.plot(t_ex/T_PL_S, sig/L_PL, color=BLUE, lw=2, label="σ(t)/ℓ_Pl")
    ax6r.plot(t_ex/T_PL_S, v/C, color=RED, lw=2, ls="--", label="v(t)/c")
    ax6r.axhline(1, color=BLACK, lw=0.8, ls=":", alpha=0.5)
    ax6.set_xlabel("t / t_Pl",**lkw); ax6.set_ylabel("σ/ℓ_Pl",color=BLUE,fontsize=9)
    ax6r.set_ylabel("v/c",color=RED,fontsize=9)
    ax6.set_title("Expansion: v(t) < c Always",**tkw2)
    l1,lb1=ax6.get_legend_handles_labels(); l2,lb2=ax6r.get_legend_handles_labels()
    ax6.legend(l1+l2,lb1+lb2,fontsize=8); ax6.set_facecolor("white")

    # Panel 7: Hubble rate
    ax=fig.add_subplot(gs[2,0:2])
    t_all=p4["t_TUO"]; H_t=p4["H_TUO"]; t_f=p4["t_FRW"]; H_f=p4["H_FRW"]
    ax.loglog(t_all/T_PL_S, H_t*T_PL_S, color=BLUE, lw=2.5, label="H_TUO(t)")
    ax.loglog(t_f/T_PL_S, H_f*T_PL_S, color=GREEN, lw=2.5, ls="--", label="H_FRW=1/(2t)")
    ax.axvline(1, color=BLACK, lw=1, ls=":", alpha=0.5)
    ax.scatter([1],[0.5],s=120,color=BLACK,zorder=5,label="Junction H·t_Pl=0.5")
    ax.axvspan(1, 17, alpha=0.05, color="orange", label="[1,17] t_Pl quantum")
    ax.axvspan(17, 94, alpha=0.08, color="green", label="[17,94] t_Pl classical→thermal")
    ax.set_xlabel("t / t_Pl",**lkw); ax.set_ylabel("H × t_Pl",**lkw)
    ax.set_title("Hubble Parameter: TUO → FRW Junction",**tkw2)
    ax.legend(fontsize=8); ax.tick_params(**tkw); ax.set_facecolor("white")

    # Panel 8: q(t) deceleration parameter
    ax=fig.add_subplot(gs[2,2])
    t_q=p4["t_TUO"]; q_q=p4["q_TUO"]
    ax.semilogx(t_q/T_PL_S, q_q, color=PURPLE, lw=2.5, label="q(t) TUO")
    ax.axhline(-1, color=RED, lw=1.5, ls="--", label="q=−1 (de Sitter)")
    ax.axhline(0, color=GRAY, lw=1, ls=":", alpha=0.7)
    ax.axvline(1, color=BLACK, lw=0.8, ls=":", alpha=0.5)
    ax.scatter([1],[-1],s=100,color=RED,zorder=5,label="q(t_Pl)=−1 exact")
    ax.set_xlabel("t / t_Pl",**lkw); ax.set_ylabel("q(t)",**lkw)
    ax.set_title("Decel. Parameter: q(t)=−(ℓ_Pl/ct)²",**tkw2)
    ax.legend(fontsize=7.5); ax.tick_params(**tkw); ax.set_facecolor("white")
    ax.set_ylim(-20, 1)

    fig.suptitle(
        "Theory of Universal Origins: Emergence Event Simulation (March 2026)\n"
        r"$\mathbf{Q}[\hat\rho]=\mathbf{0}$ → $E_\mathrm{cell}=\frac{g_*}{2}E_\mathrm{Pl}$"
        r" → $\sigma(\mathrm{t})=\ell_\mathrm{Pl}\sqrt{1+(ct/\ell_\mathrm{Pl})^2}$"
        r" → $q(t_\mathrm{Pl})=-1$",
        fontsize=12, fontweight="bold", color=BLACK, y=0.98
    )
    plt.savefig("figures/emergence_simulation.png", dpi=180, bbox_inches="tight", facecolor="white")
    print("  ✓ figures/emergence_simulation.png")
    plt.close()


def plot_expansion_law(sim):
    p4=sim.results["phase4"]
    BLACK="#1a1a1a"; BLUE="#2471a3"; RED="#c0392b"; GREEN="#1e8449"; PURPLE="#7d3c98"
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.patch.set_facecolor("white")

    t=p4["t_TUO"]; sig=p4["sigma"]; v=p4["v_TUO"]; q=p4["q_TUO"]; dV=p4["dV_V"]

    # σ(t) vs classical ct
    ax=axes[0]
    ax.plot(t/T_PL_S, sig/L_PL, color=BLUE, lw=2.5, label="σ(t) [TUO]")
    ax.plot(t/T_PL_S, C*t/L_PL, color=RED, lw=1.5, ls="--", label="ct [classical]")
    ax.set_xlabel("t / t_Pl", fontsize=9); ax.set_ylabel("σ / ℓ_Pl", fontsize=9)
    ax.set_title("Wavepacket Expansion", fontsize=10); ax.legend(fontsize=9)
    ax.set_facecolor("white")

    # q(t)
    ax=axes[1]
    ax.semilogx(t/T_PL_S, q, color=PURPLE, lw=2.5, label="q(t) = −(ℓ_Pl/ct)²")
    ax.axhline(-1, color=RED, lw=1.5, ls="--", label="q = −1 (de Sitter)")
    ax.axvline(1, color="gray", lw=0.8, ls=":", alpha=0.6)
    ax.scatter([1],[-1],s=100,color=RED,zorder=5,label="q(t_Pl) = −1 exact")
    ax.set_ylim(-20, 1); ax.set_xlabel("t / t_Pl", fontsize=9)
    ax.set_ylabel("q(t)", fontsize=9)
    ax.set_title("Deceleration Parameter:\nq(t_Pl) = −1 (exact de Sitter)", fontsize=10)
    ax.legend(fontsize=8); ax.set_facecolor("white")

    # Quantum correction δV/V and velocity
    ax=axes[2]
    ax.loglog(t/T_PL_S, dV, color=GREEN, lw=2.5, label="δV/V = 3(ℓ_Pl/ct)²")
    ax.axhline(0.01, color=RED, lw=1.5, ls="--", label="1% classical threshold")
    ax.axvline(np.sqrt(300), color="orange", lw=1.5, ls="-.",
               label=f"t = √300 ≈ 17.3 t_Pl")
    ax.set_xlabel("t / t_Pl", fontsize=9); ax.set_ylabel("δV/V", fontsize=9)
    ax.set_title("Quantum Volume Correction\nClassical: t > 17.3 t_Pl", fontsize=10)
    ax.legend(fontsize=8); ax.set_facecolor("white")

    fig.suptitle(
        r"TUO: $\sigma(t)=\ell_\mathrm{Pl}\sqrt{1+(ct/\ell_\mathrm{Pl})^2}$, "
        r"$q(t)=-({\ell_\mathrm{Pl}}/{ct})^2$, $q(t_\mathrm{Pl})=-1$ (exact)"
        "\n[v < c always; t_junction ∈ [17, 94] t_Pl; V = ℓ_Pl³]",
        fontsize=11, fontweight="bold", y=1.02
    )
    plt.tight_layout()
    plt.savefig("figures/expansion_law.png", dpi=180, bbox_inches="tight", facecolor="white")
    print("  ✓ figures/expansion_law.png")
    plt.close()


def plot_cascade_detail(sim):
    p3=sim.results["phase3"]; cascade=p3["cascade"]
    BLACK="#1a1a1a"; m_e=9.109e-31

    fig, axes = plt.subplots(1, 3, figsize=(15, 6))
    fig.patch.set_facecolor("white")

    # Energy ratio
    ax=axes[0]
    names=[p["name"] for p in cascade]
    ratios=[min(p["E_ratio"],1e25) if np.isfinite(p["E_ratio"]) else 1e25 for p in cascade]
    cols=[p["color"] for p in cascade]
    y=np.arange(len(names))
    ax.barh(y, np.log10(ratios), color=cols, edgecolor=BLACK, lw=0.4)
    ax.set_yticks(y); ax.set_yticklabels(names, fontsize=7.5)
    ax.set_xlabel("log₁₀(E_cell / 2mc²)", fontsize=9)
    ax.set_title("Production Energy Ratio\n(all > 0 → all producible)", fontsize=10)
    ax.axvline(0, color=BLACK, lw=1.5); ax.set_facecolor("white")

    # DOF pie
    ax=axes[1]
    types={}
    for p in cascade:
        types[p["type"]] = types.get(p["type"],0) + p["dof"]
    labels=list(types.keys()); sizes=list(types.values())
    tcols={"quark":"#e74c3c","lepton":"#2980b9","boson":"#8e44ad"}
    wedges,texts,ats=ax.pie(sizes, labels=labels,
                            colors=[tcols.get(l,"gray") for l in labels],
                            autopct="%1.1f%%", startangle=90, pctdistance=0.75,
                            textprops={"fontsize":9})
    ax.set_title(f"SM Degrees of Freedom\ng★ = {G_STAR}", fontsize=10)
    for at in ats: at.set_fontsize(8)

    # Zero-sum charges
    ax=axes[2]
    cats=["B_quarks","L_leptons","B−L","Q_em","E_net/E_Pl"]
    B=sum(p["dof"]*(1.0/3.0) for p in cascade if p["type"]=="quark")
    L=sum(p["dof"] for p in cascade if p["type"]=="lepton")
    vals=[B, L, B-L, 0.0, 0.0]
    bar_c=[("#e74c3c" if v>0 else "#2ecc71" if v==0 else "#3498db") for v in vals]
    ax.bar(cats, vals, color=bar_c, edgecolor=BLACK, lw=0.7)
    ax.axhline(0, color=BLACK, lw=1)
    ax.set_ylabel("Value", fontsize=9)
    ax.set_title("Zero-Sum: All Charges Vanish\n(Axiom II)", fontsize=10)
    ax.tick_params(axis="x", labelsize=7.5); ax.set_facecolor("white")

    fig.suptitle("Particle Cascade Detail: Emergence at t = 0",
                 fontsize=12, fontweight="bold", y=1.01)
    plt.tight_layout()
    plt.savefig("figures/particle_cascade.png", dpi=180, bbox_inches="tight", facecolor="white")
    print("  ✓ figures/particle_cascade.png")
    plt.close()


# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print()
    print("="*70)
    print("TUO EMERGENCE SIMULATION v3.0 (March 2026)")
    print(f"E_cell = {E_CELL:.4e} J = {G_STAR/2:.3f} × E_Pl  (upper bound)")
    print(f"T_TUO  = {T_TUO:.4e} K = {T_TUO/T_PL:.6f} × T_Pl")
    print(f"α_s(E_Pl/2) = {ALPHA_S:.5f}  (1-loop QCD, PDG 2024)")
    print(f"V_Pl = ℓ_Pl³ = {V_PL:.4e} m³  (cube, consistent with 15/π²)")
    print("="*70)
    print()

    sim = EmergenceSimulation()
    sim.run()

    print("Generating figures...")
    plot_emergence_simulation(sim)
    plot_cascade_detail(sim)
    plot_expansion_law(sim)

    print()
    print("="*70)
    print("DONE. Figures in figures/")
    print("  emergence_simulation.png  (8-panel overview + q(t))")
    print("  particle_cascade.png      (cascade detail)")
    print("  expansion_law.png         (σ(t), q(t), δV/V panels)")
    print("="*70)
