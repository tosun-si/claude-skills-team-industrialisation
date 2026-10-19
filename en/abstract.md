# Title & abstract — English (Devoxx Belgium submission)

> Two-speaker version. Translated from the DevFest Toulouse (2-speaker) French
> abstract in `../abstract.md`.

## Title

**✅ CHOSEN — A:**
> Industrializing AI as a team: skills that encode your conventions

_Alternatives kept just in case:_

**B — keeps the "vibe coding" hook (good for a CFP that likes a catchphrase):**
> From vibe coding to a team workflow: industrializing AI with shared skills

**C — value first:**
> Making AI code to your team's conventions with shared skills

## Abstract — 2-speaker version

Generating code with an AI has become trivial. Doing it **to your team's
conventions** — the right architecture, the right Dockerfiles, the right CI, the
tests you expect, clean PRs — is another story. That's where individual vibe
coding hits its limits.

We share how we industrialized Claude Code at GroupBees: from a monolithic
`CLAUDE.md` that became unmanageable to a **library of modular, shared skills**
that we built — and adopted — together, encoding our best practices: Python
hexagonal architecture, multi-stage Dockerfiles, testing conventions, clean
commits, labeled PRs, Cloud Run deployment. What used to live in each person's
head becomes activable on demand, for the whole team.

In the demo, we start from an idea and generate a small app: a Python hexagonal
backend, a Dockerfile, CI/CD, tests to our conventions, a squashed commit and a
PR — all the way to deployment on GCP. The key moment isn't the magic, it's the
**contrast**: the same request without the skills, then with. The rules make the
difference.

But a library of skills has to be **governed**: versioned, reviewed (a skill
applies to *everything* that will be generated, by the whole team), kept free of
what becomes obsolete, maintained continuously — otherwise you just recreate the
unmanageable monolith.

You'll walk away with a methodology that transfers to other assistants (Cursor,
Copilot): going from the prompt that works to the workflow that scales.
