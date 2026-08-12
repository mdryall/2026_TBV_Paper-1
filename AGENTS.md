# TBV Paper — Agent Instructions

## Authority

The sole authoritative manuscript is:

    paper/tbv_mdr_GPTedit-02.tex

Its TRUTH VERSION header must agree with its filename.

Do not infer authority from older filenames, PDFs, Git history, archived
manuscripts, notes, reviews, or presentation files.

The authoritative bibliography is:

    paper/MDR_TBV_Paper01.bib

The matching compiled manuscript PDF is:

    paper/tbv_mdr_GPTedit-02.pdf

A new manuscript version becomes authoritative only when the author explicitly
promotes it. Never invent or promote a new version number autonomously.

## Required project context

Before substantive manuscript work, read:

    notes/STATUS.md
    notes/REDRAFT_PLAN.md

Historical planning and repair notes may provide context but do not override
those two files or an explicit author instruction.

`Machine_Reviews/`, `archive/`, `talks/`, `agenda/`, and supporting research
notes are not authoritative manuscript instructions unless the author explicitly
brings them into scope.

## Editing discipline

1. Preserve the manuscript's structure and modeling goals.
2. Preserve one-sentence-per-line LaTeX formatting.
3. Do not silently change notation, definitions, assumptions, propositions,
   theorems, proofs, examples, or substantive claims.
4. When a requested edit appears to require such a change, stop and report the
   technical issue before implementing it unless the author has explicitly
   approved that exact substantive change.
5. Make edits minimal and local unless the approved change necessarily
   propagates.
6. Do not repair perceived theoretical problems on your own.
7. Do not re-litigate settled design decisions unless:
   a. the author explicitly requests it, or
   b. `notes/REDRAFT_PLAN.md` explicitly places that issue under review.
8. Never treat a historical repair plan as permission to reapply old edits.
9. Preserve citations, labels, cross-references, notation, and assumptions
   unless an approved changeset requires modification.
10. If an approved change creates a downstream inconsistency, report it rather
    than silently resolving it.

## Role of AI editing agents

For the current redraft, substantive theoretical and mathematical decisions
are approved through the Main Branch editorial process.

Unless explicitly asked to perform independent analysis, Codex's default role
is implementation and verification:

    approved change specification
        -> edit authoritative source
        -> compile
        -> inspect diff
        -> report

Do not broaden an approved changeset.

## Verification

Before editing:

    git status --short --branch

After manuscript edits:

    cd paper
    latexmk -pdf tbv_mdr_GPTedit-02.tex

Do not fix substantive content merely to make compilation succeed. If an
approved edit causes a compilation error, diagnose and report it.

Intermediate LaTeX build products remain governed by `.gitignore` and should
not be committed.

The authoritative `.tex`, bibliography, and matching deliverable PDF are
tracked.

After editing, report:

- files changed
- concise diff/stat
- compilation result
- warnings or unresolved technical issues
- whether any changes went beyond the approved specification

Do not commit unless explicitly instructed.

## Claude and Codex configuration

Tool-specific permission files remain tool-specific.

Do not copy Claude permission syntax from `.claude/` into `AGENTS.md`.
Do not alter `.claude/settings.local.json` unless explicitly requested.
