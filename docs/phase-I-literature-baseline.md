# Phase I Literature Baseline: Fundamental Particles Beyond Bose and Fermi

**Status:** Initial source-verified baseline; not an exhaustive classification.  
**Scope:** Fundamental particles in relativistic QFT only. Condensed-matter quasiparticles, collective excitations, emergent excitations, and composite bound states are excluded.

## Executive result

The broad existence question is already answered **yes** if 2+1-dimensional relativistic QFT is in scope.

Massive anyons and non-Abelian plektons are established particle-bearing sectors of local relativistic quantum theories in 2+1-dimensional Minkowski spacetime. Their one-particle states are associated with unitary ray representations of the 2+1D Poincare group; massive anyons can have arbitrary real spin; their localization is string-like/spacelike-cone-like rather than point-like; and a relativistic spin-statistics theorem has been proved under explicit mass-spectrum assumptions.

This is not a condensed-matter result. The relevant constructions and theorems are formulated directly in relativistic particle theory and local relativistic QFT.

The research question must therefore be sharpened after this baseline:

- The existence of at least one non-Bose/non-Fermi fundamental-particle class is established in 2+1D.
- The remaining work is to determine whether there are further classes beyond known anyons/plektons, and to establish the strongest dimension- and localization-dependent restrictions in 1+1D, 3+1D, and higher dimensions.

## 1. Particle representations: Wigner's starting point

For a Poincare-covariant theory, an elementary one-particle state is organized by a positive-energy unitary irreducible representation (or ray representation, when projective representations are relevant) of the spacetime symmetry group.

The induced-representation method separates:

1. the orbit of the momentum under Lorentz transformations, which gives the mass shell or massless orbit;
2. the little group stabilizing a standard momentum;
3. a unitary irreducible representation of that little group, which supplies the particle's spin or polarization data.

For spacetime dimension D:

- Massive representations are controlled by the rotation little group Spin(D-1).
- Massless representations are controlled by the Euclidean little group ISO(D-2), with finite-helicity/discrete-spin representations when the translation part acts trivially and continuous-spin-type representations when it acts nontrivially.

The most important dimension-specific cases for this project are:

| Spacetime | Massive little group (universal cover) | Immediate implication |
| --- | --- | --- |
| 1+1 | Trivial connected rotation little group | No ordinary massive spin label; low-dimensional sector statistics require separate treatment |
| 2+1 | Universal cover of SO(2), isomorphic to R | Massive spin can be any real number |
| 3+1 | SU(2) | Massive spin is integer or half-integer |
| D>4 | Spin(D-1) | Richer little-group representations, but this alone does not imply new exchange statistics |

The 2+1D case is decisive: the universal cover of the massive rotation subgroup allows arbitrary real spin. This representation-theoretic fact is part of the foundation of relativistic anyons.

### Continuous-spin representations are not a third statistics class

Continuous-spin representations are genuine, unusual Poincare representations. In 3+1D, their helicity spectrum contains an unbounded tower of integer helicities or an unbounded tower of half-integer helicities. The representation is new at the level of spacetime symmetry, but it does not by itself establish a statistics class beyond Bose/Fermi.

This project must keep two questions separate:

- Is the Poincare representation new?
- Is the physical exchange/statistics structure genuinely beyond Bose/Fermi?

A positive answer to the first does not imply a positive answer to the second.

Primary references:
- E. P. Wigner, “On Unitary Representations of the Inhomogeneous Lorentz Group,” Ann. Math. 40, 149–204 (1939), DOI: 10.2307/1968551.
- X. Bekaert and E. D. Skvortsov, “Elementary particles with continuous spin,” arXiv:1708.01030.
- X. Bekaert, J. Mourad, and M. Najafizadeh, “Continuous-spin field propagator and interaction with matter,” JHEP 11 (2017) 113, DOI: 10.1007/JHEP11(2017)113.

## 2. The conventional spin-statistics theorem

