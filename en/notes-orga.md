# CFP submission — Devoxx Belgium (English)

> Two-speaker version. What goes into the CFP form. Internal prep (demo risks,
> safety nets, room requirements) lives in `prep-internal.md`.

## Elevator pitch (~85 words)

> At GroupBees, we went from a sprawl of personal `CLAUDE.md` files — hard to
> share, hard to maintain, and expensive in context — to a library of **team
> skills**. Each skill encapsulates one convention: hexagonal architecture,
> multi-stage Dockerfiles, CI/CD, testing, Git best practices, or Cloud Run
> deployment. The result: the team's knowledge becomes reusable building blocks,
> activated only when they're needed. But this approach brings new challenges
> too: governance, review, versioning, obsolescence, and blast radius. In this
> field report, we show how we built this skills library, what it gives us day
> to day, and why industrializing AI as a team ends up looking a lot like
> industrializing software itself.

## Audience & level

Developers, tech leads, engineering managers, and architects who want to bring
AI assistants into their team workflows. Familiarity with modern development
workflows (Git, CI/CD, Docker) helps, but **no Claude Code experience is
required** — the methodology transfers to Cursor, GitHub Copilot, and others.

## What makes this talk different

Most "AI for devs" talks saturate the upside: individual productivity gains. We
tackle a different, undercovered problem — how to make AI work at **team scale**,
durably and maintainably. It's a field report from GroupBees, scars included,
not a cosmetic demo. And it dares to show the part most AI talks hide: that a
skills library is a system you have to **govern**.

## Key takeaways

- A concrete methodology for encoding team conventions into AI skills —
  applicable to Claude Code, Cursor, Copilot.
- The **governance process** that makes it durable: versioning, review,
  obsolescence detection, owners — and why the review bar for a skill is *higher*
  than for normal code (blast radius: one skill shapes everything the whole team
  generates).
- Concrete, transferable artifacts seen live: multi-stage Dockerfile, Python
  hexagonal architecture, CI/CD, labeled PR.

## Demo

From a business idea, we generate a small app end to end — clean-architecture
front, Python hexagonal backend, multi-stage Dockerfile, automated tests, CI/CD
pipeline, Git workflow + PR, deployment on Google Cloud. The key moment is the
**contrast**: the same request without skills, then with. The rules make the
difference.

## Format

35 min + 5–10 min Q&A. 30 / 40 / 50 min variants available.

## Speaker bios

_[to fill in — both speakers]_
