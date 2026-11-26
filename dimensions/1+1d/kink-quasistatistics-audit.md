# 1+1D: do the kink quasi-statistics operators carry exchange holonomy?

**Result.** For a fixed admissible family of Schlingemann one-kink homomorphisms, the canonical quasi-statistics maps between different creation arrangements form a representation of a **pair groupoid**. Every closed chain of these maps is exactly the identity. The maps cancel out of the in/out collision overlap after the same canonical relabeling of asymptotic tensor factors on both sides. This rules out these maps as a witness of a new observable exchange holonomy, not the kink sectors, vacuum-label selection rules, model-dependent scattering, or other candidate statistics in 1+1D.

**中文摘要：** 对固定的一族有质量扭结，Schlingemann 的准统计算符是不同合法构造顺序之间的幺正换标；闭合重排的算符严格等于恒等算符。把入态和出态按同一规则换标后，散射振幅不变。这排除了把这组算符本身视为第三种交换统计的证据，但不排除有质量扭结、真空标签约束、非平凡散射或其他候选结构。

## 1. What changes with an arrangement?

The [1+1D literature dossier](README.md) identifies kink quasi-statistics as the first standard-Minkowski candidate to test. The primary source is [Schlingemann, DESY 96-228](https://www.physik.uni-hamburg.de/th2/ag-fredenhagen/dokumente/desy96-228.pdf), §§6.1–6.3 and Appendix B.2. Printed page numbers are used below.

Fix two ordered chains of one-kink factors and their vacuum labels, as in Definitions 6.1.1–6.1.2 (pp. 112–114). For $n,m\geq1$, the allowed creation orders consist of alternating nonempty runs of $+$ and $-$ factors, beginning with $+$ and ending with $-$; each run takes its factors consecutively from its own chain. Orientation here concerns which end of the configuration is extended. It does not assert that charged fields are observables or that particles traverse the line to exchange.

Choosing the cuts in the two connected partitions independently, with the same number $\ell$ of blocks, gives
$$
|P(n,m)|=\sum_{\ell=1}^{\min(n,m)}
\binom{n-1}{\ell-1}\binom{m-1}{\ell-1}
=\binom{n+m-2}{n-1}.
$$
Equivalently, the first plus and last minus are fixed and one chooses the remaining $n-1$ plus positions. For $n=m=2$ there are just two orders, $++--$ and $+-+-$, not the 24 permutations of four slots. The single-sided case has one order (remark (ii), p. 114). Same-orientation factors keep their original order and outer vacuum labels are unchanged.

## 2. Exact result: identity for every closed arrangement loop

Theorem 6.2.1 (pp. 115–116) supplies an intertwiner
$$
\epsilon_{ab}:\mathcal H_b\to\mathcal H_a,\qquad
\rho_a(A)\epsilon_{ab}=\epsilon_{ab}\rho_b(A),
$$
for every pair $a,b$ of arrangements. In the proof in Appendix B.2 (p. 156), the same displaced auxiliary family may be used for all arrangements: opposite orientations are spacelike separated and commute in the displaced description (Lemma B.2.1). The auxiliary representation is therefore common and the original arrangements are transported from it by unitaries $u_a$. In the Appendix's direction convention,
$$
\epsilon_{ab}=u_a u_b^\dagger .
$$
Merely knowing that two representations are unitarily equivalent would not prove this identity. The explicit factorization gives
$$
\epsilon_{aa}=1,\quad
\epsilon_{ba}=\epsilon_{ab}^\dagger,\quad
\epsilon_{ab}\epsilon_{bc}=\epsilon_{ac}.
$$
Hence the source's set $G(n,m)=P(n,m)\times P(n,m)$ is the pair groupoid when given the natural source, target and multiplication. There is one arrow between any two objects and the only arrow from an arrangement to itself is its identity. All closed products telescope **exactly**, without a residue or a projective phase. This applies to any admissible closed sequence, not only an exchange followed by its inverse.

Transporting each representative by $V_a$ sends the arrow to $V_a\epsilon_{ab}V_b^\dagger$. A loop is merely conjugated in its base fiber and remains the identity. Theorem 6.2.1 and Appendix B.2 separately show independence from auxiliary homomorphisms and charge transporters for a fixed input family. The proof addresses the canonical operators constructed there, not all possible intertwiners in reducible multiparticle representations.

## 3. Collision amplitudes: the extra maps cancel

In Theorem 6.3.6 (p. 135), denote by $T_a^{\rm in/out}$ the stated maps from the interacting fiber to its free tensor-ordered description, and by $U_{ab}$ the canonical tensor-factor reordering from $b$ to $a$. For the channels to which the theorem applies, with time and support conditions as in §6.3, its interchange relation reads
$$
T_a^{\rm in/out}\epsilon_{ab}=U_{ab}T_b^{\rm in/out}.
$$
Define the channel overlap $S_a=T_a^{\rm out}(T_a^{\rm in})^\dagger$, without assuming completeness or a global scattering operator. Substitution yields
$$
S_a=U_{ab}S_b U_{ab}^\dagger .
$$
Thus each collision matrix element agrees for matched wave packets relabeled by $U_{ab}$ on both ends. This does not make the dynamical scattering trivial: it rules out an additional exchange phase or matrix from changing only the creation arrangement of an unchanged channel. It does not compare different momentum orderings by physically crossing worldlines, and is not a statement about amplitudes in unequal channels without transforming their external state descriptions.

## 4. Decision

- **Established under the source's hypotheses:** genuine massive one-kink states and constrained composition tied to the interpolated vacua. Not every representation with kink boundary conditions necessarily has an isolated one-particle shell.
- **Excluded:** a nontrivial closed-exchange phase, matrix or extra collision signal from these canonical arrangement intertwiners alone.
- **Not decided:** whether a specific massive local relativistic model has another observable kink invariant that cannot be reproduced by ordinary statistics plus vacuum-label constraints. This is not an equivalence proof for whole theories or a general no-go for all massive 1+1D sectors.

The next discriminator remains in 1+1D: test a concrete massive kink model against the crossed and elastic amplitudes at fixed outer vacuum labels. A proposed invariant should survive a change of field presentation and comparison with a Bose/Fermi reference with the same label constraints. The separate deformed-spacetime candidate also still requires an equivalence audit.

### Reproduction

Run **python3 checks/verify_kink_quasistatistics.py** from the repository root. The verifier enumerates arrangements in two independent ways and uses noncommuting, exact permutation matrices to check loop cancellation, representative covariance and in/out overlap relabeling. It checks the finite identities, not the underlying QFT construction.
