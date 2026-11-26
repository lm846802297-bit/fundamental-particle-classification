# Adler 分支：孤立质量壳上的 boost 与可观测表示的边界

目标：在[已有平移质量壳与同种编织审查](adler-massive-braiding-audit.md)上，分开核验原有界双锥产生的准局域代数上的 boost、扩张代数上的运输，以及连续编织参数能否在原准局域代数上标记不等价的一粒子种类。这里只做一个代数问题，不新算散射，不升维。

原始依据：[Adler, hep-th/9512111v1](https://arxiv.org/pdf/hep-th/9512111) §3 Eqs. (37)–(41)、Lemmas 1–2、Propositions 1–2；§4 Eqs. (50)–(52)；§5 Eq. (73)。令 \(\mathfrak A_{\mathrm{ql}}\) 为有界双锥生成的原可观测代数，\(\alpha_g\) 为自由 massive Dirac 网的正时定向 Poincaré 作用。避免预设 \(\mathfrak A_{\mathrm{ql}}=\mathfrak A_1\)。

## 原准局域代数：确有协变的孤立质量壳

选 \(V_\lambda=\Gamma(U(n,\lambda))\)，以 Adler Eq. (39) 的约定 \(\rho_\lambda(A)=V_\lambda A V_\lambda^*\)。在真空 Hilbert 空间 \(\mathcal H_0\) 上，\(W_\lambda=V_\lambda^*|_{\mathcal H_0}\) 是到某一固定整数电荷分量 \(\mathcal H_q\) 的酉映射；电荷符号取决于实现子取伴随的约定，本论证只用同一 \(n\) 给同一 \(q\)，且 \(|n|=1\Rightarrow |q|=1\)。Eq. (37)、Lemma 2 和对角全局 \(U(1)\) 的 Eq. (43) 给出这一固定移荷性质。逐项代入有
\[
 W_\lambda(\pi_0\circ\rho_\lambda)(A) W_\lambda^*=\pi_q(A).
\]
自由 Poincaré 表示保持电荷，记其在 \(\mathcal H_q\) 的限制为 \(U_q(g)\)。所以
\[
 U_\lambda(g)=W_\lambda^*U_q(g)W_\lambda,\qquad
 U_\lambda(g)(\pi_0\circ\rho_\lambda)(A)U_\lambda(g)^*
       =(\pi_0\circ\rho_\lambda)(\alpha_g A).
\]
群乘法和强连续性直接继承；没有给其额外添加投影相位。在 \(|q|=1\) 的孤立正质量壳上，自由有质量轨道可用 \(\theta\) 标记，\((E,p)=m(\cosh\theta,\sinh\theta)\)，boost 使快度平移，保留 \(d\theta\)、质量和分离快度支撑的顺序；正能量和 \(3m\) 阈值也随酉等价继承。这证明的是原代数上的表示协变，和 Eq. (73) 单独给出的平移识别不同。不需要声称已经构造了 \(\mathfrak A_1\) 中的局域 boost 共循环。

以真空作用 \(U_0(g)\) 为基准，\(z_\lambda(g)=U_\lambda(g)U_0(g)^*\) 总属于 \(B(\mathcal H_0)\) 并由群乘法满足 \(z(gh)=z(g)U_0(g)z(h)U_0(g)^*\)。这是算符级群共循环；从这个构造不能推出 \(z_\lambda(g)\) 属于指定局域代数，也不能推出它在 \(\mathfrak A_1\) 的无界补集生成元上实现所需共变性。

## 为什么不等于发现另一种可由原可观测量区分的基本粒子

若 \(\lambda,\lambda'\) 固定同一个 \(n\)，则 \(T=W_{\lambda'}^*W_\lambda\) 同时交织原代数的表示与上述 Poincaré 实现。对任一归一化向量 \(\psi\)，在两者的对应态 \(\psi,T\psi\) 中，任何 \(A\in\mathfrak A_{\mathrm{ql}}\) 的期望相同。这是对匹配态/原代数的精确等价，不是对任意不同制备、扩张观测或相干干涉实验的否定。

两个不同 \(\lambda\) 仍可有不同自编织。若存在指定带编织范畴内的酉等价，则由编织的自然性，标量自编织必须相同。例如同 \(n=1\) 的 \(\lambda=0\) 和 \(\lambda=1/4\) 在 Eq. (47) 的同一个运输方向上分别给 \(-1,-i\)。所以不能把上述 \(B(\mathcal H_0)\) 中的表示交织子当作该范畴里的等价，或把原准局域表示的等价推广为含无界补集的扩张代数等价。这正是“同一质量壳与同种编织可以共存”和“有另一种操作可辨识粒子”之间的差别。

交叉核对：把 \(T\) 代回两种 \(\pi_0\rho_\lambda=W_\lambda^*\pi_q W_\lambda\) 可直接验算表示与群作用交织；同方向自编织 \(-1\) 与 \(-i\) 则不可能通过共轭变成彼此。本轮没有额外数值或软件测试；\(\mathfrak A_1\) 上的 boost/运输实现、物理可操作的统计辨别与更一般 1+1D 定理仍未完成。
