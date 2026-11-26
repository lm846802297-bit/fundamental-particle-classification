# 1+1D: quantum-double monodromy versus a massive particle shell

**Result.** A massive scalar doublet with an unbroken $\mathbb Z_3$ symmetry distinguishes three facts on the same continuum starting theory. Its electric DHR charges have identical left and right exchange intertwiners and trivial electric–electric monodromy. Müger's nonlocal order–disorder extension nonetheless has exact $\mathbb Z_3$ quantum-double monodromies, including $e^{2\pi i/3}$. The flux labels of that algebra do not supply additional mass-$m$ particle states in its represented Fock space. The nontrivial phase is genuine algebraic monodromy; the failure is the inference from it to the statistics of extra massive particles.

**中文摘要：** 同一个有质量标量双重态中，电荷 DHR 扇区的左、右交换相同，纯电荷双交换为恒等。引入无序算符后的非局域扩张则确实出现非平凡的量子双重编织相位。谱的检查表明，这些无序标签并不是额外的质量壳粒子。

## 1. Setup and inputs

Take the strictly local bosonic net $F$ of two free equal-mass real scalar fields on the infinite line, with $G=\mathbb Z_3$ acting by a rotation through $2\pi/3$ in their two-component space. It has untwisted Haag duality and wedge split: use [Müger, hep-th/9705019v2, §7(a)](https://arxiv.org/pdf/hep-th/9705019) for the single scalar and [Buchholz–Lechner, §4](https://arxiv.org/pdf/math-ph/0402072) for the free wedge split proof; the finite tensor product of the two scalar copies inherits the duality and split identifications. The unbroken internal action commutes with the Poincaré representation and fixes the vacuum. On the one-particle space the internal rotation has the two eigencharacters $\chi_e(g)=\zeta^{eg}$, where $e=1,2$, $g=0,1,2$ are taken modulo three and $\zeta=e^{2\pi i/3}$.

Write $A=F^G$ for the original invariant observable net, $A^d$ for its dual net in the invariant vacuum representation, and $\widehat F_L$ for the **nonlocal** field extension by left disorder operators. These are not interchangeable nets. The hypotheses and construction used here are [Müger, hep-th/9606175v3, Definitions 2.2, 2.4, 2.5 and 3.1; Theorem 3.10; Proposition 4.11](https://arxiv.org/pdf/hep-th/9606175). The theorem identifies $\widehat F_L^G$ with the dual net *in a simple-sector representation*. It does not make $\widehat F_L$ a local observable net.

## 2. Left/right electric exchange: a direct transporter check

A bounded-region localized electric representative on $A$ can be written $\rho_e=\operatorname{Ad}v_e$, with $v_e$ a local unitary of character $\chi_e^{-1}$ so that $v_e^\dagger$ maps the vacuum-charge subspace to $\mathcal H_e$. This is the fixed-net realization in [Müger, hep-th/9705019v2, §6.1, Eq. (6.4)](https://arxiv.org/pdf/hep-th/9705019), with the inverse character assigned here to the implementing unitary. In the two-scalar example, one may obtain either charged unitary using the polar phase of $\phi_1(f)+i\phi_2(f)$ with a common real nonzero one-mode smearing $f$ supported in a double cone, or its adjoint. The real and imaginary parts strongly commute on the two independent oscillator factors, and the joint spectral projection at zero is zero, so the polar phase is a unitary in $F(O)$.

Transport $\rho_f$ to a representative $\widetilde\rho_f$ in a double cone strictly to either side of the localization of $v_e$. With the common transporter convention of [hep-th/9606175v3, Eq. (4.38)](https://arxiv.org/pdf/hep-th/9606175), $T_f=\widetilde v_f v_f^\dagger$ is gauge invariant and
$$
\varepsilon_{L/R}(\rho_e,\rho_f)
=T_f^\dagger\,\rho_e(T_f)
=v_f v_e v_f^\dagger v_e^\dagger.
$$
The equality uses $[v_e,\widetilde v_f]=0$ by bosonic locality and holds for transport to either side. The displayed intertwiner is the identity if the starting representatives are already spacelike separated. More generally, exchanging the two arguments gives its inverse, so the double braid is still the identity. This is a calculation in the electric subcategory given by these localized fields, not a theorem that all charges of a wedge-dual net must have symmetric statistics. It does not use double-cone Haag duality for $A$.

## 3. A nontrivial monodromy in the disorder algebra

By Definition 2.2 of hep-th/9606175v3, the left disorder unitary $U_L^O(g)$ implements the symmetry on fields in the left complementary wedge and the identity on those in the right complementary wedge. Thus it gives a phase $\chi_e(g)$ on commuting past an electric field on its active side and no phase on the inactive side. It is not a bounded-region local field of $F$, even though $O$ labels the interpolation region.

For Abelian $G$, use labels $(g,e)$ (flux, electric character). Proposition 4.11, Eqs. (4.33)–(4.34), and Proposition 4.14, Eqs. (4.44)–(4.47), give the left-oriented exchange and monodromy from $R=\sum_g V_g\otimes U(g)$ and $R R_{21}$. Since $V_h$ is the flux projector, on labels $x=(g,e),\,y=(h,f)$ these give
$$
c_{x,y}:x\otimes y\longmapsto\zeta^{g f}\,y\otimes x,\qquad
M_{x,y}=\zeta^{g f+h e}.
$$
For electric $E=(0,1)$ and disorder $D=(1,0)$, $M_{E,D}=\zeta$. For $X=(1,1)$, $M_{X,X}=\zeta^2$. The two directed exchanges between $E$ and $D$ have phases $1$ and $\zeta$; their product is not the operation of reversing the *same* exchange. On electric pairs $g=h=0$ the formula gives $M=1$, consistent with §2. In fact the full $9\times9$ monodromy table has orthogonal rows because $(g,e)\mapsto[(h,f)\mapsto\zeta^{g f+h e}]$ consists of all nine distinct characters of $\mathbb Z_3^2$. Its restriction to the three electric labels is an all-ones table.

There is also an exact left/right signature when passing to the dual observable net, not an additional electric interchange phase. [Hep-th/9705019v2, §6.1, Eqs. (6.7)–(6.11)](https://arxiv.org/pdf/hep-th/9705019) gives $U_L^O(g)U_R^O(g)=U(g)$, hence
$$
U_L^O(g)\big|_{\mathcal H_e}
=\chi_e(g)\,U_R^O(g^{-1})\big|_{\mathcal H_e}.
$$
On the vacuum-charge subspace the two representatives of the disorder observable coincide, whereas on $\mathcal H_e$ their relative factor is $\chi_e(g)$. In the conventions of that section the left and right extensions of a nontrivial electric charge to $A^d$ are solitons with vacuum pairs $(\omega_0,\omega_{\chi_e^{-1}})$ and $(\omega_{\chi_e},\omega_0)$, respectively. These pairs are different from the same-vacuum DHR condition. Neither the relative disorder factor nor the algebraic monodromy gives a second massive electric species.

## 4. Independent shell check

The two bosonic one-particle species have characters $e=\pm1$ and joint translation spectrum $H_m^+$. With additive Fock translations, a state of $n$ constituents has invariant mass at least $nm$. The invariant-character subspace $\mathcal H_0$ therefore contains the vacuum but no mass-$m$ state. In each $\mathcal H_{\pm1}$ there is one copy of the mass-$m$ single-particle representation. The next charged continuum starts at $2m$ (two constituents of the opposite sign carry the same total character modulo three); there's no extra copy labeled by flux.

The disorder extension in Definition 3.1 acts on the **original** Hilbert space, not on a direct sum of nine massive one-particle representations. For this Abelian example $U_L^O(g)$ commutes with $G$, so $U_L^O(g)\Omega\in\mathcal H_0$ and its projection to the isolated mass-$m$ shell is zero. A dyonic operator of character $e\ne0$ can at most overlap the mass-$m$ copy already present in $\mathcal H_e$. This is not a claim about which other inequivalent representations of the extended algebras exist or what their spectra are. Müger himself distinguishes full algebraic $D(G)$ multiplets from physical superselection sectors when the dual part of the symmetry is broken (remark 2 after Proposition 4.12; §6 of hep-th/9606175v3). The named monodromies thus cannot be assigned to two new elementary massive particles in this example.

Run **python3 checks/verify_massive_order_disorder_monodromy.py** from the repository root. It checks the phase and orientation algebra using exact exponents modulo three, computes character-table orthogonality exactly, and independently enumerates the one- and two-constituent charge channels. It does not simulate the field net or infer a spectrum from finite matrices.
