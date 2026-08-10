# AGENTS.md

Instructions for a coding agent (Claude Code, or any agent that can run a shell and read files) working in this repo. Two jobs: **install the skills** and **calibrate the humanize voice profile**. Do them in that order.

## Job 1: install the skills

Copy the skill folders into the user's skills directory. For Claude Code that is `~/.claude/skills/`.

```bash
cp -r plainspoken ~/.claude/skills/
cp -r humanize   ~/.claude/skills/
cp -r ste        ~/.claude/skills/
```

Then confirm they registered:

```bash
ls ~/.claude/skills/plainspoken/SKILL.md ~/.claude/skills/humanize/SKILL.md ~/.claude/skills/ste/SKILL.md
```

Skills load from frontmatter, so a new session (or a skill reload) picks them up. Tell the user to restart their session, then invoke with `/plainspoken`, `/humanize`, or `/ste`.

If the user runs a different harness, the unit that matters is the folder plus its `SKILL.md`. Drop the folder wherever that harness discovers skills.

Do **not** overwrite an existing `~/.claude/skills/humanize/references/voice-profile.md` without asking. That file holds the user's own writing samples once calibrated, and clobbering it with the blank template throws away their work. Check first:

```bash
test -f ~/.claude/skills/humanize/references/voice-profile.md && echo "EXISTS — ask before replacing"
```

## Job 2: calibrate the humanize voice profile

`humanize` ships with `references/voice-profile.md` as a **blank template**. Until it is filled, `humanize` de-slops toward a generic human, not toward *this* user. Filling it is what makes the rewrite sound like them.

The profile outranks the general rules in `humanize/SKILL.md` wherever the two disagree. If the profile records that the user leans on em dashes, the em-dash audit stands down. That is the point of it.

### How to run the calibration with the user

1. **Ask for three to five samples of their own unedited writing.** Messier is better. Good sources: a long Slack or email reply, a design doc, a pre-AI blog post, a code-review comment they wrote when annoyed. Bad sources: anything a model already edited, anything written for a committee. Annoyed code-review comments are gold — they show the real voice with the politeness filter off.

2. **Scrub before pasting.** Strip third-party real names, internal project names, private links, anything under NDA. The profile needs the user's *style*, not their private content. This repo's own template was scrubbed the same way. If a sample is mostly private content, ask for a different one.

3. **Fill each `Observed patterns` line from evidence, and quote the line that shows it.** Do not guess. The sections are: sentence rhythm, openers, transitions, person and stance, formality, punctuation habits, vocabulary fingerprints, structure, what they refuse to do, how they land an ending. An empty section is more useful than an invented one — leave it blank if the samples do not show it.

4. **Record overrides.** When the user's real habit contradicts a `SKILL.md` rule (em dashes, exclamation points, contractions, non-native constructions they keep on purpose), write it in the `Overrides` section with the evidence. Never invent errors to seem human — that rule in `SKILL.md` always stands.

5. **Set the status line.** Change `Status: **BLANK TEMPLATE**` to `Status: **CALIBRATED**` once real samples and patterns are in.

### Keeping it current

The profile improves with more samples, especially messier ones. Tell the user they can hand you a new sample anytime and you will fold its patterns into the existing profile rather than starting over. Add the sample under a new `Sample N` heading, then update only the `Observed patterns` and `Overrides` lines the new evidence changes.

## House style for this repo

When you edit or add prose here, follow the `plainspoken` rules: answer first, own the voice, cut the preamble, no hype adverbs, no "isn't X it's Y." If you touch the writing, run it past `humanize/scripts/audit.py` before committing.

```bash
python humanize/scripts/audit.py <file.md>
```
