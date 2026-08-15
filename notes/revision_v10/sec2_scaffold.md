# Section 2 scaffold — "The problem in miniature" (Session 3A)

For the author to write from. Fragments only, per runbook — no draft prose here.

**Constraints on the section itself** (plan §5, Section 2 row):
- Budget 1,400 words. Five acts. Verbal + arithmetic only; zero formalism, zero coined-term definitions beyond plain-word glosses.
- Includes the state-array figure (`fig:example-array`; currently rendered as Figure 3 in §4.7 — Session 3B relocates it here).
- Success criterion: a reader who stops after §2 has the entire paper.
- Every headline number frozen (plan §1); sources below. Session 3B verifies each against Appendix C and flags mismatches with `% MDR-DECISION`.

**Appendix C paragraph key** (used as source refs below):
- C¶1 = "Dominance thresholds"
- C¶2 = "Per-token gain and deliberative leverage"
- C¶3 = "The trap and its knife edge"
- C¶4 = "Persistence payoffs"

**Source gaps to know about** (numbers NOT in Appendix C; frozen all the same):
- 15 / 11 / 4 partition counts, column-world coupling, worst-case coin flip — live in inquiry excont (§7) + `thm:nonidentification`; no C paragraph.
- Coh = 1, W = ½, gap = +½ — live in pivot excont (§9); no C paragraph.
- If author wants App C to carry these too → new authorization; out of v10 scope as planned.

---

## Act 1 — setup; belief-driven differentiation ends in dissonance

Beats:
- Two firms, one market; four customer configurations arranged 2×2 (rows × columns); equally likely each period.
- Each firm picks one of two product architectures (0 or 1).
- Truth = row law: the ROW decides which architecture customers prefer; column irrelevant. τ(s_rc)=θ^r. [ex:setup]
- Payoffs: differentiate → preferred architecture takes market (1 vs 0); pool on preferred → ½ each; pool on wrong → β/2 each, customer withholds 1−β; neutral mechanism θ^n → ½ regardless. β=1 baseline = perfectly forgiving demand. [ex:setup]
- Both firms start blind: one mental category covering all four configurations ("the market"). Expressible theories = the three constant ones: architecture 0 preferred / 1 preferred / doesn't matter. Row law NOT expressible.
- Priors differ: firm 1 leans "0 preferred," firm 2 leans "1 preferred" → at β=1 belief asymmetry alone makes each firm's leaning strictly dominant → differentiated play. [C¶1: dominant iff p⁰ > (2−β)p¹; at β=1 simple asymmetry]
- Two periods land on the diagonal configurations (s_00 then s_11) — a possible draw, not a guaranteed one.
- Outcome pair: firm 1 wins at s_00 (1,0), loses at s_11 (0,1). Each firm has one win, one loss, under the same differentiated profile.
- All three constant theories now personally refuted for each firm: "0 preferred" dies at s_11, "1 preferred" at s_00, "doesn't matter" predicted ½ at both and saw 1 and 0. [dissonance excont]
- Deterministic mechanisms → the refutations are exact; last theory's death = the Bayesian machinery itself jams (zero normalizer). Bayes cannot even say "all my theories are wrong." [bayesian excont]
- Dissonance = the firm's separate registration that nothing it can say survives its own record.
- Counterfactual for later: had beliefs been symmetric → pooling → every period pays ½ → all three theories fine forever. Differentiation is what made the shared blindness visible. [dissonance excont; seeds Act 5 trap]

Numbers Act 1 must carry: 2×2 four states; uniform draws; 1/0, ½/½, β/2; β=1; three constant theories; two diagonal periods; (1,0) and (0,1).

Constructs previewed → sections:
- coarse awareness, expressible theories → §4 (model, `def:awareness`)
- Bayesian boundary / self-sealing / zero normalizer → §5 (`prop:no-emergence`, self-sealing ¶)
- causal dissonance, active set emptying → §6 (`def:test`, `def:dissonance`)
- exposure vs concealment (differentiation exposes; pooling conceals) → §6 (`def:exposure`) and §10

