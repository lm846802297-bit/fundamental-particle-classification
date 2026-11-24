# 1+1D Federbush model: a constant mutual collision phase between ordinary fermions

**Finding.** The constructive fermionic Federbush model has isolated charged mass shells, graded-local interpolating fields and asymptotically complete fermionic scattering. Its collision phase between different species can nevertheless be exactly $i$ or $-i$. Neither that phase nor a convention-dependent mixed exchange of dressed fields makes either individual particle nonfermionic.

## On-shell states and locality in the constructive model

[Ruijsenaars, *The Wightman Axioms for the Fermionic Federbush Model*, §§5A–C](https://www.researchgate.net/publication/225232249_The_Wightman_axioms_for_the_fermionic_Federbush_model) ([DOI](https://doi.org/10.1007/BF01218561)) constructs the theory on antisymmetric Fock space over two massive species, each with a particle and an antiparticle. For species $s=\pm1$ the one-body momentum is $p_s(\theta)=m_s(\cosh\theta,\sinh\theta)$; translations use the sum of these momenta in every Fock component (Eqs. (5.1)–(5.2)). The fields in Eq. (5.3) interpolate these species: Eqs. (5.26)–(5.28) give their LSZ fields, the proof identifies the one-fermion states of those fields and their adjoints with the Haag–Ruelle ones, and Eq. (5.40) completes that comparison on ordered multiparticle packets. Theorem 5.3 gives the Wightman axioms and asymptotic completeness for $|\lambda|<1/2$.

One can isolate the shells without requiring that the heavier mass lie below the lighter neutral continuum. Write the two conserved charges as $Q_s=n_s-\bar n_s$. In the component of total charge $\pm e_s$, where $e_s$ is the unit charge of species $s$, subtract one particle (or antiparticle for the minus sign) of species $s$. Every residual occupation has zero net charge **in each species**, so any nonempty residual content has at least one same-species particle–antiparticle pair. For positive-energy on-shell vectors the invariant mass of their sum is at least the sum of their masses, because each pairwise Minkowski product is $m_i m_j\cosh(\theta_i-\theta_j)\ge m_i m_j$. The threshold for any extra content in either charge-sign component is therefore
$$
M_{\rm extra}\ge m_s+2\min(m_{+},m_{-})>m_s .
$$
The threshold is an infimum approached by coincident velocities, regardless of antisymmetry. This is an isolation claim in the conserved charge components of the explicit Fock representation, not a classification of all DHR representations of an observable net.

At common coupling, Lemma 5.2, Eqs. (5.14)–(5.17), gives spacelike graded anticommutation of the odd interpolating fields and their adjoints on the stated domain. In particular the mixed-species coupling-difference phases in (5.16)–(5.17) equal one when $\lambda'=\lambda$. This is a locality statement for spacelike-separated smearings, **not** a claim that the interacting fields satisfy canonical equal-time CAR (the introduction explicitly distinguishes this). The in/out creation operators separately have the usual antisymmetric Fock statistics, by the LSZ/Haag–Ruelle identification; swapping identical-species asymptotic creators gives the ordinary fermion sign.

## Mixed collision eigenvalues are not a particle exchange invariant

The normalized LSZ operator in Ruijsenaars Eq. (5.27) acts on a two-particle component by
$$
S_\lambda(\theta_1,s_1,\delta_1;\theta_2,s_2,\delta_2)
 =\exp\!\left[-i\pi\lambda\,\operatorname{sgn}(\theta_1-\theta_2)
     (s_1-s_2)\delta_1\delta_2\right],
$$
where $s_i=\pm1$ is the species label and $\delta_i=\pm1$ distinguishes the two charge signs. The phase is symmetric under a simultaneous swap of both full particle slots; it multiplies an already antisymmetric state. At $\lambda=1/4$, for two positive charges with $\theta_1>\theta_2$, the two different-species channels $(+,-)$ and $(-,+)$ have the diagonal scattering operator
$$
D_{1/4}=\operatorname{diag}(-i,+i),\qquad
\operatorname{tr}D_{1/4}=0,\qquad
\det D_{1/4}=1 .
$$
The free reference in this same convention has $D_0=I$ and trace $2$. The mixed block cannot become $I$ by the same unitary change of labeled channel basis on both the in and out sides, which conjugates it. No claim is made about independent in/out rephasings, observability of a stand-alone phase, or equivalence of different field algebras.

[Castro-Alvaredo and Fring, *Form factors from free fermionic Fock fields, the Federbush model*, Eq. (64), p. 450](https://www.staff.city.ac.uk/~fring/AF-papers/QFT/Federbush.pdf) give the same mixed entries up to species/slot convention and explain their overall fermion minus as a choice to order the in and out states oppositely. Their array lists pairwise scattering factors, not transitions mixing the two ordered channels. Equations (51) and (55)–(59), pp. 448–449, also give a **different field-locality convention**, employing a step-function current primitive. For $\alpha,\beta=1,2$ their equal-time relation (59) has factor $c_{\alpha\beta}=-\exp[-2\pi i\lambda(-1)^\beta\delta_{|\alpha-\beta|,1}]$. For identical species $c_{\alpha\alpha}=-1$; for different species $c_{12}$ and $c_{21}$ are complex-conjugate phases, with $c_{12}c_{21}=1$. Thus the labeled reordering operator $|\alpha,\beta\rangle\mapsto c_{\alpha\beta}|\beta,\alpha\rangle$ squares to identity even in that presentation. The authors state that using the antisymmetric current primitive instead gives graded mutual locality for all species. The calculation neither equates the two field systems nor claims that charge dressing removes the LSZ interaction.

These are separate tests: graded locality and asymptotic self exchange characterize each charged fermion here; the mixed scattering eigenvalues characterize a collision. Involutivity of the labeled field reordering is not an inference from inverse-scattering unitarity and is not a DHR monodromy computation.
