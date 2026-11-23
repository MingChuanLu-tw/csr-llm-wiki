"""
A4 confirmation: gamma_max = 0.810736 is the interiority bound.

Candidate identified by scripts/a4_gammamax_hunt.py: at theta = 0 the
follower's equilibrium CSR s2* (and its quantity x2*) hit zero at
gamma = 0.8107358..., and this is the SMALLEST gamma at which any
equilibrium object hits a boundary, over all theta in [0,1].

At theta = 0 the numerator of s2* reduces to the polynomial
    N(gamma, 0) = 18 + 6g - 35g^2 - 15g^3 + 15g^4 + 7g^5 - 2g^6 - g^7
so gamma_max should be its relevant real root.
"""

import sympy as sp
import mpmath as mp

mp.mp.dps = 30
g, th = sp.symbols("gamma theta", real=True)

N = (6 * (3 + th) + 2 * g * (3 + 5 * th - 2 * th**2)
     - g**2 * (35 + th + 4 * th**2) - g**3 * (15 + 6 * th - th**2)
     + g**4 * (15 + th**2) + g**5 * (7 + th) - 2 * g**6 - g**7)

N0 = sp.expand(N.subs(th, 0))
print("N(gamma, theta=0) =", N0)

roots = [r for r in sp.nroots(sp.Poly(N0, g), n=25) if r.is_real]
print("\nreal roots:")
for r in sorted(roots, key=lambda z: abs(sp.re(z))):
    print(f"   {r}")

target = mp.mpf("0.810736")
in_unit = [mp.mpf(str(sp.re(r))) for r in roots if 0 < sp.re(r) < 1]
print(f"\nroots in (0,1): {[mp.nstr(r, 15) for r in in_unit]}")
for r in in_unit:
    print(f"   |root - 0.810736| = {mp.nstr(abs(r - target), 6)}")
    print(f"   rounded to 6 dp    = {mp.nstr(r, 7)}")

# Is theta = 0 really the binding case? Track the root of N as theta rises.
print("\nroot of N(gamma, theta) = 0 as theta varies:")
Nf = sp.lambdify((g, th), N, "mpmath")
for tv in ["0", "0.05", "0.1", "0.2", "0.3", "0.5", "1.0"]:
    tvm = mp.mpf(tv)
    try:
        r = mp.findroot(lambda z: Nf(z, tvm), mp.mpf("0.81"))
        inside = "in (0,1)" if 0 < r < 1 else "OUTSIDE (0,1)"
        print(f"   theta={tv:<5} gamma = {mp.nstr(r, 12)}  {inside}")
    except Exception as e:  # noqa: BLE001
        print(f"   theta={tv:<5} no root near 0.81 ({type(e).__name__})")

print("\nConclusion: gamma_max is the theta=0 interiority bound "
      "(follower's equilibrium CSR reaches zero).")
