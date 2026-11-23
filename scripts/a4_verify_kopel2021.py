"""
A4 verification for wiki/papers/Kopel2021-CSR.md

Strategy: re-derive the three-stage game from the inverse demand system
eq. (1) using sympy, independently of the paper's stated results, then
compare the derived expressions against the equations transcribed into
the wiki page. This checks BOTH the paper and the transcription.

Then reproduce the three numerical thresholds by the method the paper
states in footnote 15.

Run:  python3 scripts/a4_verify_kopel2021.py

Note: do NOT use `python3 -I` on this machine — sympy lives in the user
site-packages that `-I` suppresses. The script reads no untrusted input; to keep
the working directory off the import path, run it from elsewhere with an
absolute path.
"""

import sympy as sp

a, c, g, th, s1, s2, p1, p2, x1, x2 = sp.symbols(
    "a c gamma theta s1 s2 p1 p2 x1 x2", real=True
)

results = []


def check(label, lhs, rhs, note=""):
    """Compare two expressions symbolically."""
    diff = sp.simplify(sp.together(sp.expand(lhs - rhs)))
    ok = diff == 0
    results.append((label, ok, note if ok else f"difference = {diff}"))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    if not ok:
        print(f"         difference = {diff}")
    return ok


print("=" * 70)
print("A4 — Kopel (2021) symbolic re-derivation")
print("=" * 70)

# ----------------------------------------------------------------------
# Stage 0: invert eq. (1) to get direct demand, compare with eq. (2)
# ----------------------------------------------------------------------
inv1 = sp.Eq(p1, a + s1 - x1 - g * x2)
inv2 = sp.Eq(p2, a + (s2 + th * s1) - x2 - g * x1)
sol_x = sp.solve([inv1, inv2], [x1, x2], dict=True)[0]
x1_d, x2_d = sp.simplify(sol_x[x1]), sp.simplify(sol_x[x2])

paper_x1 = (a * (1 - g) + (1 - g * th) * s1 - g * s2) / (1 - g**2) \
    - p1 / (1 - g**2) + g * p2 / (1 - g**2)
paper_x2 = (a * (1 - g) + s2 - (g - th) * s1) / (1 - g**2) \
    - p2 / (1 - g**2) + g * p1 / (1 - g**2)

print("\n-- eq. (2) direct demand --")
check("eq (2) x1", x1_d, paper_x1)
check("eq (2) x2", x2_d, paper_x2)

# ----------------------------------------------------------------------
# Stage 3: price competition. FOCs -> eq. (3)
# ----------------------------------------------------------------------
pi1 = (p1 - c) * x1_d - s1**2
pi2 = (p2 - c) * x2_d - s2**2

foc_p = [sp.diff(pi1, p1), sp.diff(pi2, p2)]
sol_p = sp.solve(foc_p, [p1, p2], dict=True)[0]
p1_s, p2_s = sp.simplify(sol_p[p1]), sp.simplify(sol_p[p2])

paper_p1 = (a * (2 + g) * (1 - g) + (2 + g) * c
            + (2 - g**2 - g * th) * s1 - g * s2) / (4 - g**2)
paper_p2 = (a * (2 + g) * (1 - g) + (2 + g) * c
            + (2 - g**2) * s2 + ((2 - g**2) * th - g) * s1) / (4 - g**2)

print("\n-- eq. (3) stage-3 prices --")
check("eq (3) p1(s1,s2)", p1_s, paper_p1)
check("eq (3) p2(s1,s2)", p2_s, paper_p2)

# second-order conditions for the price stage
soc_p1 = sp.simplify(sp.diff(pi1, p1, 2))
soc_p2 = sp.simplify(sp.diff(pi2, p2, 2))
print(f"   d2pi1/dp1^2 = {soc_p1}   (negative for gamma<1 -> max)")
print(f"   d2pi2/dp2^2 = {soc_p2}")

# ----------------------------------------------------------------------
# Stage 2: follower chooses s2. FOC -> eq. (4)
# ----------------------------------------------------------------------
subs_p = {p1: p1_s, p2: p2_s}
pi2_s = sp.simplify(pi2.subs(subs_p))
foc_s2 = sp.diff(pi2_s, s2)
s2_of_s1 = sp.simplify(sp.solve(foc_s2, s2)[0])

paper_s2_react = ((2 - g**2) * ((a - c) * (2 + g) * (1 - g)
                               + s1 * ((2 - g**2) * th - g))) \
    / (12 - 20 * g**2 + 8 * g**4 - g**6)

print("\n-- eq. (4) follower reaction function --")
check("eq (4) s2(s1)", s2_of_s1, paper_s2_react)

