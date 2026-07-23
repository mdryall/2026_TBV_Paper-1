---
marp: true
paginate: true
math: katex
size: 16:9
footer: Author Name  |  Venue  |  Date
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
     SLIDE 1: TITLE SLIDE
     _class: title-slide      disables footer and page number
     _paginate: false          (same effect on page number)
     ═══════════════════════════════════════════════════════════ -->

<!-- _class: title-slide -->
<!-- _paginate: false -->

# Presentation Title Goes Here

**Author Name**$^1$ &nbsp; and &nbsp; **Co-Author Name**$^2$

$^1$ University One &nbsp;&nbsp; $^2$ University Two

Month, Year

---

<!-- ═══════════════════════════════════════════════════════════
     SLIDE 2: AGENDA / TABLE OF CONTENTS
     Plain content slide — just use an ordered list
     ═══════════════════════════════════════════════════════════ -->

# Agenda

1. First section topic
2. Second section topic
3. Third section topic

---

<!-- ═══════════════════════════════════════════════════════════
     SLIDE 3: SECTION DIVIDER
     _class: section-slide     dark background, left orange bar
     Use <br> for line breaks in the heading
     ═══════════════════════════════════════════════════════════ -->

<!-- _class: section-slide -->

# First section<br>topic title

---

<!-- ═══════════════════════════════════════════════════════════
     SLIDE 4: STANDARD CONTENT — bullets, nesting, alert text
     ═══════════════════════════════════════════════════════════ -->

# Standard content slide

- **Top-level bold point** — context here
  - Second-level item
  - Another second-level item
    - Third-level item (use sparingly)

- **Another top-level point**
  - Sub-item with <span class="alert">alert/emphasis text</span>
  - Sub-item with *italic* or **bold** inline

- Plain bullet without bold lead-in

---

<!-- ═══════════════════════════════════════════════════════════
     SLIDE 5: STANDOUT / INTERSTITIAL
     _class: standout     centered white text on dark background
     Good for: case labels, dramatic pauses, section pivots
     ═══════════════════════════════════════════════════════════ -->

<!-- _class: standout -->

# a key point or case label

---

<!-- ═══════════════════════════════════════════════════════════
     SLIDE 6: INLINE AND DISPLAY MATH
     math: katex in frontmatter enables this
     Inline:  $...$ or \(...\)
     Display: $$...$$ on its own line
     ═══════════════════════════════════════════════════════════ -->

# Slide with mathematics

Inline math flows naturally: the expected value is $\mathbb{E}[\pi] = \sum_{i} p_i \pi_i$.

Display equation on its own line:

$$P(v) = \prod_{j \in N} \rho_j(v_j \mid d_j)$$

Aligned equations use the `aligned` environment inside `$$`:

$$\rho_{j|\hat{a}}(v_j|d_j) \equiv
\begin{cases}
1 & \text{if } v_j = \hat{a} \\[4pt]
\rho_j(v_j|d_j) & \text{otherwise}
\end{cases}$$

Sets, arrows, and operators: $\mathcal{V}, \mathcal{D}_j, \Delta^+(\cdot), \Rightarrow, \leftarrow$

---

<!-- ═══════════════════════════════════════════════════════════
     SLIDE 7: DEFINITION BOX  (blockquote = blue)
     IMPORTANT: always use blockquote (>) for boxes containing
     math. Never use <div> — math will not render inside divs.
     ═══════════════════════════════════════════════════════════ -->

# Slide with a definition box

> <span style="font-weight:700; color:#0277BB;">Definition (Term Name)</span>
>
> The *widget* is **identifiable** if for all models $M'$ satisfying condition $(i)$,
>
> $$f(x) = g(x) \quad \forall x \in \mathcal{X}$$
>
> and condition $(ii)$ also holds with $A_i \rightarrow V_j$.

Text below the box continues normally, with inline math like $\mathbb{R}$ working fine.

---

<!-- ═══════════════════════════════════════════════════════════
     SLIDE 8: PROPOSITION BOX  (blockquote = orange)
     Requires _class: prop on this slide
     ═══════════════════════════════════════════════════════════ -->

<!-- _class: prop -->

# Slide with a proposition box

> <span style="font-weight:700; color:#EB811B;">Proposition 1</span>
>
> Given model $M$, intervention $\mathbf{do}(a_i)$ is identifiable if and only if
> there is no bi-directed path $A_i \leftarrow U_h \rightarrow V_j$ such that $A_i \rightarrow V_j$.

**Implication 1:** The problematic structure is <span class="alert">special</span> in model space.

**Implication 2:** But it may be quite <span class="alert">common</span> in practice.

---

<!-- ═══════════════════════════════════════════════════════════
     SLIDE 9: EXAMPLE / THEOREM BOX  (blockquote = green)
     Requires _class: example on this slide
     ═══════════════════════════════════════════════════════════ -->

<!-- _class: example -->

# Slide with an example or theorem box

> <span style="font-weight:700; color:#14B03B;">Theorem (Result Name)</span>
>
> Under assumptions 1–3, the equilibrium payoff satisfies $\pi^* \geq \underline{\pi}$
> for all parameter values $\theta \in \Theta$.

Normal text resumes here. You can mix the box with regular bullets:

- First implication of the theorem
- Second implication

---

<!-- ═══════════════════════════════════════════════════════════
     SLIDE 10: TABLE
     Column alignment: | left | center | right |
     Use :---: for center, ---: for right, :--- for left
     ═══════════════════════════════════════════════════════════ -->