Pauli's original relativistic argument connects positive energy and spacelike commutativity of observables with Fermi-Dirac statistics for half-integral spin and Einstein-Bose statistics for integral spin. Its scope and hypotheses must be recorded precisely; it is not a dimension-independent theorem obtained from group theory alone.

Luders and Zumino subsequently established the spin-statistics connection for interacting fields from a set of QFT postulates, with their 1958 paper explicitly treating spin zero and spin one-half.

For this project, every use of “the spin-statistics theorem” must identify:

- spacetime dimension and spacetime symmetry group;
- whether the result concerns free wave equations, Wightman fields, observable-algebra sectors, or another framework;
- positivity and spectrum assumptions;
- point/bounded-region versus string/cone localization;
- locality or graded-locality assumptions;
- whether finite statistics, mass gaps, or mass degeneracy restrictions are imposed.

Primary references:
- W. Pauli, “The Connection Between Spin and Statistics,” Phys. Rev. 58, 716 (1940), DOI: 10.1103/PhysRev.58.716.
- G. Lüders and B. Zumino, “Connection between Spin and Statistics,” Phys. Rev. 110, 1450–1453 (1958), DOI: 10.1103/PhysRev.110.1450.

## 3. DHR sectors, parastatistics, and gauge reconstruction

Doplicher, Haag, and Roberts (DHR) developed a description of superselection sectors using local observables. Under their localization and transportability framework, composing identical sectors produces representations of the permutation group. Their analysis includes parastatistics: the statistics parameter can take values corresponding to para-Bose or para-Fermi statistics of finite order.

The key distinction for this project is between:

- a nontrivial representation of the permutation group at the level of sector composition;
- a genuinely new physical particle statistics class;
- a reformulation using ordinary Bose/Fermi fields with additional internal or gauge degrees of freedom.

Doplicher-Roberts reconstruction shows, under the relevant symmetric tensor-category hypotheses, how a compact gauge group and a field algebra can be reconstructed from the observable-sector structure. This is why finite parastatistics in the standard DHR setting are not automatically evidence for a new fundamental statistics class under this project's inequivalence criterion.

The localization regime is essential. In 2+1D, bounded-region DHR localization and spacelike-cone localization must not be conflated: the relativistic anyon/plekton sectors use spacelike-cone-like localization, which allows braid-group statistics. One must not infer braid statistics from the spacetime dimension alone.

The theorem is conditional. The hypotheses—especially localization, finite statistics, conjugates, symmetry of the tensor category, and the structure of the tensor unit—must be checked before applying the reconstruction result.

Primary references:
- S. Doplicher, R. Haag, and J. E. Roberts, “Local Observables and Particle Statistics I,” Commun. Math. Phys. 23, 199–230 (1971), DOI: 10.1007/BF01877742.
- S. Doplicher, R. Haag, and J. E. Roberts, “Local Observables and Particle Statistics II,” Commun. Math. Phys. 35, 49–85 (1974), DOI: 10.1007/BF01646454.
- S. Doplicher and J. E. Roberts, “A New Duality Theory for Compact Groups,” Invent. Math. 98, 157–218 (1989), DOI: 10.1007/BF01388849.
- S. Doplicher and J. E. Roberts, “Why There Is a Field Algebra with a Compact Gauge Group Describing the Superselection Structure in Particle Physics,” Commun. Math. Phys. 131, 51–107 (1990), DOI: 10.1007/BF02097680.

## 4. Localization: point, bounded-region, string, and cone

Localization is a decisive variable, not a technical afterthought.

In their four-dimensional analysis, Buchholz and Fredenhagen showed that massive particle states in local relativistic theories, including gauge theories, can be associated with localization in spacelike cones even when their field-theoretic description requires nonlocal, unobservable fields assigned to infinite string-like regions. In that framework the resulting particle statistics are Bose, Fermi, or para-statistics; cone localization by itself does not produce 2+1D braid statistics.

