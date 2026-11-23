# 1+1D interacting control: physical reflection of sine-Gordon kinks

**Result.** In the repulsive continuum sine-Gordon theory, soliton–antisoliton scattering can change which topological charge emerges in the fast rapidity bin. This is not the bookkeeping switch found in the [three-state Potts control](ordered-potts-kink-audit.md). At coupling $\xi=2$, the probability is $4M^2/s$, where $M$ is the kink mass and $s$ the squared center-of-mass energy. A charge-resolved projector makes the result invariant under reindexing and under consistent changes of basis. The soliton operator nevertheless has ordinary equal-time fermionic anticommutation in the massive-Thirring description. This example separates measurable reflection from exchange statistics.

**中文摘要：** 排斥区 sine-Gordon 连续场论中，快速出射粒子的拓扑电荷确实可以反转，不能靠重标记消去。在 $\xi=2$ 时，反射概率为 $4M^2/s$。独立计算表明，与这些扭结对应的 Thirring 费米场仍满足普通等时反对易关系。因此，非对角散射是物理相互作用，并不等于第三种交换统计。

## 1. On-shell model and inputs

Use the infinite-line Lorentz-invariant quantum sine-Gordon model, not a medium, lattice quasiparticle or classical soliton approximation. In the standard scalar normalization let $\xi=\beta^2/(8\pi-\beta^2)$ and specialize to $\xi=2$ ($\beta^2=16\pi/3$). In the repulsive regime $\xi>1$ the exact scattering spectrum consists of the stable charge-$+1$ soliton and charge-$-1$ antisoliton of common mass $M$, with no breathers. [Nagy, Takács and Kormos, §2, Eqs. (2.2)–(2.5)](https://arxiv.org/pdf/2312.03909) state the continuum spectrum and amplitudes; [Pálmai and Takács, §II, Eq. (2.1) and the following equations](https://arxiv.org/pdf/1209.6034) give the same matrix convention. The original scattering construction is [Zamolodchikov and Zamolodchikov, Ann. Phys. 120, 253–291 (1979), §4](https://doi.org/10.1016/0003-4916(79)90391-9).

Each one-kink state has $p=M(\cosh\theta,\sinh\theta)$. Total charge in the sector of one kink is $\pm1$, so with only the doublet in the spectrum the next possible number of on-shell kinks is three. The sum of future momenta has invariant mass at least $3M$ for such states. The single-kink shell is therefore separated from the multiparticle continuum in this charged sector of the exact scattering description. There is no neutral bound-state composite being counted here.

## 2. Reflection that survives a charge-preserving reindexing

For real rapidity gap $\theta=\theta_{\rm fast}-\theta_{\rm slow}>0$, use basis $(|+-\rangle,|-+\rangle)$ in which the slots are **physical rapidities, fast then slow**, both incoming and outgoing. The source amplitudes in this convention give
$$
S_{\rm neutral}=S_0(\theta,\xi)\widetilde S,\qquad
\widetilde S=\begin{pmatrix}t&r\\r&t\end{pmatrix},\quad
t=\frac{\sinh(\theta/\xi)}{\sinh[(i\pi-\theta)/\xi]},\quad
r=\frac{i\sin(\pi/\xi)}{\sinh[(i\pi-\theta)/\xi]} .
$$
$S_0$ is a pure phase on real rapidity. Transmission keeps the charge attached to each rapidity; reflection exchanges the charges at those rapidities while preserving total charge and the unordered set of momenta. An ordered-leg ZF convention which reverses the outgoing rapidity list must first be converted to this fixed-rapidity convention.

For an incoming fast positive charge, the probability of outgoing fast negative charge is
$$
\mathcal P=\operatorname{tr}
  (P_-^{\rm out}\widetilde S P_+^{\rm in}\widetilde S^\dagger)=|r|^2 ,
$$
where the projectors resolve the physical fast-bin charge in each Hilbert space. Under independent unitary basis changes $U_{\rm in/out}$, transform $\widetilde S\mapsto U_{\rm out}\widetilde S U_{\rm in}^\dagger$ and transform each projector on its respective side. The trace is unchanged. Diagonalization of $\widetilde S$ cannot remove the reflection prediction: it instead makes the charge projectors non-diagonal. Similarly, permuting the two outgoing basis vectors without transporting the projectors compares different observables. One can distinguish the asymptotically separated packets by velocity and the sign of the topological charge they carry, the latter given by the scalar-field winding or the integral of $j^0=(\beta/2\pi)\partial_x\phi$ over the packet region. The expression above is the narrow-packet on-shell limit, not a finite-time claim about a sharp local charge projector. It is not a same-species braid diagnostic.

For real $\theta$, the exact formulas give
$$
|r|^2=\frac{\sin^2(\pi/\xi)}
{\sinh^2(\theta/\xi)+\sin^2(\pi/\xi)}.
$$
At $\xi=2$ this reduces to $\operatorname{sech}^2(\theta/2)$, and on-shell kinematics give $s=4M^2\cosh^2(\theta/2)$. At the exact test point $\theta=2\log2$ one has
$$
t=-3i/5,\quad r=4/5,\quad s=25M^2/4,\quad
\mathcal P=16/25 .
$$
The two eigenvalues $(-3i\pm4)/5$ of the stripped block are interaction-dependent eigenphases, not statistics signs. Across the elastic continuum the reflection probability falls strictly as $s$ rises above threshold. At the different coupling $\xi=1$ (the free fermion point) reflection is absent for every fixed $\theta>0$. This is a change of dynamics, not a change of fermion exchange. Inverse scattering unitarity relates $\theta$ to $-\theta$; squaring a numerical matrix at the same positive gap does not implement a double topological exchange.

## 3. Independent equal-time check

[Coleman](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.11.2088) relates the neutral sector to the massive Thirring model and identifies the sine-Gordon soliton with its fundamental fermion. We do not use the neutral-sector result alone to infer a statement about charged fields. [Mandelstam](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.11.3026) constructs charged soliton operators satisfying the Thirring anticommutation relations. [Juričić and Sazdović, Eqs. (3.26)–(3.30)](https://arxiv.org/pdf/hep-th/0210074) give an independent canonical derivation.

The same-component sign can be checked directly at distinct equal-time points. Write $I(x)=\int_{-\infty}^x\Pi(z)\,dz$ and $A_\pm(x)=\pm(\beta/2)\phi(x)+(2\pi/\beta)I(x)$; normalizations and the common sign of the exponent do not affect the following reordering. The soliton operator has the form $:\!e^{-iA_\pm(x)}\!:$ up to component factors. With $[\phi(x),\Pi(y)]=i\delta(x-y)$, one obtains
$$
[A_\pm(x),A_\pm(y)]=\mp i\pi\,\operatorname{sgn}(x-y).
$$
The central commutator therefore yields a factor $e^{\pm i\pi\operatorname{sgn}(x-y)}=-1$ when the separated operators are reversed. The coefficient is independent of $\beta$ because $(\beta/2)(2\pi/\beta)=\pi$. This calculation only checks the separated same-component sign; coincident-point distributional CAR and the full charged-field construction are supplied by the references. The string integral also shows why this operator is not just a point-local polynomial in the scalar field. Neither this calculation nor the neutral duality asserts equality of all local nets, boundary conditions or field presentations.

## 4. Scope and reproduction

Physical reflection survives reindexing in this model and has a coupling- and energy-dependent probability, even though the charged interpolating fields admit a conventional fermionic presentation. Thus real, nonzero vacuum/charge redistribution in a collision is not sufficient evidence for an additional particle statistics class. No general no-go or claim about other kink models follows.

Run **python3 checks/verify_repulsive_sine_gordon_kink.py** from the repository root. The verifier uses exact rational and Gaussian-rational arithmetic to check the amplitude reduction, on-shell kinematics in two parametrizations, inverse scattering and fast-bin probability before and after independent basis changes, and the separated canonical phase. It checks the deductions from the cited exact theory, not a simulation or proof of that theory.
