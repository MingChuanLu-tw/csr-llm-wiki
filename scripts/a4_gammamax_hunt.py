"""
A4 follow-up: where does gamma_max = 0.810736 come from?

The main A4 run reproduced every equation and both theta thresholds, but
could NOT reproduce gamma_max from the denominator D or from the leader's
stage-1 second-order condition. This script tests the remaining candidates.
"""

import sympy as sp
import mpmath as mp

mp.mp.dps = 25

a, c, g, th, s1, s2, p1, p2, x1, x2 = sp.symbols(
    "a c gamma theta s1 s2 p1 p2 x1 x2", real=True
)

# rebuild the model (same as the main script)
sol_x = sp.solve([sp.Eq(p1, a + s1 - x1 - g * x2),
                  sp.Eq(p2, a + (s2 + th * s1) - x2 - g * x1)],
                 [x1, x2], dict=True)[0]
x1_d, x2_d = sp.simplify(sol_x[x1]), sp.simplify(sol_x[x2])
pi1 = (p1 - c) * x1_d - s1**2
pi2 = (p2 - c) * x2_d - s2**2
sol_p = sp.solve([sp.diff(pi1, p1), sp.diff(pi2, p2)], [p1, p2], dict=True)[0]
p1_s, p2_s = sp.simplify(sol_p[p1]), sp.simplify(sol_p[p2])
subs_p = {p1: p1_s, p2: p2_s}
pi2_s = sp.simplify(pi2.subs(subs_p))
s2_of_s1 = sp.simplify(sp.solve(sp.diff(pi2_s, s2), s2)[0])
pi1_s = sp.simplify(pi1.subs(subs_p))
pi1_stage1 = sp.simplify(pi1_s.subs(s2, s2_of_s1))
s1_star = sp.simplify(sp.solve(sp.diff(pi1_stage1, s1), s1)[0])
s2_star = sp.simplify(s2_of_s1.subs(s1, s1_star))

NUM = {a: 1, c: 0}
TARGET = mp.mpf("0.810736")

print("=" * 72)
print("Hunting for gamma_max = 0.810736")
print("=" * 72)


def scan(name, expr, theta_vals=(0, 0.5, 1.0)):
    """Report the smallest positive root in (0,1) over several theta values."""
    f = sp.lambdify((g, th), expr.subs(NUM), "mpmath")
    print(f"\n{name}")
    for tv in theta_vals:
        tvm = mp.mpf(tv)
        vals = []
        prev = None
        root = None
        for k in range(1, 1000):
            gg = mp.mpf(k) / 1000
            try:
                v = f(gg, tvm)
            except Exception:  # noqa: BLE001
                continue
            if prev is not None and prev[1] * v < 0:
                try:
                    root = mp.findroot(lambda z: f(z, tvm), (prev[0], gg),
                                       solver="bisect")
                except Exception:  # noqa: BLE001
                    root = None
                break
            prev = (gg, v)
            vals.append(v)
        at_target = f(TARGET, tvm)
        mark = "  <<< MATCHES 0.810736" if root is not None and \
            abs(root - TARGET) < mp.mpf("1e-5") else ""
        print(f"   theta={float(tvm):<4} first sign change at "
              f"gamma = {mp.nstr(root, 9) if root else 'none in (0,1)':<14}"
              f" value at 0.810736 = {mp.nstr(at_target, 6)}{mark}")


# --- candidate 1: follower's stage-2 SOC
soc_s2 = sp.simplify(sp.diff(pi2_s, s2, 2))
scan("1. follower stage-2 SOC  d2pi2/ds2^2  (needs < 0)", soc_s2)

# --- candidate 2: leader's stage-1 SOC
soc_s1 = sp.simplify(sp.diff(pi1_stage1, s1, 2))
scan("2. leader stage-1 SOC  d2pi1/ds1^2  (needs < 0)", soc_s1)

