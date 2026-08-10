# Claude writing skills

Three [Claude Code](https://docs.claude.com/en/docs/claude-code) skills for making written and spoken output read like a human wrote it.

## `plainspoken`

A talking-register mode. It changes how the assistant speaks in chat: answer first, decide instead of surveying options, own the voice, and strip the usual AI tells. Persistent like a mode — on when you say `plainspoken`, off on `stop plainspoken` / `normal mode`.

Distilled from four ideas: the Pyramid Principle (lead with the conclusion), tight prose discipline, AI-tell removal, and decide-don't-survey.

## `ste`

An [ASD-STE100 Simplified Technical English](https://www.asd-ste100.org) (Issue 9, 2025) writing mode for technical prose: docs, procedures, READMEs, reports, UI text. Compresses the full standard — all 53 writing rules, the 8 general recommendations, the recurring-errors replacement table, and the complete approved-verb list — into one skill. Active voice, imperative instructions, 20/25-word sentence caps, one meaning per word. Persistent like a mode — on when you say `ste`, off on `stop ste` / `normal english`.

## `humanize`

Rewrites drafts so a person appears to have written them: cut filler, force claims that commit, break the machine cadence, then run a mechanical audit for AI tells. Tuned for blog posts, essays, emails, READMEs, and docs, with a separate override set for scientific and academic papers.

Ships with:
- `scripts/audit.py` — flags AI tells and cadence problems. Standard library only, no dependencies.
- `references/tells.md` — the catalog of tells, why each signals a machine, and how to repair it.
- `references/voice-profile.md` — a **blank template**. Fill it with three to five samples of a writer's own unedited prose so the rewrite matches their voice instead of a generic one.

## Install

Drop either folder into your skills directory:

```bash
cp -r plainspoken ~/.claude/skills/
cp -r humanize   ~/.claude/skills/
cp -r ste        ~/.claude/skills/
```

Then invoke by name (`/plainspoken`, `/humanize`, `/ste`) or let the descriptions trigger them.

Run the humanize audit standalone:

```bash
python humanize/scripts/audit.py draft.md
```

## License

MIT. See [LICENSE](LICENSE).
