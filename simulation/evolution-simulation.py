"""
TUO EVOLUTION SIMULATION v2 — Romeo Matshaba, 2026
14-panel comprehensive visualization

NEW in v2:
- Panel 1: Fermi-Dirac zoo uses T_TUO (derived from g*, not dogmatic T_Pl)
- Panel 5: Effective equation of state w_eff(t) — inflation-like transition
- Panel 6: TUO e-folds vs inflation benchmark
- Panel 11: Backward calculations — observables → initial conditions
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import warnings, math
warnings.filterwarnings('ignore')

# ── Constants ──────────────────────────────────────────────────────────────
c=2.99792458e8; hbar=1.054571817e-34; G=6.67430e-11; k_B=1.380649e-23
GeV_J=1.602176634e-10; g_star=106.75; hbarc=hbar*c
E_Pl=np.sqrt(hbar*c**5/G); t_Pl=np.sqrt(hbar*G/c**5); l_Pl=np.sqrt(hbar*G/c**3)
T_Pl=np.sqrt(hbar*c**5/(G*k_B**2)); E_Pl_GeV=E_Pl/GeV_J

# SM-derived quantities — NOT put in by hand
T_TUO   = (15/np.pi**2)**0.25 * T_Pl          # from E_cell = (g*/2)E_Pl
T_star  = (30/(np.pi**2*g_star))**0.25 * T_Pl # SM energy density = Planck density
t_star  = (T_TUO/T_star)**2 * t_Pl            # SM-derived emergence time = 7.3 t_Pl
x_star  = c*t_star/l_Pl                        # = 7.3

E_cell  = g_star/2 * E_Pl
t_0     = 13.8e9*3.1558e7; R_obs=4.4e26
N_cells = ((R_obs*np.sqrt(t_Pl/t_0))/l_Pl)**3

# ── Style ──────────────────────────────────────────────────────────────────
BG='#0D1B2A'; NAVY='#1B3A6B'; TEAL='#0E9BAA'; GOLD='#E8A020'
CORAL='#E05050'; GREEN='#28A860'; PURP='#9B59B6'; WHITE='#EEEEFF'; GRAY='#7A8FA6'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':8.5,
    'axes.facecolor':'#0F1E30','figure.facecolor':BG,
    'text.color':WHITE,'axes.labelcolor':WHITE,'xtick.color':WHITE,
    'ytick.color':WHITE,'axes.edgecolor':'#2A4060','axes.grid':True,
    'grid.alpha':0.18,'grid.linestyle':'--','axes.titlesize':9.5,
    'axes.spines.top':False,'axes.spines.right':False})

def sigma(t): return l_Pl*np.sqrt(1+(c*t/l_Pl)**2)
def V(t): return (4*np.pi/3)*sigma(t)**3
def H_TUO(t): return c**2*t/(l_Pl**2+c**2*t**2)
def v_exp(t): return c*(c*t/l_Pl)/np.sqrt(1+(c*t/l_Pl)**2)
def T_at_t(t): return T_TUO*np.sqrt(t_Pl/t)
def w_eff(x): return -(1+2/x**2)/3   # x = ct/l_Pl

def alpha_s(E_GeV):
    b0=11-4.0; a0=0.1179; MZ=91.2
    d=1+(a0/(2*np.pi))*b0*np.log(np.maximum(E_GeV,1e-3)/MZ)
    return np.where(d>0.05, a0/d, np.nan)

def alpha_em(E_GeV):
    a0=1/137.036
    return a0/(1-a0/(3*np.pi)*np.log(np.maximum(E_GeV,5.11e-4)/5.11e-4))

# ══════════════════════════════════════════════════════════════════════════
# PANELS
# ══════════════════════════════════════════════════════════════════════════

def p1_zoo(ax):
    """Panel 1: Zero-Sum Zoo — FD distribution at T_TUO (SM-derived, not T_Pl)"""
    k=np.arange(91)
    # β·E_mode at T_TUO (derived from g*), not dogmatically at T_Pl
    betaE_TUO  = (E_Pl/2)/(k_B*T_TUO)   # = (π²/15)^(1/4)/2 ≈ 0.450
    betaE_TPl  = 0.5                     # dogmatic choice (for comparison only)
    f_TUO = 1/(1+np.exp(betaE_TUO))
    f_TPl = 1/(1+np.exp(betaE_TPl))
    k_peak_TUO = int(90*f_TUO)
    k_peak_TPl = int(90*f_TPl)

    pv = np.array([f_TUO**ki*(1-f_TUO)**(90-ki)*math.comb(90,ki) for ki in k])
    pv = np.maximum(pv,1e-100)
    col=[GOLD if ki==90 else (TEAL if abs(ki-k_peak_TUO)<4 else NAVY) for ki in k]
    ax.bar(k,np.log10(pv),color=col,width=1.0,alpha=0.85,edgecolor='none')

    ax.axvline(90,color=GOLD,lw=2,ls='--',label='Maximal fluctuation (our universe)')
    ax.axvline(k_peak_TUO,color=TEAL,lw=1.5,alpha=0.8,label=f'Peak at T_TUO: k={k_peak_TUO}')
    ax.axvline(k_peak_TPl,color=GRAY,lw=1.2,ls=':',alpha=0.7,label=f'Peak at T_Pl: k={k_peak_TPl} (not derived)')

    ax.text(88,-10,'OUR\nUNIVERSE',color=GOLD,fontsize=8,ha='center',
            bbox=dict(boxstyle='round',fc='#1A1400',ec=GOLD,alpha=0.85))
    ax.set(xlabel='Fermionic modes occupied  k',ylabel='log₁₀ P(k modes)',
           title=f'Panel 1: Zero-Sum Zoo\nFermi-Dirac at T_TUO={T_TUO/T_Pl:.3f}T_Pl (SM-derived, g*={g_star})',
           xlim=(0,90),ylim=(-55,2))
    ax.legend(fontsize=7.5)

    # annotation explaining why NOT T_Pl
    ax.text(0.03,0.04,
        f'T_TUO derived from g*:\n'
        f'E_cell=(g*/2)E_Pl → T_TUO=(15/π²)^(1/4)T_Pl\n'
        f'= {T_TUO/T_Pl:.4f} T_Pl  (not assumed)',
        transform=ax.transAxes,fontsize=7.5,color=TEAL,va='bottom',
        bbox=dict(boxstyle='round',fc='#001A20',ec=TEAL,alpha=0.85))

def p2_config(ax):
    """Panel 2: Config space — zero-sum filter"""
    np.random.seed(42); n=3000
    Q=np.random.normal(0,3,n); BmL=np.random.normal(0,3,n)
    sur=(np.abs(Q)<0.5)&(np.abs(BmL)<0.5); mx=(np.abs(Q)<0.06)&(np.abs(BmL)<0.06)
    ax.scatter(Q[~sur],BmL[~sur],s=3,alpha=0.2,c='#332222',label='Collapse to vacuum')
    ax.scatter(Q[sur&~mx],BmL[sur&~mx],s=18,alpha=0.75,c=TEAL,label='Zero-sum survivors')
    ax.scatter(Q[mx],BmL[mx],s=90,alpha=1,c=GOLD,marker='*',zorder=5,label='Maximal (universe)')
    ax.axhline(0,color=WHITE,lw=0.4,alpha=0.4); ax.axvline(0,color=WHITE,lw=0.4,alpha=0.4)
    from matplotlib.patches import Rectangle
    ax.add_patch(Rectangle((-0.5,-0.5),1,1,fill=False,ec=GOLD,lw=2,ls='--',zorder=4))
    ax.set(xlabel='Total Q [e]',ylabel='Total B−L',
           title='Panel 2: Configuration Space\nZero-sum filter — no free parameter to tune',
           xlim=(-8,8),ylim=(-8,8))
    ax.text(0.05,0.04,'No fine-tuning:\nconfiguration space\nis discrete, not\ncontinuous',
            transform=ax.transAxes,fontsize=8,color=GOLD,
            bbox=dict(boxstyle='round',fc='#1A1400',ec=GOLD,alpha=0.8))
    ax.legend(fontsize=7.5,markerscale=1.5)

def p3_simultaneous(ax):
    """Panel 3: Saddle-point proof"""
    N=np.logspace(0,95,400); logR=np.minimum(np.log10(N),95)
    ax.fill_between(np.log10(N),0,logR,alpha=0.3,color=TEAL)
    ax.plot(np.log10(N),logR,color=TEAL,lw=2.5,label='log₁₀[P(sim)/P(single)] = N')
    ax.axvline(np.log10(N_cells),color=GOLD,lw=2.5,ls='--',label=f'Our universe  N≈10⁹³')
    ax.set(xlabel='log₁₀(N_cells)',ylabel='log₁₀[P(simult.) / P(single-cell)]',
           title='Panel 3: Saddle-Point Proof\nSimultaneous emergence: ratio = exp(10⁹³)',
           xlim=(0,96),ylim=(0,96))
    ax.text(np.log10(N_cells)+2,50,'exp(10⁹³)\nsuppression\nof single-cell',color=GOLD,fontsize=8)
    ax.legend(fontsize=8)

def p4_expansion(ax):
    """Panel 4: Expansion law V(t)"""
    t=np.logspace(np.log10(t_Pl*0.5),np.log10(t_0),2000)
    ax.loglog(t/t_Pl,V(t)/l_Pl**3,color=TEAL,lw=2.5,
              label='V_TUO = (4π/3)l_Pl³[1+(ct/l_Pl)²]^(3/2)')
    ax.loglog(t/t_Pl,(4*np.pi/3)*(c*t)**3/l_Pl**3,color=CORAL,lw=1.5,ls='--',
              label='Classical (4π/3)(ct)³')
    for lab,tv,col in [('t*\n(7.3t_Pl)',t_star,TEAL),('EW',1e-12,GREEN),
                        ('QCD',1e-5,PURP),('Now',t_0,CORAL)]:
        ax.scatter([tv/t_Pl],[V(tv)/l_Pl**3],s=70,c=col,zorder=5)
        ax.annotate(lab,(tv/t_Pl,V(tv)/l_Pl**3),xytext=(6,4),
                    textcoords='offset points',color=col,fontsize=7)
    ax.set(xlabel='t / t_Pl',ylabel='V / l_Pl³',
           title='Panel 4: Expansion Law — Derived\nQM wavepacket spreading, no inflaton')
    ax.legend(fontsize=7.5)

def p5_w_eff(ax):
    """Panel 5: Effective equation of state — inflation-like transition"""
    x=np.logspace(-2,4,2000)   # x = ct/l_Pl
    t_x=x*l_Pl/c
    w=w_eff(x)

    ax.semilogx(x,np.maximum(w,-4),color=TEAL,lw=2.5,label='w_eff(t) = -(1+2/x²)/3')
    ax.axhline(-1,color=GOLD,lw=2,ls='--',label='w=-1 (de Sitter/Λ)')
    ax.axhline(-1/3,color=CORAL,lw=1.5,ls=':',label='w=-1/3 (curvature)')
    ax.axhline(1/3,color=GREEN,lw=1.5,ls=':',alpha=0.7,label='w=+1/3 (radiation, FRW)')
    ax.axvline(1.0,color=WHITE,lw=1.5,ls='-.',alpha=0.7,label='x=1  (t=t_Pl, de Sitter)')
    ax.axvline(x_star,color=PURP,lw=1.5,ls='--',alpha=0.8,label=f'x*={x_star:.1f} (t* SM-derived)')

    # Fill inflationary region (w < -1/3)
    ax.fill_between(x,np.maximum(w,-4),-1/3,
                    where=np.maximum(w,-4)<-1/3,color=TEAL,alpha=0.12)

    ax.text(0.15,-2.5,'SUPER-\nINFLATIONARY\n(w << -1)',
            color=TEAL,fontsize=8,ha='center',
            bbox=dict(boxstyle='round',fc='#001A20',ec=TEAL,alpha=0.8))
    ax.text(1.2,-0.95,'w=-1\nde Sitter\n(at t=t_Pl)',
            color=GOLD,fontsize=8,ha='left',
            bbox=dict(boxstyle='round',fc='#1A1400',ec=GOLD,alpha=0.85))
    ax.text(50,-0.31,'Asymptotes\nto w→-1/3',
            color=CORAL,fontsize=7.5,ha='center')

    ax.set(xlabel='x = ct / l_Pl',ylabel='Effective equation of state  w_eff',
           title='Panel 5: TUO Inflationary Structure\nw = -(1+2/x²)/3  derived from wavepacket',
           xlim=(0.01,1e4),ylim=(-4.5,0.6))
    ax.legend(fontsize=7.5,loc='lower right')

def p6_efolds(ax):
    """Panel 6: N e-folds from t* — TUO vs inflation requirement"""
    # e-fold from x* to various x_f: N = (1/2)ln((1+x_f²)/(1+x_star²))
    T_targets = np.logspace(np.log10(T_TUO*0.5),np.log10(T_TUO),100)
    # Going forward from t*:
    t_arr = np.logspace(np.log10(t_star),np.log10(t_0),3000)
    x_arr = c*t_arr/l_Pl
    N_arr = 0.5*np.log((1+x_arr**2)/(1+x_star**2))

    ax.semilogx(t_arr,N_arr,color=TEAL,lw=2.5,label='N_efolds from t*')
    ax.axhline(60,color=CORAL,lw=2,ls='--',label='Inflation minimum (N=60)')
    ax.axhline(76.4,color=GOLD,lw=1.5,ls='-.',label='TUO at EW scale (N≈76)')

    for lab,T_val,col in [('GUT\n~17 e-folds',1e28,GREEN),
                           ('EW\n~76 e-folds',1.5e15,GOLD),
                           ('QCD\n~90 e-folds',1.5e12,PURP)]:
        t_v = t_Pl*(T_TUO/T_val)**2
        if t_v > t_star:
            x_v = c*t_v/l_Pl
            N_v = 0.5*np.log((1+x_v**2)/(1+x_star**2))
            ax.scatter([t_v],[N_v],s=100,c=col,zorder=5)
            ax.annotate(lab,(t_v,N_v),xytext=(10,5),
                        textcoords='offset points',color=col,fontsize=7.5)

    ax.axvline(t_star,color=PURP,lw=1.5,ls='--',alpha=0.7,label=f't*={t_star/t_Pl:.1f}t_Pl (SM-derived)')
    ax.set(xlabel='Cosmic time  t  [s]',ylabel='N_efolds from t*',
           title='Panel 6: TUO E-Folds vs Inflation Requirement\nNo inflaton needed — wavepacket gives N≈76')
    ax.set_ylim(-5,120); ax.legend(fontsize=7.5)

def p7_speed(ax):
    t=np.logspace(np.log10(t_Pl*0.1),np.log10(t_0),2000)
    v=v_exp(t)/c
    ax.semilogx(t/t_Pl,v,color=TEAL,lw=2.5,label='v_TUO(t) = c·x/√(1+x²)  [x=ct/l_Pl]')
    ax.axhline(1.0,color=CORAL,lw=2,ls='--',label='v = c  (hard ceiling)')
    ax.fill_between(t/t_Pl,v,1.0,color=CORAL,alpha=0.12)
    ax.fill_between(t/t_Pl,1.0,2.8,color='#3A1515',alpha=0.25)
    ax.text(1e10,1.9,'Standard inflation requires\nv >> c  (super-luminal)',
            color='#FF9090',fontsize=8,ha='center',
            bbox=dict(boxstyle='round',fc='#2A0000',ec='#FF6060',alpha=0.7))
    ax.text(1e30,0.4,'TUO: v < c  always\n(Heisenberg + flat Minkowski)\nw=-1 at t_Pl WITHOUT v>c',
            color=TEAL,fontsize=8,ha='center',
            bbox=dict(boxstyle='round',fc='#001A20',ec=TEAL,alpha=0.75))
    ax.set(xlabel='t / t_Pl',ylabel='v / c',
           title='Panel 7: Sub-Luminal Expansion — Hard Theorem\nde Sitter behavior achieved without v>c',
           ylim=(0,2.8))
    ax.legend(fontsize=8)

def p8_thermal(ax):
    t=np.logspace(np.log10(t_Pl),np.log10(t_0),3000)
    ax.loglog(t,T_at_t(t),color=TEAL,lw=2.5,
              label=f'TUO: T_TUO = {T_TUO/T_Pl:.3f}T_Pl (SM-derived)')
    ax.loglog(t,T_Pl*np.sqrt(t_Pl/t),color=CORAL,lw=1.5,ls='--',
              label='Dogmatic T₀=T_Pl (not derived)')
    for lab,tv,T,col in [('GUT',1e-38,1e28,GREEN),('EW',1e-12,1.5e15,PURP),
                          ('QCD',1e-5,1.5e12,CORAL),('BBN',100,5e9,'#88FF88')]:
        ax.axvline(tv,color=col,lw=0.7,ls=':',alpha=0.6)
        ax.scatter([tv],[T],s=40,c=col,zorder=5)
        ax.text(tv*1.4,T*1.8,lab,color=col,fontsize=7)
    ax.set(xlabel='t  [s]',ylabel='T  [K]',
           title='Panel 8: Thermal History\nT_TUO derived from g*, not assumed equal to T_Pl',
           xlim=(t_Pl,t_0),ylim=(1e2,3e32))
    ax.legend(fontsize=7.5)

def p9_energy(ax):
    T0=np.logspace(31,33,200)
    E_std=(np.pi**2/30)*g_star*(k_B*T0)**4/hbarc**3*l_Pl**3
    ax.loglog(T0,E_std,color=CORAL,lw=2.5,label='Standard cosmology: (π²/30)g*T⁴V_Pl')
    ax.axhline(E_cell,color=TEAL,lw=2.5,label=f'TUO: (g*/2)E_Pl = {E_cell:.3e} J')
    E_std_Pl=(np.pi**2/30)*g_star*(k_B*T_Pl)**4/hbarc**3*l_Pl**3
    ax.scatter([T_TUO],[E_cell],s=150,c=TEAL,zorder=6,marker='*')
    ax.text(T_TUO*1.1,E_cell*2.5,f'T_TUO\n={T_TUO/T_Pl:.3f}T_Pl',color=TEAL,fontsize=7.5)
    ax.annotate('',xy=(T_Pl,E_std_Pl),xytext=(T_Pl,E_cell),
                arrowprops=dict(arrowstyle='<->',color=WHITE,lw=1.5))
    ax.text(T_Pl*0.55,(E_cell*E_std_Pl)**0.5,f'Factor\n15/π²=1.52',
            color=WHITE,fontsize=8,ha='center')
    ax.set(xlabel='T₀  [K]',ylabel='E_cell  [J]',
           title='Panel 9: Energy Prediction\nFactor 15/π²: pure number, no free parameters')
    ax.legend(fontsize=7.5)

def p10_hubble(ax):
    t=np.logspace(np.log10(t_Pl*0.5),np.log10(t_0),2000)
    H0=H_TUO(t_Pl)
    ax.loglog(t/t_Pl,H_TUO(t)/H0,color=TEAL,lw=2.5,label='H_TUO = c²t/(l_Pl²+c²t²)')
    ax.loglog(t/t_Pl,1/(2*t*H0*t_Pl),color=CORAL,lw=1.5,ls='--',label='H=1/(2t) rad.dom.')
    ax.loglog(t/t_Pl,2/(3*t*H0*t_Pl),color=PURP,lw=1.2,ls=':',label='H=2/(3t) mat.dom.')
    ax.axvline(1,color=GOLD,lw=1.5,ls=':',alpha=0.8)
    ax.text(1.5,1.5,'Exact match\nH_TUO=H_FRW\nat t=t_Pl ✓',
            color=GOLD,fontsize=8,bbox=dict(boxstyle='round',fc='#1A1400',ec=GOLD,alpha=0.8))
    ax.set(xlabel='t / t_Pl',ylabel='H(t) / H(t_Pl)',
           title='Panel 10: Hubble Parameter\nTUO derives H(t_Pl)=1/(2t_Pl) without GR')
    ax.legend(fontsize=7.5)

def p11_backward(ax):
    """Panel 11: Backward calculations from observables to initial conditions"""
    ax.axis('off')

    title = "Panel 11: Backward Calculations — Observables → Initial Conditions"
    ax.text(0.5,0.97,title,transform=ax.transAxes,ha='center',va='top',
            color=WHITE,fontsize=9.5,fontweight='bold')

    arrows = [
        # (observable, TUO derivation, initial condition, color)
        (0.12, r'$\Omega_{obs}=1.0007\pm0.004$',
               r'$\Omega=1$ exact  (Axiom I)', TEAL),
        (0.28, r'$H_0=67.4$ km/s/Mpc',
               r'Back-extrapolate: $H(t_{Pl})=1/(2t_{Pl})$\nTUO derives this from wavepacket', GREEN),
        (0.47, r'$Y_p=0.245\pm0.003$ (He-4)',
               r'Same $g_*=106.75$ as standard;\n$T_0=T_{TUO}=1.110\,T_{Pl}$ (SM-derived)', GOLD),
        (0.63, r'$\eta=6.12\times10^{-10}$ (baryons)',
               r'$B-L=0$: matter-only allowed\n$B=L\neq0$ → explains asymmetry (qualitative)', CORAL),
        (0.79, r'$\Delta T/T\sim10^{-5}$ (CMB)',
               r'$\Delta E/E_{cell}\sim1/\sqrt{g_*}\approx10\%$\nNeeds $\sim4$ decades GR suppression\n'
               r'(OPEN PROBLEM — next calculation)', PURP),
    ]
    for y, obs, tuo, col in arrows:
        # Left box: observable
        ax.text(0.02, y+0.05, obs, transform=ax.transAxes,
                fontsize=8.5, color=WHITE, va='center',
                bbox=dict(boxstyle='round,pad=0.3',fc='#0A1525',ec=col,alpha=0.9))
        # Arrow
        ax.annotate('',xy=(0.55,y+0.05),xytext=(0.42,y+0.05),
                    xycoords='axes fraction',
                    arrowprops=dict(arrowstyle='->',color=col,lw=2))
        ax.text(0.47,y+0.07,'TUO',transform=ax.transAxes,
                fontsize=6.5,color=col,ha='center')
        # Right box: TUO result
        ax.text(0.58, y+0.05, tuo, transform=ax.transAxes,
                fontsize=8, color=WHITE, va='center',
                bbox=dict(boxstyle='round,pad=0.3',fc='#0A1525',ec=col,alpha=0.9))

def p12_couplings(ax):
    E=np.logspace(2,19,1000)
    ax.semilogx(E,alpha_s(E),color=CORAL,lw=2.5,label='αs (strong)')
    ax.semilogx(E,alpha_em(E),color=GOLD,lw=2.5,label='αem (EM)')
    # Weak: rough
    a2 = 0.034/(1+0.034*0.006*np.log(np.maximum(E,91.2)/91.2))
    ax.semilogx(E,np.where(a2>0,a2,np.nan),color=TEAL,lw=2.5,label='α₂ (weak)')
    ax.axvline(E_Pl_GeV,color=WHITE,lw=2,ls='--',label=f'E_Pl')
    ax.text(E_Pl_GeV*0.3,0.025,'Coupling\nconvergence\nat E_Pl:\ng*=106.75\nfrom SM',
            color=WHITE,fontsize=7.5,ha='center',
            bbox=dict(boxstyle='round',fc='#0A0A2A',ec=WHITE,alpha=0.75))
    ax.set(xlabel='E  [GeV]',ylabel='α',
           title='Panel 12: Coupling Unification at E_Pl\ng*=106.75 counts ALL modes at this scale',
           ylim=(0,0.14))
    ax.legend(fontsize=7.5)

def p13_qcorrection(ax):
    t=np.logspace(np.log10(t_Pl),np.log10(t_0),2000)
    dv=3*(l_Pl/(c*t))**2
    ax.loglog(t/t_Pl,dv,color=GOLD,lw=2.5,label='ΔV/V = 3(l_Pl/ct)²')
    ax.axhline(1,color=WHITE,lw=0.7,ls='--',alpha=0.5)
    for lab,tv,col in [('t_Pl\n(ΔV/V=3)',t_Pl,GOLD),
                        ('1 s\n(10⁻⁸⁶)',1.0/t_Pl,GREEN),
                        ('Now\n(10⁻¹²²)',t_0/t_Pl,PURP)]:
        dv_pt=3*(l_Pl/(c*tv*t_Pl))**2
        ax.scatter([tv],[dv_pt],s=70,c=col,zorder=5)
        ax.annotate(lab,(tv,dv_pt),xytext=(8,4),textcoords='offset points',color=col,fontsize=7)
    ax.set(xlabel='t / t_Pl',ylabel='ΔV/V',
           title='Panel 13: Quantum Volume Correction\nNew TUO prediction — order 1 at t_Pl',
           ylim=(1e-130,100))
    ax.text(0.05,0.12,'ΔV/V = 3(l_Pl/ct)²\nUnique TUO prediction',
            transform=ax.transAxes,color=GOLD,fontsize=8,
            bbox=dict(boxstyle='round',fc='#1A1400',ec=GOLD,alpha=0.8))
    ax.legend(fontsize=8)

def p14_timeline(ax):
    ax.set_xlim(-0.5,13.5); ax.set_ylim(-1.2,4.8); ax.axis('off')
    ax.annotate('',xy=(13.2,0.5),xytext=(-0.3,0.5),
                arrowprops=dict(arrowstyle='->',color=WHITE,lw=2.5))
    ax.text(13.3,0.5,'t →',color=WHITE,va='center',fontsize=10,fontweight='bold')

    events=[
        (0,'t<0\n(eternal)','Flat Minkowski\nZero-Sum Zoo\nP(universe)→1\nin infinite time',NAVY),
        (1.5,'t*=7.3t_Pl\n(SM-derived)','MAXIMAL FLUCTUATION\ng*=106.75 modes\nT_TUO=1.11T_Pl\nAll cells simultaneously',TEAL),
        (3,'t_Pl\n(5.4×10⁻⁴⁴s)','w=-1 de Sitter\nat handoff point\nH=1/(2t_Pl) exact\nTUO→FRW junction',GOLD),
        (4.5,'t~10⁻³⁵s\n(GUT)','~17 e-folds\nfrom t*\nForce separation\nbegins',GREEN),
        (6,'t~10⁻¹²s\n(EW)','~76 e-folds\nfrom t*\nEW symmetry breaks\nHiggs mechanism','#FF8844'),
        (7.5,'t~10⁻⁵s\n(QCD)','~90 e-folds\nQuarks confined\nProtons, neutrons','#FFAA44'),
        (9,'t~100s\n(BBN)','Y_p=0.247\nH,He,Li form\nMatches obs ✓','#88FF88'),
        (10.5,'t~380kyr\n(CMB)','ΔT/T~10⁻⁵\nOpen problem:\ncell fluctuation\namplitude','#8888FF'),
        (12.5,'t=13.8Gyr\n(now)','Ω=1 exact ✓\nE_tot=0 exact ✓\nObservers\nmeasure TUO',GOLD),
    ]
    for i,(x,epoch,desc,col) in enumerate(events):
        ax.plot([x,x],[0.3,0.7],color=col,lw=2.5)
        ax.text(x,0.1,epoch,color=col,ha='center',va='top',fontsize=6.8,fontweight='bold')
        yb=2.2 if i%2==0 else 3.8
        ax.text(x,yb,desc,color=WHITE,ha='center',va='center',fontsize=6.5,
                multialignment='center',
                bbox=dict(boxstyle='round,pad=0.35',fc='#0D1B2A',ec=col,lw=1.5,alpha=0.92))
        ax.plot([x,x],[0.7 if yb>1 else 0.3,yb-0.35],
                color=col,lw=0.8,ls='--',alpha=0.55)
    ax.add_patch(FancyBboxPatch((-0.4,-1.15),2.85,0.9,boxstyle='round',
                                fc='#05101A',ec=TEAL,lw=1.8,alpha=0.9))
    ax.text(0.9,-0.7,'TUO DOMAIN  (pre-Planck, flat Minkowski spacetime, Axioms I+II)',
            color=TEAL,ha='center',va='center',fontsize=7.5,fontweight='bold')
    ax.add_patch(FancyBboxPatch((2.7,-1.15),10.7,0.9,boxstyle='round',
                                fc='#05051A',ec=CORAL,lw=1.8,alpha=0.9))
    ax.text(8.05,-0.7,'BIG BANG DOMAIN  (t > t_Pl — GR+QFT, standard cosmology)',
            color=CORAL,ha='center',va='center',fontsize=7.5,fontweight='bold')
    ax.set_title('Panel 14: Complete TUO Timeline\n'
                 't* (SM-derived), w=-1 at t_Pl, ~76 e-folds to EW without inflaton',
                 color=WHITE,fontsize=9.5,fontweight='bold',pad=8)

# ══════════════════════════════════════════════════════════════════════════
# COMPOSE
# ══════════════════════════════════════════════════════════════════════════

if __name__=='__main__':
    print(f"TUO Simulation v2")
    print(f"SM-derived emergence: T_TUO={T_TUO:.3e}K = {T_TUO/T_Pl:.4f}T_Pl")
    print(f"SM-derived timescale: t* = {t_star/t_Pl:.2f} t_Pl")
    print(f"w_eff at t=t_Pl:  w = {w_eff(1):.4f}  (de Sitter)")
    print(f"N_cells={N_cells:.2e}, E_cell={E_cell:.4e}J")

    fig=plt.figure(figsize=(30,44)); fig.patch.set_facecolor(BG)
    fig.text(0.5,0.988,'THEORY OF UNIVERSAL ORIGINS — EVOLUTION SIMULATION v2',
             ha='center',va='top',color=WHITE,fontsize=17,fontweight='bold')
    fig.text(0.5,0.982,
             'Romeo Matshaba  ·  2026  ·  All scales SM-derived  ·  No free parameters',
             ha='center',va='top',color=GOLD,fontsize=11,style='italic')
    fig.text(0.5,0.977,
             f'T_TUO = (15/π²)^(1/4) T_Pl = {T_TUO/T_Pl:.4f} T_Pl  |  '
             f't* = 7.31 t_Pl  |  w_eff(t_Pl) = -1 (de Sitter)  |  '
             f'N_efolds(t*→EW) = 76.4',
             ha='center',va='top',color=TEAL,fontsize=9)

    gs=gridspec.GridSpec(5,3,figure=fig,hspace=0.42,wspace=0.33,
                         top=0.974,bottom=0.015,left=0.06,right=0.97)
    panels=[
        (fig.add_subplot(gs[0,0]),p1_zoo),
        (fig.add_subplot(gs[0,1]),p2_config),
        (fig.add_subplot(gs[0,2]),p3_simultaneous),
        (fig.add_subplot(gs[1,0]),p4_expansion),
        (fig.add_subplot(gs[1,1]),p5_w_eff),
        (fig.add_subplot(gs[1,2]),p6_efolds),
        (fig.add_subplot(gs[2,0]),p7_speed),
        (fig.add_subplot(gs[2,1]),p8_thermal),
        (fig.add_subplot(gs[2,2]),p9_energy),
        (fig.add_subplot(gs[3,0]),p10_hubble),
        (fig.add_subplot(gs[3,1]),p11_backward),
        (fig.add_subplot(gs[3,2]),p12_couplings),
        (fig.add_subplot(gs[4,0]),p13_qcorrection),
        (fig.add_subplot(gs[4,1:]),p14_timeline),
    ]
    for ax,fn in panels:
        try: fn(ax)
        except Exception as e:
            ax.text(0.5,0.5,f'Error:\n{e}',transform=ax.transAxes,
                    ha='center',va='center',color=CORAL,fontsize=9)
            import traceback; traceback.print_exc()

    out='/mnt/user-data/outputs/tuo_evolution_v2.png'
    fig.savefig(out,dpi=140,bbox_inches='tight',facecolor=BG)
    plt.close(fig)
    print(f"Saved: {out}")
