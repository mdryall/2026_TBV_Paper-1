# REVISION_RUNBOOK_v10.md — Execution protocol for the GPTedit-10 revision

**Intended repo location:** `notes/REVISION_RUNBOOK_v10.md`
**Companion:** `notes/REVISION_PLAN_v10.md` (the change specification). The plan says *what*; this file says *how, in what order, with what gates*.

---

## 1. Author setup (one-time, before any agent session)

**The author's only manual step is to save `REVISION_PLAN_v10.md` and this file into `notes/`.** Committing them **is** the authorization for the scoped project they describe. The governance-file updates below are applied by the agent in Session 0 on the author's instruction, using the exact text in items 1 and 2; the author verifies them in the Session 0 diff.

Author decisions, resolved and recorded here (no further input needed):

- **Voice:** first person "I" for authorial actions, impersonal for facts (plan R9 default; the plan §6 abstract is drafted accordingly).
- **Section 2 authorship:** the author writes Section 2 personally. The agent supplies a fragment-level scaffold beforehand (Session 3A) and integrates afterward without editing the author's prose (Session 3B).

1. Block to append to `AGENTS.md` (verbatim):

   ```
   ## Active project: GPTedit-10 revision (expository restructuring)
   Directive: notes/REVISION_PLAN_v10.md + notes/REVISION_RUNBOOK_v10.md. Read both in full before any edit.
   Working file: paper/tbv_mdr_GPTedit-10.tex (created in Phase 0 as a copy of -09).
   paper/tbv_mdr_GPTedit-09.tex is READ-ONLY for this project. It remains the sole authoritative manuscript.
   Promotion of -10 to authoritative is an author act only. Agents never promote.
   The frozen-architecture list in REVISION_PLAN_v10.md §1 is binding. Conflicts resolve in favor of the frozen
   decision, flagged with % MDR-DECISION: comments — never resolved silently.
   Mathematical content of retained statements is unchanged; approved structural changes are those listed in the plan.
   One new formal item exists (winner/loser proposition); it is approval-gated per the runbook.
   Commits only on explicit author instruction at session boundaries. Never push. Never promote.
   One sentence per line, all prose, always.
   Journal formatting / submission packaging remain out of scope (separately authorized project).
   ```

2. Block to append to `notes/STATUS.md`:

   ```
   ## [date] GPTedit-10 revision project OPEN
   Directive: notes/REVISION_PLAN_v10.md; execution per notes/REVISION_RUNBOOK_v10.md.
   Scope: expository restructuring only. B1–B8 remains CLOSED; the formal architecture remains FROZEN.
   Authoritative manuscript remains paper/tbv_mdr_GPTedit-09.tex until explicit author promotion.
   ```

---

## 2. Standing rules for every session

- **Read order at session start:** `notes/STATUS.md` → `AGENTS.md` → `notes/REVISION_PLAN_v10.md` (in full) → this file's section for the current session. In Session 0 only, also read `agenda/Questions_Before_Priors.tex` (positioning constraints; the "no-baked-in" checklist is a constraint source — flag conflicts, never resolve them).
- **Scope discipline:** execute only the current session's listed scope. Anything discovered along the way (an inconsistency, a tempting improvement, a downstream breakage caused by an approved edit) is *reported*, not fixed, unless it is inside scope.
- **Stop conditions:** session gate passes → stop and report. Gate cannot pass → stop and report why. Ambiguity about a frozen decision or mathematical content → `% MDR-DECISION:` flag, continue with the rest of scope, report.
- **No commits until instructed.** Every session ends with a report; the author reviews the diff and says "commit" (message format: `v10 session N: <summary>`) or requests changes.
- **Working artifacts** live in `notes/revision_v10/`: `METRICS.md` (word counts, environment counts, label map old→new, all MDR-DECISION and VERIFY-CITE flags, updated every session); `skiptest_<sec>.md` (math-stripped residue per rewritten section, for author reading).
- **Report template** (end of every session):
  1. Session/phase and scope executed.
  2. Files touched; diff summary in prose (one-sentence-per-line makes the raw diff reviewable — point to the hunks that matter).
  3. Environment/label changes this session (delta to the label map).
  4. Word counts vs budget for touched sections.
  5. Skip Test residue file paths (if prose was written).
  6. New `% MDR-DECISION:` and `% VERIFY-CITE` flags.
  7. Compile status (`latexmk -pdf` from `paper/`, clean or not, with log excerpts on failure).
  8. Open questions for the author.