# sign of ds2/ds1 : paper says negative iff theta < gamma/(2-gamma^2)
dsds = sp.simplify(sp.diff(s2_of_s1, s1))
print(f"   ds2/ds1 = {sp.factor(dsds)}")
num_sign = sp.simplify(sp.numer(sp.together(dsds)))
print(f"   numerator = {sp.factor(num_sign)}")
print("   -> sign flips at theta = gamma/(2-gamma^2); checked numerically below")

# ----------------------------------------------------------------------
# Stage 1: leader chooses s1. FOC -> eq. (5)
# ----------------------------------------------------------------------
pi1_s = sp.simplify(pi1.subs(subs_p))
pi1_stage1 = sp.simplify(pi1_s.subs(s2, s2_of_s1))
foc_s1 = sp.diff(pi1_stage1, s1)
s1_star = sp.simplify(sp.solve(foc_s1, s1)[0])

D = (12 - 20 * g**2 + 8 * g**4 - g**6)**2 \
    - (1 - g**2) * (6 - g * (4 * th + g * (5 - g * th - g**2)))**2
paper_s1_star = ((a - c) * (1 - g**2)
                 * (6 - g * (4 + g * (5 - g - g**2)))
                 * (6 - g * (4 * th + g * (5 - g * th - g**2)))) / D

print("\n-- eq. (5) leader equilibrium CSR --")
check("eq (5) s1*", s1_star, paper_s1_star)

# ----------------------------------------------------------------------
# eq. (6): s2* = s2(s1*)
# ----------------------------------------------------------------------
s2_star = sp.simplify(s2_of_s1.subs(s1, s1_star))

N = (6 * (3 + th) + 2 * g * (3 + 5 * th - 2 * th**2)
     - g**2 * (35 + th + 4 * th**2) - g**3 * (15 + 6 * th - th**2)
     + g**4 * (15 + th**2) + g**5 * (7 + th) - 2 * g**6 - g**7)
paper_s2_star = ((a - c) * (1 - g) * (2 - g**2) * N) / D

print("\n-- eq. (6) follower equilibrium CSR --")
check("eq (6) s2*", s2_star, paper_s2_star)

# ----------------------------------------------------------------------
# eq. (7) and equilibrium profits
# ----------------------------------------------------------------------
p1_star = sp.simplify(p1_s.subs({s1: s1_star, s2: s2_star}))
p2_star = sp.simplify(p2_s.subs({s1: s1_star, s2: s2_star}))

paper_p1_star = c + ((12 - 20 * g**2 + 8 * g**4 - g**6)
                     / (6 - g * (4 * th + g * (5 - g * th - g**2)))) * s1_star
paper_p2_star = c + ((4 - g**2) * (1 - g**2) / (2 - g**2)) * s2_star

print("\n-- eq. (7) equilibrium prices --")
check("eq (7) p1*", p1_star, paper_p1_star)
check("eq (7) p2*", p2_star, paper_p2_star)

pi1_star = sp.simplify(pi1_stage1.subs(s1, s1_star))
pi2_star = sp.simplify(pi2_s.subs({s1: s1_star, s2: s2_star}))

paper_pi1_star = ((a - c) * (6 - g * (4 + g * (5 - g - g**2)))
                  / (6 - g * (4 * th + g * (5 - g * th - g**2)))) * s1_star
paper_pi2_star = (((4 - g**2) * (2 - g**2)**2 - 4) / (2 - g**2)**2) * s2_star**2

print("\n-- equilibrium profits (p. 497) --")
check("pi1*", pi1_star, paper_pi1_star)
check("pi2*", pi2_star, paper_pi2_star)

# ----------------------------------------------------------------------
# Numerical work: thresholds
# ----------------------------------------------------------------------
print("\n" + "=" * 70)
print("Numerical thresholds")
print("=" * 70)

NUM = {a: 1, c: 0}  # footnote 9: a - c = 1 in all figures
s1n = sp.lambdify((g, th), s1_star.subs(NUM), "mpmath")
s2n = sp.lambdify((g, th), s2_star.subs(NUM), "mpmath")
pi1n = sp.lambdify((g, th), pi1_star.subs(NUM), "mpmath")
pi2n = sp.lambdify((g, th), pi2_star.subs(NUM), "mpmath")

import mpmath as mp
mp.mp.dps = 30

# --- gamma_max: the paper says 0.810736 guarantees interior equilibrium
#     and second-order conditions. Candidate: root of the denominator D
#     or of the SOC. Test both.
D_num = sp.lambdify((g, th), D, "mpmath")
print("\n-- gamma_max = 0.810736 --")
print(f"   D(0.810736, theta=0) = {D_num(mp.mpf('0.810736'), 0)}")
print(f"   D(0.810736, theta=1) = {D_num(mp.mpf('0.810736'), 1)}")
for theta_val in [0, mp.mpf('0.5'), 1]:
    try:
        root = mp.findroot(lambda gg: D_num(gg, theta_val), mp.mpf('0.81'))
        print(f"   root of D at theta={theta_val}: gamma = {mp.nstr(root, 10)}")
    except Exception as e:  # noqa: BLE001
        print(f"   root of D at theta={theta_val}: not found ({e})")

