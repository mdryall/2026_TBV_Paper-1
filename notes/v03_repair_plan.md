# v03 Repair Plan — Questions Before Priors

Consolidated from GPT machine review #2 (Draft01-GPTReview02.pdf) + four internal
audits (example, feasibility, proof-rigor, claims). Fork decisions: **A1 + B1 + C1**.

Target file: `paper/tbv_mdr_Paper01-v03.tex` (copy of v02, TRUTH-VERSION header updated).
v02 stays as the reviewed baseline.

---

## THE SPINE (architectural — approved)

1. **Two typed records.** Deliberative `r_i` = tokens `(C, a, x_i)` (agent decides on
   these). Analyst `r̄_i` = additionally holds `s` (R, Λ, Θ, nonidentification,
   warrant live here). Recodability = capacity acquired WITH the predicate, flagged
   idealization. Assign every object to the reader that can compute it.

2. **B̂ = subjective estimate over deliberative coherent token-groupings.** Agent groups
   retained tokens so each group is coherent (one mechanism fits its `(a,x)` within
   tolerance — no states needed); values robust gain per group vs carried-forward policy.
   λ prices ACHIEVABILITY (prob inquiry yields a refinement delivering the estimated
   value), not just success. Old analyst-invariant B is dropped.

3. **Determinism certification remark (HARMONIZATION HINGE).** Deterministic mechanisms:
   observable conflict certifies separability ⇒ B̂ = old B, answer-invariance holds as a
   THEOREM in the deterministic case. Stochastic: conflict may be noise (the row-vs-noise
   question the agent can't pose); B̂ is an estimate, λ carries the difference.

4. **λ^{(k)} decay.** Nonincreasing in consecutive failures → 0, per-agent counter, reset
   only on success. Bounded B̂ + γ>0 ⇒ elections finite deterministically (replaces the
   agent-infeasible "elect only at repairable records" gate). Counter joins SCUE state;
   warrant theorem conditions on election/failure history. New phenomenon: ABANDONED
   QUESTIONS (agent can give up on a true, valuable, repairable question). Headline
   softens: inquiry dies out = answered OR unpriced OR abandoned.

## FORK DECISIONS

- **A1**: B̂ normalized to recurrence-RATE (per-generation expected robust gain, groups
  weighted by empirical freq of their (C,a) pairs). Bounded by T·Δu; no record-length
  growth. Subjective-recurrence premise: empirical token DISTRIBUTION recurs.
- **B1**: persistence instance moves to β<1 (coarse loser genuinely in dissonant stasis;
  ¾/¼ payoffs survive; play stable). β=1 oscillation story → optional remark only.
- **C1**: keep priced inquiry as a GENERAL result (value-of-a-question theorems stay
  general, not demoted to example). Maximal-contribution path.

## WORK ORDER (each tier depends on the prior)

### Tier 1 — Spine  ✅ DONE
- [x] Two typed records (r_i deliberative / r̄_i analyst) in ass:observation; retagged
      def:technology (consumes r̄_i), def:restorative, def:leverage, thm:nonidentification,
      def:warrant.
- [x] Recodability = agent capacity acquired with predicate; idealization flagged.
- [x] B̂ (recurrence-rate = (T/|r|)·Σ per-token robust gain over coherent groupings)
      replaces meet-based B. def:pinned now "deliberative groupings & coherent classes."
- [x] rem:certification (new): determinism certifies separability ⇒ B̂=B theorem in det.
      case; noise ⇒ estimate + λ carries gap. THE harmonization hinge.
- [x] λ^{(k)} decay + failure counter k_i in ass:elective and SCUE state.
- [x] Participation on B̂, λ^{(k)}; "gain is secured" → option value; election value
      λ^{(k)}B̂−γ.
- [x] rem:irreparable: irreparability is analyst-level; dropped "agent recognizes"/"no
      cost wasted."

### Tier 2 — Proof gaps  ✅ DONE
- [x] Restoration on AGGREGATED counts + coarsening clause (dilution closed); prop:coherence
      updated.
- [x] Absorption (d): auxiliary-coupling decomposition over (G_2,σ*).
- [x] lem:test-consistency restated with frozen/recurrent clauses + η=0 exemption;
      prop:exposure gets no-legacy proviso.
- [x] Nonidentification: visited-pair marginal-equality hypothesis + coupling induction.
- [x] Rest-points (ii-b): entry count ≥N at EVERY recurrent pair; (η+ε)-dominance route
      (no KL needed); B̂.
- [x] Warrant thm conditions on analyst record + election/failure history (counterexample
      noted in prose).

### Tier 3 — Structural  ✅ DONE
- [x] def:stasis standalone before absorption; "absorbing profile" defined.
- [x] Partial-SCUE (rest-points (i)); "restricted to non-stasis" now well-typed.
- [x] SCUE (ii) → limit agreement; (iii) → acting-mass-on-inadequate vanishes; (iv) → B̂,λ^{(k)}.
- [x] Rest-points (i) → converge + strict-margin continuity.

### Tier 4 — Prose  ✅ DONE
- [x] All B→B̂, λ→λ^{(k)} across dynamics/appendix/discussion.
- [x] Abstract/intro/conclusion: "Bayesian world OR rationally tolerated dissonance
      (unpriced/unanswerable/abandoned)."
- [x] Two-force biconditional restricted to shared false theories; pricing prong for
      performance gaps.
- [x] Transparency/opacity: anomalies accumulate in OPAQUE + insensitive-transparent.
- [x] Warrant → analyst/external assessor (discussion cognitional §); heuristic
      anticipation → agent's grouping search, κ noted analyst-side.
- [x] "value computable/invariant" → "agent estimates from own record"; gap size
      "outside assessor can compute."
- [x] "anomaly tolerance is equilibrium" → "absorbing-state."
- [x] T=2 fixed + condition-on-realization; validation B̂₂=½ (was 1); persistence to β<1
      + β=1 oscillation remark; payoff-½ parenthetical fixed; example nonident refs → realized-record.
- [x] prop:no-emergence observation algebra; full-support → ass:full-support (numbered);
      μ⁺ "judged updating resumes."

### RECALIBRATED NUMBERS (verified)
- Discovery B̂=½; validation B̂₁=0, B̂₂=½ (asymmetry 0<½ is the point, NOT the old 0 vs 1);
  trap B̂=0; warrant 1/½/½; persistence ¾/¼ at β<1.

### STATUS: v03 compiles clean, 36 pp, 0 undefined refs. NOT committed.
Next: user read-through of v03, or re-run machine review. Remaining cosmetic (deferred,
low priority): ε_i symbol barely used; x_i double-encodes profile in example; a few
uncited bib entries.

## KEY RECALIBRATED NUMBERS (A1)
- Discovery B̂ = ½ (unchanged).
- Validation B̂₂: was 1 under record-sum; under A1 recurrence-rate ≈ ½ (2 off-diagonal
  states out of 4, gain ½ each, rate = T·avg). Recompute exactly during impl.
- Trap B̂ = 0 (unchanged). Persistence (β<1) B̂₂ > 0 but < γ₂ (stasis).
- Warrant coherence 1 / warrant ½ / gap ½ (unchanged; analyst-level).
