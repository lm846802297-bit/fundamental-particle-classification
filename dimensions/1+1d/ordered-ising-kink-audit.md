# 1+1D concrete control: the massive ordered Ising kink

**Result.** The thermal deformation of the continuum Ising CFT on the ordered side, with no magnetic perturbation, has an isolated massive kink particle. Its exact asymptotic exchange, at fixed outer vacua, is accounted for by ordinary Majorana anticommutation and the vacuum-label constraints. An independent calculation using exact local spin-field matrix elements checks the same exchange sign, while their nonconstant crossed matrix elements are operator-dependent and not a new two-kink statistics phase. This excludes the massive ordered Ising kink as a third statistics class at the level tested here, not all massive kinks in $1+1$ dimensions.

**中文摘要：** 在零磁扰动的相对论性有序 Ising 场论中，扭结确实有孤立质量壳。固定两端真空后，交换号完全由普通 Majorana 反对易关系给出；局域自旋算符的交叉矩阵元虽然依赖快度，却不改变弹性散射的费米符号。这是一个具体的排除案例，不是对所有 $1+1$ 维扭结的禁定理。

## 1. Physical particle and vacuum labels

We use the $1+1$-dimensional continuum QFT on the infinite spatial line, not a spin chain, medium, finite-volume symmetry eigenstate or replica theory. [Fonseca and Zamolodchikov, Ising Spectroscopy I, §2 and Eqs. (3.1)–(3.2)](https://arxiv.org/pdf/hep-th/0612304) identify the $h=0$, ordered $m>0$ theory with free massive Majorana dynamics, with two distinct vacua and mass-$m$ fermions interpreted as the interpolating kinks. [Capizzi and Mazzoni, §3, Eqs. (3.5)–(3.6)](https://arxiv.org/pdf/2307.12127) give the full alternating kink chain and its additive relativistic energy-momentum; only the single-field construction is used here.

Denote the vacua by $a=\pm1$. With outer vacuum labels $(a,b)$, the $n$-kink chain is
$$
K_{a_0a_1}(\theta_1)\cdots K_{a_{n-1}a_n}(\theta_n),
\qquad a_0=a,\quad a_j=(-1)^j a,\quad a_n=b.
$$
Thus $b=(-1)^n a$ and for fixed left vacuum and kink count the intermediate labels are unique. In particular, a single kink exists in the unequal-boundary sector, not as a single excitation produced by a local neutral field in a fixed-vacuum sector. For $p_j=m(\cosh\theta_j,\sinh\theta_j)$,
$$
\left(\sum_jp_j\right)^2=m^2\left(n+2\sum_{i<j}\cosh(\theta_i-\theta_j)\right)\geq n^2m^2.
$$
In each unequal-boundary channel the next allowed nonempty multiparticle sector has three kinks, so the isolated one-particle shell at $m$ has a strict gap to the $3m$ threshold. This threshold is an infimum approached by distinct rapidities that coalesce, not a forbidden state with coincident fermionic momenta. For the equal-boundary channel the first continuum is at $2m$.

## 2. Exact exchange with fixed outer vacua

The single-copy limit of [Capizzi and Mazzoni, Eqs. (3.11)–(3.12)](https://arxiv.org/pdf/2307.12127) gives
$$
K_{a,-a}(\theta_1)K_{-a,a}(\theta_2)
=-K_{a,-a}(\theta_2)K_{-a,a}(\theta_1).
$$
The spatial vacuum labels stay attached to the slots; only the rapidities interchange. The factor is independent of rapidity. There is no second intermediate vacuum in this channel and hence no nontrivial mixing matrix. The vacuum-label parity is a restriction on allowed states, not a phase.

For an ordered rapidity list and fixed outer vacua, strip the uniquely determined intermediate labels and map to the corresponding ordered Majorana creation state. This is an isometry in the common fermionic normalization (the CAR and bulk Hamiltonian are specified in [Fonseca and Zamolodchikov, §3](https://arxiv.org/pdf/hep-th/0612304)). It extends to the antisymmetric $n$-body space; the sign of every allowed rapidity permutation is precisely its parity. In particular, the ZF operation $R_i=-P_i$ gives $R_i^2=1$ and the usual symmetric-group relations. On a fixed ordered fermionic Hilbert space the free dynamical scattering is the identity; the published ZF amplitude $S_{\rm ZF}=-1$ compares opposite rapidity orders. These are consistent statements in different conventions, not two different scattering predictions. This identification concerns the asymptotic channels, not an assertion that the local Ising spin algebra and the local fermion field algebra are identical.

## 3. Independent check from local spin-field form factors

[Capizzi and Mazzoni, §3](https://arxiv.org/pdf/2307.12127) show that a local spin field $\sigma$ preserves the boundary labels for vacuum-to-state form factors, hence sees an even kink count. The infinite-volume spin-field result in [Fonseca and Zamolodchikov, Eq. (2.14), specialized to the ordered phase](https://arxiv.org/pdf/hep-th/0112167) gives, for the $+$ vacuum and a common choice of phases,
$$
F_{0,2r}^\sigma=i^r\bar\sigma\prod_{j<k}\tanh\frac{\theta_j-\theta_k}{2}.
$$
For the $-$ vacuum the overall sign can be fixed by the $\mathbb Z_2$ symmetry; it cannot affect exchange or spectral weights. Set $x_j=e^{\theta_j}$. Each factor is $(x_j-x_k)/(x_j+x_k)$. Its product is an alternating Vandermonde numerator over a symmetric denominator. It therefore changes by exactly $-1$ for every adjacent rapidity swap, giving the Watson exchange relation independently of applying the kink ZF algebra. This check needs distinct real rapidities; taking a ratio at a zero of the form factor is not legitimate.

The same primary equation gives the one-to-one spin matrix element away from coinciding rapidities. Strip its overall $i\bar\sigma$ and write it as $\coth((\theta-\theta')/2)$, where the first argument denotes the bra rapidity. It is the continuation of $\tanh((\theta-\theta')/2)$ by $\theta\mapsto\theta+i\pi$. In rational variables this is simply $x\mapsto -x$. For $x=3,\ x'=5$, the vacuum-to-two factor is $-1/4$ and the crossed one-to-one factor is $-4$, whereas the two-body ZF exchange factor remains the constant $S_{\rm ZF}=-1$; it is not replaced by the crossed form factor. The continued form factor has an annihilation pole at coincidence; it is a local-operator matrix element, not a two-body elastic collision. No statement at the coincident point (where disconnected terms must also be handled) is needed.

As a real-axis observable cross-check, define the stripped two-kink contribution per unit center-of-mass rapidity by removing the overall $|\bar\sigma|^2$ and the conventional $2\pi$ measure factors. For relative rapidity $u=\theta_1-\theta_2$ and invariant mass-squared $s$ it is
$$
\widehat\rho_2(s)=\frac{1}{2!}\int_{-\infty}^{\infty}du\,
\tanh^2(u/2)\,\delta\big(s-4m^2\cosh^2(u/2)\big)
=\frac{\sqrt{s-4m^2}}{s^{3/2}}\quad (s>4m^2).
$$
Both roots contribute and $|ds/du|=\sqrt{s(s-4m^2)}$; $\tanh^2(u/2)=1-4m^2/s$. The local spin spectral weight is zero below $4m^2$ in this channel and rises as $\sqrt{s-4m^2}$ above it. The nontrivial observable response survives despite free fermionic dynamics. In particular, neither this threshold shape nor the analytic continuation of the order field is evidence for a new exchange class.

## 4. Decision and reproduction

- **Positive:** a noncomposite massive asymptotic kink on an isolated shell, in a continuum local relativistic theory with two vacuum labels.
- **Negative control:** a fermionic exchange map with the same vacuum-label constraints accounts for the exact ordered asymptotic data; exact local form factors do not introduce an independent statistics phase.
- **Not decided:** an interacting $1+1$D kink model with multiple allowed intermediate labels, or the separate deformed-spacetime candidate. The [closed-arrangement result](kink-quasistatistics-audit.md) and this explicit Ising control are complementary, not a general classification.

Run **python3 checks/verify_ordered_ising_kink.py** at repository root. The standard-library verifier tests label parity, the CAR exterior-state signs, adjacent form-factor exchange (up to six factors), rational crossing, and the stripped two-particle weight at two exact on-shell points. It checks the deductions from the sourced exact amplitudes, not a lattice simulation or the construction of a local net from scratch.
