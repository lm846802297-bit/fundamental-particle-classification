# Existence audit 01: massive braid statistics and the locality test

This note applies the [research program's existence test](research-program.md) to explicit relativistic models. **The strongest positive result verified here is a massive, positive-energy anyon in a (2+1)-dimensional wedge-local field model. A stronger claim, namely that this same model yields such a particle as a locally detectable cone-localized sector of a Haag–Kastler observable theory, does not follow. In fact, its published scattering law obstructs that promotion if the scattering law and braid statistics are kept.** A fully local chiral conformal net independently supplies a rigorous beyond-Bose/Fermi charge sector, but not a massive asymptotic particle. Neither result establishes an experimentally observed new elementary particle.

## 1. Massive (2+1) example: the particle and the statistic

**Model.** Plaschke, [*Wedge Local Deformations of Charged Fields Leading to Anyonic Commutation Relations*](https://arxiv.org/pdf/1208.6141), §§3.1–3.3, works in Minkowski spacetime on a positive-inner-product charged Hilbert space. The creation/annihilation operators are deformed, and the proper orthochronous Poincaré **cover** acts covariantly. Charged fields carry paths of wedges, not only wedge supports. The construction is a continuum relativistic field model, not a representation of excitations in a material. Auxiliary Bose-symmetric Fock coordinates do not by themselves describe the model's exchange operation.

**Mass-shell check.** Write $q=n_+-n_-$ for the charge and $P=\sum_i p_i$ for the momentum in an $n_++n_-$ block. In §3.1, Eqs. (3.3)–(3.6), every constituent belongs to the forward mass shell at a common $m>0$ and translations are unchanged by the deformation. For forward timelike momenta of mass $m$, $p_i\cdot p_j\ge m^2$ by the reverse timelike Cauchy–Schwarz inequality (or by boosting one to rest). Therefore

$$P^2=\sum_i m^2+2\sum_{i<j}p_i\cdot p_j\ge (n_++n_-)^2 m^2.$$

In charge $q=\pm1$ the single-constituent shell is at $m$ and the next possible block has three constituents. Its threshold is $3m$ (attained as an infimum by co-moving momenta). Thus this is a genuine isolated shell of the model, not a formal parameter in a Lagrangian, and the bound is strict throughout the mass interval $(m,3m)$. The universal-cover massive little group is $\mathbb R$, and the one-particle and one-antiparticle subspaces both carry the Wigner representation with spin $\lambda\in\mathbb R$, with a full $2\pi$ rotation acting by $e^{2\pi i\lambda}$. There is no underlying within-model bound-state construction for this single-constituent shell. This is not an assertion about compositeness in other presentations or about real matter.

**Exact winding check.** Lemma 3.1 sets $k=-2N-1$ for relative path winding $N\in\mathbb Z$. Proposition 3.1 and Eq. (3.49) give the same-charge field-exchange and outgoing-state relation, respectively, with factor

$$E_\lambda(N)=e^{-2\pi i\lambda k}=e^{2\pi i\lambda(2N+1)}.$$

Comparing a fixed ordering at adjacent windings therefore gives the pure-winding multiplier

$$\frac{E_\lambda(N+1)}{E_\lambda(N)}=e^{4\pi i\lambda}.$$

For $\lambda=1/4$, $E_{1/4}(0)=i$, $E_{1/4}(1)=-i$ and the multiplier is $-1$. Reversing the orientation conjugates the phases; merely reversing the same exchange sends $N\mapsto-N-1$ and gives the inverse, not an independent positive winding. For integer and half-integer $\lambda$, the corresponding exchange is $+1$ or $-1$ and the multiplier is $+1$. Hence the $\lambda=1/4$ **path-sensitive exchange data** do not factor through the permutation quotient $B_2\to S_2$: that quotient kills two exchanges of the same orientation, even on representations with internal labels. Conjugating operators in the same path-sensitive description cannot change a scalar holonomy. This is a statement about the published field/scattering description, not an assertion that a local observable category has already been reconstructed or that a global phase by itself is measured.

## 2. Why the wedge example cannot simply be promoted to the cone-local setting

Plaschke's §3.3 Eq. (3.51) is a two-particle **overlap** of in/out states with the stated wedge-ordered velocity supports. It is diagonal in individual momenta (up to the identical-particle relabeling): its kernel in wave packets contains the same $p_1,p_2$ in the incoming and outgoing factors. The momentum-dependent deformation factor and winding phase do not change this support.

An explicit gap in the angular support can be read off without computing the deformation function. In the center-of-mass frame take incoming spatial momenta $\pm(p,0)$ and outgoing momenta $\pm(p\cos\alpha,p\sin\alpha)$ with $p>0$ and $0<\alpha<\pi/2$. All four on-shell momenta are different; both pairs sum to the same $(2\sqrt{m^2+p^2},0,0)$. In both pairs the first minus the second velocity has positive $x^1$-component, the ordering for the right wedge. Choose sufficiently small disjoint open wave-packet neighborhoods preserving this ordering. The overlap vanishes identically in Eq. (3.51), including under identical-particle relabeling. This checks an open angular patch, not only one zero at a special angle.

By contrast, [Bros & Mund, Theorem 2](https://arxiv.org/pdf/1112.5785) says that in their local relativistic framework for massive, cone-localizable charges with non-real statistics parameter, every kinematically allowed open elastic patch has scattering in the same-charge channel for abelian anyons. Their Corollary 3 excludes temperate wedge-localized polarization-free generators in that framework. Plaschke explicitly has wedge polarization-free generators and does not obtain the Reeh–Schlieder property in spacelike cones for his construction (§3.2, end). **Consequently an extension satisfying the Bros–Mund hypotheses cannot preserve both the anyonic charge and the same elastic scattering amplitudes on this patch.** This is an obstruction to an unchanged promotion of this example, not a theorem against interacting cone-local anyons.

Related boundary checks: [Mund, Theorem 4.1](https://arxiv.org/pdf/0801.3621) derives $e^{2\pi i s}=\omega_\chi$ for a massive charged particle in the local framework, assuming an isolated mass with finitely many same-spin types at that mass in the sector. It is conditional and constrains the statistics **phase**, not a full nonabelian braid matrix. [Fredenhagen, Gaberdiel & Rüger, §3](https://arxiv.org/pdf/hep-th/9410115) construct scattering states assuming such suitable massive sectors; that result is not itself an existence construction. [Jain et al., §2.6, Eqs. (2.46)–(2.47)](https://arxiv.org/pdf/1404.6373) provide a separate continuum Chern–Simons–matter lead: at fixed 't Hooft coupling their same-charge Aharonov–Bohm parameters are $O(1/N)$, whereas the particle–antiparticle singlet parameter is $O(1)$. The planar singlet result is not a demonstration of same-species self-exchange or a nonperturbative local-net construction. [Mehta et al., §§3.5 and 4.3](https://arxiv.org/pdf/2210.07272) develop finite-rank/topological data while explicitly marking the promotion to full matter scattering as conjectural.

## 3. Fully local sector control: chiral Ising

The unitary $c=1/2$ Virasoro **chiral conformal net** is an explicit local relativistic observable theory ([Kawahigashi & Longo, §3](https://annals.math.princeton.edu/wp-content/uploads/annals-v160-n2-p04.pdf)). For $(1,\sigma,\psi)$ use weights $(0,1/16,1/2)$ and $\sigma\otimes\sigma=1\oplus\psi$ ([Brehm & Runkel, §8.1, Eqs. (8.2)–(8.3)](https://arxiv.org/pdf/2112.01563)). These are chiral sector data; the argument uses the relativistic continuum net itself, not its possible lattice or material realizations. The rotation/statistics identification for finite-index chiral sectors is [Guido & Longo's conformal spin–statistics theorem](https://arxiv.org/abs/hep-th/9505059). Balancing gives the double braid on a fusion channel $c$:

$$\left.(c_{\sigma,\sigma})^2\right|_c=\frac{\theta_c}{\theta_\sigma^2}=\exp\!\left(2\pi i (h_c-2h_\sigma)\right).$$

The two eigenphases are $e^{-i\pi/4}$ on (1) and $e^{3i\pi/4}$ on $\psi$. Their ratio is $-1$; even a common rephasing would not make both $+1$. Any symmetric Bose/Fermi category with ordinary internal multiplicities has identity double braiding, so a braided equivalence cannot turn these sectors into it. The example is stronger on observable locality than §1 and weaker on the particle criterion: these are positive-energy chiral charge representations, not a massive (1+1) scattering construction or ordinary spacelike exchanges of point particles on a line.

## 4. Decision and next discriminant

| Claim | Status after this audit |
| --- | --- |
| A massive charged relativistic particle can have genuine path-sensitive non-permutation exchange data in an explicit **wedge-local** model | **Verified model example**, with exact isolated-shell and winding checks above |
| Non-symmetric charge sectors can occur in a **local chiral observable net** | **Verified example**, with channel-resolved double braid |
| The same wedge-local example also gives a **cone-localizable massive sector** with the same elastic data | **Obstructed** by the open angular zero and Bros–Mund under their hypotheses |
| A less restricted interacting (2+1) construction meets both strict locality and massive-particle gates simultaneously | **Not settled by this audit**; test a different model, not an unchanged wedge promotion |
| A new elementary particle outside Bose/Fermi is observed in nature | **Not established** by any result here |

The next decisive test is an interacting (2+1) candidate with off-forward elastic support: exhibit the positive-norm charged state and isolated mass shell, reconstruct the allowed localization in the observable theory, and evaluate *same-species* monodromy. A Wilson-line phase, a Wigner representation alone, or an exotic gauge-field commutator is insufficient. This audit is a source-based derivation and cross-check of published constructions; it does not claim discovery or priority for a new model.

### Reproduction

From the repository root run `python3 checks/verify_existence_audit_01.py`. The small standard-library check uses exact rational phase exponents and independently checks the two momentum pairs and their wedge ordering with rational coordinates. It checks the derived diagnostics, not the full cited field constructions or their axioms.
