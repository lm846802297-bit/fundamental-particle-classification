# 1+1D: oriented chiral transport is not same-direction collision exchange

**Result.** In the [charged chiral-current example](chiral-current-wave-statistics-audit.md), two bounded right-moving charge creators realize the oriented algebraic phase at disjoint spatial locations. Nevertheless the direct co-moving version of light-ray collision averaging has identical incoming and outgoing products. For these creators its normalized in/out overlap is exactly one, not the sector braid. Manually reversing the order of the two stationary factors instead gives the algebraic phase. This is an obstruction to that specific extraction of asymptotic exchange, not a no-go theorem for all same-direction particle constructions.

## Bounded charge creators and exact co-moving limit

Use the two-dimensional product of chiral current observables on $u=t-x$ and $v=t+x$. Fix a localized right-ray automorphism $\rho$ of charge $q=1/\sqrt{2}$. Its product powers are charge $nq$, $n\in\mathbb{Z}$, by charge additivity; see [Adamo–Giorgetti–Tanimoto, §6.1](https://doi.org/10.1007/s00220-023-04835-1), including the calculation after Fig. 3. Take the direct sum of these representations with the neutral left-ray spectator. In a common realization on copies of the vacuum Hilbert space let $\pi(A)_n=\rho^n(A)$, with $\rho$ acting as the identity on the spectator. Use the vacuum vector $\Omega$ in the $n=0$ summand. Define the bilateral unitary shift $F$ sending $n$ to $n+1$ on the direct sum by the identity between those underlying copies. Then
$$
F^*\pi(A)F=\pi(\rho(A)).
$$
Choose a chiral observable transporter $V$ with $\rho'=\operatorname{Ad}V\circ\rho$ localized strictly to one side of $\rho$, and set $G=F\pi(V^*)$. Thus $G^*\pi(A)G=\pi(\rho'(A))$. Each creator commutes with observables spacelike to its chosen double cone because its corresponding automorphism is the identity there. This defines charged operators relatively local to observables; it does not assert that the charged creators form an ordinary local net with one another.

In the orientation with $c=V^*\rho(V)$, the same-charge chiral braid is $c=i$ (the other orientation gives $-i$). The covariance relation for $F$ gives
$$
FG=F^2\pi(V^*),\qquad
GF=F^2\pi(\rho(V^*))=\overline{c}\,FG .
$$
This is an operator calculation of stationary order, with self-monodromy $c^2=-1$. Both products applied to $\Omega$ have unit norm and lie in the $2q$ charge summand. The charge $2q$ labels their irreducible sector; it does not itself assign a particle number.

On each summand the translation by $(s,s)$ acts only on the common spectator representation. It therefore fixes $F$ and $G$ under conjugation, including for the transported representative. For every test profile $h_T$ with integral one, the right-moving light-ray average of either operator is itself. The direct $+,+$ analogue of the collision vectors is
$$
\Psi_T^{++}=F_+(h_T)G_+(h_T)\Omega=FG\Omega
$$
for every $T$, including either time sign. Consequently the analogue of the normalized in/out overlap is
$$
\frac{\langle\Psi_T^{++},\Psi_{-T}^{++}\rangle}
{\langle F_+(h_T)\Omega,F_+(h_{-T})\Omega\rangle
 \langle G_+(h_T)\Omega,G_+(h_{-T})\Omega\rangle}
=\frac{\|FG\Omega\|^2}{\|F\Omega\|^2\|G\Omega\|^2}=1 .
$$
Replacing $FG$ in one of the two products by $GF$ produces a phase (in the convention linear in the second entry, $\langle FG\Omega,GF\Omega\rangle=\overline c$), but it is a different prescription, not the early-time limit. There is no increasing relative separation under simultaneous right translation: the two smearing intervals in $u$ are unchanged. More concretely, for centers translated by $(T,\sigma_i T)$ their relative spatial offset is $\Delta x_0+(\sigma_2-\sigma_1)T$; fixed co-moving offsets do not reverse order. Opposite signs give a separation of order $|T|$ with opposite spatial order for the two time limits. This remains true at leading order under the sublinear time-smearing windows used for opposite-direction scattering. Fixed offsets can be spacelike for all synchronized $T$; the point is the absence of growing separation and early/late order reversal, not the absence of spacelike intervals.

## Independent check: even the neutral wave product is not a same-ray tensor map

[Dybalski–Tanimoto, arXiv:1101.5700v3](https://arxiv.org/pdf/1101.5700v3), §2.2 and §3.2, Proposition 3.2 and Theorem 3.3, identifies the vacuum asymptotic plus field of $A\otimes1$ as $A\otimes1$ in both limits. Its collision isometry uses a **plus and a minus** wave, one from each tensor factor. Attempt to reuse its multiplication prescription for two plus waves, after suppressing the spectator:
$$
A\Omega_{\rm R}\otimes B\Omega_{\rm R}\longmapsto AB\Omega_{\rm R}.
$$
Take a chiral vacuum Weyl unitary $W$ with nonzero one-particle smearing, so $|\langle\Omega_{\rm R},W\Omega_{\rm R}\rangle|<1$ by the Fock vacuum Weyl expectation. The two unit inputs $W\Omega_{\rm R}\otimes W^*\Omega_{\rm R}$ and $\Omega_{\rm R}\otimes\Omega_{\rm R}$ both give $\Omega_{\rm R}$ on the right, but their inner product is $|\langle\Omega_{\rm R},W\Omega_{\rm R}\rangle|^2<1$. An isometry on the full two-wave tensor space agreeing with this product prescription on all these vectors is impossible. This does not rule out an asymptotic construction whose input is not that tensor space or whose map is not this multiplication.

## Contrast: a genuine charge-dependent phase in an opposite-ray limit

[Dybalski–Mund, arXiv:2109.02128](https://arxiv.org/pdf/2109.02128), Eqs. (1.1)–(1.4), normalize an overlap of $F_+(h_T)G_-(h_T)\Omega$ with the corresponding early-time vector. In the **nonregular** vacuum GNS representation of the massless scalar Weyl field, Theorem 2.1, Eq. (2.8), obtains $\exp(-i q_f q_g/2)$ for $F=\pi(W(f)),G=\pi(W(g))$, with $q_f=\int f\,d^2x$ and $q_g=\int g\,d^2x$. In this specific GNS representation Eq. (2.7) puts all sharp null wave states in the neutral subspace; a nontrivial phase from charged operators describes infraparticle scattering under their normalized-overlap definition, not same-ray collisions of charged sharp waves. It is not legitimate to identify their charges or their collision phase with the current-net charge $q$ or its DHR braid. This example also rules out using momentum independence alone to identify a phase as statistics.