---

## 3. Session map

Run each session in a **fresh agent context**. Between sessions the author reviews the diff, reads the skip-test residues, and instructs commit or revision. From Session 4 onward, every kickoff prompt includes: *"Match the register of the current abstract in tbv_mdr_GPTedit-10.tex; it is the tonal reference."*

### Session 0 — Phases 0–1: baseline and mechanical demotions

**Kickoff prompt:**
> Read, in order: notes/STATUS.md, AGENTS.md, notes/REVISION_PLAN_v10.md in full, notes/REVISION_RUNBOOK_v10.md Session 0, and agenda/Questions_Before_Priors.tex. First, apply the governance updates: append the AGENTS.md block from runbook §1 item 1 verbatim to AGENTS.md, and the STATUS.md block from §1 item 2 to notes/STATUS.md with today's date substituted for [date]. Append only; change nothing else in either file. Then execute Phase 0: copy paper/tbv_mdr_GPTedit-09.tex to paper/tbv_mdr_GPTedit-10.tex; update the truth-version header comment in -10 to identify it as the working draft (non-authoritative); build the baseline PDF; create notes/revision_v10/METRICS.md with baseline counts (total/main/appendix words, pages, environment counts by type). Then execute Phase 1: move the plan §4.2 items to a new Appendix D verbatim (statements + proofs), leaving one-sentence pointers at their original locations; convert the plan §4.3 remarks to prose in place, content preserved, environments deleted. No rewriting of prose beyond what conversion mechanically requires. -09 is untouched. Compile, update METRICS.md, stop, and report. Do not commit.

**Gate:** governance blocks appended verbatim with nothing else in those files changed; -10 compiles clean; -09 byte-identical to before; every demoted item present in Appendix D with a pointer; label map recorded; ≤2 remark environments remain in main text.
**Author review:** skim Appendix D for completeness; confirm nothing was paraphrased during the move.

### Session 1 — Phase 2: infrastructure

