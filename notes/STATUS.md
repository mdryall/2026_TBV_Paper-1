# Where we are — TBV Paper 1 (read this first when returning)

Last worked: **14 August 2026.** Everything below describes the state at that date.
Source of truth: **`paper/tbv_mdr_GPTedit-09.tex`** (one sentence per line; bib
`MDR_TBV_Paper01.bib`). Matching PDF: **`paper/tbv_mdr_GPTedit-09.pdf`**.
Build: `cd paper` followed by `latexmk -pdf tbv_mdr_GPTedit-09.tex`.
Compiles clean, **48 pp**.

Current redraft stage: B1–B8 COMPLETE / PASS.
B1 --- Evidence Process & Detection Mathematics: COMPLETE / PASS.
B2 --- Formal Hygiene & Notational Architecture: COMPLETE / PASS.
B3 --- The Value of a Question: COMPLETE / PASS.
B4 --- Warrant, Confidence & Insight: post-implementation review PASS.
B5 --- Dissonance, Questions & Scope of Generativity: post-implementation review PASS.
B6 --- Strategic Dynamics & Claim Audit: targeted post-implementation review PASS.
B7 --- Contribution Architecture / AHA Pass: implementation and scope review PASS.
B8 --- Whole-Manuscript Integration Audit: COMPLETE / PASS.
B8 PASS — READY FOR FINAL PROMOTION. No acceptance-bar blockers identified.
Redraft status: COMPLETE / CLOSED. Formal architecture: FROZEN.
B3 completed the approved deliberative-leverage implementation and
post-implementation review; both passed.
B2 completed the formal-hygiene, notation, epistemic-status, and
transition-initialization audit; implementation and final verification passed.

The current redraft is governed by `notes/REDRAFT_PLAN.md`. Earlier design and
repair documents remain historical context; where the redraft plan explicitly
reopens an issue, the redraft plan controls.

## Bottom line
The **formal core** — setup (§3) + propositions (§4–§9) + appendix — is complete,
internally consistent, independently stress-tested, and its new proofs verified.
The B8 acceptance-bar audit passed without requiring manuscript changes.
The **front matter and closing sections** now foreground the paper's four signature
findings and align their scope with the formal results.

## The model now (the setup you asked to focus on)
- **Single clock** of periods `t=1,2,…` (generations/episodes are gone).
- **`τ:S→Θ`** — a fixed finite mechanism vocabulary `Θ` and an objective assignment
  `τ`; theories are cell-constant `Θ`-assignments. This is the unawareness engine and
  is load-bearing (do not collapse it — see design note).
- **Standing policy + (S,s) switching**: `σ_i` persists; switch to the belief-optimal
  `σ*_i` iff the horizon-`T` gain clears a one-time **switching hurdle `κ_i`**
  (`T` = a common valuation/planning horizon). Policy inertia is emergent.
- **Sequential dissonance detector** with agent-specific **capacity `b_i`**: each
  theory carries an e-process; reject permanently when `log E ≥ b_i`; Ville ⇒
  false-alarm `≤ e^{-b_i}`; deterministic `η=0` recovers the exact test. Explicit
  construction in Appendix (`app:eprocess`).
- **Inquiry prices the QUESTION, not the answer**: elect iff `λ_i B̂_i ≥ γ_i`. `κ_i`
  deliberately does NOT enter — pre-insight the refined policy is unrepresentable, so
  it cannot be priced (general principle: pre-insight deliberation quantifies only over
  currently-represented objects).

## Propositions (what now follows from the setup)
Boundary (no-emergence, self-sealing) → detection (test-consistency, exposure) →
direction/fallibility (nonidentification, robust-sufficiency) → **pricing the question**
(participation, certification) → warrant (insight-is-not-evidence, self-audit) →
dynamics (absorption, SCUE, rest-points) → persistence. New this cycle:
- **`rem:stickiness` — enlightened inertia**: learn the model, decline the priced-out
  switch. Second persistence channel (now in `prop:persistence`).
- **`prop:capacity`**: capacity is one cognitive-style dial — detection time `O(b_i/D_i)`
  vs. rest-point robustness `1−Σe^{-b_i}`.
- **`rem:two-sources`**: two heterogeneity origins — awareness-path (identical agents,
  different experiences) vs. cognitive-style (`b_i`, `κ_i`).
- **`prop:punishing`**: diagnosticity is *robust* (open condition on primitives);
  concealment is the `β=1` knife-edge only as `η→0`.

## Decisions locked (settled with you — don't relitigate unless you want to)
- Single clock; standing-policy/(S,s)/`κ_i`; sequential detector/`b_i`.
- Inquiry does NOT net `κ_i` (question-not-answer).
- Capacity heterogeneity = **modest-core** (one proposition + the two-sources remark).
- `τ:S→Θ` two-level structure kept (the unawareness engine).

## Future work
Future work, journal formatting, or submission packaging must begin as a separately
authorized project and must not silently modify GPTedit-09.

## Where to look
- `notes/single-clock-redesign.md` — the design spec for the overhaul (primitives,
  the two triggers, the claim-by-claim change map).
- `notes/formal-core-plan.md` — the 5-phase plan (Phases 1–3 executed).
- `git log --oneline b28f3c9~1..HEAD` — the formal-core work, one commit per phase.
- Auto-memory (`paper1-revision-state.md`) carries the same state for the assistant.

## 2026-08-15 GPTedit-10 revision project OPEN
Directive: notes/REVISION_PLAN_v10.md; execution per notes/REVISION_RUNBOOK_v10.md.
Scope: expository restructuring only. B1–B8 remains CLOSED; the formal architecture remains FROZEN.
Authoritative manuscript remains paper/tbv_mdr_GPTedit-09.tex until explicit author promotion.
