---
marp: true
paginate: true
math: katex
size: 16:9
footer: Michael D. Ryall  |  Questions Before Priors  |  2026
---

<style>
/* ════════════════════════════════════════════════════════════════
   RYALL MARP THEME  —  based on Metropolis Beamer
   Font paths assume this file lives in the same folder as fonts/
   If your .md file is in a subfolder, change to ../fonts/
   ════════════════════════════════════════════════════════════════ */

/* ── Font Loading ─────────────────────────────────────────────── */
@font-face {
  font-family: 'NotoSans';
  src: url('fonts/NotoSans-Regular.ttf');
  font-weight: 400; font-style: normal;
}
@font-face {
  font-family: 'NotoSans';
  src: url('fonts/NotoSans-Bold.ttf');
  font-weight: 700; font-style: normal;
}
@font-face {
  font-family: 'NotoSans';
  src: url('fonts/NotoSans-Italic.ttf');
  font-weight: 400; font-style: italic;
}
@font-face {
  font-family: 'NotoSans';
  src: url('fonts/NotoSans-BoldItalic.ttf');
  font-weight: 700; font-style: italic;
}
@font-face {
  font-family: 'Montserrat';
  src: url('fonts/Montserrat-Regular.ttf');
  font-weight: 400;
}
@font-face {
  font-family: 'Montserrat';
  src: url('fonts/Montserrat-Bold.ttf');
  font-weight: 700;
}
@font-face {
  font-family: 'Inconsolata';
  src: url('fonts/Inconsolata.otf');
}

/* ── Base slide ──────────────────────────────────────────────── */
section {
  font-family: 'NotoSans', sans-serif;
  background-color: #ffffff;
  color: #23373B;
  font-size: 18px;
  padding: 50px 64px 56px 64px;
}

/* ── Slide title (h1 = \frametitle) ──────────────────────────── */
h1 {
  font-family: 'NotoSans', sans-serif;
  font-weight: 700;
  font-size: 1.25em;
  color: #23373B;
  border-bottom: 3px solid #EB811B;
  padding-bottom: 6px;
  margin-top: 0;
  margin-bottom: 0.6em;
}

/* ── Footer and page number ──────────────────────────────────── */
footer {
  font-size: 0.6em;
  color: #999999;
  bottom: 12px;
  left: 64px;
}
section::after {
  font-size: 12px;
  color: #EB811B;
  font-weight: 700;
  bottom: 12px;
  right: 24px;
}

/* ── Lists ───────────────────────────────────────────────────── */
ul, ol { padding-left: 1.4em; margin: 0.1em 0; }
li { margin-bottom: 0.3em; }
ul ul, ol ul, ul ol { margin-top: 0.15em; font-size: 0.93em; }
ul ul ul { font-size: 0.91em; }

/* ── Tables ──────────────────────────────────────────────────── */
table {
  border-collapse: collapse;
  margin: 0.6em auto;
  font-size: 0.88em;
}
th {
  border-bottom: 2px solid #EB811B;
  padding: 4px 12px;
  font-weight: 700;
  color: #23373B;
  text-align: center;
}
td {
  padding: 3px 12px;
  border-bottom: 1px solid #dddddd;
  text-align: right;
}
td:first-child, th:first-child { text-align: left; }

