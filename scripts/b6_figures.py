"""
B6 — generate the deck's figures from the A4-verified expressions.

Outline decision 5: plot from the verified equilibrium expressions rather than
copying the paper's figures. The paper is CC BY 4.0 so copying would be allowed,
but plotting guarantees the curve is the one we checked, and lets us annotate.

Outputs SVG into slides_html/fig/ so the deck can inline or link them.

Run:  python3 scripts/b6_figures.py       (from anywhere; paths are absolute)
"""

import pathlib
import sympy as sp
import mpmath as mp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "slides_html" / "fig"
OUT.mkdir(parents=True, exist_ok=True)
mp.mp.dps = 25

INK, ACCENT, MUTED = "#1b2733", "#b3261e", "#5b6b7a"
GRID = "#dfe5ea"

# ----------------------------------------------------------------------
# Re-derive the model (identical to scripts/a4_verify_kopel2021.py)
# ----------------------------------------------------------------------
a, c, g, th, s1, s2, p1, p2, x1, x2 = sp.symbols(
    "a c gamma theta s1 s2 p1 p2 x1 x2", real=True)

sol_x = sp.solve([sp.Eq(p1, a + s1 - x1 - g * x2),
                  sp.Eq(p2, a + (s2 + th * s1) - x2 - g * x1)],
                 [x1, x2], dict=True)[0]
x1_d, x2_d = sp.simplify(sol_x[x1]), sp.simplify(sol_x[x2])
pi1 = (p1 - c) * x1_d - s1**2
pi2 = (p2 - c) * x2_d - s2**2
sol_p = sp.solve([sp.diff(pi1, p1), sp.diff(pi2, p2)], [p1, p2], dict=True)[0]
subs_p = {p1: sol_p[p1], p2: sol_p[p2]}
pi2_s = sp.simplify(pi2.subs(subs_p))
s2_of_s1 = sp.simplify(sp.solve(sp.diff(pi2_s, s2), s2)[0])
pi1_stage1 = sp.simplify(sp.simplify(pi1.subs(subs_p)).subs(s2, s2_of_s1))
s1_star = sp.simplify(sp.solve(sp.diff(pi1_stage1, s1), s1)[0])
s2_star = sp.simplify(s2_of_s1.subs(s1, s1_star))
pi1_star = sp.simplify(pi1_stage1.subs(s1, s1_star))
pi2_star = sp.simplify(pi2_s.subs({s1: s1_star, s2: s2_star}))

NUM = {a: 1, c: 0}                      # footnote 9: a - c = 1
GMAX = mp.mpf("0.8107358771227719")     # A4 §2a
f_s1 = sp.lambdify((g, th), s1_star.subs(NUM), "mpmath")
f_s2 = sp.lambdify((g, th), s2_star.subs(NUM), "mpmath")
f_p1 = sp.lambdify((g, th), pi1_star.subs(NUM), "mpmath")
f_p2 = sp.lambdify((g, th), pi2_star.subs(NUM), "mpmath")


def grid(n=400, hi=None):
    hi = hi or GMAX
    return [mp.mpf(k) / n * hi for k in range(1, n)]


def style(ax, xlabel, ylabel):
    ax.set_xlabel(xlabel, fontsize=11, color=INK)
    ax.set_ylabel(ylabel, fontsize=11, color=INK, rotation=0, labelpad=18)
    ax.grid(True, color=GRID, lw=0.7)
    ax.set_axisbelow(True)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(MUTED)
    ax.tick_params(colors=MUTED, labelsize=9)


def save(fig, name):
    fig.savefig(OUT / name, format="svg", bbox_inches="tight",
                transparent=True)
    plt.close(fig)
    print(f"  wrote slides_html/fig/{name}")


# ----------------------------------------------------------------------
# Figure A — benchmark, theta = 0 (the paper's Fig. 1)
# ----------------------------------------------------------------------
xs = grid()
y1 = [float(f_s1(x, 0)) for x in xs]
y2 = [float(f_s2(x, 0)) for x in xs]

fig, ax = plt.subplots(figsize=(7.2, 4.1))
ax.plot([float(x) for x in xs], y1, color=INK, lw=2.2, label=r"leader  $s_1^*$")
ax.plot([float(x) for x in xs], y2, color=ACCENT, lw=2.0, ls="--",
        label=r"follower  $s_2^*$")
tp = float(mp.findroot(lambda z: sp.lambdify(
    (g, th), sp.diff(s1_star.subs(NUM), g), "mpmath")(z, 0), mp.mpf("0.53")))