# Slide with a table

| Variable | Symbol | Values | $P(\cdot)$ |
|:---|:---:|:---:|---:|
| Agent action | $A$ | $\{0,1\}$ | — |
| Work product | $\Omega$ | $\{0,1\}$ | — |
| Profit | $\Pi$ | $\{0,1\}$ | — |
| Intervention | $\mathbf{do}(a)$ | $\{0,1\}$ | 61.2% |

Note: $\mathbb{E}(\pi) = 61.2\%$ under status-quo distribution.

---

<!-- ═══════════════════════════════════════════════════════════
     SLIDE 11: TWO COLUMNS  (equal split)
     Wrap content in <div class="columns"> ... </div>
     Each direct child <div> becomes a column
     NOTE: math renders fine here since columns use divs only
     for layout, not for containing markdown blocks directly
     ═══════════════════════════════════════════════════════════ -->

# Two-column slide

<div class="columns">
<div>

**Left column heading**

- Point one on the left
- Point two on the left
- Point three on the left

$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$

</div>
<div>

**Right column heading**

- Point one on the right
- Point two on the right

![w:280](images/iPhone.webp)

</div>
</div>

---

<!-- ═══════════════════════════════════════════════════════════
     SLIDE 12: TWO COLUMNS  (70/30 split — text + image)
     Use class columns-70-30 or columns-60-40
     ═══════════════════════════════════════════════════════════ -->

# Two-column slide (70/30)

<div class="columns-70-30">
<div>

- **Main content** goes in the wide left column
  - Sub-point one
  - Sub-point two

- **Another point** with more detail
  - Supporting evidence

</div>
<div style="padding-top:3em; text-align:center;">

![w:200](images/iPhone.webp)

*Caption if needed*

</div>
</div>

---

<!-- ═══════════════════════════════════════════════════════════
     SLIDE 13: FULL-BACKGROUND IMAGE
     The ![bg ...] directive makes the image fill the slide
     opacity: controls transparency (0=invisible, 1=opaque)
     Text overlay uses absolute positioning
     ═══════════════════════════════════════════════════════════ -->

<!-- _paginate: false -->

![bg opacity:0.9](images/Archimedes.png)

<div style="position:absolute; bottom:28%; left:50%; transform:translateX(-50%); text-align:center;">
  <span style="color:#E65100; font-size:3em; font-weight:700; font-family:Montserrat,sans-serif; text-shadow:2px 2px 6px rgba(250,250,250,0.8);">Overlay Text</span>
</div>

---

<!-- ═══════════════════════════════════════════════════════════
     SLIDE 14: CENTERED IMAGE WITH TITLE
     _class: img-center      centers content vertically
     Control image width with w:NNN (pixels)
     ═══════════════════════════════════════════════════════════ -->

<!-- _class: img-center -->

# Slide with a centered figure

![w:700](images/Archimedes.png)

---

<!-- ═══════════════════════════════════════════════════════════
     SLIDE 15: DENSE CONTENT  (small font)
     _class: small     reduces font to 16px
     _class: xsmall    reduces font to 14px  (use sparingly)
     Can be combined: <!-- _class: small prop -->
     ═══════════════════════════════════════════════════════════ -->

<!-- _class: small -->

# Dense content slide (small font)

| $a$ | $\Omega$ | $\Pi$ | $P_{\mathbf{do}(a)}(\omega,\pi)$ | $P(\omega,\pi\mid a)$ |
|:---:|:---:|:---:|---:|---:|
| 0 | 0 | 0 | 4.0% | 4.0% |
| 0 | 0 | 1 | 76.0% | 76.0% |
| 0 | 1 | 0 | 12.0% | 12.0% |
| 0 | 1 | 1 | 8.0% | 8.0% |
| 1 | 0 | 0 | 1.0% | 1.0% |
| 1 | 0 | 1 | 19.0% | 19.0% |
| 1 | 1 | 0 | 48.0% | 48.0% |
| 1 | 1 | 1 | 32.0% | 32.0% |

$$\mathbb{E}(\pi)=61.2\% \qquad \mathbb{E}_{\mathbf{do}(0)}(\pi)=84.0\% \qquad \mathbb{E}_{\mathbf{do}(1)}(\pi)=51.0\%$$

---

<!-- ═══════════════════════════════════════════════════════════
     SLIDE 16: COMBINING CLASSES
     Multiple classes: <!-- _class: small prop -->
     ═══════════════════════════════════════════════════════════ -->

<!-- _class: small prop -->

# Combining slide classes

> <span style="font-weight:700; color:#EB811B;">Proposition 2 (small + prop classes combined)</span>
>
> For all $i \in I$, if $\mathcal{B} \subseteq \mathcal{V}_C$, then the set of identifiable interventions
> $\mathcal{A}^* \subseteq \mathcal{A}$ satisfies $|\mathcal{A}^*| \geq |\mathcal{A}| - |\mathcal{B}|$.

This slide uses `_class: small prop` — small reduces the font size, prop colors the blockquote orange. You can similarly combine `small example`, `xsmall prop`, etc.

---

<!-- ═══════════════════════════════════════════════════════════
     FINAL SLIDE: FIN / THANK YOU
     Use standout class for a clean ending
     ═══════════════════════════════════════════════════════════ -->

<!-- _class: standout -->

# fin
