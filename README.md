# Fundamental Particles Beyond Bose and Fermi

A research project on whether fundamental particles beyond ordinary bosons and fermions exist in relativistic quantum field theory (QFT), and on the dimensions and assumptions under which further particle classes are possible.

## Central existence question

Do physically consistent fundamental particles beyond the ordinary Bose and Fermi classes exist?

**Known answer: yes, in 2+1-dimensional relativistic QFT.** Massive anyons and non-Abelian plektons are described by physical particle sectors with braid-group statistics. Their one-particle states carry unitary representations of the 2+1-dimensional Poincare group, and the relativistic spin-statistics relation has been proved under explicit mass-spectrum assumptions.

- English: [Phase I literature baseline](docs/phase-I-literature-baseline.md)
- 中文：[Phase I 文献基线](docs/phase-I-literature-baseline.zh-CN.md)
- Primary-source bibliography: [literature/bibliography.bib](literature/bibliography.bib)

The project treats relativistic anyons/plektons as an established positive benchmark, not as a new result to rediscover. The research itself proceeds strictly from the lowest nontrivial relativistic dimension upward: 1+1 first, then 2+1, 3+1, and higher dimensions. The 1+1D review is the active stage; the known 2+1D result is retained as a benchmark, not used to skip the lower-dimensional analysis.

## Scope

- **Fundamental particles only.** Study physical one-particle states and particle-bearing superselection sectors in relativistic QFT. State explicitly which object is used in each argument; these notions are related but not interchangeable.
- **All relevant spacetime dimensions.** Include 1+1, 2+1, 3+1, and higher-dimensional theories where they change the available structures or assumptions.
- **No restriction to a named candidate.** Examine parastatistics, braid-group statistics (including abelian anyons and non-Abelian plektons), and any further mathematically and physically admissible possibilities.
- **Use the full QFT consistency framework.** Analyze Poincare representations, spin-statistics relations, localization, observable locality/causality, unitarity, spectrum conditions, superselection sectors, fusion/composition, gauge structure, and CPT where the relevant assumptions apply.
- **Exclude condensed-matter quasiparticles, collective/emergent excitations, and composite bound states.**

## Main questions

1. Beyond the established 2+1D anyon/plekton examples, are there further fundamental-particle classes outside ordinary Bose and Fermi statistics?
2. Under which assumptions do 3+1D and higher-dimensional relativistic QFTs enforce permutation statistics and reduce parastatistics to ordinary Bose/Fermi fields with internal or gauge structure?
3. What changes in 1+1D, and which braid-like sector structures correspond to genuine massive particle states rather than only chiral/conformal sectors?
4. Can any proposed generalized statistics survive passage to the physical observable algebra and physical Hilbert space?
5. What precise no-go theorems or explicit constructions settle the remaining cases?

## Research workflow

1. Start with 1+1D and complete its particle criteria, localization, statistics, kink sectors, and no-go results.
2. Only after closing 1+1D, proceed to 2+1D and re-derive the established anyon/plekton benchmark.
3. Continue sequentially to 3+1D, 4+1D, and higher dimensions.
4. At every dimension, compare particle criteria, spacetime representations, statistics, localization, superselection sectors, fusion, and consistency conditions.
5. Test each candidate against explicit relativistic QFT requirements and equivalence to ordinary Bose/Fermi theories.

See the [research program](docs/research-program.md), the [dimension-by-dimension research index](dimensions/README.md), the [active 1+1D review](dimensions/1+1d/README.md), and the [literature review template](docs/literature-review-template.md).

## Working standards

- Separate proved theorems, explicit constructions, model-dependent results, interpretations, and conjectures.
- Cite primary sources and record stable identifiers such as DOI or arXiv ID.
- State definitions and theorem assumptions before comparing conclusions.
- For calculations, preserve exact source versions, input hashes, environment and parameters, native outputs, convergence/error analysis, and independent physical checks.
- Develop substantive changes on a branch and submit them for pull-request review.

## Status

The broad existence question is answered affirmatively in 2+1D by relativistic anyons/plektons. The active research stage is now 1+1D; its kink quasi-statistics and conformal-sector candidates are under review. No claim is made that all possible non-Bose/non-Fermi fundamental-particle classes have been classified.
