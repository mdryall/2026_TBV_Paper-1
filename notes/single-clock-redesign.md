# Single-clock redesign — design note (working spec)

Status: **proposal for review**, July 24 2026. Nothing in the paper is edited yet.
Purpose: replace the generation/episode two-clock timing with a single clock, make
policy inertia and dissonance detection endogenous agent-level objects, and add a
policy switching cost. Pin the design here; then execute the paper in tranches.

Decisions locked with MDR:
- **1(b)** sequential-test formalization of dissonance capacity.
- Switching cost on **policy** change (costly to change strategy); model change and
  policy change are **decoupled** — one may adopt a better model yet keep the old
  policy because switching is not worth its cost.
- Keep inquiry costly, but **do not** state trivial "cost-too-high ⇒ no action"
  results. Costs shape *timing*; insight is in the comparative statics.
- Keep the **capacity-heterogeneity** analysis for now (cuttable later).

Open sub-decisions are flagged inline as **[FORK]**.

---

## 1. Timing: one clock

Periods `t = 1,2,\dots`. There are no generations and no episodes. In period `t`:

1. State `s_t \sim \rho` drawn i.i.d., full support on finite `S`.
2. Agent `i` perceives its awareness cell `C_{\mathcal P_i}(s_t)` (never `s_t`).
3. Agent `i` plays `a_{i,t} = \sigma_i(C_{\mathcal P_i}(s_t))` under its **standing**
   policy `\sigma_i` (a persistent state variable, not re-chosen from scratch).
4. Consequence `x_t` drawn from the mechanism `\tau(s_t)(a_t)`; agent `i` observes
   `(a_t, x_{i,t})` and appends token `(C_{\mathcal P_i}(s_t), a_t, x_{i,t})` to `r_i`.
5. Agent `i` updates the reference posterior `\bar\mu_i` (Bayes on the new token),
   updates its sequential adequacy statistic (§3), and takes at most two costly
   revision actions: a **policy switch** (§4) and/or an **inquiry election** (§5).

The "committed profile / generation" of the old model is replaced by a **stable
stretch**: a maximal run of periods over which every `\sigma_i` is unchanged. Stable
stretches are now *endogenous* (they end when someone switches or inquires), not
imposed. This is the object the statistical results condition on, and it arises the
same way self-confirming-equilibrium results arise — in the limit, play settles.

Terminology: "episode" → "period"; drop "generation" entirely. (Also removes the
OLG connotation MDR flagged.)

---

## 2. What each agent carries (state)

`\xi_i = (\mathcal P_i, r_i, \bar\mu_i, q_i, \sigma_i, \text{sequential stats}, k_i)`
— awareness, record, reference posterior, conjecture, **standing policy**, the
running adequacy statistics of §3, and the failure counter `k_i`. Acting belief
`\mu_i` is derived by judged updating (posterior restricted to the not-yet-rejected
theories). The standing policy is now part of the state precisely because it persists
by inertia.

---

## 3. Dissonance capacity as a sequential test  **[core new object]**

### 3.1 Adequacy region (unchanged in spirit)
Fix a tolerance `\eta \ge 0`. A theory `m` is **adequate** on the current stable
stretch if `\mathrm{TV}(p_i^*(\cdot\mid C,a), \mathrm{marg}_i m(C)(a)) \le \eta` at
every visited pair `(C,a)`. `\eta` is a global modeling primitive (how much misfit
still counts as "the same mechanism"), **not** the capacity parameter.
**[FORK: allow `\eta_i` agent-specific too? Recommend NO — keep `\eta` global, let
`b_i` carry all agent heterogeneity, so capacity has a single clean handle.]**

