# METRICS.md — GPTedit-10 revision working metrics

Updated: 2026-08-15 (Session 1, Phase 2).
Counting method: `notes/revision_v10/wordcount.py` (saved in Session 1) — python strip of comments, LaTeX commands, and environment markers over the compiled body; main = `\begin{document}` to `\appendix`, appendix = `\appendix` to `\end{document}`; tokens containing at least one alphanumeric character count as words.
**Method note (Session 1):** the Session 0 script was not saved and its exact numbers could not be reproduced (closest reconstruction ran ≈1,300 words below its main-text figure on identical input).
To keep the series consistent, `wordcount.py` is now the standing method and the Phase 0/Phase 1 checkpoints below are RESTATED under it (original Session 0 figures in parentheses).
The method still runs above the plan §2 baseline estimates (≈16,200/≈2,400); budget targets are tracked as deltas against the restated baseline.

## Baseline (Phase 0: exact copy of -09, header aside)

| Quantity | Value |
|---|---|
| Compiled pages | 48 |
| Total words | 19,365 (Session 0 method: 21,032) |
| Main-text words | 16,795 (Session 0 method: 18,143) |
| Appendix words | 2,570 (Session 0 method: 2,889) |
| Main-text formal results (thm/prop/lem/cor) | 16 (3 thm, 11 prop, 1 lem, 1 cor) |
| Main-text definitions + assumptions | 19 (14 def, 5 ass) |
| Main-text remark environments | 9 |
| Main-text excont / example environments | 6 / 1 |
| Figures / tables in main text | 0 / 0 |

## After Phase 1 (demotions to Appendix D + remark-to-prose conversions)

| Quantity | Value | Target (-10) |
|---|---|---|
| Compiled pages | 51 | ≈34–38 (shrinks in Phases 2–4) |
| Main-text words | 14,985 restated (Session 0 method: 15,955) | ≤13,500 |
| Appendix words | 5,125 restated (Session 0 method: 5,798) | ≈6,500 |
| Main-text formal results (thm/prop/lem/cor) | 9 (3 thm, 5 prop, 0 lem, 1 cor) | 9 ✓ |
| Main-text definitions + assumptions | 18 (13 def, 5 ass) | ≤12 |
| Main-text remark environments | 0 | ≤2 (prefer 0) ✓ |
| Appendix D environments | 1 lem, 6 prop, 1 def, 3 rem | — |

Compile: `latexmk -pdf` clean; no undefined references, no multiply-defined labels.
`paper/tbv_mdr_GPTedit-09.tex` untouched (md5 9aee39991ac0c3f8b1d1abd427ffc174 before and after).

## After Phase 2 (Session 1: infrastructure — tables, figures, Calibration Convention, subsections 4.4/4.5)

| Quantity | Value | Target (-10) |
|---|---|---|
| Compiled pages | 53 | ≈34–38 (shrinks in Phases 3–4) |
| Main-text words | 15,847 | ≤13,500 |
| Appendix words | 5,125 (unchanged — appendix untouched) | ≈6,500 |
| Main-text formal results (thm/prop/lem/cor) | 9 (3 thm, 5 prop, 0 lem, 1 cor) | 9 ✓ |
| Main-text definitions + assumptions | 18 (13 def, 5 ass) | ≤12 |
| Main-text remark environments | 0 | ≤2 (prefer 0) ✓ |
| Figures / tables in main text | 3 / 2 | 3 / 2 ✓ |

Compile: `latexmk -pdf` clean; no undefined references, no multiply-defined labels, no overfull boxes.
`paper/tbv_mdr_GPTedit-09.tex` untouched (md5 9aee39991ac0c3f8b1d1abd427ffc174 before and after).
Main-text delta +862 words: the Calibration Convention paragraph, three figure captions, two tables with captions, and six mechanical pointer/reference sentences; the five moved epistemic statements and the deleted case-duplications net roughly zero.

### New labels (Session 1; no renames, no deletions)

| Label | Object | Location | Rendered as |
|---|---|---|---|
| `fig:chain` | process-chain figure (plan "Figure 3"), replaces the intro `align*` chain | §1 | Figure 1 |
| `fig:timeline` | period-timeline figure (plan "Figure 1") | §3.3 end | Figure 2 |
| `fig:example-array` | 2×2 state array + four minimal repairs (plan "Figure 2") | §3.7 after `ex:setup` | Figure 3 |
| `tab:ledger` | Table 1, epistemic ledger | new §3.4 | Table 1 |
| `tab:terminal` | Table 2, terminal-conditions taxonomy | §9 after `def:stasis` | Table 2 |
| `conv:calibration` | Calibration Convention `\paragraph` | §3.2 end | cross-refs render as "section 3.2" (same behavior as the converted remarks; cleaned by Phase 3 prose) |
| `sec:epistemics` | new subsection "What agents know and don't know" | §3.4 | — |