# --- candidate 3: equilibrium quantities positive
x1_star = sp.simplify(x1_d.subs(subs_p).subs({s1: s1_star, s2: s2_star}))
x2_star = sp.simplify(x2_d.subs(subs_p).subs({s1: s1_star, s2: s2_star}))
scan("3. equilibrium quantity x1*  (needs > 0)", x1_star)
scan("4. equilibrium quantity x2*  (needs > 0)", x2_star)

# --- candidate 4: equilibrium CSR positive
scan("5. equilibrium s1*  (needs > 0)", s1_star)
scan("6. equilibrium s2*  (needs > 0)", s2_star)

# --- candidate 5: the bracket  6 - g(4 + g(5 - g - g^2))
br1 = 6 - g * (4 + g * (5 - g - g**2))
scan("7. bracket 6 - g(4 + g(5 - g - g^2))", br1, theta_vals=(0,))

# --- candidate 6: the other bracket, theta-dependent
br2 = 6 - g * (4 * th + g * (5 - g * th - g**2))
scan("8. bracket 6 - g(4t + g(5 - gt - g^2))", br2)

# --- candidate 7: 12 - 20g^2 + 8g^4 - g^6
den4 = 12 - 20 * g**2 + 8 * g**4 - g**6
scan("9. 12 - 20g^2 + 8g^4 - g^6", den4, theta_vals=(0,))

# --- candidate 8: the full denominator D
D = den4**2 - (1 - g**2) * br2**2
scan("10. D = (12-20g^2+8g^4-g^6)^2 - (1-g^2)(6-g(4t+g(5-gt-g^2)))^2", D)

# --- candidate 9: profits positive
pi1_star = sp.simplify(pi1_stage1.subs(s1, s1_star))
pi2_star = sp.simplify(pi2_s.subs({s1: s1_star, s2: s2_star}))
scan("11. pi1*  (needs > 0)", pi1_star)
scan("12. pi2*  (needs > 0)", pi2_star)

# --- direct test: what simple algebraic number is 0.810736?
print("\n" + "=" * 72)
print("What number is 0.810736?")
print("=" * 72)
cands = {
    "sqrt(2)-1/2":        mp.sqrt(2) - mp.mpf(1) / 2,
    "2-sqrt(e)":          2 - mp.e ** mp.mpf("0.5"),
    "root of g^3+g^2-2":  None,
    "(sqrt(17)-1)/4":     (mp.sqrt(17) - 1) / 4,
    "sqrt(0.657)":        mp.sqrt(mp.mpf("0.657")),
    "2/(1+sqrt(2))*...":  None,
}
print(f"   target                 = {TARGET}")
print(f"   sqrt(2) - 1/2          = {mp.nstr(cands['sqrt(2)-1/2'], 10)}")
print(f"   (sqrt(17)-1)/4         = {mp.nstr(cands['(sqrt(17)-1)/4'], 10)}")
# root of 6 - g(4 + g(5 - g - g^2)) = 0  i.e. g^4 + g^3 - 5g^2 - 4g + 6 = 0
poly = sp.Poly(sp.expand(6 - g * (4 + g * (5 - g - g**2))), g)
print(f"\n   bracket 7 as polynomial: {poly.as_expr()}")
for r in sp.nroots(poly):
    if r.is_real and 0 < r < 1.5:
        print(f"      real root in (0,1.5): {r}")

# the paper cites Garella & Petrakis (2008) for the same restriction;
# report the Hessian determinant of the price stage as a last candidate
H = sp.Matrix([[sp.diff(pi1, p1, 2), sp.diff(pi1, p1, p2)],
               [sp.diff(pi2, p2, p1), sp.diff(pi2, p2, 2)]])
print(f"\n   price-stage Hessian det = {sp.simplify(H.det())}")

print("\n" + "=" * 72)
print("Conclusion is written by hand into checks/a4_report.md")
print("=" * 72)