### 3.2 Sequential detector (replaces the fixed `\bar n`, `w(\cdot)` slack test)
For each expressible theory `m`, maintain a nonnegative **e-process** `E^m_t`
(`E^m_0 = 1`) that is a supermartingale under the null "`m` is adequate," built from
the per-token likelihood ratios against the adequacy region. Concretely, `E^m_t`
accumulates evidence *against* `m`: it stays `O(1)` while `m` fits and grows
exponentially once `m` is genuinely inadequate, at rate equal to a
Kullback–Leibler / Chernoff divergence between the on-path conditional and the
adequacy region. (Standard composite-null e-value construction; the exact kernel is
**[FORK: mixture e-value vs. universal-inference plug-in — recommend mixture, it needs
no auxiliary MLE and gives closed-form rates].**)

The agent **rejects** `m` the first period `log E^m_t \ge b_i`.
The **active set** `\widehat M_i` is the theories not yet rejected.
**Dissonance** = active set empty.

### 3.3 Dissonance capacity `b_i`  **[the agent parameter]**
`b_i > 0` is agent `i`'s **dissonance capacity**: the log-evidence threshold it
requires before abandoning a theory as inadequate.

- **High `b_i`** = tolerant: demands overwhelming evidence, rarely triggers, clings
  to its language, persists.
- **Low `b_i`** = intolerant: triggers on modest misfit, questions often, churns.

Two facts fall out immediately and are the analytical payoff:

- **False-alarm control (Ville's inequality — already used in `prop:rest-points`):**
  `\Pr(\text{ever reject an adequate } m) \le e^{-b_i}` per theory, so
  `\Pr(\text{spurious dissonance}) \le |M(\mathcal P_i)|\, e^{-b_i}`. Higher capacity ⇒
  fewer false alarms. This *replaces* the old genericity-of-`\eta` caveat and the
  finite-sample slack `w(\cdot)` — the anytime-valid guarantee handles optional
  stopping (the agent tests every period) correctly by construction. **Net
  simplification of `def:test` and `lem:test-consistency`.**
- **Detection time under genuine inadequacy:** expected periods to trigger
  `\approx b_i / D`, where `D` is the misfit divergence. So **time-to-dissonance
  scales linearly in capacity and inversely in severity** — the closed form behind
  "average period of stability is a feature of the agent."

Deterministic case (`\eta = 0`): `E^m` jumps to `\infty` on the first
zero-likelihood observation, so rejection is instantaneous for any `b_i` — recovers
the current exact test exactly, capacity-independent, as it should.

---

## 4. Switching cost and the standing policy  **[core new object]**

### 4.1 Primitive
Switching cost `c_i \ge 0` **[FORK: symbol — `c_i` mildly clashes with the example's
column coordinate `c`; alternatives `\chi_i`, `\kappa_i` (now free). Recommend
`\kappa_i`.]**, paid once whenever `\sigma_i` changes at any cell.

### 4.2 (S,s) update rule
Each period the agent computes the belief-optimal policy `\sigma_i^\star` (the argmax
of `eq:subjective-optimality` under the current acting belief and conjecture) — this
computation is **free**; only *acting* on it costs. It switches iff the subjective
per-period payoff gain of `\sigma_i^\star` over the incumbent exceeds a threshold in
`c_i`:

`\;G_i(\sigma_i^\star, \sigma_i \mid \mu_i, q_i) > \theta(c_i).\;`

**[FORK: horizon/amortization.** A one-time cost vs. a payoff *stream* needs a
horizon. Options: (i) myopic — `\theta(c_i)=c_i` treated as a per-period gain
threshold (keeps the paper's no-discounting stance, simplest, still yields an
inaction band); (ii) light discounting `\delta_i`, compare `c_i` to the discounted
gain stream; (iii) compare `c_i` to gain × *expected holding tenure* (endogenous,
circular, avoid). **Recommend (i)** for the core; note (ii) as the natural
robustness pass.]**

The band `G \le \theta(c_i)` is the source of inertia: beliefs drift, the argmax may
flip, but the policy holds until the gain clears the band.

### 4.3 The decoupling — MDR's centerpiece
`\sigma_i^\star` is computed under the *current* belief, which may be **post-inquiry**
(refined language, new theory). If the gain from the newly-optimal policy does not
clear the band, the agent **keeps its old policy while holding the new model**. This
is rational stickiness after enlightenment, and it is a persistence channel *distinct*
from unpriced inquiry:

- Old channel (retained): the *question* is priced below cost — no inquiry, no new
  model. (`\lambda_i \widehat B_i < \gamma_i`.)
- New channel: the model *is* updated, but the *policy change* it recommends is
  priced below `c_i` — so behavior, and hence performance, does not move.

Both feed `prop:persistence`; the second is new and should be stated as such.

### 4.4 Consistency between inquiry value and switching
Inquiry only pays off if the resulting distinction actually changes behavior, which
only happens if the induced switch clears `c_i`. So the deliberative leverage
`\widehat B_i` (§5) must be measured **net of the switching cost** it would trigger —
otherwise the agent could rationally pay `\gamma_i` for a distinction it will never
act on. This is a clean tightening, not a new free parameter, and it keeps §5 honest
without a trivial threshold proposition. **[Detail to work out in T2: whether `c_i`
enters `\widehat B_i` per-group or once per policy change.]**

---

## 5. Inquiry economics, revised and lean

Keep: election at cost `\gamma_i` on dissonance; achievability weight `\lambda_i^{(k)}`
decaying in consecutive failures `k`; participation `\lambda_i^{(k)}\widehat B_i \ge
\gamma_i`. Change:

- Horizon: the `T/|r_i|` normalization in `eq:leverage` loses its `T`. Replace the
  per-generation scaling with a **per-recurrence** (or per-period expected) horizon;
  the running example's numbers are preserved by conditioning on the same events (see
  §8). **[Renormalization detail for T2; the old "rescale `\widehat B` and `\gamma`
  together" remark already anticipates this.]**
- `\widehat B_i` measured net of `\kappa_i` (§4.4).
- **No new headline propositions about cost thresholds.** The costs are plumbing.

---

## 6. Endogenous stability duration (the payoff of the whole change)

A stable stretch for agent `i` ends at the **first passage** of either trigger:

- **argmax exit:** belief drift moves `G_i` past the switching band `\theta(\kappa_i)`;
- **dissonance:** `\max_m \log E^m_t \ge b_i` — the adequacy test fires.

Expected stretch length is therefore a function of `(\eta, b_i, \kappa_i)` and the
environment's severity `D`. Clean comparative statics (to state as results, these are
the *insightful* ones):