For 2+1D anyons, string-like/spacelike-cone localization is precisely the setting in which braid-group statistics can occur. Thus “not point-localized” must not be confused with “not a fundamental particle.” The physical one-particle state and its observable sector remain the objects to classify.

The comparison must distinguish:

- point-local fields;
- bounded-region-localized charges;
- spacelike-cone-localized charges;
- string-localized field operators;
- localization structures defined directly on the one-particle Hilbert space.

Primary references:
- D. Buchholz and K. Fredenhagen, “Locality and the Structure of Particle States,” Commun. Math. Phys. 84, 1–54 (1982), DOI: 10.1007/BF01208370.
- J. Mund, “Modular Localization of Massive Particles with ‘Any’ Spin in d=2+1,” arXiv:hep-th/0208195.

## 5. Established non-Bose/non-Fermi fundamental particles in 2+1D

### 5.1 One-particle representation

Jackiw and Nair construct anyon one-particle states as unitary representations of the 2+1D Poincare algebra. A massive anyon has one physical polarization, while a covariant field realization for nonintegral/non-half-integral spin requires more field components and an appropriate gauge symmetry or constraint.

Mund constructs a modular localization structure for massive anyons with arbitrary real spin directly from the corresponding Poincare ray representation. The localization is string-like rather than point-like or bounded-region-like.

### 5.2 Statistics and spin

In 2+1D, the exchange topology is governed by the braid group rather than only the permutation group. For Abelian anyons, an exchange acts by a phase. For non-Abelian plektons, exchanges act by matrices on the relevant multiparticle/fusion space.

Mund proves the relativistic spin-statistics relation for massive braid-statistics sectors:
\[
e^{2\pi i s}=\omega.
\]

The theorem starts from local relativistic quantum theory. Its stated assumptions include a massive particle of mass m>0 in a charged sector, a mass gap separating m from the rest of that sector's mass spectrum, and finitely many particle types at that mass with a common spin. It also establishes particle-antiparticle symmetry for these sectors.

This is a direct positive result for the project's fundamental-particle criterion. It is not based on a condensed-matter medium or a collective excitation.

Primary references:
- R. Jackiw and V. P. Nair, “Relativistic Wave Equation for Anyons,” Phys. Rev. D 43, 1933–1942 (1991), DOI: 10.1103/PhysRevD.43.1933.
- J. Mund, “Modular Localization of Massive Particles with ‘Any’ Spin in d=2+1,” arXiv:hep-th/0208195.
- J. Mund, “The Spin-Statistics Theorem for Anyons and Plektons in d=2+1,” Commun. Math. Phys. 286, 1159–1180 (2009), DOI: 10.1007/s00220-008-0628-9, arXiv:0801.3621.
- K. Fredenhagen, K.-H. Rehren, and B. Schroer, “Superselection Sectors with Braid Group Statistics and Exchange Algebras. I. General Theory,” Commun. Math. Phys. 125, 201–226 (1989), DOI: 10.1007/BF01217906.
- K. Fredenhagen, K.-H. Rehren, and B. Schroer, “Superselection Sectors with Braid Group Statistics and Exchange Algebras II: Geometric Aspects and Conformal Covariance,” Rev. Math. Phys. 4, 113–157 (1992), DOI: 10.1142/S0129055X92000170.

## 6. Adjacent generalized spin-statistics results

Krulewski, Müller, and Stehouwer (2025) prove a higher spin-statistics theorem for reflection-positive invertible field theories using an action of the stable orthogonal group and higher-categorical data. This is an important generalized spin-statistics result, but it is not a classification of ordinary particle exchange statistics. The paper explicitly excludes 2+1D anyons when introducing the usual Bose/Fermi particle dichotomy. It should therefore be tracked as adjacent mathematical structure, not counted as evidence for an additional elementary-particle statistics class.

Reference: C. Krulewski, L. Müller, and L. Stehouwer, “A Higher Spin Statistics Theorem for Invertible Quantum Field Theories,” Commun. Math. Phys. 406, 230 (2025), DOI: 10.1007/s00220-025-05405-3, arXiv:2408.03981.