**Figure-name note:** the plan's figure names (1 = timeline, 2 = array, 3 = chain) cannot match LaTeX's rendered numbers, because the chain figure sits in §1 and numbering follows position; rendered order is chain = 1, timeline = 2, array = 3.
Once Session 3B moves the array figure into the new §2, rendered order becomes chain 1, array 2, timeline 3.
Labels, not numbers, are the stable identifiers.

### Content moves (Session 1)

- New §3.4 "What agents know and don't know" (`sec:epistemics`), inserted between the awareness subsection and On-path conditionals, holds the five scattered epistemic statements moved verbatim: (1) start-of-period cell perception / state never perceived, (2) full-action-profile observability, (3) recodability idealization (two sentences), (4) Θ common knowledge (two sentences), (5) ρ(C) knowledge (three sentences, moved out of `ass:commitment`; the equation's trailing comma became a period).
- §3.5 "Modeling commitments" retitled "Scope and modeling commitments" (label `sec:commitments` unchanged); the five disciplines stay in place; the vocabulary-expansion scope sentence ("Expansion of the mechanism vocabulary itself…") moved there from the awareness subsection.
- Intro `align*` chain deleted, replaced by `fig:chain` and a one-line pointer.

### Calibration Convention: deleted/converted case-duplications (grep-verified gone from main text)

| Old location | Old text (key phrase) | Disposition |
|---|---|---|
| `ex:setup` §3.7 | "every test below operates in its exact, zero-tolerance instance" | → "runs in the exact calibration of the Calibration Convention (`conv:calibration`)" |
| `def:test` §5 | parenthetical "(The exact deterministic case η=0 instead uses the separate zero-likelihood detector…)" | deleted from the environment (R4); covered by the Convention + retained pointer below |
| §5 prose after `def:test` | "The deterministic case uses the separate exact detector… Capacity b_i plays no role in this detector and false alarms are zero." (2 sentences) | compressed to one Convention-pointer sentence retaining the `app:eprocess` reference and the capacity fact |
| §6 after `def:restorative` | "In the exact deterministic case η=0 and w≡0, the repair test is exact consistency…" | → Convention-pointer phrasing |
| `ass:regularity`(i) §9 | "In the deterministic case η=0 this holds automatically and the sequential detector recovers the exact test." | deleted from the environment; the immediately following sandwich prose already restated it and now carries the Convention cref |
| §9 concealment paragraph | "under the exact deterministic detector an active adequate theory is never falsely rejected" | → "under the exact calibration false rejection is impossible (`conv:calibration`)" |

Remaining deterministic/stochastic mentions in main text are substantive contrasts, not duplications, and are left for their sections' Phase 3 rewrites: `ass:full-support` exemption parenthetical (§5), judged-updating deterministic-coincidence sentence (§5), dissonance-implies-insufficiency contrast (§5), the retained irreparability paragraph (§6), the determinism-certifies pointer sentence (§7), SCUE asymptotics commentary (§9), and the Phase 1 pointer sentences for `prop:rest-points`/`prop:capacity` (§9).
The only hit for the deleted phrases is inside Appendix D's verbatim `prop:capacity` proof, which is untouched by design.

### Notes / reported items (Session 1, not MDR-DECISION flags)

4. **Two consecutive assumption environments in §3.3:** moving the post-`ass:observation` prose paragraph into §3.4 leaves `ass:observation` immediately followed by `ass:commitment` with no sandwich prose; Session 4's Model rewrite (R2) supplies it.
5. **Table 1 ρ(C) reference column** points to `eq:subjective-value` (where ρ(C) is used), since the defining statement now lives in §3.4's own unnumbered prose; Session 4 may prefer a numbered anchor.
6. **Table 1 includes two rows the manuscript did not previously state explicitly** — "rivals' partitions, beliefs, policies: never accessed" (no interactive epistemics) and "test calibration/capacity: the agent's own" — both are in the plan §5 Model-row specification of 4.4 and consistent with `prop:participation`'s "agent-known … test calibration"; author should verify against his understanding per the Session 1 gate.
7. **TikZ style rename:** the timeline figure's node style was named `pbox` because `step` collides with the pgf grid key.
8. **Preamble change:** added `tikz` + `arrows.meta`, `positioning` libraries (authorized by plan §0.5).

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
