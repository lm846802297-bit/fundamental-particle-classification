# 1+1D chiral current: a null wave with nontrivial sector monodromy

**Decision.** In the local two-dimensional product of two chiral $U(1)$-current nets, one charged sector has both a nonzero, sharp null-wave subspace and nontrivial DHR monodromy. It has exactly one wave direction. Neither this result nor the corresponding two-sided-charge control gives a fundamental massive particle or demonstrates a same-chirality multiparticle exchange on an asymptotic particle space. Absence of massive particles is not absence of all sharp waves in a braided sector.

## Same net, same sector

Use $u=t-x,\ v=t+x$; the double-cone net is $\mathcal A(I\times J)=\mathcal A_1(I)\bar\otimes\mathcal A_2(J)$, with the chiral current net on each ray. The local observable net on the Minkowski plane is the product itself, not an extension by charged fields. Write $X=(a,b)$ for the product of current automorphism sectors of charges $a,b\in\mathbb R$. The chiral charges are transportable and can be localized in arbitrary bounded intervals. Consequently $X$ localizes in a double cone: both chiral automorphisms are trivial on the projections of either spacelike complementary component; charge transporters are products of chiral transporters. The sector is positive-energy covariant for ordinary connected $1+1$-dimensional Poincaré transformations, obtained from translations of the two rays and opposite ray dilations.

Use the final charge convention in §6.1 of [Adamo, Giorgetti and Tanimoto, *Wightman Fields for Two-Dimensional Conformal Field Theories with Pointed Representation Category*](https://doi.org/10.1007/s00220-023-04835-1), including the equal-profile calculation after Fig. 3: the oriented chiral **sector** braiding is $e^{i\pi ac}$ for charges $a,c$, or its opposite for the reverse spatial order. In the two-dimensional transporter formula the signs on the two ray factors are opposite: a region to the spatial right has $u$ lower and $v$ higher. Taking one orientation as positive, for $Y=(c,d)$ the scalar braid and the same-orientation double braid are therefore
$$
 c^{+}_{X,Y}=e^{i\pi(ac-bd)},\qquad
 M_{X,Y}=c^{+}_{Y,X}c^{+}_{X,Y}=e^{2\pi i(ac-bd)}.
$$
Reversing the overall convention complex-conjugates both. This product of two same-orientation braids is not the composition of a braid with its inverse. It is an endomorphism of $X\otimes Y$; changing the sector representatives or the tensor-intertwiner basis conjugates it, so its scalar cannot be removed by an equivalent presentation. It is not a collision $S$-matrix.

## Independent translation-spectrum test

Let $K_a\ge 0$ generate translations on a ray in charge $a$, and $E_a$ be its projection onto $\ker K_a$. In the vacuum charge $E_0=|\Omega\rangle\langle\Omega|$; for $a\ne0$, $E_a=0$. For the latter statement the current Fock charge representation has $J_0=a$ and lowest rotation energy $h=a^2/2>0$ (current stress tensor $L_0=\tfrac12 J_0^2+\sum_{n>0}J_{-n}J_n$; compare [Adamo–Giorgetti–Tanimoto](https://doi.org/10.1007/s00220-023-04835-1), §§2.1, 6.2). A translation-fixed vector of a strongly continuous unitary Möbius representation, including the universal cover, is Möbius-fixed. One way to see it is to denote upper and lower unipotents by $n,\bar n$ and $D_r=\operatorname{diag}(r,r^{-1})$, $r>0$. For $y\ne0$,
$$
 n_{(r-1)/y}\bar n_y n_{(r^{-1}-1)/y}=\bar n_{y/r}D_r .
$$
It also holds for the continuous lifts (both sides agree at $r=1$, then vary continuously). The matrix element of the left side on a translation-fixed vector tends to its norm squared as $y\to0$; hence the vector is fixed by $D_r$. Diagonal conjugation then contracts the lower unipotents to the identity, so the vector is fixed by both unipotent groups, which generate the cover. Positive $h$ forbids such a vector.

In $X=(a,b)$ write $A=K_a\otimes1$, $B=1\otimes K_b$. Using $U(t,x)=e^{iHt-iPx}$, one has $H=A+B,\ P=A-B,\ M^2=4AB$; the joint spectral theorem gives the **exact projections**
$$
 \mathbf1_{H-P=0}=1\otimes E_b,\qquad
 \mathbf1_{H+P=0}=E_a\otimes1.
$$
These are the projection versions of [Dybalski and Tanimoto, arXiv:1101.5700v3](https://arxiv.org/pdf/1101.5700v3), §3.3, Proposition 3.5. In every row below common dilations scale $M^2$ by an arbitrary positive factor. If $M^2$ had a positive eigenvalue, its unitary translates under dilations would give nonzero orthogonal eigenspaces for uncountably many distinct eigenvalues, impossible on a separable Hilbert space. This excludes even a positive-mass atom in these product sectors, but does **not** say their timelike spectrum is empty.

With $q=1/\sqrt 2$:

| Charge sector $X$ | Oriented self-braid | Self-monodromy | Sharp null-wave subspaces | Positive mass shell |
|---|---:|---:|---|---|
| $(0,0)$ | $+1$ | $+1$ | Both, with the common vacuum removed | No |
| $(q,0)$ | $i$ | $-1$ | Right only: $\mathcal H_q\otimes\mathbb C\Omega$ | No |
| $(0,q)$ | $-i$ | $-1$ | Left only: $\mathbb C\Omega\otimes\mathcal H_q$ | No |
| $(q,q)$ | $+1$ | $+1$ | Neither | No |

Dybalski–Tanimoto §2.1 use the term “Wigner particles” in their two-dimensional scattering framework when there are nonvacuum waves in **both** directions. Their Proposition 3.5 and Theorem 3.6 allow a charged irreducible product representation with a wave in one direction and nonzero asymptotic detector functionals, still classified there as an infraparticle theory. Their vacuum result (Theorem 3.3) does not construct exchange scattering of two charged waves in one direction. The table establishes a sharp null projection and braided transport in one and the same charged representation, not that its null subspace is a unique elementary Wigner species or that the braid is an operational asymptotic exchange.

## Position in the 1+1D review

| Track | Best established in this dossier | What is still missing from the fundamental-particle claim |
|---|---|---|
| Massive kink sectors | Genuine kink shells and orientation-compatible composition; round trips of the reconstructed admissible arrangement intertwiners cancel ([audit](kink-quasistatistics-audit.md)). | A transport-invariant non-Bose/Fermi exchange on identical asymptotic particles in a specified model. |
| Massive compact-localized charges | Conditional DHR exclusion under double-cone Haag duality and wedge split; the charged scalar control drops the former and has bosonic statistics ([audit](massive-dhr-duality-audit.md)). | A massive charged example together with an intrinsic non-symmetric statistics invariant in its own physical sector. |
| Massive order–disorder extension | Nontrivial monodromy in the nonlocal extension, but not on the demonstrated electric shell of the original represented observables ([audit](massive-order-disorder-monodromy-audit.md)). | A new mass shell in the flux sector, with the nontrivial braiding certified in that same physical setting. |
| Product $U(1)$-current sector | Nontrivial monodromy and one sharp wave direction coexist in one massless charged sector. | Fundamental single-particle identification and a charged asymptotic exchange that realizes the monodromy; no positive-mass candidate here. |

This is a checkpoint for the investigated classes, not a universal 1+1D exclusion. It does not close the separate deformed-spacetime track. The highest-signal next massless check is a source-backed two-charge asymptotic construction (or an obstruction to it), not another chiral twist computation.