## 7. Initial dimension-by-dimension map

| Spacetime | Established particle/statistics structure | What remains to check |
| --- | --- | --- |
| 1+1 | Chiral/conformal superselection theories can have braid-like statistics | Which structures correspond to massive asymptotic fundamental particles in relativistic QFT; do not identify chiral sectors with massive particle exchange without proof |
| 2+1 | Massive anyons and non-Abelian plektons with braid-group statistics are established in relativistic QFT | Whether any further inequivalent fundamental-particle classes exist beyond the known braid-statistics framework |
| 3+1 | Standard local QFT and DHR/BF frameworks yield permutation-type statistics; finite parastatistics can be related to compact gauge structure under reconstruction hypotheses | Establish the strongest no-go result and inspect sectors outside the exact DHR/BF assumptions |
| D>4 | Point-particle configuration-space topology has permutation group S_N for spatial dimension at least three; massive/massless little groups become richer | Prove which QFT sector and localization theorems extend to each dimension; do not infer a complete no-go from topology alone |

The point-particle configuration-space result is a kinematic constraint: in at least three spatial dimensions the fundamental group of the configuration space of identical point particles is the permutation group. It does not, by itself, prove every possible QFT no-go theorem. Higher-dimensional little-group representations can be more complicated without creating a new exchange-statistics class.

## 8. Candidate classes: current status

| Candidate | Status for this project | Reason |
| --- | --- | --- |
| Ordinary bosons and fermions | Established baseline | Standard relativistic particle classes |
| Abelian anyons | Established positive result in 2+1D relativistic QFT | Arbitrary real spin and Abelian braid statistics |
| Non-Abelian plektons | Established positive result in 2+1D relativistic QFT | Non-Abelian braid-group statistics |
| Parastatistics | Established mathematical/statistical sectors; not automatically a new physical class | DHR/DR reconstruction can encode finite parastatistics using ordinary fields with compact gauge structure under stated assumptions |
| Higher-spin particles | Not a new statistics class by themselves | New Poincare representation labels do not determine a new exchange algebra |
| Continuous-spin particles | Not a new statistics class by themselves | New massless Poincare representations; in 4D the helicity tower is integer or half-integer |
| Infinite statistics and other generalized algebras | Candidate area; not accepted without a relativistic fundamental-particle construction | Must pass observable-sector, locality, positivity, and inequivalence tests |
| R-matrix/generalized parastatistics constructions | Algebraic candidate area; not yet an accepted QFT particle result | A condensed-matter realization or exchange algebra alone does not meet this project's particle criterion |

## 9. Phase I conclusions and next tasks

### Established conclusions

1. The broad existence question has a positive answer in 2+1D: relativistic anyons and plektons are fundamental particle sectors beyond ordinary Bose/Fermi statistics.
2. Arbitrary real spin in 2+1D is tied to braid-group statistics by a relativistic spin-statistics theorem under stated spectral assumptions.
3. String/cone localization is compatible with fundamental particle status.
4. Higher-spin and continuous-spin representations must not be counted as new statistics classes without a separate exchange-statistics result.
5. Parastatistics must be tested against DHR/DR gauge reconstruction before being counted as physically inequivalent.

### Next bounded tasks

1. Complete a theorem-hypothesis ledger for Pauli, Lüders-Zumino, DHR I/II, Buchholz-Fredenhagen, and Doplicher-Roberts.
2. Derive the little-group comparison for D=2, 3, 4, and D>4 from the induced-representation method.
3. Separate the 1+1D chiral/conformal braid-sector literature from massive asymptotic-particle constructions.
4. Establish exactly which 3+1D no-go statements follow from bounded localization, spacelike-cone localization, finite statistics, and the Bisognano-Wichmann property.
5. Extend the comparison to D>4 without assuming that the four-dimensional theorem automatically generalizes.

**Phase I is not yet complete.** This document records a verified first baseline and the next finite set of literature checks; it does not claim an exhaustive classification.
