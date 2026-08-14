# Questions Before Priors — TBV Paper 1

Formal theory of pre-Bayesian strategic insight: how experience generates directed
causal questions, how a fallible representation-producing technology yields genuinely
new theories, and how strategic action controls the evidence that exposes or protects
false theories. First paper in a multi-paper Theory-Based View agenda. Target:
*Management Science*.

## Layout

| Path | Contents |
|---|---|
| `paper/` | Authoritative manuscript `tbv_mdr_GPTedit-08.tex`, bibliography `MDR_TBV_Paper01.bib`, and matching PDF `tbv_mdr_GPTedit-08.pdf` |
| `notes/` | Current status in `STATUS.md`, live roadmap in `REDRAFT_PLAN.md`, and supporting formal notes |
| `agenda/` | `Questions_Before_Priors.tex` — the research-program design memo (four-paper agenda, no-baked-in checklist, SCM architecture horizon) |
| `literature/own-work/` | Prior Ryall papers and manuscripts feeding the agenda (SCE 2003, causal ambiguity 2009, value capture 2017, unawareness 2022, Ryall–Wilkins, action-theory Appendix A) |
| `literature/tbv/` | TBV and unawareness literature (collect here) |
| `talks/` | Presentation decks (Utah/FAU pre-Bayesian talk, Jan 2025) |
| `archive/` | Superseded idea documents (content consolidated into `agenda/`) |

## Current plan (July 2026)

1. ✅ **Done** — three mechanisms drafted into the 2×2 laboratory
   (`notes/rigorous_four_state_insight_model.tex`, now 28 pp.):
   - **Inquiry-decision layer** (§ Economics of inquiry) — costly elective
     activation; disagreement set L and leverage B = |L|/2 (conjecture-free at
     β = 1); answer-invariance = formal delabeling; participation rule θB ≥ γ;
     action-separation, trap immunity to cheap inquiry, rational cessation /
     loser's leverage.
   - **Bridge prior / judgment** (§ Formulation…judgment) — reflective assessment
     (𝒟, ν); guaranteed-fit lemma; prior preservation under truth-blind
     production; warrant gap G = ½; diagnostic closure; self-audit requires
     complete awareness; permanent gap at the trap.
   - **Outside option** (§ Value destruction) — β-payoffs; generalized dominance
     (threshold p⁰ > (2−β)p¹); demand-side revelation; no payoff-relevant
     self-confirmation for β < 1; knife-edge corollary (trap, gap, leverage lock
     all require β = 1); two sources of diagnosticity.
2. ✅ **Drafted** — `notes/general_model.tex` (14 pp.): Kalai–Lehrer/Ryall-2003
   chassis with n agents, general finite states s, consequences x, elementary
   causal mechanisms Θ, objective assignment τ, F(·|s,a) = τ(s)(a). Theories =
   cell-constant mechanism assignments (the structured class that makes
   stochastic dissonance possible). Statistical tests/active sets; exposure vs
   concealment; cellwise-coherence restoration; general nonidentification and
   robust sufficiency (join); pinned distinctions and leverage as robust lower
   bound; "the insight is not evidence" theorem; SCUE defined as "everyone
   lives in a Bayesian world"; absorption sketch (SCUE vs dissonant stasis /
   rational anomaly tolerance); persistence of performance differences derived
   from process economics; diagnostic environments; full 2×2 mapping table.
   Fulcrum discipline observed: equilibrium subordinate to the
   dissonance → inquiry → awareness → models → Bayes chain.
3. ✅ **First draft assembled** — `paper/tbv_mdr_GPTedit-01.tex` (43 pp. compiled), titled
   "Questions Before Priors: Causal Dissonance, Insight, and the Origin of
   Strategic Theories." Structure: intro (positioned on the verified gap) →
   related literature (TBV / unawareness / causal learning / subjective
   rationality) → model (general, mechanism-based) → Bayesian boundary →
   dissonance → inquiry → economics of inquiry → pivot/warrant → dynamics
   (SCUE = "everyone lives in a Bayesian world") → discussion → appendix
   (absorption sketch + example computations). The 2×2 runs as Example 1
   throughout. Next: author read-through and revision; tighten proofs; decide
   target-journal formatting (Management Science).

## Current manuscript operations

Read `notes/STATUS.md` and `notes/REDRAFT_PLAN.md` before substantive manuscript
work. Build the authoritative manuscript with:

```bash
cd paper
latexmk -pdf tbv_mdr_GPTedit-08.tex
```

## Agenda (papers 2–4)

2. Theory → plan: commitment under changing awareness (C^Plan machinery).
3. The theory-bearing firm: collective intentionality (Ryall–Wilkins).
4. Competing theories and value capture (awareness rents, disclosure).
