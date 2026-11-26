# 1+1D interacting control: ordered three-state Potts kinks

**Result.** The ordered, thermally perturbed continuum three-state Potts theory has massive elementary kink scattering states. Its two-kink block at fixed equal outer vacua has two allowed middle vacua, and the exact elastic matrix switches them. Nevertheless, in a charge-increment basis the switch is precisely the reordering of two charge–rapidity pairs. After that reordering is accounted for, the remaining scalar factors are rapidity-dependent scattering amplitudes with crossing-related poles. The switch and the two-body amplitudes do not supply a separate exchange-statistics invariant.

**中文摘要：** 有序三态 Potts 连续场论的双扭结散射确实会切换中间真空标签。但改用相邻真空之差来标记扭结后，这个切换正好对应电荷与快度成对换序。余下的是依赖快度、具有交叉道极点的动力学散射相位，不是额外的编织统计。结论限于这个模型和所检验的散射数据。

## 1. Primary inputs and the one-kink sector

We use the Lorentz-invariant integrable field theory obtained by perturbing the $c=4/5$ critical Potts CFT by the thermal operator, on the ordered side with no external field. The model is defined on the infinite line; no lattice quasiparticle or medium is an input. The exact bulk amplitudes are due to [Chim and Zamolodchikov](https://doi.org/10.1142/S0217751X9200243X). For reproducible conventions, [Delfino and Cardy, §2, Eqs. (2.11)–(2.14), (2.21)–(2.25)](https://arxiv.org/pdf/hep-th/9712111) give the ordered kink chain and define which amplitudes change its intermediate vacuum; [Capizzi et al., Eqs. (2.13), (2.16)–(2.18)](https://inspirehep.net/files/59b87e63b1e94e1b756425c63032b114) give the specialized $q=3$ functions and the direct-channel pole.

There are three vacua labeled $a\in\mathbb Z_3$. The equal-mass kinks $K_{ab}$ with $a\ne b$ have on-shell momentum $p=m(\cosh\theta,\sinh\theta)$ and form the lightest charged scattering states in the source's $q=3$ bootstrap spectrum. A physical chain has neighboring labels unequal. A fixed $a\ne b$ boundary sector contains one $K_{ab}$ shell and allows a two-kink continuum with the third vacuum in the middle. In particular, for $p_i$ on the future mass shell, $(p_1+p_2)^2=4m^2\cosh^2((\theta_1-\theta_2)/2)\geq4m^2$, so the mass-$m$ shell is isolated below the continuum at $2m$. This is a statement in the documented scattering theory, not an independent mathematical construction of its observable net. The bootstrap also permits two kinks to fuse into the same elementary kink species; this is not evidence for an additional massive multiplet.

## 2. What actually flips in the neutral channel?

Fix equal outside vacua, say $a=0$. The two paths are $0\to1\to0$ and $0\to2\to0$. With rows and columns named by the outgoing and incoming **middle** vacuum, the ordered Zamolodchikov–Faddeev (ZF) map is
$$
R_{00}(\theta)=S_3(\theta) I+S_2(\theta)P
=S_2(\theta)\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad
S_2(\theta)=-\frac{\sinh[(\theta+i\pi/3)/2]}{\sinh[(\theta-i\pi/3)/2]} .
$$
Here $\theta=\theta_1-\theta_2$, and the rapidities on the outgoing ordered leg list are $(\theta_2,\theta_1)$. The zero $S_3$ holds specifically at $q=3$. For unequal outside vacua there is a single possible middle vacuum, with scalar
$$
S_1(\theta)=\frac{\sinh[(\theta+2i\pi/3)/2]}{\sinh[(\theta-2i\pi/3)/2]} .
$$

For arbitrary chain length, set $d_j=a_j-a_{j-1}\bmod3$, represented as $+1$ or $-1$. Given the starting vacuum and the ordered increments, all vacuum labels are recovered recursively. The ending vacuum only fixes $\sum_j d_j\bmod3$. In the neutral two-kink sector the paths above are the words $(+,-)$ and $(-,+)$, so the matrix $P$ swaps their charge increments. In the charged two-kink sector those increments are equal. Thus under this same relabeling on every chain the full rule is
$$
((d_1,\theta_1),(d_2,\theta_2))
\longmapsto S_{d_1d_2}(\theta)
((d_2,\theta_2),(d_1,\theta_1)),\qquad
S_{++}=S_{--}=S_1,\quad S_{+-}=S_{-+}=S_2.
$$
The unchanged external charges can equivalently be read at **fixed rapidity**: after reordering the outgoing list back to the incoming rapidity convention there is no charge transfer. This transformation only reindexes asymptotic labels. It neither identifies distinct physical vacuum sectors nor asserts an equivalence of local field algebras. The fact that $S_3=0$ and the increments are conserved at each rapidity is essential to this conclusion and is not assumed for $q>3$.

## 3. An exact dynamical diagnostic

In the fixed-charge/rapidity identification the neutral amplitude is the scalar $S_2$. A consistent per-particle rephasing of charged asymptotic states cancels between the two sides of the ZF relation: each side has exactly the same two $(d,\theta)$ pairs. This does not give an absolute phase under arbitrary independent in/out multi-particle conventions, but it does let us check the standard scattering phase without depending on how the vacuum paths were named.

The logarithmic phase slope in this convention is
$$
-i\,\partial_\theta\log S_2(\theta)=-\frac{\sqrt3}{2\cosh\theta-1},
\qquad
-i\,\partial_\theta\log S_1(\theta)=-\frac{\sqrt3}{2\cosh\theta+1}.
$$
At $\theta=\log2$, the two slopes are $-2\sqrt3/3$ and $-2\sqrt3/7$. A constant Bose/Fermi sign or a constant statistics matrix has no such scattering-phase slope. In fact the slopes differ, so a common rapidity-dependent scalar cannot turn both channels into constants. This compares channel functions; it does not require coherent interference between distinct topological sectors.

Analytic continuation independently checks that the functions are scattering data. With $x=e^\theta$ and $z=e^{i\pi/3}$, put $f_v(x)=(xv-1)/(x-v)$. Then $S_1=f_{z^2}(x)$ and $S_2=-f_z(x)$. Crossing $\theta\to i\pi-\theta$ sends $x\to-1/x$; algebraically $f_{z^2}(x)=-f_z(-1/x)$. In the physical strip $0<\operatorname{Im}\theta<\pi$ the direct pole is at $\theta=2i\pi/3$ in $S_1$ with $\operatorname{Res}_\theta S_1=i\sqrt3$, and its crossed partner is at $\theta=i\pi/3$ in $S_2$ with $\operatorname{Res}_\theta S_2=-i\sqrt3$ in these conventions. Explicitly, the Jacobian $dx/d\theta=x$ turns the residue of $f_v$ into $v-v^{-1}$. The direct pole gives $M=2m\cos(\pi/3)=m$, precisely the existing elementary kink. The crossed pole is not an additional neutral bound state at $q=3$. The charge assignments also close the elementary fusion bootstrap: writing the two equal-charge constituent rapidities as $\theta\pm i\pi/3$, their scattering against an equal-charge spectator obeys $S_1(\theta+i\pi/3)S_1(\theta-i\pi/3)=S_2(\theta)$, the amplitude for the fused opposite-charge kink against that spectator.

Finally $R(\theta)R(-\theta)=I$: the second ZF step is at $-\theta$ because the first swapped the rapidities. This is **elastic inverse-scattering unitarity**, not a statement about the holonomy of a same-oriented exchange path. Squaring the numerical matrix at the same $\theta$ instead would generally give $S_2(\theta)^2 I$ in the neutral block, but is not the operation on ordered asymptotic states. Likewise $S_{1,2}(+\infty)=e^{\pm2\pi i/3}$ are high-rapidity limits of the above analytic amplitudes; by themselves they do not define a braid of massive identical particles. These observations do not classify separate UV field-locality or parafermion data.

## 4. Decision and reproduction

This is an interacting $1+1$D control after the [free Ising case](ordered-ising-kink-audit.md). The middle-vacuum switch and nonconstant two-body phases are accounted for by asymptotic charge relabeling and factorized scattering, respectively. No new statistics is established by these observables. A whole-theory Bose/Fermi equivalence, a general obstruction for other kink models, and a classification of field exchange algebras are not claimed. In another interacting candidate one must redo the on-shell and labeling checks, especially if the analogue of $S_3$ is nonzero.

Run **python3 checks/verify_ordered_potts_kink.py** from the repository root. It verifies the vacuum-path bijection, the permutation of charge–rapidity pairs, crossing, inverse-scattering unitarity, factorized three-kink reorder consistency, and the phase slope and pole residues using exact rational arithmetic in $\mathbb Q(i\sqrt3)$. It tests consequences of the quoted amplitudes, not their bootstrap derivation or completeness of the model.