**Kickoff prompt:**
> Read the standing files, then runbook Session 1. Execute Phase 2 per plan §7: build Table 1 (epistemic ledger), Table 2 (terminal-conditions taxonomy), Figures 1–3 (TikZ, greyscale-safe); insert the Calibration Convention paragraph in the Model section and delete the inline deterministic/stochastic duplications it replaces; create the skeletons of manuscript subsections 4.4 (What agents know and don't know) and 4.5 (Scope and modeling commitments), moving the five scattered epistemic statements into 4.4 and the existing five modeling disciplines into 4.5. Content moves; no new narrative yet beyond the Convention paragraph and table/figure captions. Compile, update METRICS.md, stop, report. Do not commit.

**Gate:** compiles; tables/figures render and are referenced; the scattered statements and case-duplications the new infrastructure replaces are demonstrably gone (grep evidence in the report).
**Author review:** check Table 1 against your own understanding of the information structure — this table is the single answer to "what do agents know," so it must be exactly right.

### Session 2 — Phase 3a: abstract + Introduction

**Kickoff prompt:**
> Read the standing files, then runbook Session 2. Rewrite the abstract using plan §6 verbatim as the base, formatted one sentence per line. Rewrite Section 1 (Introduction) per the plan §5 paragraph architecture and budget (2,200 words), keeping the four-findings skeleton and replacing all prose; obey the reader contract R1–R11. Leave a placeholder \section for the new Section 2 with a % TODO. Write notes/revision_v10/skiptest_intro.md. Compile, update METRICS.md, stop, report. Do not commit.

**Gate:** budget met; skip-test residue reads as a complete essay; the four findings appear in strategy language with example numbers.
**Author review:** **edit the abstract into your voice now.** From this point it is the register reference for every later session.

### Session 3A — Phase 3b(i): Section 2 scaffold (no prose)

**Kickoff prompt:**
> Read the standing files, then runbook Session 3A. Produce a scaffold for the new Section 2 at notes/revision_v10/sec2_scaffold.md, for the author to write from. It must contain, act by act (five acts per plan §5, Section 2 row): the beats to hit; every number that must appear, each with its Appendix C source reference; the constructs previewed and the later section each one sets up; and any point where the example's arithmetic constrains how the story can be told. Bullet points and fragments only — do NOT write polished prose, sentences the author might be tempted to keep, or a draft in any register; the author writes this section. Note anything in the example a reader will likely stumble over, any number in the current excont blocks that Section 2 must preview, and which later excont blocks will shrink once Section 2 exists. Do not modify the manuscript. Stop and report.

**Gate:** scaffold exists; it is fragments, not prose; every frozen number appears with its Appendix C reference.

**Between 3A and 3B — the author writes Section 2** in full at `notes/revision_v10/sec2_draft.md`, working from the scaffold. This is the paper's front door and stays in the author's voice.

### Session 3B — Phase 3b(ii): Section 2 integration

**Kickoff prompt:**
> Read the standing files, then runbook Session 3B. Integrate notes/revision_v10/sec2_draft.md into paper/tbv_mdr_GPTedit-10.tex as Section 2, replacing the placeholder. Preserve the author's wording exactly: format one sentence per line, convert to LaTeX, add labels and cross-references, and match the text to Figure 2. Do not rewrite, tighten, smooth, or re-register the author's prose; if a passage seems unclear or a claim seems unsupported, flag it in the report rather than editing it. Verify every number against Appendix C and flag any mismatch with % MDR-DECISION rather than changing either side. Then shrink every later excont block ~60% into pointers back to Section 2, preserving any computation Section 2 does not preview. Write skiptest_sec2.md. Compile, update METRICS.md, stop, report. Do not commit.

**Gate:** author's wording intact (the report confirms no prose edits); all headline numbers verified against Appendix C; excont blocks shrunk with nothing lost that Appendix C doesn't hold; budget met.

### Session 4 — Phase 3c: Model (manuscript §4)

**Kickoff prompt:**
> Read the standing files, then runbook Session 4. Rewrite the Model section per plan §5 (2,600 words): narrative for 4.1–4.3 per the reader contract; complete 4.4 around Table 1; complete 4.5 as the sole container of defensive material, including the fixed-Θ scoping paragraph (companion-work phrasing; check agenda/Questions_Before_Priors.tex for prescribed wording and flag if unclear) and the open defense of the technology's access to the analyst record. Unbundle Assumption environments per the one-job rule with content preserved. Match the abstract's register. Write skiptest_model.md. Compile, update METRICS.md, stop, report. Do not commit.

**Gate:** budget; skip test; no defensive sentence outside 4.5 (grep for hedging markers reported); label map updated.

### Session 5 — Phase 3d: Bayesian boundary + Causal dissonance (manuscript §§5–6)

**Kickoff prompt:**
> Read the standing files, then runbook Session 5. Rewrite manuscript §5 (700 words) and §6 (1,200 words) per plan §5, using the plan §8.2 unbundling exemplar for def:test exactly; detector mathematics unchanged (frozen); Belief bookkeeping as a titled sub-subsection with a five-step protocol; exposure/concealment and the merged exposure proposition per Keep-#8, with the diagnostic machinery pointered to Appendix D. Insert the anytime-valid testing citations as % VERIFY-CITE placeholders if not yet verified. Write skiptest_boundary.md and skiptest_dissonance.md. Compile, update METRICS.md, stop, report. Do not commit.

**Gate:** budgets; skip tests; def:test content mathematically identical across the split (state this check explicitly in the report).

### Session 6 — Phase 3e: Inquiry + The value of a question (manuscript §§7–8) — **approval gate**

**Kickoff prompt:**
> Read the standing files, then runbook Session 6. Rewrite manuscript §7 (1,100 words) and §8 (1,700 words) per plan §5, including the enlightened-inertia prose with the frozen rationale (κ excluded from participation because pre-insight the refined policy is unrepresentable and cannot be priced). Then attempt the winner/loser proposition per plan §9.1, honoring the fallback rule. DO NOT integrate the new proposition into the manuscript: render its statement, proof, and your general-vs-example-class recommendation in the session report for author approval. Write skiptest_inquiry.md and skiptest_value.md. Compile, update METRICS.md, stop, report. Do not commit.

**Gate:** budgets; skip tests; the proposition draft is in the report, not the manuscript.
**Author review:** approve, amend, or reject the proposition; a short follow-up instruction in the same or next session integrates the approved version.

### Session 7 — Phase 3f: Warrant + Dynamics (manuscript §§9–10)

**Kickoff prompt:**
> Read the standing files, then runbook Session 7. Integrate the approved winner/loser proposition into manuscript §8 if instructed. Rewrite §9 (1,200 words) and §10 (1,500 words) per plan §5, using the plan §8.3 theorem-framing exemplar for thm:uninformative; rename representation-relative coherence to the agent's confidence (Coh unchanged); build the Dynamics section around Table 2, with the converted anomaly-tolerance and two-sources paragraphs (the latter carrying the modest-core capacity channel) and the capacity comparative-statics pointer. Write skiptest_warrant.md and skiptest_dynamics.md. Compile, update METRICS.md, stop, report. Do not commit.

**Gate:** budgets; skip tests; fulcrum discipline visible (equilibrium machinery subordinate — one section, apparatus pointered down).

### Session 8 — Phase 3g: Discussion + Conclusion + Related work (manuscript §§11–12, then §3)

**Kickoff prompt:**
> Read the standing files, then runbook Session 8. Rewrite Discussion (1,800 words) per plan §5 including the new Testable implications subsection per plan §9.2 and the one-paragraph cognitional interpretation; rewrite the Conclusion (300 words); then rewrite Related work LAST (900 words), verdict-first, weaving in the plan §10 additions as % VERIFY-CITE placeholders where unverified. Write skiptest_discussion.md and skiptest_related.md. Compile, update METRICS.md, stop, report. Do not commit.

**Gate:** budgets; skip tests; every §10 addition placed or flagged.

### Session 9 — Phase 4: terminology sweep

**Kickoff prompt:**
> Read the standing files, then runbook Session 9. Apply the plan §7.1 rename/kill map globally to the main text; confirm by grep that no killed or appendix-only term appears above the appendices and paste the grep evidence into the report; confirm every kept term is defined in plain words at first use. Compile, update METRICS.md, stop, report. Do not commit.

**Gate:** grep evidence clean; compile clean.

### Session 10 — Phase 5: literature repair

**Kickoff prompt:**
> Read the standing files, then runbook Session 10. Execute plan §10: if web access is available, verify every entry (venue, year, spelling, existence of "verify"-marked items) before finalizing; add entries to paper/MDR_TBV_Paper01.bib in AuthorYear key style; resolve the % VERIFY-CITE placeholders you can, and produce a consolidated list of any you cannot. Compile (bibliography included), update METRICS.md, stop, report. Do not commit.

**Gate:** every plan §10 row either cited-and-verified or on the consolidated unresolved list (the author routes unresolved items to an environment with web search).

### Session 11 — Phase 6: global pass and handoff

**Kickoff prompt:**
> Read the standing files, then runbook Session 11. Global pass: align the abstract, Introduction, Discussion, and Conclusion so each signature finding is described in the same words in all four places; fix all cross-references; verify the full acceptance checklist in plan §11 item by item and record the results in METRICS.md; append final metrics vs the plan §2 baseline table; consolidate all % MDR-DECISION and % VERIFY-CITE flags into a closing section of METRICS.md. Final latexmk build. Stop and produce the handoff report: checklist results, final metrics, flag list, and any residual open questions. Do not commit. Do not promote.

**Gate:** all 10 acceptance items pass or are explicitly waived by the author.

---

## 4. Author close-out (after Session 11)

1. Full read-through of -10 against the skip-test residues; resolve all MDR-DECISION flags; route unresolved VERIFY-CITE items for external verification.
2. When satisfied, instruct the final commit, then **promote by explicit instruction** (e.g., update `AGENTS.md` and `notes/STATUS.md` to name `paper/tbv_mdr_GPTedit-10.tex` authoritative and mark -09 superseded). Promotion is yours alone.
3. Journal formatting and submission packaging begin only afterward, as their own separately authorized project per `notes/STATUS.md`.