ax.axvline(tp, color=MUTED, lw=0.9, ls=":")
ax.annotate(f"turning point\n$\\gamma = {tp:.4f}$", xy=(tp, float(f_s1(tp, 0))),
            xytext=(tp - 0.26, 0.45), fontsize=9, color=MUTED,
            arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
ax.annotate("follower's CSR and output\nreach zero here",
            xy=(float(GMAX), 0), xytext=(0.40, 0.09), fontsize=9, color=ACCENT,
            arrowprops=dict(arrowstyle="->", color=ACCENT, lw=0.9))
ax.set_xlim(0, float(GMAX) * 1.02)
ax.set_ylim(0, 0.70)
style(ax, r"$\gamma$   (competition intensity)", r"$s^*$")
ax.legend(frameon=False, fontsize=10, loc="upper left")
save(fig, "fig-benchmark.svg")

# ----------------------------------------------------------------------
# Figure B — theta = 0.21, both U-shaped, follower above (paper's Fig. 3)
# ----------------------------------------------------------------------
T = mp.mpf("0.21")
y1 = [float(f_s1(x, T)) for x in xs]
y2 = [float(f_s2(x, T)) for x in xs]

fig, ax = plt.subplots(figsize=(7.2, 4.1))
ax.plot([float(x) for x in xs], y1, color=INK, lw=2.2, label=r"leader  $s_1^*$")
ax.plot([float(x) for x in xs], y2, color=ACCENT, lw=2.0, ls="--",
        label=r"follower  $s_2^*$")
ax.annotate("follower now invests MORE", xy=(0.45, float(f_s2(mp.mpf("0.45"), T))),
            xytext=(0.30, 0.345), fontsize=9.5, color=ACCENT,
            arrowprops=dict(arrowstyle="->", color=ACCENT, lw=0.9))
ax.set_xlim(0, float(GMAX) * 1.02)
ax.set_ylim(0.18, 0.40)
style(ax, r"$\gamma$   (competition intensity)", r"$s^*$")
ax.legend(frameon=False, fontsize=10, loc="upper right")
ax.set_title(r"$\theta = 0.21$ — inside the band where both are U-shaped",
             fontsize=10.5, color=MUTED, pad=10)
save(fig, "fig-theta021.svg")

# ----------------------------------------------------------------------
# Figure C — the three thresholds (our headline, A5-01)
# ----------------------------------------------------------------------
gs = [mp.mpf(k) / 100 for k in range(5, 81)]
fma, inv, det = [], [], []
for gv in gs:
    fma.append(float(mp.findroot(lambda t: f_p1(gv, t) - f_p2(gv, t),
                                 mp.mpf("0.01"))))
    inv.append(float(mp.findroot(lambda t: f_s1(gv, t) - f_s2(gv, t),
                                 mp.mpf("0.02"))))
    det.append(float(gv / (2 - gv**2)))
gx = [float(v) for v in gs]

fig, ax = plt.subplots(figsize=(7.4, 4.3))
ax.plot(gx, det, color=MUTED, lw=2.0, ls="-.",
        label=r"deterrence switches  $\theta=\gamma/(2-\gamma^2)$")
ax.plot(gx, inv, color=INK, lw=2.0, ls="--",
        label=r"leader stops out-investing  $s_1^*=s_2^*$")
ax.plot(gx, fma, color=ACCENT, lw=2.6,
        label=r"first-mover advantage dies  $\pi_1^*=\pi_2^*$")
ax.fill_between(gx, 1e-6, fma, color=ACCENT, alpha=0.10)
ax.annotate("FMA survives only here", xy=(0.55, 0.004), fontsize=9.5,
            color=ACCENT)
ax.axvline(0.3, color=GRID, lw=1.0)
ax.annotate(r"at $\gamma=0.3$:  $0.0015$  vs  $0.0169$  vs  $0.157$"
            "\n≈ 105× apart",
            xy=(0.3, 0.157), xytext=(0.33, 0.30), fontsize=9.5, color=INK,
            arrowprops=dict(arrowstyle="->", color=MUTED, lw=0.9))
ax.set_yscale("log")
ax.set_ylim(2e-5, 1.0)
ax.set_xlim(0.05, 0.80)
style(ax, r"$\gamma$   (competition intensity)", r"$\theta$")
ax.legend(frameon=False, fontsize=9.5, loc="lower right")
save(fig, "fig-thresholds.svg")

# ----------------------------------------------------------------------
print("\nvalues used in the deck (own calculation):")
for gv in ["0.1", "0.3", "0.5", "0.7", "0.8"]:
    gm = mp.mpf(gv)
    fr = mp.findroot(lambda t: f_p1(gm, t) - f_p2(gm, t), mp.mpf("0.01"))
    iv = mp.findroot(lambda t: f_s1(gm, t) - f_s2(gm, t), mp.mpf("0.02"))
    sw = gm / (2 - gm**2)
    print(f"  gamma={gv}: FMA {mp.nstr(fr,4):>10}  invest {mp.nstr(iv,4):>9}"
          f"  switch {mp.nstr(sw,4):>8}  ratio {float(sw/fr):7.0f}x")
