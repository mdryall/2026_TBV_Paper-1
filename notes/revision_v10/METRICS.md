# METRICS.md — GPTedit-10 revision working metrics

Updated: 2026-08-15 (Session 0, Phases 0–1).
Counting method: python strip of comments, LaTeX commands, and environment markers over the compiled body of `paper/tbv_mdr_GPTedit-10.tex`; main = `\begin{document}` to `\appendix`, appendix = `\appendix` to `\end{document}`.
This method runs slightly above the plan §2 baseline estimates (≈16,200/≈2,400); it is applied identically at every checkpoint, so deltas and budget tracking are consistent.

## Baseline (Phase 0: exact copy of -09, header aside)

| Quantity | Value |
|---|---|
| Compiled pages | 48 |
| Total words | 21,032 |
| Main-text words | 18,143 |
| Appendix words | 2,889 |
| Main-text formal results (thm/prop/lem/cor) | 16 (3 thm, 11 prop, 1 lem, 1 cor) |
| Main-text definitions + assumptions | 19 (14 def, 5 ass) |
| Main-text remark environments | 9 |
| Main-text excont / example environments | 6 / 1 |
| Figures / tables in main text | 0 / 0 |

## After Phase 1 (demotions to Appendix D + remark-to-prose conversions)

| Quantity | Value | Target (-10) |
|---|---|---|
| Compiled pages | 51 | ≈34–38 (shrinks in Phases 2–4) |
| Main-text words | 15,955 | ≤13,500 |
| Appendix words | 5,798 | ≈6,500 |
| Main-text formal results (thm/prop/lem/cor) | 9 (3 thm, 5 prop, 0 lem, 1 cor) | 9 ✓ |
| Main-text definitions + assumptions | 18 (13 def, 5 ass) | ≤12 |
| Main-text remark environments | 0 | ≤2 (prefer 0) ✓ |
| Appendix D environments | 1 lem, 6 prop, 1 def, 3 rem | — |

Compile: `latexmk -pdf` clean; no undefined references, no multiply-defined labels.
`paper/tbv_mdr_GPTedit-09.tex` untouched (md5 9aee39991ac0c3f8b1d1abd427ffc174 before and after).

## Label map (old → new)

No label was renamed or deleted. Locations and rendered numbers changed as follows.

### Demoted to Appendix D (`app:deferred`), statements + proofs verbatim

| Label | Was (main text) | Now | Pointer left at original location |
|---|---|---|---|
| `lem:test-consistency` | Lemma 5.2, §5.1 | Lemma D.1 | one sentence, §5.1 |
| `prop:coherence` | Prop. 6.2, §6.1 | Prop. D.2 | plan-supplied coloring sentence, §6.1 |
| `rem:irreparable` | Remark 6.3, §6.1 | Remark D.3 | one paragraph kept in text (see notes) |
| `rem:certification` | Remark 7.x, §7 | Remark D.4 | one sentence, §7 |
| `prop:rest-points` | Prop. 9.x, §9 | Prop. D.5 | one sentence, §9 (proof stays in `app:absorption`) |
| `prop:adequacy` | Prop. 9.x, §9 | Prop. D.6 | one sentence, §9 |
| `prop:capacity` | Prop. 9.x, §9 | Prop. D.7 | one sentence (modest-core), §9 |
| `def:diagnostic` | Def. 9.x, §9 | Def. D.8 | merged one-sentence pointer with prop:diagnostic, §9 |
| `prop:diagnostic` | Prop. 9.x, §9 | Prop. D.9 | (covered by merged pointer) |
| `prop:punishing` | Prop. 9.x, §9 | Prop. D.10 | one sentence, §9 |
| `rem:local-robustness` | unlabeled Remark, §9 | Remark D.11 | one sentence, §9 — **NEW label** (remark had none) |

### Converted remark → prose in place (environment deleted, `\paragraph{Title.}` + label kept)

| Label | Location | Note |
|---|---|---|
| `rem:self-sealing` | §4 (Bayesian boundary) | now renders as "section 4" in cross-refs |
| `rem:stickiness` | §7 (economics) | renders as "section 7" |
| `rem:grain` | §9 (dynamics) | renders as "section 9" |
| `rem:scope` | §9 | renders as "section 9" |
| `rem:anomaly` | §9 | renders as "section 9" |
| `rem:two-sources` | §9 | renders as "section 9" |

## Notes / reported items (not MDR-DECISION flags)

1. **Cross-references to converted remarks now render as section numbers** (e.g., `\cref{rem:stickiness}` → "section 7" instead of "remark 7.x") at ~10 sites (`rem:stickiness` ×4, `rem:self-sealing` ×3, `rem:anomaly` ×1, plus self-references). Mechanically correct and compiling; prose reads slightly oddly until the Phase 3 rewrites of those sections, which replace this prose anyway.
2. **`rem:irreparable` retention:** per plan §4.2 the text keeps one paragraph. Kept verbatim: the stochastic-failure paragraph (feeds the stasis taxonomy). Its opening antecedent ("this guarantee") is supplied by the new one-sentence pointer covering the deterministic-repairability half; that paragraph is therefore duplicated between main text and the verbatim Appendix D remark. Flagged for author skim.
3. **Word-count deltas Phase 1:** main −2,188; appendix +2,909 (verbatim statements + orienting sentences). Net document +721 words / +3 pages — expected, since Phase 1 adds pointers and appendix scaffolding without any prose cuts.

## MDR-DECISION flags

None so far.

## VERIFY-CITE flags

None so far.
