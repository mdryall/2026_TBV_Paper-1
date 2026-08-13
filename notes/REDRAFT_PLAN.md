# Questions Before Priors — Redraft Plan

## Current source of truth

    paper/tbv_mdr_GPTedit-05.tex

This file is the sole authoritative manuscript until the author explicitly
promotes a successor.

## Editorial objective

Revise the manuscript without redesigning its basic architecture.

The revision should:

- correct identified mathematical and probability-theory issues;
- improve notation and formal consistency;
- ensure narrative claims do not exceed the mathematics;
- preserve the pre-Bayesian focus:
  unawareness -> dissonance -> inquiry -> refinement -> return to Bayes;
- sharpen the contribution to the Theory-Based View;
- foreground the paper's principal AHA results.

## Signature findings to preserve and sharpen

1. Directed but underdetermined theory generation:
   experience can identify a defect and constrain a repair without identifying
   the correct new representation.

2. The value of a question before its answers are representable:
   inquiry can be economically valuable because a yet-unnamed distinction may
   change action.

3. Generation and warrant are distinct:
   evidence that generated a truth-blind representation cannot simply be
   counted again as independent validation of that representation.

4. Persistent strategic heterogeneity can originate before priors:
   different question histories and inquiry paths can generate different
   causal languages, theories, actions, and performance.

The Bayesian-boundary and absorption results are important supporting
architecture rather than the primary headline contributions.

## Branch roadmap

### B1 — Evidence Process & Detection Mathematics

Status: COMPLETE

Completed 2026-08-12: mathematical audit, approved implementation, and targeted
post-implementation verification completed --- `B1 IMPLEMENTATION: PASS`.

Repair and verify:

- Lemma 6.2 legacy-evidence false-alarm bound;
- the log-growth argument in its proof;
- conditional Ville inequality treatment;
- Proposition 10.10 stochastic versus deterministic cases;
- Appendix A mixture construction and divergence terminology;
- any necessary propagation into exposure and absorption results.

Exit condition:
the evidence process, test-consistency results, exposure results, and capacity
results form one mathematically consistent package.

### B2 — Formal Hygiene & Notational Architecture

Status: COMPLETE

Completed 2026-08-13: manuscript-wide formal-hygiene and notation audit,
approved implementation, targeted post-implementation verification, final
propagation verification, and settled compilation completed --- final result:
`PASS`.

Address:

- remove drafting residue including WORKING HERE;
- repair local textual/formal errors;
- clarify the epistemic status of rho in subjective valuation;
- distinguish reference posterior from acting belief consistently;
- remove the repair-test / n-bar contradiction;
- conduct a global notation-consistency check.

Exit condition:
every symbol and probabilistic object has one clear role and no drafting residue
remains.

### B3 — The Value of a Question

Status: COMPLETE

Completed 2026-08-13: approved implementation and post-implementation review
completed --- final result: `PASS`.

Stress-test deliberative leverage B-hat.

Determine whether the current benchmark can price value available through an
ordinary current-language action correction rather than value attributable to
a genuinely finer distinction.

Do NOT alter Definition 8.3 merely because this issue appears in the plan.
First analyze the issue and obtain explicit author approval for any substantive
change.

If a revision is approved, verify its effect on:

- Proposition 8.4;
- the running example;
- absorption;
- dissonant stasis;
- persistence.

Exit condition:
B-hat measures the intended value of acquiring a finer representation rather
than value already available without insight.

### B4 — Warrant, Confidence & Insight

Status: COMPLETE

Completed 2026-08-13: approved implementation, formal correction, and final
post-implementation review completed --- `B4 POST-IMPLEMENTATION REVIEW: PASS`.

Align all claims with Theorem 9.2.

In particular:

- preserve the conditional-independence/double-counting result;
- do not assume the general warrant gap is positive unless proved;
- distinguish a signed warrant gap from overconfidence;
- sharpen the interpretation of "the insight is not evidence";
- verify Corollary 9.3 and downstream claims.

Exit condition:
every warrant/confidence claim is exactly supported by the formal result.

### B5 — Dissonance, Questions & Scope of Generativity

Status: PENDING / NOT BEGUN

Address:

- falsity versus on-path misspecification in Remark 5.2;
- the scope of dissonance as a source of questions for intelligence;
- the distinction between modeling the conditions, direction, product, and
  price of insight versus deriving the conscious creative act;
- the fixed-Theta and finite-S boundary.

Exit condition:
the manuscript makes the strongest defensible pre-Bayesian claim without
claiming to derive semantic creativity itself.

### B6 — Strategic Dynamics & Claim Audit

Status: PENDING

Audit general claims concerning:

- winner/loser inquiry incentives;
- strategic variety;
- environmental harshness;
- concealment;
- diagnostic environments;
- shared false theories;
- persistent performance differences.

Distinguish general propositions from mechanisms or results established only in
the running example.

Exit condition:
no strategic narrative claim exceeds its mathematical support.

### B7 — Contribution Architecture / AHA Pass

Status: PENDING

Revise the abstract, introduction, statement of contribution, discussion, and
conclusion so the signature findings dominate the exposition.

Demote mathematical scaffolding from headline status where appropriate.

Clarify the contribution relative to existing Theory-Based View work.

Exit condition:
a reader can identify the paper's distinctive contribution and principal
results directly from the front matter.

### B8 — Whole-Manuscript Integration Audit

Status: PENDING

Perform a complete final audit of:

- mathematical statements and proofs;
- notation;
- definitions and assumptions;
- running-example computations;
- labels and cross-references;
- theorem-to-narrative correspondence;
- abstract/introduction/discussion/conclusion consistency;
- compilation.

Exit condition:
PASS only if no mathematical, notational, internal-consistency, or
theorem-to-narrative blockers remain.

## Branch discipline

Branches diagnose and propose changes.

A substantive change to notation, definitions, assumptions, propositions,
theorems, or modeling architecture requires explicit author approval before
implementation.

After an approved branch changeset is implemented and verified, the author may
promote a new source-of-truth manuscript version.

Do not begin a downstream branch from an unapproved or unpromoted substantive
change.
