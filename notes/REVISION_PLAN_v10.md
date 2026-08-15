# REVISION_PLAN_v10.md — "Questions Before Priors": GPTedit-09 → GPTedit-10

**Intended repo location:** `notes/REVISION_PLAN_v10.md`
**Companion file:** `notes/REVISION_RUNBOOK_v10.md` (session-by-session execution; read it for *how*, this file for *what*).

---

## 0. Authority, scope, and status

1. This document is the **author-approved change specification** for a full expository restructuring of the manuscript. Per `AGENTS.md` discipline, the agent implements approved specifications and does not broaden them: everything listed here is approved; anything not listed is out of scope.
2. **Source of authority:** `paper/tbv_mdr_GPTedit-09.tex` remains the sole authoritative manuscript throughout this project. It is **read-only** for this project after Phase 0.
3. **Working draft:** `paper/tbv_mdr_GPTedit-10.tex`, created in Phase 0 as an exact copy of -09. All edits happen there. The agent **never promotes** -10 to authoritative; promotion is an explicit author act at project end.
4. **Bibliography:** `paper/MDR_TBV_Paper01.bib` — version-agnostic; edited in place in Phase 5 only; never renamed.
5. **Build:** `latexmk -pdf` from `paper/`. The compile gate for every phase is a clean latexmk run of -10. Do not change engines or refactor the preamble except to add `tikz` and `booktabs` if absent.
6. **Formatting invariant:** one sentence per line, everywhere, including all new prose. Diffs are reviewed line-wise; this invariant is what makes them readable.
7. **Out of scope:** journal formatting and submission packaging (a separately authorized project per `notes/STATUS.md`); any change to `notes/` scaffolding files (`rigorous_four_state_insight_model.tex`, `general_model.tex` — context, not authority; do not import from them); reopening points already addressed in `Machine_Reviews/`.
8. **Commits:** only when the author explicitly instructs, at session boundaries (see runbook). **Never push. Never promote.**
9. **Target venue:** Management Science (Business Strategy). This raises the tolerance for formalism but not the teaching bar — MS published Ryall (2003, 2009) and Camuffo et al. (2020); assume a mixed referee panel of TBV scholars and formal theorists. The selection logic in §4 (result triage) is keyed to that panel.

**Nature of this revision:** exposition, selection, and sequencing. **The mathematics is settled and is not being redone.**

---

## 1. Frozen architecture — do not relitigate

Per `notes/STATUS.md`, the B1–B8 redraft is closed and the formal architecture is frozen. The following are **locked**; if any instruction in this plan appears to conflict with a locked decision, the locked decision wins and the agent inserts a `% MDR-DECISION:` comment instead of resolving:

