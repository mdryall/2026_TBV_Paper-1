# Plan: a complete, coherent formal core for pre-Bayesian theory-building

Goal (MDR, July 25 2026): a formal core (SETUP + PROPOSITIONS) that hangs together and
delivers the original concept — a theory of *pre-Bayesian theory-building* sitting at the
intersection of MDR's formal work. Front matter (abstract/intro/lit/discussion) is
**out of scope for now**; focus is the setup's sensibility and whether interesting
propositions follow. Work the formal core to a settled state *before* MDR resumes manual edits.

Status going in: single-clock overhaul complete, compiles 41pp; three-way stress-test done;
minors + two clear corrections fixed (commit b28f3c9). Two audit items still open (#1, #4).

---

## Phase 1 — Close soundness (finish the audit)

**1A. Recast `prop:rest-points`(ii-b) onto the sequential detector [#1].**
Current proof argues non-dissonance via the *retired* fixed-sample TV test (both math
auditors flagged this). Correct fix is *simpler* than the current proof:
- entry-active theories are all η-adequate ⇒ each `E^m_i` is a supermartingale ⇒ Ville ⇒
  survives w.p. ≥ `1 − e^{-b_i}`; union ⇒ all survive w.p. ≥ `1 − |M_i|e^{-b_i}`;
- permanent rejection keeps the active set ⊆ entry set ⇒ acting belief stays on
  η-adequate theories ⇒ strict optimality fixes the action ⇒ no switch, no election.
- Most of the Hoeffding / `N(δ)` / `ε ≤ 2(η−η')` apparatus **drops out**; new bound is the
  clean capacity-governed `1 − |M_i|e^{-b_i}`.
- **Payoff:** this yields a genuine result — *capacity governs rest-point robustness*: a
  low-`b_i` agent can spuriously destabilize a good configuration. Feeds Phase 3's capacity
  proposition. **Needs sign-off** (changes hypotheses + bound of a proposition).

**1B. Reconcile `prop:persistence` with enlightened inertia [#4].**
Statement says every disadvantaged agent is "in dissonant stasis," but the inertia agent is
*not* dissonant (it learned, returned to a Bayesian world, declined the priced-out switch).
Options: (a) broaden the proposition to two channels — dissonant stasis OR non-dissonant
below-hurdle inertia; (b) keep it dissonant-only and state inertia as its own result.
Recommend (a). **Needs sign-off.**

Deliverable: every proposition sound; re-verify proofs.

---

## Phase 2 — Interrogate the setup ("sensible and minimal?")

For each primitive/assumption ask: does it earn its place, and is it the cleanest realization
of the concept? Targeted questions:

- **τ:S→Θ + fixed vocabulary** (the unawareness engine — settled to keep). Check the
  "vocabulary known, distinctions lacking" framing is used *consistently* in every result;
  confirm the single-mechanism restriction (vs distributions) is stated at its tightest.
- **Standing policy / (S,s) / κ_i / valuation horizon T.** Is `T` a clean primitive or a
  kludge? (It amortizes a lumpy cost; decide whether to interpret it or leave as a common
  horizon.) Is κ_i the right object (per-policy, as now, vs per-cell)? Is "evaluate over `T`
  periods, no discounting" the minimal myopic rule? This apparatus is MDR's deliberation /
  cached-conclusions connection — keep central, but make it minimal.
- **Dissonance capacity b_i / sequential e-process.** Is the e-process the cleanest way to
  present DETECTION for the audience, or should detection read as a threshold on accumulated
  misfit with the e-process as rigorous backing (appendix)? Decide capacity's status (see
  Decision 1).
- **η, w, n̄ (retrospective-fit params).** Now that detection is sequential, are these
  minimal? Can the repair and grouping tests be unified, or w/n̄ trimmed? (Possible further
  simplification — the payoff is fewer knobs.)
- **Two records (r_i / r̄_i) + recodability idealization.** Confirm this is the minimal
  apparatus that lets the agent "price the question, not the answer" and that the warrant /
  nonidentification results genuinely need it (they do) — no more.
- **Assumption sufficiency.** For each proposition, confirm its hypotheses are *supported*
  by the stated assumptions and not over-assumed (ass:regularity, ass:full-support,
  ass:elective, ass:observation).

Deliverable: a short "setup audit" — each primitive justified or trimmed; a defensibly
minimal setup.

---

## Phase 3 — Proposition audit ("interesting propositions follow")

Inventory every proposition against the concept's arc; grade each for interest / non-vacuity;
strengthen weak ones, cut dead ones, add missing ones.

- **Keep (strong, distinctive):** no-emergence + self-sealing (Bayes can't detect its own
  failure); nonidentification + robust-sufficiency (no truth-blind rule uniformly correct);
  participation + certification (price a question before its answer); the-insight-is-not-
  evidence + self-audit (warrant gap); absorption + SCUE.
- **Strengthen:** `prop:diagnostic` (flagged near-tautological in prior notes) — pin the
  substantive content to primitive conditions (e.g. β<1 ⇒ exposure under all sustainable
  profiles) rather than restating def:exposure.
- **Promote to a named proposition:** *enlightened inertia* (currently `rem:stickiness`) if
  it is to be a headline second-persistence-channel result.
- **Add (candidates):**
  - *Capacity comparative statics* — expected stability duration ≈ `b_i / D` (severity);
    rest-point robustness ≥ `1 − |M_i|e^{-b_i}` (from 1A). Turns the capacity story into a
    result. (Only if Decision 1 = core.)
  - *Two sources of heterogeneity* — a clean statement separating the awareness-path channel
    (identical agents, different experiences) from the cognitive-style channel (different
    b_i/κ_i). Resolves the intro tension the conceptual audit flagged.
  - *(optional) value-capture hook* — the discovering firm's transient edge as a rent to
    awareness (bridge to Gans–Ryall / Bryan–Ryall–Schipper), as a small result or a flagged
    extension.

Deliverable: proposition inventory with grades + a strengthen/add/cut action list.

---

## Phase 4 — Situate in MDR's corpus (the "intersection")

Make the setup's contact points crisp — this is what makes it *the* hub of MDR's program:

- **SCE / subjective rationality (Ryall 2003):** SCUE = SCE + two epistemic conditions;
  fixed-language special case recovers SCE *exactly*. Make the reduction explicit.
- **Causal learning over structures (Ryall 2009):** the within-vocabulary tier *is* the
  causal-ambiguity/operating-structures inference; the paper "begins where that stops."
  State the bridge.
- **Deliberation / cached conclusions / when-to-reconsider (RyallAction 2026):** the (S,s)
  switching rule *is* the reconsideration mechanism; enlightened inertia is the theory-to-plan
  stickiness. Strong intersection — state it.
- **Value capture (Gans–Ryall; Bryan–Ryall–Schipper 2022):** awareness earns rents there;
  here awareness *originates*. Hook as above.
- **Lonergan / cognitional (Ryall–Wilkins 2018):** the cognitional map disciplines which
  objects must not be conflated (already in place) — confirm it stays disciplining.

Deliverable: an explicit "situating" showing the paper as the front-end hub of the program.

---

## Phase 5 — Verify

Re-run a focused consistency/proof check over the revised core; confirm each proposition's
hypotheses are supported and non-vacuous; compile. THEN (deferred) update the front matter to
match (the conceptual audit already lists exactly what is stale/missing).

---

## Decisions needed from MDR to start Phases 2–3

1. **Capacity heterogeneity (b_i): core result or extension?** If core, we add the capacity
   comparative-statics proposition(s) and the "two heterogeneity sources" statement; if
   extension, we keep b_i mostly as detection machinery and flag the comparative statics for a
   later paper. *Recommendation:* modest-core — one proposition (stability duration /
   rest-point robustness), since 1A produces the bound for free.
2. **`prop:persistence` scope [#4]:** broaden to two channels (recommended) or keep separate.
3. **`rest-points`(ii-b) recast [#1]:** approve the capacity-governed bound (recommended).
4. **How aggressively to minimize the setup** (Phase 2): trim η/w/n̄ / interpret T, or leave
   the current apparatus and only justify it?