Arithmetic constraints on the telling:
- Differentiation NEEDS the prior asymmetry; symmetric priors can pool → no story. State the asymmetry early.
- The diagonal two-period draw is a positive-probability event to condition on — narrate as "suppose the first two customers happen to be…" not as inevitable.
- θ^n must die on-screen too — readers forget it; it dies only because play was differentiated (saw 1 and 0, not ½).
- Firms never see configurations. They see: own action, rival's action, own payoff. "s_00" is analyst labeling — the firm remembers "the period I won" / "the period I lost." Keep the narration inside the firm's head fragmentary on purpose.

## Act 2 — the record admits exactly four repairs; the row/column fork

Beats:
- What must any successful new theory accomplish? Reconcile the record: the winning period and the losing period can no longer be "alike."
- Counting: 15 ways to partition four configurations; 11 fail (don't separate the two labeled diagonal cells); exactly 4 minimal repairs: rows, columns, isolate-the-win, isolate-the-loss. [inquiry excont; figure `fig:example-array`]
- Direction without determination: record rules out 11, cannot choose among 4.
- Simplicity narrows further: rows and columns are one-coordinate distinctions, the isolating pair need two → a factor-seeking mind lands on the row/column fork. And there direction runs out. [inquiry excont]
- Column world τ'(s_rc)=θ^c: agrees with the row world at both visited configurations — generates the identical record — yet demands the opposite repair. No record-reading procedure can be right in both worlds; best worst-case = coin flip. [inquiry excont; thm:nonidentification]
- Price of guaranteed correctness: a language fine enough for both worlds = all four configurations distinguished = every distinction the language can draw. Economy forces fallibility. [inquiry excont; prop:robust-sufficiency]
- Whichever factor arrives, its unique consistent theory extrapolates to the two never-visited configurations — and in one of the two worlds those extrapolations are wrong. Fallibility located precisely. [inquiry excont]

Numbers: 15 / 11 / 4; two one-coordinate repairs; coin flip (½ worst case); four-way singleton = robustness cost; two unlabeled cells.

Constructs previewed → sections:
- restorative refinement, minimality → §7 (`def:restorative`)
- truth-blind technology, complexity ordering → §7 (`def:technology`)
- nonidentification + robustness price → §7 (`thm:nonidentification`, `prop:robust-sufficiency`)

Arithmetic constraints:
- "Four" depends on counting the two isolating partitions as minimal — pre-empt "why do those count?" (they separate the conflict with a single new cell; nothing coarser between them and the coarse language works).
- The two worlds agree only at the VISITED pairs — the equivalence is record-relative, not global. If the narration says "identical worlds," it breaks Act 4/5 (off-diagonal play separates them).

## Act 3 — pricing the question; leverage = ½; unresolved action margin, not defeat per se

Beats:
- The decision problem at dissonance: pay for inquiry or not — with no belief to compute with and no candidate answers representable. What CAN the firm compute? Its own record.
- The firm's reading: the losing period will recur; a distinction sorting win-period from loss-period would let it act differently there.
- Per-token arithmetic (β=1, transparency: each remembered period pins its mechanism): on the losing token, switching to the pinned architecture gains ½ whatever the rival does (loss 0→pool ½, or pool ½→win 1); on the winning token, gain 0. [C¶2]
- Fine-contingent value ½; best one-action correction in the current one-category language: 0 (reversal gains ½ on the loss, loses ½ on the win — cancels). Increment = ½ − 0 = ½. Scale: two remembered periods, horizon two → B̂ = (2/2)·½ = ½. [C¶2]
- Same number for both firms — opposite experiences, identical question value. At discovery the win/loss ledger is symmetric (one each).
- Elect iff hope × value ≥ cost: λ·½ ≥ γ. [economics excont; prop:participation]
- The point of the benchmark: value is NOT compensation for defeat; it is the presence of an action margin the current language cannot resolve. Defeat mattered only because it created a period the firm would act on differently.
- Proof by later contrast (validation stretch, off-diagonal periods served; firm 1 now row-refined/true, firm 2 column-refined/false): firm 1 — every remembered period already optimally served → fine value = current value = 0 → B̂₁ = 0; never inquires again, awareness permanently incomplete. Firm 2 — two of four tokens misserved (½ each) → fine 1, current 0 (within-column reversal cancels ±½) → B̂₂ = (2/4)·1 = ½. [C¶2]
- Winner/loser asymmetry B̂₁ = 0 < B̂₂ = ½: success extinguishes the question; unresolved defeat funds it. (Formal version = the Session 6 approval-gated proposition, §8.)
- Post-insight epilogue for Act 3: acting on the answer is a second, separately priced decision. Row refinement in hand → re-differentiating gains exactly ½ over the horizon → switch iff switching cost κ < ½; at κ ≥ ½ the firm KNOWS the truth and rationally stays put. First appearance of enlightened inertia. [economics excont; C¶2 gain arithmetic]

Numbers: per-token ½ / 0; L_fine ½, L_cur 0, J ½; B̂ = (2/2)·½ = ½ both firms; election λ·½ ≥ γ; validation B̂₁ = 0, B̂₂ = (2/4)·1 = ½; κ threshold ½.

Constructs previewed → sections:
- deliberative grouping, coherence, leverage, participation → §8 (`def:pinned`, `def:leverage`, `prop:participation`)
- rational cessation, winner/loser prop → §8
- enlightened inertia, switching hurdle κ → §4 (`ass:commitment`) + §8 (`rem:stickiness` ¶) + §10 (Table 2)

Arithmetic constraints:
- B̂ = ½ needs horizon T = 2 AND exactly the two-token discovery record — (T/|r|) scaling; don't let the narration add remembered periods.
- Discovery-stage SYMMETRY (both ½) vs validation-stage ASYMMETRY (0 vs ½) — two different records; conflating them wrecks the punchline. The asymmetry needs the later four-token off-diagonal stretch with refinements already in hand.
- B̂₂ = ½ at validation equals the discovery value by coincidence ((2/4)·1 vs (2/2)·½); App C says the durable content is the asymmetry, not the equality. Don't lean on it.
- The ½-gain-vs-any-rival-action step is what makes the valuation conjecture-free — worth one clause, else readers ask "what about the rival?"

## Act 4 — the +½ warrant gap; certainty without validation; no self-audit

Beats:
- Suppose firm's inquiry delivers the COLUMN refinement (the wrong factor). Recoded record pins a unique consistent theory (0 on first column, 1 on second). Firm's own confidence in it: 1 — nothing else on its language survives. [pivot excont]
- The outside audit: candidate worlds {row, column}, even prior. The two worlds generate this exact record with equal probability, and the technology never reads the truth → seeing the output changes nothing → warranted probability stays ½. [pivot excont; thm:uninformative]
- Signed gap = 1 − ½ = +½. Same gap if the firm had drawn the ROW refinement: confidence 1, warrant ½ — even when the theory is TRUE, the generating record hasn't earned the certainty. [pivot excont]
- Why the firm can't run this audit on itself: comparing row world vs column world requires distinguishing all four configurations — finer than either repair. The assessment is literally inexpressible for the firm. Broader-awareness outsiders (board, investor) can hold it. [pivot excont; cor:self-audit]
- What WOULD close the gap: one differentiated period at an off-diagonal configuration — the two worlds predict opposite winners there. Correct theory → warrant 1; false theory → refuted outright. Pooled periods at β=1: zero discrimination, any number of them. [pivot excont]
- Moral for Act 5: validation is purchased by play that separates worlds; pooled play buys none.

Numbers: Coh 1; W ½; gap +½ (truth-independent); one off-diagonal differentiated observation resolves; pooled observations nondiagnostic at β=1.

Constructs previewed → sections:
- formulation, bridge prior, confidence (Coh) → §9 (pivot open + `def:warrant`)
- insight-is-not-evidence / no double counting → §9 (`thm:uninformative`)
- self-audit boundary, governance role → §9 (`cor:self-audit`) + §11 discussion

Arithmetic constraints:
- W = ½ is relative to the two-world candidate set + symmetric prior — assessment-specific. General theory says gap UNRESTRICTED in sign; +½ is this example's value. One clause of honesty here protects §9.
- Equal record-probability of the two worlds is conditional on the diagonal discovery event — same conditioning as Act 1. Keep the "suppose those customers arrived" thread alive.

## Act 5 — three endings

Beats (ending 1 — the trap, β = 1):
- Both firms' inquiries return the column refinement (possible; the technology is a coin flip on the fork). Both certain of the false law.
- Column policies pool at every configuration → every payoff ½ → exactly what the false theory predicts → no contradiction ever again. [C¶3]
- A shared false theory, held with full confidence, forever: stable, self-confirming, payoff-relevantly wrong. Warrant frozen at ½ while confidence sits at 1 — permanently half-warranted. [dynamics excont]
- No villain: policies optimal given beliefs, conjectures confirmed, no priced question (B̂ = 0 — no token misfits). Forgiving demand protects the consensus.
- SCUE preview in plain words: everyone lives in a Bayesian world again — that is the problem.

Beats (ending 2 — the knife edge, β < 1):
- Tiny change: customers withhold value when misserved (β < 1). First off-diagonal period under pooled play: payoff β/2 where the theory said ½. [C¶3]
- β/2 does more than refute: it uniquely fingers the OTHER architecture as preferred (a ½ payoff would have left "preferred" vs "neutral" open). [C¶3 — subtle, keep]
- One number does three jobs at once: dissonance returns, the question reprices (B̂ > 0), and the row/column ambiguity dies (the off-diagonal reveal separates the worlds). [C¶3]
- The trap is a knife edge of perfectly forgiving demand; the plan's line to hit: what demand withholds from the firms, their epistemics receives as evidence — destroyed value 1−β IS the corrective signal.

Beats (ending 3 — persistence, β < 1):
- Asymmetric configuration: firm 1 row-refined, plays the truth; firm 2 still coarse, plays one architecture everywhere.
- Play: firms differentiate at the two configurations of the row firm 2 misserves — firm 1 wins both; pool on firm 2's correct row — ½ each. Averages: firm 1 (1+1+½+½)/4 = ¾; firm 2 (0+0+½+½)/4 = ¼. Permanent. [C¶4]
- Firm 2 is genuinely dissonant, not merely wrong: its record kills all three constant theories (differentiated losses kill its own architecture's theory; pooled ½ kills the opposite theory, which predicts β/2 there; the losses kill neutrality). [C¶4]
- Its question is priced: B̂₂ = ½ (same fine-1/current-0 pattern as Act 3 validation). But stasis holds iff cost exceeds hoped value: γ₂ > λ₂·B̂₂ along the whole continuation (record-uniform sufficient condition: γ₂ > λ₂·T·payoff-range). Rational, permanent, ¼-earning stasis. [C¶4; dynamics excont]
- Meanwhile firm 1: B̂₁ = 0 → the truth-holder rationally never inquires again — permanent incomplete awareness on top, no cost.
- Closing sweep: three endings = the paper's terminal taxonomy (answered-and-inert / concealed trap / priced-out stasis + enlightened inertia from Act 3) → Table 2, §10. Heterogeneity — different languages, theories, payoffs — from identical firms and one shared market, before any prior existed.

Numbers: ½-forever trap; β/2 vs predicted ½; withheld 1−β; ¾ vs ¼; B̂₂ = ½; stasis condition γ₂ > λ₂B̂₂ (sufficient: γ₂ > λ₂T·range); B̂₁ = 0.

Constructs previewed → sections:
- SCUE, dissonant stasis, absorbing configuration → §10 (`def:scue`, `def:stasis`, `thm:absorption`)
- persistence two channels → §10 (`prop:persistence`)
- exposure mechanisms: strategic variety vs demand punishment → §6/§10
- forgiving-demand knife edge → §10 dynamics excont + §11 testable implication (2)

Arithmetic constraints:
- Trap requires BOTH technologies to return column — narrate as one possible run of the coin flips, not the destined ending.
- Knife-edge identification needs β/2 ≠ ½ strictly — the whole reveal argument evaporates at β = 1. "Even slightly punishing" is load-bearing.
- ¾–¼ needs uniform configuration frequencies; don't drop the "equally likely" from Act 1.
- Stasis is a PARAMETER REGIME (γ₂ high enough vs λ₂B̂₂), not a consequence of the payoffs — one clause, or readers think ¼ forever is automatic.
- β = 1 variant of the persistence configuration behaves differently (one-switch-then-dissonance or inertia; no oscillation) — [C¶4 end]; probably OMIT from §2 for budget; §10 keeps it.

---

## Reader stumble points (example-wide)

- Firms never observe configurations, only (own action, rival action, own payoff); analyst labels s_rc are ours, not theirs. Every "the firm saw s_00" formulation is a category error the section must dodge without formal apparatus.
- Coarse awareness = ONE category; "perceiving your category" is vacuous until refinement — blindness, not information.
- Rival's action IS observed (part of the consequence) — otherwise the loss stories don't identify anything.
- θ^n (neutral) is the forgettable third theory; its on-screen death in Act 1 is required for dissonance.
- Determinism does real work everywhere (exact refutation; token→mechanism pinning; exact leverage; zero false alarms). One early clause that "in this market, one contradiction is proof" prevents repeated confusion; general stochastic story is §4–§10's job (Calibration Convention).
- Recoding: after refinement the firm CAN re-sort its memories under the new distinction — silently assumed in Acts 3–4; a half-clause helps.
- "Preferred architecture" ≠ "winning firm": at pooled-wrong play both firms hold the market at β/2 — nobody visibly loses to a rival, which is why only demand (β < 1) can expose it.
- Firm 2's one-step jump to full awareness after Act 5 inquiry (both column cells split) — only if the author wants it; else omit.

## Excont shrink map (Session 3B executes, ~60% cuts into pointers back to §2)

| Block (current location, line refs as of c1b210c) | Overlap with §2 | Survives locally |
|---|---|---|
| §5 bayesian excont (~l.602) | Act 1 zero-normalizer death | tie to `prop:no-emergence` + stochastic contrast |
| §6 dissonance excont (~l.700) | Act 1 nearly whole | dominance-threshold formula pointer (C¶1), exposure/concealment tie to `def:exposure` |
| §7 inquiry excont (~l.853) | Act 2 nearly whole | coupling detail for `thm:nonidentification`, complexity-ordering formalities |
| §8 economics excont (~l.1051) | Act 3 whole arc | grouping/Θ_i(g) formal walk-through, transparency remark tie (`rem:certification`), λ/γ election restated formally |
| §9 pivot excont (~l.1167) | Act 4 whole arc | reflective-assessment formal setup, `cor:self-audit` singleton-partition point |
| §10 dynamics excont (~l.1322) | Act 5 all three endings | stasis inequality display, β=1 continuation analysis, routes-out sentence |

Detailed computations stay in Appendix C untouched.

## Numbers §2 must preview (single checklist)

β=1 baseline; payoffs 1/0, ½/½, β/2 · dominance = belief asymmetry at β=1 [C¶1] · two diagonal periods, (1,0) and (0,1) · three constant theories die · 15/11/4 partitions [inquiry excont] · row/column fork, coin flip [inquiry excont] · per-token ½ vs 0, L_fine ½, L_cur 0, B̂ = ½ both firms [C¶2] · λ·½ ≥ γ election · κ ≶ ½ inertia threshold [economics excont] · validation B̂₁ = 0 vs B̂₂ = ½ [C¶2] · Coh 1, W ½, gap +½ [pivot excont] · off-diagonal observation resolves; pooled play nondiagnostic [pivot excont] · trap: ½ each forever [C¶3] · knife edge: β/2 vs ½, withheld 1−β [C¶3] · persistence ¾ vs ¼ [C¶4] · stasis γ₂ > λ₂B̂₂ [C¶4]