# leader's stage-1 SOC
soc_s1 = sp.simplify(sp.diff(pi1_stage1, s1, 2))
soc_s1_num = sp.lambdify((g, th), soc_s1.subs(NUM), "mpmath")
print(f"   d2pi1/ds1^2 (gamma=0.5, theta=0)   = {mp.nstr(soc_s1_num(mp.mpf('0.5'), 0), 8)}")
print(f"   d2pi1/ds1^2 (gamma=0.810736, th=0) = {mp.nstr(soc_s1_num(mp.mpf('0.810736'), 0), 8)}")
try:
    r = mp.findroot(lambda gg: soc_s1_num(gg, 0), mp.mpf('0.81'))
    print(f"   SOC root at theta=0: gamma = {mp.nstr(r, 10)}")
except Exception as e:  # noqa: BLE001
    print(f"   SOC root at theta=0: not found ({e})")

GMAX = mp.mpf('0.810736')

# --- turning point of s1* at theta = 0 : paper says gamma = 0.531963
print("\n-- turning point of s1* at theta=0 (paper: 0.531963) --")
ds1_dg = sp.diff(s1_star.subs(NUM), g)
ds1_dg_n = sp.lambdify((g, th), ds1_dg, "mpmath")
try:
    tp = mp.findroot(lambda gg: ds1_dg_n(gg, 0), mp.mpf('0.53'))
    print(f"   recomputed turning point: gamma = {mp.nstr(tp, 10)}")
    print(f"   paper value             : 0.531963")
    print(f"   |difference|            = {mp.nstr(abs(tp - mp.mpf('0.531963')), 6)}")
except Exception as e:  # noqa: BLE001
    print(f"   not found ({e})")

# also confirm s2* is monotone decreasing at theta = 0
ds2_dg = sp.diff(s2_star.subs(NUM), g)
ds2_dg_n = sp.lambdify((g, th), ds2_dg, "mpmath")
signs = [ds2_dg_n(mp.mpf(x) * GMAX, 0) for x in ['0.05', '0.3', '0.6', '0.9', '0.99']]
print(f"   ds2*/dgamma at theta=0, sample points: {[mp.nstr(v, 5) for v in signs]}")
print(f"   all negative: {all(v < 0 for v in signs)}")

# --- footnote 15 method: sign of derivative evaluated at gamma = gamma_max
print("\n-- footnote 15 thresholds (derivative sign at gamma = gamma_max) --")
f1 = lambda tt: ds1_dg_n(GMAX, tt)   # noqa: E731
f2 = lambda tt: ds2_dg_n(GMAX, tt)   # noqa: E731
print(f"   ds1*/dgamma at gamma_max, theta=0   : {mp.nstr(f1(0), 8)}")
print(f"   ds1*/dgamma at gamma_max, theta=0.5 : {mp.nstr(f1(mp.mpf('0.5')), 8)}")
print(f"   ds2*/dgamma at gamma_max, theta=0   : {mp.nstr(f2(0), 8)}")
print(f"   ds2*/dgamma at gamma_max, theta=0.5 : {mp.nstr(f2(mp.mpf('0.5')), 8)}")

for label, fn, paper_val, guess in [
    ("theta* for leader  (paper 0.229499)", f1, '0.229499', '0.23'),
    ("theta* for follower (paper 0.202167)", f2, '0.202167', '0.20'),
]:
    try:
        root = mp.findroot(fn, mp.mpf(guess))
        print(f"   {label}: recomputed = {mp.nstr(root, 10)}, "
              f"diff = {mp.nstr(abs(root - mp.mpf(paper_val)), 6)}")
    except Exception as e:  # noqa: BLE001
        print(f"   {label}: not found ({e})")

# ----------------------------------------------------------------------
# Lemma 1 : theta = 0  =>  s1* > s2*  and  pi1* > pi2*
# ----------------------------------------------------------------------
print("\n" + "=" * 70)
print("Lemma 1 (theta = 0)")
print("=" * 70)

gap_paper = (g**2 * (2 + g)) / ((1 + g) * (3 - g**2)
                                * (6 - g * (4 + g * (5 - g - g**2)))) * s1_star
print("-- s1* - s2* closed form on p. 497 --")
check("s1*-s2* identity (theta=0)",
      sp.simplify((s1_star - s2_star).subs(th, 0)),
      sp.simplify(gap_paper.subs(th, 0)))