- Single clock of periods.
- Standing policy with switching against hurdle κ_i; policy inertia emergent, not assumed.
- Sequential e-process dissonance detector with agent capacity b_i (false alarm ≤ e^{−b_i}).
- Inquiry prices the *question*, not the answer: elect iff λ_i·B̂_i ≥ γ_i, with **κ_i deliberately excluded from participation** — pre-insight, the refined policy is unrepresentable and cannot be priced. (Use this rationale verbatim in the §8 prose; it is better than the current draft's phrasing.)
- The two-level structure Θ with objective assignment τ: S → Θ — the unawareness engine; load-bearing; do not collapse.
- Θ vocabulary fixed; vocabulary expansion is Paper 2 of the research program (`agenda/Questions_Before_Priors.tex`). The scope paragraph (§5, row for Model §4.5) states this as "reserved for companion work in this research program" unless the agenda memo prescribes different manuscript phrasing — check it; flag if unclear.
- Capacity heterogeneity as **modest-core**: the formal comparative statics may move to the appendix (§4.2 below), but the capacity channel remains *named* in the main text — one sentence where b_i is introduced, one paragraph in Dynamics (from the converted "two sources of heterogeneity" remark). Demotion ≠ deletion.
- No optimism-α.
- General-theory-plus-simple-illustration format: the general theorems carry all results; the 2×2 model illustrates. **Author-approved exception, on the record:** the new §2 ("The problem in miniature," §5 below) is a *narrative preview* of the example, placed before the general theory. It changes reading order, not logical architecture — no result is stated at example level that the general theory does not later carry (except the winner/loser result if its fallback triggers, which is then labeled as example-class explicitly). The author has approved this exception.
- Fulcrum discipline: the paper is about the dissonance → inquiry → awareness → models → Bayes chain; SCUE equilibrium machinery is subordinate. (This *supports* the triage in §4: the heavy equilibrium apparatus is exactly what moves down.)

Additional hard guardrails:

- No change to the mathematical content of any retained statement. Environment restructurings listed in §4 and §8.2 are approved as *structural* changes: content moves verbatim or with meaning-preserving rephrasing; anything requiring a substantive restatement gets a `% MDR-DECISION:` flag and stops there.
- The running example's numbers are frozen (leverage ½ at discovery; B̂₁ = 0 vs B̂₂ = ½ at the validation stretch; warrant gap +½; the β = 1 trap; the β < 1 knife edge; ¾–¼ persistence payoffs). §2 is built on them; Appendix C verifies them.
- The title is unchanged.
- Preserve all `\label{}`s where content survives; new environments produced by unbundling get new labels; maintain a label map in `notes/revision_v10/METRICS.md`.
- New formal content (there is exactly one item: the winner/loser proposition, §9.1) requires **author approval of the drafted statement and proof before integration** — see runbook approval gate.

---

## 2. Diagnosis and the two governing principles

The draft is internally coherent and its results are real, but it is written to survive referees rather than to teach a reader: nearly every sentence compresses a theorem, ~20 coined terms carry the argument with no visual support, definitions bundle three or four objects each, claims are restated defensively in remarks, and the strategy payoff arrives in the final pages in the paper's own idiolect. The fix is architectural.

**Principle 1 — Teach first.** Every formal object is introduced by the problem it solves, in the running example's concrete terms, before it is defined; every result is followed by what it means for a firm, in words. A reader who skips all mathematics must still get the complete argument (the Skip Test, R1).

**Principle 2 — Funded expansion.** No narrative is added except where machinery is removed. Budget arithmetic (baseline measured on -09; Phase 0 recomputes with repo tooling):

| Quantity | Baseline (-09) | Target (-10) |
|---|---|---|
| Compiled pages | 48 | ≈34–38 |
| Main-text words (compiled prose+math) | ≈16,200 | ≤13,500 |
| Appendix words | ≈2,400 | ≈6,500 |
| Formal results (thm/prop/lem/cor) in main text | 16 | 9 |
| Definitions + assumptions in main text | 19 | ≤12 |
| Remark environments in main text | 9 | ≤2 (prefer 0) |
| Coined terms of art | ≈20 | ≤10 |
| Figures / tables in main text | 0 / 0 | 3 / 2 |

Demotions and deletions free ≈7,000 main-text words; new narrative consumes ≈4,500; net main text **shrinks**. When a section exceeds its budget (§5), cut in this order: (1) remark restatements of things already said; (2) inline deterministic/stochastic case duplications (replaced by the Calibration Convention, §7.3); (3) meta-commentary about what the paper does or does not claim (lives only in Scope, §4.5 of the manuscript); (4) defensive qualifications. **Never cut the plain-language interpretation paragraphs.**

---

## 3. The reader contract (checkable rules)

R1. **Skip Test.** Per section: delete every equation, theorem-like environment, and proof; the residue must read as a continuous essay stating the question, mechanism, each result in words, and the implication. Operationalized in the runbook: the agent writes the math-stripped residue to `notes/revision_v10/skiptest_<sec>.md` for author reading. This is the acceptance criterion.

R2. **Sandwich rule.** Every definition/assumption gets ≥1 motivating paragraph immediately before it, anchored in the running example. Every theorem/proposition gets ≥1 interpretation paragraph immediately after it, in managerial terms, introducing no new coined terms.

R3. **Example-first.** Every major construct debuts in the four-state example's concrete terms before its general definition, which then reads as the obvious abstraction of something already seen working.

R4. **One-job rule.** One object per definition environment. All commentary lives outside theorem-like environments. Deterministic/stochastic variants are handled once by the Calibration Convention (§7.3), never restated inside definitions.

R5. **Sentence discipline.** Topic sentences state claims, not hedges. Narrative prose: no stacked modifier chains ("possibly randomized, record-measurable, truth-blind" appears only inside formal statements); no mid-sentence cross-reference chains; average narrative sentence ≤ ~30 words. One sentence per line (repo invariant).

R6. **Hedging budget.** All scope caveats and objection-handling live in the manuscript's Scope subsection and in Limitations — nowhere else. Elsewhere: at most one qualifying clause per paragraph.

R7. **Terminology diet.** Only Keep-column terms (§6) may appear; no new coinage; every kept term defined in plain words within one sentence of first use.

R8. **Section epigraphs (recommended).** Open each results section with the question it answers, one plain italicized line (e.g., dissonance section: *How does a firm discover that its way of seeing the market has failed?*).

R9. **Voice.** Single-authored: "I" for authorial actions, impersonal for facts. `% MDR-DECISION:` if a passage forces a different choice.

R10. **Proofs.** Any proof exceeding ~8 lines moves to the appendix, replaced in text by a ≤4-sentence verbal sketch of the argument's single idea.

R11. **No silent additions.** Do not add robustness sections, a second example, extensions, or "improvements" to the example's numbers. Addition is the disease this revision cures.

---

## 4. Result triage

Selection criterion: which referee's published concerns each result answers, for a Management Science panel drawn from the TBV stream plus formal theorists.

### 4.1 Keep in main text (9 results)

| # | Result (current label where known) | Why the panel cares |
|---|---|---|
| 1 | `prop:no-emergence` | Formalizes Felin–Holweg (2024) and Zellweger–Zenger (2023): data and updating cannot substitute for theory generation. Two-line proof stays in text. |
| 2 | `rem:self-sealing` → **prose** + one displayed takeaway line | The sharpest wedge: confidence can rise while the language fails. Cite Berk (1966) **and** Esponda–Pouzo (2016) here (§10). Environment dies; content survives. |
| 3 | `thm:nonidentification` | "Insight is necessarily fallible" as a theorem. Speaks to Felin–Gambardella–Zenger (2024)'s open problem and Adner–Levinthal (2024) on limits of theory testing. Verbal proof sketch in text ("two worlds that agree on everything ever visited are indistinguishable to any procedure that only reads the record; no record-reading procedure can be right in both"); coupling proof → appendix. |
| 4 | `prop:robust-sufficiency` | The price tag on fallibility ("robustness costs every distinction"). Pairs with #3 as one unit; 3-line proof stays. |
| 5 | `def:leverage` + `prop:participation` | **Flagship 1.** The genuinely novel economic object: pricing a question before its answers are representable. Speaks to Chavda–Gans–Stern (value of a search direction), Camuffo et al. 2024 (which theory to test — this is the prior question: whether any question is worth asking), Ehrig–Zenger (value of theories). Gets the most careful rebuild (§5, row for the value-of-a-question section). |
| 6 | **NEW** winner/loser proposition | The most quotable strategy result, currently example-level. §9.1 gives the attempt-with-fallback instruction and the approval gate. Connects to Camuffo et al. (2020) empirics and Denrell's undersampling-of-failure line. |
| 7 | `thm:uninformative` + `cor:self-audit` | **Flagship 2.** Generation ≠ warrant; retrospective fit is not validation; the theorist may be unable to audit itself; boards and investors get a precise epistemic role. Disciplines the "entrepreneurs as scientists" empirical program (Camuffo et al. 2020/2024; Ott–Hannah 2024). |
| 8 | `def:exposure` + one merged proposition delivering "rival differentiation or observable demand punishment exposes a coarse language; pooled play under forgiving demand conceals it" | The market-facing mechanism: deviants as epistemic infrastructure; forgiving demand protects a false consensus. Speaks to Sorenson (2024) and Adner–Levinthal (2024). The `def:diagnostic` / `prop:diagnostic` / `prop:punishing` machinery that proves it goes to the appendix; the text states the merged result and points down. |
| 9 | `thm:absorption` + `prop:persistence` | The strategy punchline: heterogeneity before priors; permanent payoff gaps because inquiry dies economically (answered / unpriced / abandoned / unanswerable). This is Felin–Zenger (2017)'s core claim pushed upstream and the origin story for the Bryan–Ryall–Schipper (2022) awareness advantage. Absorption proof stays in the appendix. Consistent with fulcrum discipline: these two are kept; the surrounding equilibrium apparatus is what moves down. |

### 4.2 Demote to appendix (full statement + proof; one-sentence pointer in text)

`lem:test-consistency`; `prop:coherence` (text keeps one sentence: "restoration factorizes cell by cell, so finding a repair is a coloring problem"); `rem:irreparable` (text keeps one paragraph — it feeds the stasis taxonomy); `prop:capacity` (text keeps the modest-core sentence per §1); `prop:rest-points`; `prop:adequacy` (text keeps one sentence: "surviving error lives only in what play never exposes"); `def:diagnostic` + `prop:diagnostic` + `prop:punishing` (formal versions behind Keep-#8); `rem:certification` (pointwise transparency); the local-robustness remark.

### 4.3 Convert from remark environments to prose (content survives; environment dies)

`rem:stickiness` (enlightened inertia — the concept stays prominent as one of the three terminal conditions; introduced in prose at first use, reappears in Dynamics); `rem:anomaly` (rational anomaly tolerance — becomes a Dynamics/Discussion paragraph); `rem:two-sources` (one Dynamics paragraph; carries the modest-core capacity channel); `rem:scope` and `rem:grain` (fold into the manuscript's Scope subsection and Dynamics respectively); `rem:self-sealing` per Keep-#2. After conversion: ≤2 remark environments in main text; prefer 0.

---

## 5. Target architecture and word budgets

Total main text ≤ 13,500 words. Budgets are ceilings. All new prose one sentence per line.

| § | Section | Budget | Key instructions |
|---|---|---|---|
| — | Abstract | 190 | Full replacement in §6 of this plan. Zero coined terms except "causal dissonance." |
| 1 | Introduction | 2,200 | ¶1 the question ("Where do strategic theories come from?") + one concrete hook. ¶2 TBV state of play and the open problem (Felin–Gambardella–Zenger 2024 flag it explicitly — say so). ¶3 the Bayesian boundary in words, with Ortoleva/Berk/Esponda–Pouzo positioning in one footnote (§10). ¶4 what the model does — the theory→judgment→action→experience→dissonance→inquiry→refinement→theory chain, referencing Figure 3. ¶¶5–8 the four signature findings, one paragraph each, in strategy language with the example's numbers ("a firm can rationally pay for a distinction it cannot yet name; in the example that value is exactly one half"). ¶9 contribution statement + two honest scope sentences (semantic act primitive; Θ fixed, so insight here means discovering *which differences matter*, with vocabulary expansion reserved for companion work). ¶10 two-sentence roadmap. Keep the current intro's four-findings skeleton; replace its prose entirely. |
| 2 | **NEW — The problem in miniature** | 1,400 | The whole four-state example told verbally, arithmetic only, previewing every result. Act 1: setup; belief-driven differentiation ends in dissonance (neither firm can "see" rows; each firm's last theory dies). Act 2: the record admits exactly four repairs; direction without determination; the row/column fork. Act 3: pricing the question — leverage = ½, and why an unresolved action margin, not defeat per se, is what prices it. Act 4: the +½ warrant gap — certainty without validation; why neither firm can audit itself. Act 5: three endings — the β = 1 trap (a shared false theory, forever), the β < 1 knife edge ("what demand withholds from the firms, their epistemics receives as evidence"), and ¾–¼ permanent payoffs with the truth-holder rationally never inquiring again. Include Figure 2. A reader who stops after §2 has the entire paper. All later `excont` blocks then shrink ~60% into pointers back to §2; detailed computations remain in Appendix C. **Authoring:** the author writes this section personally. The agent supplies a fragment-level scaffold beforehand (runbook Session 3A: beats, required numbers with Appendix C references, constructs previewed, arithmetic constraints — no prose), and afterward integrates, formats one-sentence-per-line, builds Figure 2, and verifies every number against Appendix C, without editing the author's prose (Session 3B). |
| 3 | Related work | 900 | Four paragraphs as now (TBV; unawareness; misspecified/causal learning; subjective rationality), rewritten verdict-first ("These accounts begin with a theory available; this paper supplies the step before"), with §10 additions woven in. Drafted **last** in Phase 3 so it reflects the final positioning. |
| 4 | Model | 2,600 | 4.1 primitives; 4.2 objective causal system; 4.3 awareness and theories; **4.4 What agents know and don't know (NEW, ≈500 words + Table 1)** — consolidate the epistemic specification currently scattered across five locations: Θ common knowledge; ρ(C) known on current cells; the cell perceived, the state never; full action profile and own consequence observed; deliberative vs analyst record; recodability total and infallible upon refinement; conjectures purely empirical; no interactive epistemics (agents hold no beliefs about rivals' awareness). Table 1 is the **epistemic ledger**: rows = objects (s, C, a, x_i, τ, Θ, ρ, rivals' partitions, …); columns = agent knows / observes / never accesses, with defining reference. Delete the five scattered statements it replaces. **4.5 Scope and modeling commitments (≈450 words)** — the current five disciplines (keep them; they are good), plus the fixed-Θ scoping paragraph (companion-work phrasing per §1), plus the open defense of the technology consuming the analyst record (insight grasps the intelligible *in* the particulars; the agent has the particulars and lacks the predicate — state this plainly so it does not read as sleight of hand), plus one sentence on no interactive awareness. This subsection is the **only** home for defensive material. Include Figure 1 (period timeline). |
| 5 | The Bayesian boundary | 700 | Keep-#1 and Keep-#2. Mostly words; the proposition with its two-line proof; the self-sealing passage as prose. |
| 6 | Causal dissonance | 1,200 | Unbundle `def:test` per the worked example in §8.2 of this plan: Def. adequacy (short); one prose paragraph presenting the sequential monitor as an *interface* — "a running evidence score per theory, guaranteed not to cross the rejection threshold under adequacy except with probability e^{−b}; the construction, from the modern anytime-valid testing literature, is in Appendix A" (cite Shafer; Ramdas et al.; Grünwald et al., §10); Def. active set + causal dissonance (merged with `def:dissonance`). Judged updating becomes a titled sub-subsection ("Belief bookkeeping") with a five-step protocol replacing the current wall paragraph. Then `def:exposure` and the merged exposure proposition (Keep-#8). Mathematical content of the detector unchanged (frozen, §1); only environment structure and surrounding prose change. |
| 7 | Inquiry: direction without determination | 1,100 | Restorative refinements motivated first ("what must any successful answer accomplish?"); Keep-#3 with the verbal sketch; Keep-#4; one paragraph on irreparability; technology and formulation rule compressed to their interfaces, embedded commentary evicted per R4 (formal content unchanged). |
| 8 | The value of a question | 1,700 | **Flagship 1.** Open with the losing firm's soliloquy, currently buried: "situations like the ones I lost will recur, and a distinction that sorted them would let me act on them." Then deliberative groupings in words (the firm's hypotheses about which remembered episodes were causally alike); coherent groupings; leverage with **one** displayed equation (the two L-objects defined in prose, their displays moved to the appendix if the budget requires); Participation (Keep-#5); the answerability weight and rational cessation; enlightened inertia introduced in prose with the frozen rationale from §1 (κ excluded from participation because pre-insight the refined policy is unrepresentable and cannot be priced). Interpretation paragraph: leverage prices *action separation, not uncertainty reduction*. Then Keep-#6 (winner/loser, §9.1 — approval-gated). |
| 9 | Warrant: generation is not validation | 1,200 | **Flagship 2.** The pivot narrated in words (refinement → formulation → bridge prior → back to Bayes; nonuniqueness of the bridge prior is the boundary between insight and judgment, one sentence). Rename "representation-relative coherence" → the agent's **confidence** (symbol Coh unchanged). Keep-#7 after a plain paragraph: "the evidence that produced the theory cannot be counted again as evidence for it." Interpretation: validation requires evidence whose likelihood differs across worlds the theorist may be unable to jointly represent — hence outside warrant assessors; seed the governance implication, develop it in Discussion. |
| 10 | Dynamics: how questions die | 1,500 | SCUE, dissonant stasis, absorption + persistence (Keep-#9). Table 2: **taxonomy of terminal conditions** — rows SCUE / dissonant stasis / enlightened inertia; columns: what survives, why inquiry died (answered / unpriced / abandoned / unanswerable), payoff consequence, example instance. One paragraph each from the converted `rem:anomaly` and `rem:two-sources` (the latter carries the modest-core capacity channel). Capacity comparative statics: one sentence + appendix pointer. |
| 11 | Discussion | 1,800 | 11.1 The four implications rewritten as contributions (question histories as a pre-prior source of heterogeneity; action separation, not uncertainty reduction; warrant requires independent discrimination — governance as epistemics; exposure and concealment — deviants as epistemic infrastructure, forgiving demand protects consensus). 11.2 **Testable implications (NEW, ≈500 words)** per §9.2. 11.3 The cognitional interpretation compressed to one paragraph + citation (the Lonergan mapping is exact; five sentences, not a page). 11.4 Limitations and extensions (≈300 words; the three restrictions stated honestly, including that the model captures which-differences-matter insight, with vocabulary expansion reserved for companion work, and why that is the right first cut). |
| 12 | Conclusion | 300 | Three paragraphs: the question, the answer, the program. |
| A–D | Appendices | ≈6,500 | A: evidence-process construction (as is, plus §10 citations). B: proofs (existing + demoted). C: example computations (as is). D (NEW): deferred results from §4.2, full statements and proofs, each opened by one orienting sentence. |

---

## 6. The abstract — full replacement (also the register exemplar)

Replace the abstract with the following (author edits for taste; keep structure and register — every sentence carries a finding in words a TBV reader parses instantly; ≤190 words; format one sentence per line on insertion):

> Where do strategic theories come from? The theory-based view shows how causal theories direct managers' search, experimentation, and action, but its formal treatments begin after a theory — or at least a hypothesis space — exists. This paper models the step before: how an actor whose causal language has failed comes to possess a new one. Bayesian updating can rank the theories a manager can already express; it cannot produce a distinction never yet drawn, and confidence can grow even as every expressible theory fails. I model a separate, fallible faculty — causal dissonance — that detects when the represented class has broken, and a costly, elective inquiry process that may repair it. Four results follow. Experience directs repair without determining it, so insight is necessarily fallible. A firm can rationally value a question before it can state any answer — and an unresolved action margin, not success, is what sustains that value. The evidence that generates a theory cannot also validate it, which gives boards and investors a precise epistemic role. And because inquiry can die economically, firms facing identical environments can end with permanently different theories and payoffs: strategic heterogeneity can originate before priors.

Once the author has edited this abstract, it becomes the **register reference** for all later sessions.

---

## 7. Terminology diet, consolidation infrastructure

### 7.1 Rename/kill map (applied by global sweep, Phase 4)

**Keep (≤10):** causal dissonance; awareness (partition); truth-blind; deliberative leverage (introduced as "the value of a question"); bridge prior; warrant / signed warrant gap; self-confirming unawareness equilibrium (SCUE); dissonant stasis; enlightened inertia; exposure / concealment.

| Current | Replace with |
|---|---|
| delabeled achievability weight | answerability weight λ ("the agent's assessed chance that its question is answerable") |
| representation-relative coherence | the agent's confidence (symbol Coh unchanged) |
| dissonance capacity b_i | evidence threshold b_i ("capacity" may appear parenthetically once, and in the modest-core capacity sentences) |
| judged updating | keep the term; define in one plain sentence at first use ("beliefs ride only on theories the test has not rejected"); confine the two-tier exposition to the Belief bookkeeping sub-subsection |
| acting belief / reference posterior | keep; introduced only inside Belief bookkeeping |

**Appendix-only vocabulary (must not appear in main text after Phase 4):** repair-coherent; pointwise transparency; counterfactual transparency; diagnostic at tolerance η; strictly punishing primitives; restorative correspondence (main text may say "the set of repairs the record allows" once, with a pointer).

### 7.2 Tables and figures (built in Phase 2; TikZ/booktabs; greyscale-safe)

- **Table 1** — epistemic ledger (spec in §5, Model row).
- **Table 2** — taxonomy of terminal conditions (spec in §5, Dynamics row).
- **Figure 1** — period timeline: perceive cell → act via standing policy → observe (a, x_i) → update & test → possibly dissonance → possibly elect → possibly refine → possibly switch.
- **Figure 2** — the 2×2 state array with the row law and the four minimal repairs.
- **Figure 3** — the process chain (promote the intro's `align*` chain to a TikZ figure).

### 7.3 The Calibration Convention

One labeled paragraph early in the Model section: "Throughout, the *exact calibration* means deterministic mechanisms with η = 0 and w ≡ 0, in which tests reject at the first impossible observation and false alarms are zero; the running example uses it. All definitions are stated once for the general stochastic case; the exact calibration is the special case, and I flag the two places where it changes a conclusion." Then delete every inline "(in the deterministic case … / with stochastic mechanisms …)" duplication and replace with a reference to this convention. This single move recovers several hundred words and most of the definitional bloat.

---

## 8. Worked transformations (imitate these)

### 8.1 Sentence-level register

Current (abstract): "The leverage object isolates value requiring finer contingency from value already attainable in the current language, so the agent values a question rather than ordinary within-language information."
Rewrite: "Deliberative leverage prices a question, not an answer. It asks how much better the firm could do if it could act on a distinction it cannot yet draw, over and above the best it can already do with the categories it has. A firm can therefore rationally pay to pursue a distinction it cannot name — and rationally decline when even the most favorable reading of its own record shows nothing to gain."

### 8.2 Definition unbundling (the `def:test` exemplar)

1. *Prose (motivation, 4–6 sentences):* the firm needs a faculty the posterior cannot supply — a way to notice that *every* theory it can state is failing. In the example: after the two diagonal periods, each firm has personally refuted all three of its theories; a posterior cannot say this, a test can.
2. **Definition (Adequacy).** The TV-distance condition only. Three lines.
3. *Prose (the monitor, one paragraph):* each admitted theory carries a running evidence score; under adequacy it is a supermartingale and crosses the rejection threshold e^{b_i} with probability at most e^{−b_i}; under recurrent inadequacy it diverges and the theory is rejected, permanently. Construction in Appendix A (anytime-valid testing citations). Exact calibration: rejection at the first impossible observation (Convention 7.3).
4. **Definition (Active set and causal dissonance).** Merged with `def:dissonance`. Four lines. Then the interpretation paragraph: dissonance is an anomaly-driven question — localized by where theories failed, directed because any repair must reconcile the record, open because nothing the firm can say names the answer.

Mathematical content identical throughout; only packaging changes.

### 8.3 Theorem framing (the warrant exemplar)

Before `thm:uninformative`, one paragraph: "Successful repair fits the record that produced it — by construction. It is tempting to treat that fit as evidence. The next result says it is not: conditioning on the full record and inquiry history, the output of any truth-blind process is independent of which world is actual, so retrospective fit carries no Bayes factor. Whatever confidence the entrepreneur has in the theory the insight delivered, none of it was earned by the fact that the insight organizes the experiences that provoked it." Then the theorem, then the manager-facing paragraph (the double-counting prohibition; who *can* audit).

---

## 9. New content (the only additions)

### 9.1 The winner/loser proposition — attempt with fallback, approval-gated

Goal: elevate the example's B̂₁ = 0 < B̂₂ asymmetry to a stated result. Attempt: within the deterministic, exact-calibration, winner-take-all class in which every retained token pins a unique mechanism (the appendix-vocabulary "pointwise transparent" condition — phrase the hypothesis in words in the main text), show (i) any token whose standing action already matches its pinned optimum contributes zero to fine-contingent value, so an agent whose record contains only such tokens has B̂ = 0; (ii) an agent with at least one mismatched token in some coherent grouping has B̂ > 0 whenever the current-language benchmark cannot absorb the gain (the within-cell offset argument already used in Appendix C). Interpretation: *only unresolved action margins price questions; sustained success rationally extinguishes inquiry even under incomplete awareness.* **Fallback:** if a clean general statement needs more than two new conditions or a proof over half a page, state it for the running-example class, label it explicitly as such, and add one sentence conjecturing the general pattern. Do not force generality with hypothesis-stuffing.
**Approval gate:** the drafted statement and proof are presented in the session report and integrated only after explicit author approval (runbook Session 6).

### 9.2 Testable implications (Discussion 11.2)

Five predictions, each tied to a construct and an existing empirical paradigm, 2–3 sentences each: (1) *Inquiry follows unresolved defeat* — post-failure firms generate more novel category distinctions than post-success firms with the same information (leverage asymmetry; Camuffo-style RCTs and Ott–Hannah field methods can code question generation); (2) *Forgiving demand homogenizes beliefs* — industries where customers punish misservice weakly (the β → 1 analog) sustain more homogeneous and durable shared theories (concealment); (3) *Deviants move incumbents' beliefs beyond their information content* — entry or differentiated play triggers category revision in rivals (exposure); (4) *Founder confidence exceeds warranted confidence most when validating evidence coincides with generating evidence* — separable in experiments by distinguishing discriminating tests from retrospective fit (warrant gap); (5) *Anomaly tolerance is action-gated* — firms leave acknowledged anomalies unexplored when no decision margin depends on them (zero leverage).

### 9.3 Figures and tables per §7.2. Nothing else new (R11).

---

## 10. Literature repair (Phase 5)

Add the following; each row gives placement and the one-line positioning move. **Verification protocol:** if the agent has web access, verify every bibliographic detail (venue, year, spelling) before finalizing; items marked "verify" must be confirmed to exist as described. If web access is unavailable, insert the citation with a `% VERIFY-CITE` comment and list all such items in the session report for external verification.

| Addition | Where | Positioning move |
|---|---|---|
| Ortoleva (2012), AER, hypothesis-testing model of paradigm change | Intro fn.; Related work ¶4 | Closest relative of the dissonance trigger; differentiate in one sentence: his agent switches among *ex ante represented* priors; here the replacement is inexpressible before insight. |
| Esponda & Pouzo (2016), Econometrica, Berk–Nash equilibrium | §5 self-sealing passage; Related work ¶4 | The modern fixed-language misspecification benchmark this paper's front end sits upstream of. |
| Fudenberg, Lanzani & Strack (Econometrica, ~2021), survival/limit points of misspecified learning | Related work ¶4 | Which misspecified models persist — within a fixed hypothesis space; here the space is endogenous. |
| Ba, "Robust misspecified models and paradigm shifts" (**verify**) | Related work ¶4 | Model switching under accumulating evidence, with the alternatives represented; contrast as above. |
| Shafer (2021, JRSS-A); Ramdas, Grünwald, Vovk & Shafer (2023, Statistical Science); Grünwald, de Heide & Koolen, "Safe testing" (**verify details**) | Dissonance monitor paragraph; Appendix A | Attribute the e-process machinery and convert it into a selling point: the dissonance monitor is a state-of-the-art anytime-valid sequential test. |
| Nickerson & Zenger (2004, Org. Science); Baer, Dirks & Nickerson (2013, SMJ) | Related work ¶1; Discussion | A paper titled "Questions Before Priors" must engage problem finding/formulation; position: they treat problem choice given a representation; here the representation's failure *generates* the problem. |
| Gavetti & Levinthal (2000, ASQ); Tripsas & Gavetti (2000, SMJ); Csaszar & Levinthal (2016, SMJ) | Related work ¶1 | The managerial-cognition/representation stream; one sentence each. |
| Fryer & Jackson (categorical cognition); Mullainathan ("Thinking through categories," wp) (**verify**) | Scope subsection | The coarse-categories foil that makes the five disciplines bite: unawareness vs categorization/inattention. Optional single clause on rational inattention (Sims). |
| Denrell (2003, Org. Science), undersampling of failure | Discussion, winner/loser paragraph | Adjacent mechanism: there, success bias distorts inference within a model; here, unresolved defeat generates the diagnostic contrasts that make a *new* model priceable. |

Entries go in `paper/MDR_TBV_Paper01.bib`, keys in the existing `AuthorYear` style.

---

## 11. Acceptance checklist (all must pass; verified in Phase 6)

1. Main text ≤ 13,500 words; ≤ 9 results, ≤ 12 definitions/assumptions, ≤ 2 remarks above the line.
2. Skip Test passes for every section (residue files in `notes/revision_v10/` read as a complete essay).
3. Every formal environment is sandwiched (R2).
4. Abstract matches §6's structure; the four signature findings are statable from the abstract alone.
5. No killed term appears in the main text; every kept term defined in plain words at first use; grep-verified.
6. §2 exists, previews all headline numbers, and every later `excont` points back to it.
7. Table 1 exists and the five scattered knowledge statements it replaces are gone; Tables/Figures per §7.2 all present and referenced.
8. All §10 citations added; verified or flagged `% VERIFY-CITE` with a consolidated list.
9. No proof > 8 lines in main text; every demoted item reachable by a pointer; label map complete in METRICS.md.
10. All `% MDR-DECISION:` flags collected in METRICS.md; nothing mathematical silently changed; no frozen decision (§1) touched; `latexmk -pdf` clean; one-sentence-per-line intact throughout.