- `\uparrow b_i` (capacity) and `\uparrow \kappa_i` (switching cost) ⇒ longer stretches,
  more persistent (possibly false) theories, more tolerated anomaly.
- `\downarrow b_i` ⇒ frequent questioning, but more spurious dissonance
  (`\le e^{-b_i}`) and more inquiry cost paid — a genuine tradeoff, not "low cost ⇒
  more of it."
- Heterogeneity in `(b_i,\kappa_i)` across otherwise-identical agents ⇒ heterogeneous
  terminal languages and payoffs — a **cognitive-style** microfoundation for
  persistence, orthogonal to the awareness-path story already in the paper.

---

## 7. Results: new, enriched, retired

**New**
- *Rational stickiness after enlightenment* (§4.3): known-suboptimal policy held
  because switching is priced out. New clause in `prop:persistence`.
- *Endogenous stability duration* (§6): first-passage characterization; comparative
  statics in `(b_i,\kappa_i,D)`.
- *Capacity and false alarms*: `\Pr(\text{spurious dissonance})\le|M|e^{-b_i}` — a firm
  can rationally churn on noise if `b_i` is low.

**Enriched**
- `rem:anomaly`: second driver of tolerated anomaly — high capacity `b_i` (the agent
  does not even register the misfit as decisive), alongside the existing zero-leverage
  driver.
- `prop:persistence`/discussion: cognitive-style axis added to the awareness-path axis.

