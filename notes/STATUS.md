# Where we are — TBV Paper 1 (read this first when returning)

Last worked: **12 August 2026.** Everything below describes the state at that date.
Source of truth: **`paper/tbv_mdr_GPTedit-02.tex`** (one sentence per line; bib
`MDR_TBV_Paper01.bib`). Matching PDF: **`paper/tbv_mdr_GPTedit-02.pdf`**.
Build: `cd paper` followed by `latexmk -pdf tbv_mdr_GPTedit-02.tex`.
Compiles clean, **44 pp**.

Current redraft stage: B1 COMPLETE; B2 has not begun and remains PENDING.
B1 --- Evidence Process & Detection Mathematics: implementation and targeted post-implementation verification PASS.

The current redraft is governed by `notes/REDRAFT_PLAN.md`. Earlier design and
repair documents remain historical context; where the redraft plan explicitly
reopens an issue, the redraft plan controls.

## Bottom line
The **formal core** — setup (§3) + propositions (§4–§9) + appendix — is complete,
internally consistent, independently stress-tested, and its new proofs verified.
**It is ready for your read-through of the setup and propositions.**
The **front matter** (abstract, §1 intro, §2 related lit, discussion) is deliberately
**NOT yet updated** to the reworked model — that is the main outstanding task.

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

## OUTSTANDING when you return
1. **Your read-through** of the setup + propositions — the point of this cycle was to
   make them sensible and interesting; your judgment is the next input.
2. **Front matter sync** (deferred): abstract/intro/discussion still describe one
   persistence channel and omit enlightened inertia + capacity heterogeneity; intro's
   "five sets of results" is now incomplete; §2 (~line 203) understates SCUE (it also
   *relaxes* optimality to the inaction band); intro's "identical agents" headline
   should acknowledge the two heterogeneity sources. The conceptual audit produced the
   full itemized list — ask me to resurface it.
3. **Optional**: spell out the enlightened-inertia persistence instance in the running
   example (`κ>½` case gives a clean 3/4 vs 1/4 gap); sharpen the prose corpus-situating
   (SCE / causal-ambiguity / deliberation / value-capture / Lonergan).

## Where to look
- `notes/single-clock-redesign.md` — the design spec for the overhaul (primitives,
  the two triggers, the claim-by-claim change map).
- `notes/formal-core-plan.md` — the 5-phase plan (Phases 1–3 executed).
- `git log --oneline b28f3c9~1..HEAD` — the formal-core work, one commit per phase.
- Auto-memory (`paper1-revision-state.md`) carries the same state for the assistant.