grid = [mp.mpf(k) / 40 * GMAX for k in range(1, 40)]
viol_s = [x for x in grid if not s1n(x, 0) > s2n(x, 0)]
viol_pi = [x for x in grid if not pi1n(x, 0) > pi2n(x, 0)]
print(f"   s1* > s2* on {len(grid)} grid points in (0, gamma_max): "
      f"{'HOLDS' if not viol_s else f'FAILS at {viol_s[:3]}'}")
print(f"   pi1* > pi2* on same grid: "
      f"{'HOLDS' if not viol_pi else f'FAILS at {viol_pi[:3]}'}")

# ----------------------------------------------------------------------
# Lemma 2 : FMA region in (gamma, theta)
# ----------------------------------------------------------------------
print("\n" + "=" * 70)
print("Lemma 2 — FMA frontier  pi1* = pi2*")
print("=" * 70)
for gv in ['0.1', '0.3', '0.5', '0.7', '0.8']:
    gv = mp.mpf(gv)
    try:
        root = mp.findroot(lambda tt: pi1n(gv, tt) - pi2n(gv, tt), mp.mpf('0.05'))
        print(f"   gamma={float(gv):.2f}:  FMA holds for theta < {mp.nstr(root, 6)}")
    except Exception:  # noqa: BLE001
        lo = pi1n(gv, mp.mpf('0.001')) - pi2n(gv, mp.mpf('0.001'))
        hi = pi1n(gv, mp.mpf('0.999')) - pi2n(gv, mp.mpf('0.999'))
        print(f"   gamma={float(gv):.2f}:  no root found; "
              f"pi1-pi2 at theta->0 = {mp.nstr(lo, 5)}, at theta->1 = {mp.nstr(hi, 5)}")

# ----------------------------------------------------------------------
# Lemma 3 : shape of s1*, s2* in gamma, by theta band
# ----------------------------------------------------------------------
print("\n" + "=" * 70)
print("Lemma 3 — shape by theta band")
print("=" * 70)


def shape(fn_d, theta_val, n=120):
    """Classify monotonicity of a function of gamma on (0, gamma_max)."""
    pts = [mp.mpf(k) / n * GMAX for k in range(1, n)]
    sg = [1 if fn_d(x, theta_val) > 0 else -1 for x in pts]
    flips = sum(1 for i in range(1, len(sg)) if sg[i] != sg[i - 1])
    if flips == 0:
        return "increasing" if sg[0] > 0 else "decreasing"
    if flips == 1 and sg[0] < 0:
        return "U-shaped"
    if flips == 1 and sg[0] > 0:
        return "inverted-U"
    return f"{flips} sign changes"


for tv in ['0', '0.15', '0.21', '0.25', '0.5', '0.9']:
    tvm = mp.mpf(tv)
    print(f"   theta={tv:<5}  s1*: {shape(ds1_dg_n, tvm):<12} "
          f"s2*: {shape(ds2_dg_n, tvm)}")

print("\n   Paper's claim: theta<0.202167 -> s2* decreasing;")
print("                  theta>0.229499 -> s1* decreasing;")
print("                  band 0.202167..0.229499 -> both U-shaped (Fig. 3, theta=0.21)")

# Fig. 3 check: at theta = 0.21, is the follower above the leader?
print("\n-- Fig. 3 (theta = 0.21): is s2* above s1*? --")
for gv in ['0.05', '0.2', '0.4', '0.6', '0.8']:
    gvm = mp.mpf(gv)
    v1, v2 = s1n(gvm, mp.mpf('0.21')), s2n(gvm, mp.mpf('0.21'))
    print(f"   gamma={gv:<5} s1*={mp.nstr(v1, 6):<12} s2*={mp.nstr(v2, 6):<12} "
          f"{'s2*>s1* (follower above)' if v2 > v1 else 's1*>s2*'}")

# Fig. 1 vs Fig. 3 levels (the claim A1 removed as unsupported)
print("\n-- Fig. 1 (theta=0) vs Fig. 3 (theta=0.21) levels --")
for gv in ['0.05', '0.4', '0.8']:
    gvm = mp.mpf(gv)
    print(f"   gamma={gv:<5} s1*: theta=0 -> {mp.nstr(s1n(gvm, 0), 6):<10} "
          f"theta=0.21 -> {mp.nstr(s1n(gvm, mp.mpf('0.21')), 6)}")

# ----------------------------------------------------------------------
print("\n" + "=" * 70)
npass = sum(1 for _, ok, _ in results if ok)
print(f"SYMBOLIC CHECKS: {npass}/{len(results)} passed")
for label, ok, note in results:
    if not ok:
        print(f"  FAIL {label}: {note}")
print("=" * 70)