**Retired / simplified**
- `\bar n`, `w(\cdot)`, and the genericity-of-`\eta` hypothesis: subsumed by the
  anytime-valid e-process. Fewer moving parts.
- "Commitment / batching" remark: replaced by the endogenous-stretch story.

---

## 8. Claim-by-claim change map

| Current object | Change |
|---|---|
| §3.1 primitives (`generations`/`episodes`) | Single clock `t`; add `b_i`, `\kappa_i` as agent primitives; define standing policy. |
| `ass:commitment` + "statistics/economics meet" remark | Replace with **standing policy + (S,s) switch rule** (§4) and the endogenous-stretch remark. |
| §3.4 on-path conditional `p_i^*` (`Fix a generation…`) | "Fix a stable stretch with stationary profile `\sigma`." Object unchanged. |
| `def:test` (η, `\bar n`, `w`) | Replace with sequential e-process detector + capacity `b_i` (§3). |
| `lem:test-consistency` | Recast in periods; prefix/tail ⇒ pre-/post-switch; the anytime-valid guarantee **strengthens** it and drops the genericity caveat. |
| `def:dissonance` ("end of a generation") | "when the sequential detector rejects all expressible theories." |
| `prop:exposure` | "from some period onward"; false-alarm bound now explicit. |
| `ass:full-support`, judged updating | Unchanged (belief machinery is clock-agnostic). |
| §4 inquiry (restoration, technology, nonidentification) | Clock-agnostic; light wording only. |
| §5 economics (`ass:elective`, `def:leverage` `eq:leverage`, participation) | Drop `T`, renormalize horizon; `\widehat B_i` net of `\kappa_i`; keep lean (§5). |
| `def:scue` | Drop generation language; add "standing policy is a fixed point of the (S,s) rule"; conditions stay asymptotic. |
| `def:stasis`, `rem:anomaly` | Add capacity-driven stasis; second anomaly driver. |
| `ass:regularity` | "across elections"→"across inquiry attempts"; generic-`\eta` clause removed (subsumed). |
| `thm:absorption` | Recount in periods: refinements `\le n(|S|-1)` (same); **switches finite** (beliefs converge, each switch clears `\kappa_i`); elections finite (λ decay); dissonance triggers finite (Ville). Likely **cleaner** than now. |
| `prop:rest-points` | Rest point = no theory rejected **and** no switch clears the band; stickiness clause added. |
| `prop:persistence` + `def:diagnostic` | Add the priced-out-switch channel. |
| Appendix A (`{s_{g,t}}` over `g,t`) | Single index `{s_t}`; couplings unchanged; Ville step reused for the detector. |
| Appendix B / running example (`T=2` discovery `generation`) | "two consecutive periods serving the diagonal states"; add a `\kappa_i` value to illustrate the decoupling (a firm that learns the row law but does not re-differentiate because `\kappa` too high). Exact `\widehat B` numbers preserved. |

---

## 9. Execution tranches (after MDR signs off on this note)

- **T1 — front end:** §3.1 primitives, single clock, standing policy + (S,s) rule,
  sequential detector + `b_i`, `def:dissonance`, `lem:test-consistency`. Compile.
- **T2 — economics:** §5 leverage renormalization, `\widehat B` net of `\kappa_i`,
  participation; the decoupling result. Compile.
- **T3 — dynamics + proofs + example:** `def:scue`, absorption, rest-points,
  persistence, appendix, running example. Compile; full read-through.

Each tranche keeps earlier sections provisional; we expect to revisit §3 once §5–§7
settle (MDR's forward-dependency point).

## 10. Questions still open for MDR
1. `\eta` global vs. `\eta_i` (§3.1) — recommend global.
2. Switching-cost horizon (§4.2) — recommend myopic per-period threshold for the core.
3. Symbols: capacity `b_i`, switching cost `\kappa_i` — OK, or preferred letters?
4. e-value construction (§3.2) — mixture (recommended) vs. universal inference; MDR
   may have a preference given the audience.
