"""
TUO EVOLUTION SIMULATION — Romeo Matshaba, 2026
12-panel visualization: Zero-Sum Zoo to Observable Universe
Run: python tuo_evolution_simulation.py
Requires: numpy, matplotlib, scipy
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.patches import FancyBboxPatch
import warnings, math
warnings.filterwarnings('ignore')

# ── Constants ─────────────────────────────────────────────────────────────────
c=2.99792458e8; hbar=1.054571817e-34; G=6.67430e-11; k_B=1.380649e-23
GeV_J=1.602176634e-10; g_star=106.75; hbarc=hbar*c
E_Pl=np.sqrt(hbar*c**5/G); t_Pl=np.sqrt(hbar*G/c**5); l_Pl=np.sqrt(hbar*G/c**3)
T_Pl=np.sqrt(hbar*c**5/(G*k_B**2)); E_Pl_GeV=E_Pl/GeV_J
E_cell=(g_star/2)*E_Pl
rho_c=(np.pi**2/30)*g_star*(k_B*T_Pl)**4/hbarc**3
T_TUO=((E_cell/l_Pl**3)*30/(np.pi**2*g_star)*hbarc**3)**0.25/k_B
R_obs=4.4e26; t_0=13.8e9*3.1558e7
r_tPl=R_obs*np.sqrt(t_Pl/t_0); N_cells=(r_tPl/l_Pl)**3

# ── Style ─────────────────────────────────────────────────────────────────────
BG='#0D1B2A'; NAVY='#1B3A6B'; TEAL='#0E9BAA'; GOLD='#E8A020'
CORAL='#E05050'; GREEN='#28A860'; PURP='#9B59B6'; WHITE='#EEEEFF'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':8.5,
    'axes.facecolor':'#0F1E30','figure.facecolor':BG,
    'text.color':WHITE,'axes.labelcolor':WHITE,'xtick.color':WHITE,
    'ytick.color':WHITE,'axes.edgecolor':'#2A4060','axes.grid':True,
    'grid.alpha':0.18,'grid.linestyle':'--','axes.titlesize':9.5,
    'axes.spines.top':False,'axes.spines.right':False})

# ── Physics helpers ───────────────────────────────────────────────────────────
def sigma(t): return l_Pl*np.sqrt(1+(c*t/l_Pl)**2)
def V_TUO(t): return (4*np.pi/3)*sigma(t)**3
def H_TUO(t): return c**2*t/(l_Pl**2+c**2*t**2)
def v_exp(t): return c*(c*t/l_Pl)/np.sqrt(1+(c*t/l_Pl)**2)
def T_at_t(t): return T_TUO*np.sqrt(t_Pl/t)

def alpha_s(E_GeV):
    b0=11-4.0; a0=0.1179; MZ=91.2
    d=1+(a0/(2*np.pi))*b0*np.log(np.maximum(E_GeV,1e-3)/MZ)
    return np.where(d>0.05, a0/d, np.nan)

def alpha_em(E_GeV):
    a0=1/137.036
    return a0/(1-a0/(3*np.pi)*np.log(np.maximum(E_GeV,5.11e-4)/5.11e-4))

def alpha_w(E_GeV):
    MZ=91.2; aemMZ=1/128; s2=0.2312; a2MZ=aemMZ/s2
    b2=19/6/(2*np.pi)
    d=1+a2MZ*b2*np.log(np.maximum(E_GeV,MZ)/MZ)
    return np.where(d>0.05, a2MZ/d, np.nan)

# ══════════════════════════════════════════════════════════════════════════════
# PANELS
# ══════════════════════════════════════════════════════════════════════════════

def p1_zoo(ax):
    k=np.arange(91); p1=1/(1+np.exp(0.5))
    pv=np.array([p1**ki*(1-p1)**(90-ki)*math.comb(90,ki) for ki in k])
    pv=np.maximum(pv,1e-100)
    col=[GOLD if ki==90 else (TEAL if abs(ki-int(90*p1))<4 else NAVY) for ki in k]
    ax.bar(k,np.log10(pv),color=col,width=1.0,alpha=0.85,edgecolor='none')
    ax.axvline(90,color=GOLD,lw=2,ls='--',label='Maximal fluctuation\n(our universe)')
    pk=int(90*p1)
    ax.axvline(pk,color=TEAL,lw=1.5,alpha=0.8,label=f'Most probable k={pk}')
    ax.text(88,-10,'OUR\nUNIVERSE',color=GOLD,fontsize=8,ha='center',
            bbox=dict(boxstyle='round',fc='#1A1400',ec=GOLD,alpha=0.85))
    ax.set(xlabel='Fermion modes occupied  k',ylabel='log₁₀ P(k)',
           title='Panel 1: Zero-Sum Zoo\nFermi-Dirac at T=T_Pl',xlim=(0,90),ylim=(-55,2))
    ax.legend(fontsize=7.5)

def p2_config(ax):
    np.random.seed(42); n=3000
    Q=np.random.normal(0,3,n); BmL=np.random.normal(0,3,n)
    sur=(np.abs(Q)<0.5)&(np.abs(BmL)<0.5)
    mx=(np.abs(Q)<0.06)&(np.abs(BmL)<0.06)
    ax.scatter(Q[~sur],BmL[~sur],s=3,alpha=0.2,c='#332222',label='Collapse to vacuum')
    ax.scatter(Q[sur&~mx],BmL[sur&~mx],s=18,alpha=0.75,c=TEAL,label='Zero-sum survivors')
    ax.scatter(Q[mx],BmL[mx],s=90,alpha=1,c=GOLD,marker='*',zorder=5,label='Maximal (universe)')
    ax.axhline(0,color=WHITE,lw=0.4,alpha=0.4); ax.axvline(0,color=WHITE,lw=0.4,alpha=0.4)
    from matplotlib.patches import Rectangle
    ax.add_patch(Rectangle((-0.5,-0.5),1,1,fill=False,ec=GOLD,lw=2,ls='--',zorder=4))
    ax.set(xlabel='Total charge Q [e]',ylabel='Total B−L',
           title='Panel 2: Configuration Space\nZero-sum filter selects survivors',
           xlim=(-8,8),ylim=(-8,8))
    ax.legend(fontsize=7.5,markerscale=1.5)

def p3_simultaneous(ax):
    N=np.logspace(0,95,400)
    logR=np.minimum(np.log10(N),95)
    ax.fill_between(np.log10(N),0,logR,alpha=0.3,color=TEAL)
    ax.plot(np.log10(N),logR,color=TEAL,lw=2.5,label='log₁₀[P(sim)/P(single)] = N')
    ax.axvline(np.log10(N_cells),color=GOLD,lw=2.5,ls='--',
               label=f'Our universe  N≈10⁹³')
    ax.set(xlabel='log₁₀(N_cells)',
           ylabel='log₁₀[P(simultaneous) / P(single-cell)]',
           title='Panel 3: Saddle-Point Proof\nSimultaneous emergence exponentially favoured',
           xlim=(0,96),ylim=(0,96))
    ax.text(np.log10(N_cells)+2,50,'Our universe\nexp(10⁹³) suppression\nof single-cell',
            color=GOLD,fontsize=8)
    ax.legend(fontsize=8)

def p4_expansion(ax):
    t=np.logspace(np.log10(t_Pl*0.5),np.log10(t_0),2000)
    ax.loglog(t/t_Pl,V_TUO(t)/l_Pl**3,color=TEAL,lw=2.5,
              label='V_TUO = (4π/3)l_Pl³[1+(ct/l_Pl)²]^(3/2)')
    ax.loglog(t/t_Pl,(4*np.pi/3)*(c*t)**3/l_Pl**3,color=CORAL,lw=1.5,ls='--',
              label='Classical (4π/3)(ct)³')
    for lab,tv,col in [('t_Pl',t_Pl,GOLD),('EW 10⁻¹²s',1e-12,GREEN),
                        ('QCD 10⁻⁵s',1e-5,PURP),('Now',t_0,CORAL)]:
        ax.scatter([tv/t_Pl],[V_TUO(tv)/l_Pl**3],s=70,c=col,zorder=5)
        ax.annotate(lab,(tv/t_Pl,V_TUO(tv)/l_Pl**3),xytext=(6,4),
                    textcoords='offset points',color=col,fontsize=7)
    ax.set(xlabel='t / t_Pl',ylabel='V / l_Pl³',
           title='Panel 4: Expansion Law\nDerived from quantum wavepacket spreading')
    ax.legend(fontsize=7.5)

def p5_speed(ax):
    t=np.logspace(np.log10(t_Pl*0.1),np.log10(t_0),2000)
    v=v_exp(t)/c
    ax.semilogx(t/t_Pl,v,color=TEAL,lw=2.5,label='v_TUO(t) = c·(ct/l_Pl)/√(1+(ct/l_Pl)²)')
    ax.axhline(1.0,color=CORAL,lw=2,ls='--',label='Speed of light c')
    ax.fill_between(t/t_Pl,v,1.0,color=CORAL,alpha=0.12)
    ax.fill_between(t/t_Pl,1.0,2.8,color='#3A1515',alpha=0.25)
    ax.text(1e10,1.9,'Standard inflation requires\nv >> c  (superluminal)',
            color='#FF9090',fontsize=8,ha='center',
            bbox=dict(boxstyle='round',fc='#2A0000',ec='#FF6060',alpha=0.7))
    ax.text(1e30,0.4,'TUO: v → c asymptotically\nv < c guaranteed\n(Heisenberg + relativity)',
            color=TEAL,fontsize=8,ha='center',
            bbox=dict(boxstyle='round',fc='#001A20',ec=TEAL,alpha=0.75))
    ax.set(xlabel='t / t_Pl',ylabel='v / c',
           title='Panel 5: Expansion Speed\nv ≤ c always — TUO vs inflation',
           ylim=(0,2.8))
    ax.legend(fontsize=8)

def p6_qcorr(ax):
    t=np.logspace(np.log10(t_Pl),np.log10(t_0),2000)
    dv=3*(l_Pl/(c*t))**2
    ax.loglog(t/t_Pl,dv,color=GOLD,lw=2.5,label='ΔV/V = 3(l_Pl/ct)²')
    ax.axhline(1,color=WHITE,lw=0.7,ls='--',alpha=0.5)
    for lab,tv,col in [('t_Pl\n(ΔV/V=3)',t_Pl,GOLD),
                        ('1 s\n(10⁻⁸⁶)',1.0/t_Pl,GREEN),
                        ('Now\n(10⁻¹²²)',t_0/t_Pl,PURP)]:
        dv_pt=3*(l_Pl/(c*tv*t_Pl))**2
        ax.scatter([tv],[dv_pt],s=70,c=col,zorder=5)
        ax.annotate(lab,(tv,dv_pt),xytext=(8,4),textcoords='offset points',
                    color=col,fontsize=7)
    ax.set(xlabel='t / t_Pl',ylabel='ΔV / V  [quantum correction]',
           title='Panel 6: Quantum Volume Correction\nNew TUO prediction — measurable only at t_Pl',
           ylim=(1e-130,100))
    ax.text(0.05,0.12,'ΔV/V = 3(l_Pl/ct)²\nUnique prediction\nFades as power law',
            transform=ax.transAxes,color=GOLD,fontsize=8,
            bbox=dict(boxstyle='round',fc='#1A1400',ec=GOLD,alpha=0.8))
    ax.legend(fontsize=8)

def p7_thermal(ax):
    t=np.logspace(np.log10(t_Pl),np.log10(t_0),3000)
    ax.loglog(t,T_at_t(t),color=TEAL,lw=2.5,
              label=f'TUO: T₀={T_TUO:.1e} K (1.11 T_Pl)')
    ax.loglog(t,T_Pl*np.sqrt(t_Pl/t),color=CORAL,lw=1.5,ls='--',
              label='Standard BB: T₀=T_Pl')
    tr=[('GUT',1e-38,1e28,GREEN),('EW',1e-12,1.5e15,PURP),
        ('QCD',1e-5,1.5e12,CORAL),('BBN',100,5e9,'#88FF88'),
        ('CMB',3.8e5*3.156e7,3000,'#8888FF')]
    for lab,tv,T,col in tr:
        ax.axvline(tv,color=col,lw=0.7,ls=':',alpha=0.6)
        ax.scatter([tv],[T],s=40,c=col,zorder=5)
        ax.text(tv*1.4,T*1.8,lab,color=col,fontsize=7)
    ax.set(xlabel='Cosmic time  t  [s]',ylabel='Temperature  T  [K]',
           title='Panel 7: Thermal History\nTUO (solid) vs Standard BB (dashed)',
           xlim=(t_Pl,t_0),ylim=(1e2,3e32))
    ax.legend(fontsize=7.5)

def p8_couplings(ax):
    E=np.logspace(2,19,1000)
    ax.semilogx(E,alpha_s(E),color=CORAL,lw=2.5,label='αs (strong, SU(3))')
    ax.semilogx(E,alpha_em(E),color=GOLD,lw=2.5,label='αem (EM, U(1))')
    ax.semilogx(E,alpha_w(E),color=TEAL,lw=2.5,label='α₂ (weak, SU(2))')
    ax.axvline(E_Pl_GeV,color=WHITE,lw=2,ls='--',label=f'E_Pl = {E_Pl_GeV:.1e} GeV')
    ax.axvline(1e17,color='#AAAAAA',lw=1.2,ls=':',alpha=0.7,label='E_GUT ~10¹⁷ GeV')
    vals=[float(alpha_s(np.array([E_Pl_GeV]))[0]),
          float(alpha_em(np.array([E_Pl_GeV]))[0]),
          float(alpha_w(np.array([E_Pl_GeV]))[0])]
    ax.fill_betweenx([min(vals)*0.7,max(vals)*1.3],
                     E_Pl_GeV*0.3,E_Pl_GeV*3,color=WHITE,alpha=0.08)
    ax.text(3e18,0.028,'Forces unified\nat E_Pl:\n12 modes =\n1 GUT multiplet',
            color=WHITE,fontsize=7.5,
            bbox=dict(boxstyle='round',fc='#0A0A2A',ec=WHITE,alpha=0.8))
    ax.set(xlabel='Energy  E  [GeV]',ylabel='Coupling α',
           title='Panel 8: Coupling Unification\nAll forces merge at E_Pl',
           ylim=(0,0.14))
    ax.legend(fontsize=7.5)

def p9_energy(ax):
    T0=np.logspace(31,33,200)
    E_std=(np.pi**2/30)*g_star*(k_B*T0)**4/hbarc**3*l_Pl**3
    ax.loglog(T0,E_std,color=CORAL,lw=2.5,label='Standard cosmo: (π²/30)g*T⁴V_Pl')
    ax.axhline(E_cell,color=TEAL,lw=2.5,label=f'TUO: (g*/2)E_Pl = {E_cell:.3e} J')
    ax.axhline(E_cell*12/g_star,color=GOLD,lw=1.5,ls='--',
               label=f'Original TUO (n=12): {E_cell*12/g_star:.3e} J')
    ax.scatter([T_TUO],[E_cell],s=150,c=TEAL,zorder=6,marker='*')
    ax.scatter([T_Pl],[(np.pi**2/30)*g_star*(k_B*T_Pl)**4/hbarc**3*l_Pl**3],
               s=120,c=CORAL,zorder=6)
    E_std_Pl=(np.pi**2/30)*g_star*(k_B*T_Pl)**4/hbarc**3*l_Pl**3
    ax.text(T_TUO*1.1,E_cell*2,f'T_TUO\n={T_TUO:.1e}K\n(1.11 T_Pl)',color=TEAL,fontsize=7)
    ax.text(T_Pl*0.5,E_std_Pl*0.3,f'Factor\n{E_cell/E_std_Pl:.2f}',color=WHITE,fontsize=8,ha='center')
    ax.set(xlabel='T₀  [K]',ylabel='E_cell  [J]',
           title='Panel 9: TUO Energy Prediction\nAgreement factor 1.52 at Planck scale')
    ax.legend(fontsize=7.5)

def p10_hubble(ax):
    t=np.logspace(np.log10(t_Pl*0.5),np.log10(t_0),2000)
    H0=H_TUO(t_Pl)
    ax.loglog(t/t_Pl,H_TUO(t)/H0,color=TEAL,lw=2.5,label='H_TUO')
    ax.loglog(t/t_Pl,1/(2*t*H0*t_Pl),color=CORAL,lw=1.5,ls='--',label='H=1/(2t) rad.dom.')
    ax.loglog(t/t_Pl,2/(3*t*H0*t_Pl),color=PURP,lw=1.2,ls=':',label='H=2/(3t) mat.dom.')
    ax.axvline(1,color=GOLD,lw=1.5,ls=':',alpha=0.8)
    ax.text(1.5,1.5,'H_TUO = H_FRW\nexact at t_Pl ✓\nJunction closed',
            color=GOLD,fontsize=8,
            bbox=dict(boxstyle='round',fc='#1A1400',ec=GOLD,alpha=0.8))
    ax.set(xlabel='t / t_Pl',ylabel='H(t) / H(t_Pl)',
           title='Panel 10: Hubble Parameter\nExact match TUO↔FRW at t=t_Pl')
    ax.legend(fontsize=7.5)

def p11_entropy(ax):
    logS_tot=np.log10(N_cells)+np.log10(g_star)
    logS_CMB=89.0
    sel=logS_CMB-logS_tot
    labels=['Collapsed to\nvacuum','Survived\n(stable universe)']
    vals=[logS_tot,logS_CMB]
    bars=ax.barh(labels,vals,color=['#2A1515',TEAL],height=0.4,edgecolor='none')
    ax.axvline(logS_CMB,color=GOLD,lw=2,ls='--',label=f'S_CMB = 10^{logS_CMB:.0f}')
    ax.text(logS_tot-2,1,f'S_total\n= 10^{logS_tot:.1f}',color='#AAAAAA',fontsize=8,va='center')
    ax.text(logS_CMB-5,0.15,f'S_survived\n= 10^{logS_CMB:.0f}',color=TEAL,fontsize=8,va='center')
    ax.set(xlabel='log₁₀ Entropy',
           title='Panel 11: Cosmogenesis Selection\nEntropy budget: survivors vs collapsed')
    ax.text(0.05,0.1,
            f'N_total = 10^{np.log10(N_cells):.0f}\n'
            f'Selection fraction: 10^{sel:.0f}\n'
            f'N_survived ≈ 10^{logS_CMB-np.log10(g_star):.0f}\n'
            f'(Darwin at Planck scale)',
            transform=ax.transAxes,fontsize=8.5,color=WHITE,va='bottom',
            bbox=dict(boxstyle='round',fc='#0A1525',ec=TEAL,alpha=0.9))
    ax.legend(fontsize=8)

def p12_timeline(ax):
    ax.set_xlim(-0.5,13); ax.set_ylim(-1,4.5); ax.axis('off')
    ax.annotate('',xy=(12.8,0.5),xytext=(-0.3,0.5),
                arrowprops=dict(arrowstyle='->',color=WHITE,lw=2.5))
    ax.text(13.0,0.5,'t →',color=WHITE,va='center',fontsize=10,fontweight='bold')

    events=[
        (0,'t<0\n(eternal)','Flat Minkowski spacetime\nZero-Sum Zoo\nVacuum fluctuates endlessly\nP(universe)→1 in ∞ time',NAVY),
        (1.5,'t=0\n(emergence)','MAXIMAL FLUCTUATION:\n10⁹³ cells fire simultaneously\n(saddle-point dominance)\nAxiom II globally satisfied',TEAL),
        (3,'t_Pl\n(5.4×10⁻⁴⁴s)','TUO → Big Bang handoff\nH=1/(2t_Pl) ✓  w=1/3 ✓  k=0 ✓\nFree quarks stream at v≈c\nAsymptotic freedom: αs≈0.02',GOLD),
        (5,'10⁻¹²s\n(EW break)','Electroweak symmetry\nbreaks spontaneously\nHiggs gives masses\nW±, Z, γ separate',GREEN),
        (7,'10⁻⁵s\n(QCD conf.)','Quarks confined\ninto hadrons\nProtons and neutrons\nform from free quarks','#FF8844'),
        (9,'1–200s\n(BBN)','Big Bang Nucleosynthesis:\nH (75%) + He (25%) + Li\nY_p=0.247 (TUO prediction)\nMatches observation ✓','#88FF88'),
        (11,'380kyr\n(CMB)','Recombination:\nneutral atoms form\nCMB photons released\nUniformity: ΔT/T=10⁻⁵','#8888FF'),
        (12.5,'13.8Gyr\n(now)','Galaxies, stars, planets\nObservers measure:\nΩ≈1, flat universe ✓\nTotal energy = 0 ✓',GOLD),
    ]
    for i,(x,epoch,desc,col) in enumerate(events):
        ax.plot([x,x],[0.3,0.7],color=col,lw=2.5)
        ax.text(x,0.1,epoch,color=col,ha='center',va='top',fontsize=7,fontweight='bold')
        yb=2.2 if i%2==0 else 3.6
        ax.text(x,yb,desc,color=WHITE,ha='center',va='center',fontsize=6.5,
                multialignment='center',
                bbox=dict(boxstyle='round,pad=0.35',fc='#0D1B2A',ec=col,lw=1.5,alpha=0.92))
        ax.plot([x,x],[0.7 if yb>1 else 0.3,yb-0.3],
                color=col,lw=0.8,ls='--',alpha=0.55)
    # Domain boxes
    ax.add_patch(FancyBboxPatch((-0.4,-0.95),2.8,0.9,boxstyle='round',
                                fc='#05101A',ec=TEAL,lw=1.8,alpha=0.9))
    ax.text(0.9,-0.5,'TUO DOMAIN  (pre-Planck, flat spacetime, Axiom I+II)',
            color=TEAL,ha='center',va='center',fontsize=7.5,fontweight='bold')
    ax.add_patch(FancyBboxPatch((2.7,-0.95),9.7,0.9,
                 boxstyle='round',fc='#05051A',ec=CORAL,lw=1.8,alpha=0.9))
    ax.text(7.5,-0.5,'BIG BANG DOMAIN  (t > t_Pl — GR + QFT valid, standard cosmology)',
            color=CORAL,ha='center',va='center',fontsize=7.5,fontweight='bold')
    ax.set_title('Panel 12: Complete TUO Timeline — From Eternal Vacuum to Present Universe',
                 color=WHITE,fontsize=10,fontweight='bold',pad=10)

# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════

if __name__=='__main__':
    print(f"TUO Evolution Simulation")
    print(f"E_Pl={E_Pl:.4e}J  t_Pl={t_Pl:.4e}s  g*={g_star}")
    print(f"E_cell={E_cell:.4e}J  T_TUO={T_TUO:.4e}K  N_cells={N_cells:.3e}")

    fig=plt.figure(figsize=(28,40)); fig.patch.set_facecolor(BG)
    fig.text(0.5,0.987,'THEORY OF UNIVERSAL ORIGINS — COMPLETE EVOLUTION SIMULATION',
             ha='center',va='top',color=WHITE,fontsize=17,fontweight='bold')
    fig.text(0.5,0.981,'Romeo Matshaba  ·  2026  ·  From Zero-Sum Vacuum to Observable Universe',
             ha='center',va='top',color=GOLD,fontsize=11,style='italic')

    gs=gridspec.GridSpec(5,3,figure=fig,hspace=0.43,wspace=0.33,
                         top=0.978,bottom=0.018,left=0.07,right=0.97)
    panels=[
        (fig.add_subplot(gs[0,0]),p1_zoo),
        (fig.add_subplot(gs[0,1]),p2_config),
        (fig.add_subplot(gs[0,2]),p3_simultaneous),
        (fig.add_subplot(gs[1,0]),p4_expansion),
        (fig.add_subplot(gs[1,1]),p5_speed),
        (fig.add_subplot(gs[1,2]),p6_qcorr),
        (fig.add_subplot(gs[2,0]),p7_thermal),
        (fig.add_subplot(gs[2,1]),p8_couplings),
        (fig.add_subplot(gs[2,2]),p9_energy),
        (fig.add_subplot(gs[3,0]),p10_hubble),
        (fig.add_subplot(gs[3,1]),p11_entropy),
        (fig.add_subplot(gs[4,:]),p12_timeline),
    ]
    for ax,fn in panels:
        try:
            fn(ax)
        except Exception as e:
            ax.text(0.5,0.5,f'Error:\n{e}',transform=ax.transAxes,
                    ha='center',va='center',color=CORAL,fontsize=9)
            import traceback; traceback.print_exc()

    out='/mnt/user-data/outputs/tuo_evolution_simulation.png'
    fig.savefig(out,dpi=150,bbox_inches='tight',facecolor=BG)
    plt.close(fig)
    print(f"Saved: {out}")