/* ── Code / monospace ────────────────────────────────────────── */
code { font-family: 'Inconsolata', monospace; font-size: 0.9em; }
pre  { font-family: 'Inconsolata', monospace; font-size: 0.85em;
       background: #F4F4F4; padding: 10px 14px; border-radius: 4px; }

/* ── Blockquote = math-safe box (default: blue / definition) ─── */
blockquote {
  border-left: 4px solid #0277BB;
  background: #F0F7FF;
  padding: 8px 16px;
  margin: 10px 0;
  border-radius: 0 4px 4px 0;
}
blockquote p { margin: 0.2em 0; }

/* ── Alert text ──────────────────────────────────────────────── */
.alert { color: #EB811B; font-weight: 700; }

/* ── Two-column layout ───────────────────────────────────────── */
.columns {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 32px;
  align-items: start;
}
.columns-70-30 {
  display: grid;
  grid-template-columns: 70% 30%;
  gap: 24px;
  align-items: start;
}
.columns-60-40 {
  display: grid;
  grid-template-columns: 60% 40%;
  gap: 24px;
  align-items: start;
}

/* ════ SLIDE CLASSES ══════════════════════════════════════════ */

/* ── Title slide ─────────────────────────────────────────────── */
section.title-slide {
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  padding-bottom: 70px;
}
section.title-slide footer { display: none; }
section.title-slide::after { display: none; }
section.title-slide h1 {
  font-family: 'Montserrat', sans-serif;
  font-size: 1.55em;
  line-height: 1.3;
  color: #23373B;
  border: none;
  border-left: 6px solid #EB811B;
  padding-left: 20px;
  margin-bottom: 0.5em;
}
section.title-slide p {
  padding-left: 26px;
  margin: 0.15em 0;
  color: #555555;
}

/* ── Section divider slide ───────────────────────────────────── */
section.section-slide {
  background-color: #23373B !important;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
  padding-left: 80px;
}
section.section-slide footer { display: none; }
section.section-slide::after { display: none; }
section.section-slide h1 {
  font-family: 'Montserrat', sans-serif;
  color: #ffffff;
  font-size: 1.9em;
  line-height: 1.35;
  border: none;
  border-left: 6px solid #EB811B;
  padding-left: 20px;
  margin: 0;
}

/* ── Standout / interstitial slide ──────────────────────────── */
section.standout {
  background-color: #23373B !important;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}
section.standout footer { display: none; }
section.standout::after { display: none; }
section.standout h1 {
  color: #ffffff;
  font-family: 'Montserrat', sans-serif;
  font-size: 2.6em;
  border: none;
  text-align: center;
}

/* ── Image-centered slide ────────────────────────────────────── */
section.img-center {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
}

/* ── Proposition slide: blockquote in orange ─────────────────── */
section.prop blockquote {
  border-left: 4px solid #EB811B;
  background: #FFF8F0;
  border-radius: 0 4px 4px 0;
}

/* ── Example/theorem slide: blockquote in green ─────────────── */
section.example blockquote {
  border-left: 4px solid #14B03B;
  background: #F0FFF4;
  border-radius: 0 4px 4px 0;
}

/* ── Font-size modifiers ─────────────────────────────────────── */
section.small  { font-size: 16px; }
section.xsmall { font-size: 14px; }
</style>

<!-- ═══════════════════════════════════════════════════════════
     SLIDE 1: TITLE
     ═══════════════════════════════════════════════════════════ -->

<!-- _class: title-slide -->
<!-- _paginate: false -->

# Questions Before Priors:<br>Causal Dissonance, Insight, and the Origin of Strategic Theories

**Michael D. Ryall**

Florida Atlantic University

[Venue] &nbsp;·&nbsp; 2026

---

<!-- ═══════════════════════════════════════════════════════════
     SLIDE 2: MOTIVATION
     ═══════════════════════════════════════════════════════════ -->

# Where do strategic theories come from?

- **The theory-based view:** economic actors are theorists — causal accounts of value creation direct what managers notice, test, and do *(Felin & Zenger 2017; Strategy Science 2024 special issue)*

- **A decade of progress on *holding* a theory:**
  - theory-guided experimentation and search *(Camuffo et al.; Chavda–Gans–Stern)*
  - theories as awareness advantages earning resources and rents *(Ehrig–Zenger)*
  - field evidence that theorizing pays *(Camuffo et al. 2020, and successors)*

- **But every formal model conditions on the theory being present** — as a menu to select from, a given conjecture, or a given awareness advantage

- The *origin* step is documented empirically *(Ott & Hannah 2024)* and named as the field's open analytical problem

<br>

**Today:** <span class="alert">a formal model of the step before the priors.</span>

---

<!-- ═══════════════════════════════════════════════════════════
     SLIDE 3: UTAH CALLBACK
     ═══════════════════════════════════════════════════════════ -->

# A promise made in January 2025

<div class="columns">
<div>

**Then — speculation** *(the Utah talk)*

- Lonergan's *Insight*: experience → question → understanding → judgment → decision
- "Managers transcend pattern recognition when theorizing"
- The pre-Bayesian challenge: theory generation is a black box
- Closing slide: *"Formal linchpin: directed awareness — insight as pivot to new awareness states"*
- What was missing: **the mathematics**

</div>
<div>

**Now — theorems**

- Dissonance: the *detector* of a broken causal language
- Directed inquiry: what any answer must accomplish
- The price of a question — computable before its answers are conceivable
- Warrant: what the generating evidence does *not* license
- Equilibrium: when everyone lives in a Bayesian world

</div>
</div>

<br>

The structure of that talk survives intact. Today it has definitions, propositions, and proofs.

---

<!-- ═══════════════════════════════════════════════════════════
     SLIDE 4: WHY NOT BAYES
     ═══════════════════════════════════════════════════════════ -->

# Why Bayesian machinery cannot be the answer

Two boundary facts:

- **No emergence.** Conditioning reweights a represented space; it cannot enlarge it. No sequence of updates makes an unrepresented causal distinction available for belief or action.

- **The posterior is self-sealing** *(Berk 1966)*. When every represented theory is false, the posterior concentrates on the *least wrong* one — the agent grows **more confident**, not alarmed. Model failure is not an event in the agent's algebra.

<br>

- The economics of growing awareness *(Karni–Vierø; Schipper)* disciplines belief revision **after** expansion — but the expansion itself arrives exogenously

- So two objects are missing, and both are non-Bayesian:
  - a <span class="alert">detector</span> of representational failure
  - a <span class="alert">generator</span> of repairs — directed, costly, fallible

---

<!-- ═══════════════════════════════════════════════════════════
     SLIDE 5: THE CHAIN
     ═══════════════════════════════════════════════════════════ -->

# This paper: the full loop

$$\text{dissonance}\;\longrightarrow\;\text{inquiry}\;\longrightarrow\;\text{refined awareness}\;\longrightarrow\;\text{new models}\;\longrightarrow\;\text{Bayesian judgment}$$

- Experience **rejects every expressible theory** — dissonance, the detector Bayes lacks
- Rejection **localizes a question** without naming any answer
- A costly, fallible, truth-blind technology **may produce a new distinction**
- A bridge prior **rebuilds a probability space**; ordinary updating resumes
- All of it embedded in strategic interaction: **theories cause actions, actions cause evidence**

<br>

**Back end:** Kalai–Lehrer (1993) / Ryall (2003) — subjective rationality, self-confirming play.
This model *nests* them: hold awareness fixed and you recover the fixed-language world.

**The new part is the front end:** the language itself is endogenous.

---

<!-- ═══════════════════════════════════════════════════════════
     SLIDE 6: AGENDA
     ═══════════════════════════════════════════════════════════ -->

# Agenda

1. **A four-state laboratory** — two firms, four customer states; every object computed exactly

2. **The general model** — the same objects at full generality: mechanisms, tests, judged updating

3. **Key results** — pricing questions, the warrant theorem, epistemic absorption, persistence

4. **What it buys the theory-based view**

---

<!-- ═══════════════════════════════════════════════════════════
     SLIDE 7: SECTION DIVIDER — PART I
     ═══════════════════════════════════════════════════════════ -->

<!-- _class: section-slide -->

# Part I<br>A four-state laboratory

---

<!-- ═══════════════════════════════════════════════════════════
     SLIDE 8: SETUP
     ═══════════════════════════════════════════════════════════ -->

# The laboratory

<div class="columns-60-40">
<div>

- Two firms; unit market; product **architectures** $A_i=\{0,1\}$
- Four **customer states**, arriving uniformly
- Three **causal mechanisms** the firms can conceive:
  - $\theta^0$: architecture 0 preferred
  - $\theta^1$: architecture 1 preferred
  - $\theta^n$: architecture neutral
- Payoffs (winner-take-all market):
  - differentiate → preferred architecture wins: $(1,0)$
  - pool on the preferred one → split: $(\tfrac12,\tfrac12)$
  - pool on the wrong one → split $\beta$: $(\tfrac{\beta}{2},\tfrac{\beta}{2})$
  - neutral state → $(\tfrac12,\tfrac12)$ always
- Baseline today: $\beta=1$ (perfectly forgiving demand)

</div>
<div>

|  | $c=0$ | $c=1$ |
|:---|:---:|:---:|
| $r=0$ | $s_{00}$ | $s_{01}$ |
| $r=1$ | $s_{10}$ | $s_{11}$ |

<br>

**The objective truth** — the *row law*:

$$\tau(s_{rc})=\theta^{r}$$

Rows are causally relevant.
Columns are noise.

*Nobody knows this.*

</div>
</div>

---

<!-- ═══════════════════════════════════════════════════════════
     SLIDE 9: AWARENESS
     ═══════════════════════════════════════════════════════════ -->

# Awareness: the language a firm can think in

- A firm's **awareness partition** collects the customer distinctions it can use — in theories, in beliefs, in policies

- An awareness cell is an implicit **causal claim**: *"these customers are alike"*

- **Expressible theories** assign one mechanism per cell

- Both firms start coarse — one cell, $\{S\}$ — so only three theories are thinkable:

$$M(\mathcal P^0)=\{m^0,\;m^1,\;m^n\}\qquad\text{(constant assignments)}$$

> <span style="font-weight:700; color:#0277BB;">The key epistemic condition</span>
>
> The true row law is not among them. It is not *improbable* — it is **inexpressible**.
> Unawareness $\neq$ probability zero: the firm cannot name it, bet on it, or condition a policy on it.

---

<!-- ═══════════════════════════════════════════════════════════
     SLIDE 10: DIFFERENTIATION
     ═══════════════════════════════════════════════════════════ -->

# Private beliefs → differentiated commitments

- Firms hold private priors over $\{m^0,m^1,m^n\}$ — **heterogeneous**: firm 1 leans toward $\theta^0$, firm 2 toward $\theta^1$

- Simple dominance calculation: architecture $a$ is strictly dominant when

$$p^{a}\;>\;(2-\beta)\,p^{a'}\qquad\text{(at }\beta=1\text{: plain belief asymmetry)}$$

- So the firms commit for the product generation: **firm 1 offers 0 everywhere, firm 2 offers 1 everywhere**

<br>

- Differentiated play is the market running an experiment **nobody designed**
- Neither firm can target "the informative state" — they cannot describe any state

---

<!-- ═══════════════════════════════════════════════════════════
     SLIDE 11: DISCOVERY & DISSONANCE
     ═══════════════════════════════════════════════════════════ -->

# The discovery generation

| Episode | Actions $(a_1,a_2)$ | Payoffs | Revealed |
|:---|:---:|:---:|:---:|
| customer at $s_{00}$ | $(0,1)$ | $(1,0)$ | architecture 0 wins here |
| customer at $s_{11}$ | $(0,1)$ | $(0,1)$ | architecture 1 wins here |

- $m^0$ fails the second episode; $m^1$ fails the first; $m^n$ predicted $\tfrac12$ at both
- **No expressible theory fits the record.** The active set is empty; Bayes' denominator is zero.

> <span style="font-weight:700; color:#0277BB;">Causal dissonance</span>
>
> Every expressible theory is rejected. The question has a **determinate defect but no determinate answer**: *what difference between these customers explains the reversal?*
>
> The posterior is not wrong. It is *gone*.

---

<!-- ═══════════════════════════════════════════════════════════
     SLIDE 12: CONCEALMENT
     ═══════════════════════════════════════════════════════════ -->

# What if they had pooled?

- Same architecture at both states → each firm earns $\tfrac12$ at every episode

- That outcome is consistent with **all three** constant theories → no dissonance, ever

- The coarse language **survives its own evidence indefinitely** — nothing marks it as broken

<br>

**Exposure of a broken language has exactly two sources:**

1. <span class="alert">Strategic variety</span> — rivals acting differently *inside your categories*
2. <span class="alert">Environmental harshness</span> — demand punishing uniform misservice observably

<br>

Hold that thought: at $\beta = 1$, source 2 is switched off. Everything today runs on source 1 — until the knife-edge slide.

---

<!-- ═══════════════════════════════════════════════════════════
     SLIDE 13: RESTORATION & DIRECTION
     ═══════════════════════════════════════════════════════════ -->

# Inquiry: directed, but not determined

**What must any answer accomplish?** A strict refinement of awareness whose cells are *coherent* — each cell admits a single mechanism consistent with the recoded record.

- Four states have **15** partitions
- Every restorative refinement must separate $s_{00}$ from $s_{11}$
- Exactly **4** are minimally restorative:

| Candidate | Cells | Complexity |
|:---|:---:|:---:|
| rows | $\{s_{00},s_{01}\},\{s_{10},s_{11}\}$ | 1 coordinate |
| columns | $\{s_{00},s_{10}\},\{s_{01},s_{11}\}$ | 1 coordinate |
| isolate $s_{00}$ | $\{s_{00}\},\{\text{rest}\}$ | 2 coordinates |
| isolate $s_{11}$ | $\{s_{11}\},\{\text{rest}\}$ | 2 coordinates |

- A factor-seeking (simplicity-filtered) technology produces **rows or columns** — and there, the evidence goes silent: $15 \to 4 \to 2 \to$ <span class="alert">?</span>

---

<!-- ═══════════════════════════════════════════════════════════
     SLIDE 14: NONIDENTIFICATION
     ═══════════════════════════════════════════════════════════ -->

<!-- _class: prop -->

# The row world and the column world

Define the **column world**: $\tau'(s_{rc})=\theta^{c}$. It agrees with the row world at $s_{00}$ and $s_{11}$ — the two worlds generate **identical records**.

> <span style="font-weight:700; color:#EB811B;">Proposition (Observational nonidentification)</span>
>
> No truth-blind inquiry rule formulates correctly in both worlds. A randomized truth-blind rule succeeds, worst case, with probability at most $\tfrac12$.

> <span style="font-weight:700; color:#EB811B;">Proposition (The price of robustness)</span>
>
> A language sufficient for *both* worlds is the full partition into singletons — every distinction the state space can carry.

**Fallibility is the price of economy.** An insight process that does not brute-force every distinction must be capable of being wrong. Whichever factor arrives, its unique consistent theory **extrapolates confidently to the two unlabeled states** — and in one of the two worlds, wrongly.

---

<!-- ═══════════════════════════════════════════════════════════
     SLIDE 15: PRICING THE QUESTION
     ═══════════════════════════════════════════════════════════ -->

# Pricing a question you cannot state

At dissonance the posterior is undefined and the answers are unrepresentable. What justifies paying $\gamma$ for inquiry?

- **Leverage** $B$: count the retained episodes where the committed policy played the revealed *loser*; each is worth exactly $\tfrac12$ per recurrence — **against every rival action**
  - rival repeats its winner → your switch converts a loss $(0)$ into a split $(\tfrac12)$
  - rival switches → your switch converts a split $(\tfrac12)$ into a win $(1)$

> <span style="font-weight:700; color:#0277BB;">Participation rule</span>
>
> $B=\tfrac12\cdot|\text{disagreeing episodes}|$. Elect inquiry iff $\;\lambda B\geq\gamma\;$ ($\lambda$: a *delabeled* success weight).
> After discovery: $B_1=B_2=\tfrac12$ — identical leverage from opposite experiences.

- **Answer-invariant:** the same value whichever of the four repairs arrives — the question is priced **without a menu of answers**
- The reasoning is delabeled: *"customers like the ones I lost will recur; whatever distinction inquiry yields would let me act on them"*

---

<!-- ═══════════════════════════════════════════════════════════
     SLIDE 16: ACTION SEPARATION
     ═══════════════════════════════════════════════════════════ -->

# A question's value is action separation — not information

| Record | Residual uncertainty | Leverage $B$ |
|:---|:---:|:---:|
| all episodes pooled | maximal — nothing pinned | $0$ |
| discovery batch | nearly everything pinned | $\tfrac12$ |

- **Rational cessation.** Run a validation generation: row-firm (correct) vs. column-firm (false). Policies differ off-diagonal; the row-firm wins both.
  - Winner's record agrees with its policy everywhere: $B_1=0$ — it **never inquires again**, and its awareness stays incomplete *optimally*
  - Loser's record disagrees twice: $B_2=1$ — dissonance, evidence, and incentive all land on the same firm

<br>

<span class="alert">Sustained success extinguishes the question. Defeat concentrates it.</span>
The natural inquirers in this model are the losers.

---

<!-- ═══════════════════════════════════════════════════════════
     SLIDE 17: WARRANT
     ═══════════════════════════════════════════════════════════ -->

<!-- _class: example -->

# After insight: how much confidence is licensed?

Suppose the column refinement arrives. The recoded record pins a **unique** consistent theory — the new language awards it probability **one**.

Now assess reflectively: candidate worlds $\{\text{row},\text{column}\}$, symmetric prior.

- Restored fit is **guaranteed by construction** — every restorative repair fits the data that generated it. Fit carries no information.

> <span style="font-weight:700; color:#14B03B;">Theorem (The insight is not evidence)</span>
>
> With truth-blind production, conditioning on the insight's arrival adds nothing to the record. Warrant $=\tfrac12$. Coherence $=1$. **Warrant gap $=\tfrac12$.**

- And the *same gap* afflicts the firm that happened to get it **right**: its coherence is also 1, its warrant also $\tfrac12$
- <span class="alert">Unwarranted certainty is not a symptom of error.</span> Early confidence outruns evidence even when true.

---

<!-- ═══════════════════════════════════════════════════════════
     SLIDE 18: SELF-AUDIT & CLOSURE
     ═══════════════════════════════════════════════════════════ -->

# The gap is invisible from inside

- Computing your own warrant gap requires *expressing both candidate worlds*
- By the robustness proposition, that takes the **full partition** — which no minimally-refined firm holds

<br>

**So the overconfidence is invisible from within the representation that produced it.** Warrant must come from outside:

- fresh evidence whose likelihoods differ across the worlds — one differentiated off-diagonal observation closes the gap completely
- an assessor with broader awareness (a board, an investor, a rival)
- a future self, after further refinement

<br>

Pooled observations — in any quantity — close **nothing**.

<span class="alert">Warrant, like leverage, is purchased with differentiated action.</span>

---

<!-- ═══════════════════════════════════════════════════════════
     SLIDE 19: THE TRAP
     ═══════════════════════════════════════════════════════════ -->

# A market that believes its own mistake

Suppose **both** firms acquire the column refinement and become certain of the (false) column theory.

- Each plays the column policy → the firms **pool at every state** → every payoff is $\tfrac12$
- $\tfrac12$ is exactly what their shared theory predicts → **no dissonance, ever**
- No labeled episodes → $B_i=0$ → even a *free, infallible* inquiry technology is declined
- The warrant gap sits at $\tfrac12$ **forever**, under unbounded experience

<br>

- Subjectively optimal. Conjectures confirmed. Wrong at two of four states.
- This is a **self-confirming unawareness equilibrium** with payoff-relevant error — the market's shared false theory protects itself by eliminating the variety that would refute it

---

<!-- ═══════════════════════════════════════════════════════════
     SLIDE 20: KNIFE EDGE
     ═══════════════════════════════════════════════════════════ -->

# The knife edge: demand as epistemologist

Now let $\beta<1$ — misserved customers withhold $1-\beta$ of the unit value.

- First generation containing an off-diagonal state: pooled firms earn $\tfrac{\beta}{2}$ where their theory predicts $\tfrac12$
- The **payoff level itself reveals the label** — dissonance, leverage, and warrant closure arrive *together*

> <span style="font-weight:700; color:#0277BB;">Knife edge</span>
>
> Payoff-relevant self-confirmation exists **iff $\beta=1$**. With any outside option, consistency plus optimality force every recurring state to be correctly served.

- <span class="alert">The destroyed value is the corrective signal</span> — what demand withholds from the firms, their epistemics receives as evidence

- The two corrective forces, completed: **strategic variety** and **demand harshness**. Durable collective error requires the absence of *both*.

---

<!-- ═══════════════════════════════════════════════════════════
     SLIDE 21: SECTION DIVIDER — PART II
     ═══════════════════════════════════════════════════════════ -->

<!-- _class: section-slide -->

# Part II<br>The general model

---

<!-- ═══════════════════════════════════════════════════════════
     SLIDE 22: GENERAL CANVAS
     ═══════════════════════════════════════════════════════════ -->

# The general canvas

- $n$ agents; finite states $s\sim\rho$; per-generation **committed policies**; consequences $x_i$ = everything agent $i$ observes; payoffs $u_i(x_i)$

- **Objective causal system:** elementary mechanisms $\theta:A\to\Delta(X)$; assignment $\tau:S\to\Theta$;

$$F(\cdot\mid s,a)=\tau(s)(a)$$

- **Actions cause consequences.** $F$ is defined at *every* profile, played or not — that is the interventional content. No SCM formalism; micro-models (like the laboratory's customer market) generate mechanisms in examples.

- **Theories = one mechanism per awareness cell.** Why not arbitrary distributions? A saturated class can never be rejected — *coarseness alone cannot produce detectable failure*. A cell is a causal-homogeneity claim; dissonance is evidence of **mechanism heterogeneity inside a represented category**.

- Fixed awareness ⟹ Kalai–Lehrer / Ryall (2003) exactly. The paper endogenizes their hypothesis space.

---

<!-- ═══════════════════════════════════════════════════════════
     SLIDE 23: STATISTICAL DISSONANCE
     ═══════════════════════════════════════════════════════════ -->

# Dissonance becomes statistics

- **Consistency test:** theory $m$ passes if empirical conditionals sit within tolerance $\eta$ (plus vanishing slack) of $m$'s predictions at every visited (cell, profile) pair
- **Active set** = survivors. **Dissonance** = empty. The laboratory is the exact case $\eta=0$.

<br>

- Recall the self-sealing posterior: under misspecification, Bayes gets *confident*, not alarmed
  - the test is therefore a **distinct faculty** — judgment, not understanding
- **Judged updating:** the posterior is restricted to survivors — belief never rides on a rejected theory

> <span style="font-weight:700; color:#0277BB;">Exposure ⟺ dissonance</span>
>
> Under a committed profile, an agent is eventually dissonant (a.s.) **iff** its awareness is exposed: every expressible theory fails somewhere on the visited path. Concealing profiles — the general form of the pooled trap — are exactly what keep false languages alive.

---

<!-- ═══════════════════════════════════════════════════════════
     SLIDE 24: GENERAL PROPOSITIONS I
     ═══════════════════════════════════════════════════════════ -->

<!-- _class: small prop -->

# Direction, fallibility, and price — in general

> <span style="font-weight:700; color:#EB811B;">Restoration is cellwise coherence</span>
>
> A refinement restores expressibility iff every cell admits a single mechanism consistent with its recoded record. Restorations must separate mutually incoherent evidence clusters; minimal restorations are typically **multiple**.

> <span style="font-weight:700; color:#EB811B;">Nonidentification & the price of robustness</span>
>
> Worlds inducing identical record distributions receive identical outputs from any truth-blind technology — none is uniformly correct. Sufficiency for all candidate worlds requires the **join** of their causal partitions: economy of representation ⟹ fallibility.

> <span style="font-weight:700; color:#EB811B;">Participation (answer invariance)</span>
>
> Leverage $B$ is computable from the record alone and **identical across every possible repair**. Elect iff $\lambda B\geq\gamma$. $B>0$ only if some pinned distinction changes the robustly optimal action: questions whose every admissible answer supports current behavior are worthless at any positive cost — *however much model uncertainty remains*.

---

<!-- ═══════════════════════════════════════════════════════════
     SLIDE 25: GENERAL PROPOSITIONS II
     ═══════════════════════════════════════════════════════════ -->

<!-- _class: example -->

# The insight is not evidence — in general

> <span style="font-weight:700; color:#14B03B;">Theorem</span>
>
> With truth-blind production: the selection-adjusted warrant of a new formulation equals the ordinary reflective posterior **on the record alone**. The insight's arrival, and its retrospective success at organizing the experience that produced it, carry zero evidential weight. Among candidate worlds with identical record likelihoods, prior odds are preserved exactly.

> <span style="font-weight:700; color:#14B03B;">Corollary (Self-audit)</span>
>
> Expressing the candidate set requires awareness sufficient for **all** candidates. An agent holding a minimal repair generally cannot formulate the comparison that measures its own warrant gap.

- The boundary, stated once: **everything evidential is in the record; nothing evidential is in the arrival of the insight**
- If production *were* correlated with truth (social transmission from an informed source), arrival would be evidence — truth-blindness is the polar case

---

<!-- ═══════════════════════════════════════════════════════════
     SLIDE 26: SCUE & ABSORPTION
     ═══════════════════════════════════════════════════════════ -->

<!-- _class: small example -->

# When everyone lives in a Bayesian world

> <span style="font-weight:700; color:#14B03B;">Definition (Self-confirming unawareness equilibrium)</span>
>
> (i) policies subjectively optimal; (ii) conjectures confirmed on path; **(iii) no dissonance — the language survives its own evidence; (iv) no priced question — $\lambda_iB_i<\gamma_i$.**
>
> (i)–(ii) are classical. (iii)–(iv) are the new, *epistemic* conditions — and they carry the results.

> <span style="font-weight:700; color:#14B03B;">Theorem (Epistemic absorption)</span>
>
> Almost surely: at most $n(|S|-1)$ refinements; finitely many inquiry elections; and a finite generation after which **no language changes and no inquiry cost is paid** — every agent's epistemic life is Bayesian updating in a fixed language.

- The theorem is about the **death of inquiry**, not the convergence of play (classical, orthogonal, deliberately not claimed)
- One more rest state: **dissonant stasis** — the model is known-broken, but the break moves no decision: <span class="alert">rational anomaly tolerance</span>
- Grain-of-truth reading: refinement endogenously restores Kalai–Lehrer's condition *on the path of play*

---

<!-- ═══════════════════════════════════════════════════════════
     SLIDE 27: PERSISTENCE
     ═══════════════════════════════════════════════════════════ -->

# Why performance differences persist

- Rest configurations can hold **false theories, heterogeneous languages, permanently different payoffs**
  - laboratory instance: row-firm earns $\tfrac34$, coarse rival $\tfrac14$ — forever, when the rival's question is priced below its cost

- Not because an equilibrium concept freezes them — because **the process that would erase them died economically**:
  - no dissonance (concealing play), or
  - no leverage (no action separation), or
  - the question priced below the cost of asking

- In **diagnostic environments** (the general $\beta<1$), payoff-relevant error cannot survive at all

<br>

**Strategic variety before probability:** identical preferences, identical Bayesian competence, same objective world — different *questions* → different languages → different theories → different payoffs.

---

<!-- ═══════════════════════════════════════════════════════════
     SLIDE 28: TAKEAWAYS FOR TBV
     ═══════════════════════════════════════════════════════════ -->

# What this buys the theory-based view

- **Theory generation, formalized** — directed by defects, disciplined by restoration, fallible by necessity. The step every existing formal model assumes is now a model.

- **The value of a question is action separation, not entropy** — rational cessation for winners, concentrated incentive for losers

- **Founders' certainty outruns evidence even when correct** — organizing your own generating experience earns nothing; outside challenge is a *warrant technology*, not just monitoring. (The formal case for "test before you scale.")

- **Markets discipline theories through two channels** — captive demand + consensus ⟹ durable collective error; the deviant entrant is the industry's *epistemic infrastructure*

- **Anomaly tolerance is an equilibrium phenomenon** — broken models persist rationally exactly where their breaks have no leverage

---

<!-- ═══════════════════════════════════════════════════════════
     SLIDE 29: RESEARCH PROGRAM
     ═══════════════════════════════════════════════════════════ -->

# The research program

1. **This paper — questions before priors.** The origin of strategic theories: dissonance, inquiry, insight, warrant, absorption.

2. **From theory to plan.** Commitment under changing awareness: plans as *cached deliberation*; when confirmatory depth makes strategy rationally sticky.

3. **The theory-bearing firm.** How individual insights become shared languages, collective intentions, and an enduring center of agency.

4. **Competing theories and value capture.** Awareness rents, strategic disclosure, induced rival unawareness — joining this front end to the cooperative back end.

<br>

And beneath all of it, the deeper frontier: expanding the **mechanism vocabulary itself** — not just new distinctions, but new *kinds* of causes.

---

<!-- ═══════════════════════════════════════════════════════════
     SLIDE 30: FIN
     ═══════════════════════════════════════════════════════════ -->

<!-- _class: standout -->

# questions — before priors
