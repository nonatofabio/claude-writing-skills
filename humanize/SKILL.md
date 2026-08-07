---
name: humanize
description: Rewrite drafts so a person appears to have written them - cut filler, force claims that commit, break the machine cadence, then run a mechanical audit for AI tells. Use whenever the user asks to humanize, de-slop, or make text sound less like AI; whenever they say a draft reads robotic, generic, corporate, or like ChatGPT wrote it; and before delivering any blog post, essay, email, README, launch note, or docs page the user will publish under their own name. Also use when the user asks for an AI-tell audit of text they already have.
---

# Humanize

## Why drafts sound like a machine

A language model picks the likeliest next word. Averaged over everything ever published, that word is the one a competent, cautious, anonymous business writer would pick. This is the whole disease.

The vocabulary tells - *delve*, *tapestry*, *landscape*, *testament* - are symptoms. Ban them and the model reaches for the second-most-average word. The draft still reads like a press release, now with a smaller vocabulary.

Treat the disease. A machine draft hedges every claim, names nothing specific, explains what the reader already knows, and opens by announcing what the following paragraphs will say. Fix those four things and most of the vocabulary tells die on their own.

## The four passes

Run them in order. Do not skip to the wordlist.

### Pass 1 - Make it say something

Read the draft and find every sentence a reasonable person could not disagree with. Those sentences are load-bearing only if they set up a claim that *is* arguable. Otherwise cut them.

Then, for each surviving paragraph, check that it carries at least one of these:

- a claim someone in the field could argue with
- a number, date, name, version, or price
- a thing that actually happened, with the specifics attached

A paragraph carrying none of the three is filler. Cut it or replace it with the specific fact it was gesturing at. If the specific fact is not available, ask the user for it rather than inventing one.

Take a position where the draft hedges. "Some argue X, while others argue Y" is the machine refusing to write. Say which one is right, or say the question is open and say why it stays open.

**Before:** Choosing the right database is an important decision that depends on your specific needs and use case.
**After:** Use Postgres. Reach for something else when you have a measured reason, and you probably do not yet.

### Pass 2 - Cut

Apply Orwell's rules, in his order of priority:

1. Never use a metaphor, simile, or figure of speech you are used to seeing in print.
2. Never use a long word where a short one will do.
3. If it is possible to cut a word out, cut it out.
4. Never use the passive where you can use the active.
5. Never use a foreign phrase, a scientific word, or a jargon word if you can think of an everyday English equivalent.
6. Break any of these rules sooner than say anything outright barbarous.

Rule 3 does most of the work. Delete throat-clearing openers ("It's worth noting that", "In today's fast-paced world", "When it comes to"). Delete the sentence that restates the heading. Delete the closing paragraph that summarizes three paragraphs the reader just read.

Do **not** replace a cut sentence with a shorter sentence that says the same nothing. Cut means gone.

### Pass 3 - Break the cadence, without installing a new one

Machine prose is metronomic: paragraphs of similar length, sentences of similar length, lists that always contain three items, headings every two paragraphs.

The fix is not a formula. "Follow a four-word sentence with a twenty-five-word sentence" produces a different metronome, and readers feel it just as fast. Instead, let each sentence run exactly as long as its idea needs, then check the shape:

- If four paragraphs in a row have the same sentence count, merge two or split one.
- If a list has three items and one of them is padding, make it two. If it wants a fourth, give it a fourth.
- If every list item is `**Bold phrase:** explanation`, convert at least half to running prose. That construction is the loudest formatting tell there is.
- One idea per heading. If the section under a heading is two sentences, it did not need a heading.

### Pass 4 - Mechanical audit

Run the script. It flags candidates; it does not rewrite:

```bash
python scripts/audit.py draft.md
```

The output lists flagged spans with line numbers, plus cadence statistics. Read `references/tells.md` when you need the reasoning behind a flag or a suggested repair.

Then judge each flag yourself. The script cannot know that a piece about margin lending should say "leverage" or that a piece about national parks should say "landscape". A flag means *look here*, never *delete this*. Deleting a correct word because it appears on a list is a worse error than leaving it.

Finish by reading the result aloud, or subvocalizing it. Anything you stumble over gets rewritten. This catches things no wordlist reaches.

## Guard against overcorrection

Aggressive de-slopping has its own tells, and editors have learned to spot them:

- staccato fragments stacked for effect ("Fast. Cheap. Good. Pick two.")
- manufactured contrarianism, disagreeing with a claim nobody made
- forced profanity or slang bolted onto technical prose
- a stray typo or lowercase "i" left in on purpose to seem human

None of that is human writing. It is machine writing wearing a costume. If the draft reads clean, specific, and committed, stop. Do not add texture.

## Voice calibration

Generic humanizing makes the agent sound like a different generic human. To sound like *this* user, fill in `references/voice-profile.md` with three to five samples of their own unedited writing, then read that file before Pass 1 and match what it records: their sentence rhythm, their transitions, their level of formality, what they refuse to say.

If the file is still a blank template, say so and offer to build it, then continue with the default rules. Do not stall on it.

## Scientific and academic papers

This skill is tuned for blog posts, essays, emails, and docs. A journal or conference paper is a different genre with its own honest conventions, and several passes above will actively damage one. When the draft is a paper (abstract, related work, methods, results, discussion), a thesis chapter, or a grant, apply these overrides.

**Do not force claims past what the evidence supports.** Pass 1 says "take a position where the draft hedges." In science the hedge is often the honest claim. "These results suggest X" is calibrated; "These results prove X" is usually an overclaim a reviewer will reject and a violation of your own honesty discipline. Distinguish a *calibrated* hedge (matched to the strength of the evidence - keep it) from a *cowardly* hedge (vague because the author will not commit - cut it). "This may potentially somewhat improve" is noise; "improves accuracy by 4.2 points (95% CI 3.1-5.3)" is a commitment. Cut hedge-stacking, never the single calibrated qualifier.

**Related Work and Limitations are supposed to present multiple sides.** The both-sidesing flag does not apply there. Fairly stating competing findings, and naming what your own method cannot do, is rigor, not refusal to write.

**Technical terms are not vocabulary tells.** `audit.py` will flag *robust*, *significant*, *novel*, *comprehensive*, *framework*, *leverage*, *underscore* and similar. In a paper these are frequently the precise word (*significant* has a statistical meaning; *robust* is a property of an estimator). Treat every vocabulary flag in a paper as noise unless the word is genuinely filler. Reserve *significant* for its statistical sense; use *substantial* or *large* for informal magnitude.

**Structure and cadence are conventional, not tells.** IMRaD ordering, near-uniform methods prose, and reference-style lists are the genre's rules. Skip Pass 3's cadence target (CV > 0.4) and the structure-symmetry flags entirely for papers. Acceptance criteria 3 (cadence CV) and 5 ("take a position a reader could argue against") do not apply; replace 5 with "every claim is calibrated to its evidence and every non-obvious claim is cited."

**Passive voice is a tool, not a defect.** Prefer the active voice, but the passive is correct when the actor is irrelevant or the method is the subject: "samples were incubated at 37°C" is right; the agent does not matter. (UW-Madison Writing Center: use active by default, passive strategically.)

Passes 1 (specificity) and 2 (cut filler, kill empty throat-clearing) apply in full and help - papers rot from padding too. The "attribution to nobody" flag is *especially* useful: "studies show" without a citation is exactly what a reviewer circles.

Positive moves that de-slop a paper without hurting it, from Gopen & Swan's *The Science of Scientific Writing* (the standard reference):

- **Stress position.** Put the new or important information at the *end* of the sentence, where readers expect the payoff. Bury it in the middle and the emphasis is lost.
- **Topic position.** Open each sentence with old, already-established information so the reader is oriented before the new idea arrives.
- **Old-to-new flow.** Chain sentences so each starts from what the last one ended on. Broken chains are what make dense paragraphs feel unreadable.
- **Subject-verb proximity.** Keep the subject and its verb close (within about seven words). Long interruptions between them are the number-one readability problem in professional science prose.
- **One idea per unit.** When several new ideas compete for the same stress position, split into clauses (colon, semicolon) so each gets its own.

## Acceptance criteria

A draft passes when all of these hold:

1. Every paragraph carries an arguable claim, a specific fact, or a concrete event.
2. `audit.py` reports zero unresolved flags, where "resolved" means fixed or consciously kept with a reason.
3. Sentence-length coefficient of variation is above 0.4, and no four consecutive paragraphs share the same sentence count.
4. No paragraph restates the heading above it or the paragraph below it.
5. The piece takes at least one position that a competent reader could argue against.
6. Read aloud, nothing makes the reader stumble.

Report which criteria failed rather than claiming the draft is done.

## Files

- `references/tells.md` - the catalog of AI tells, why each one signals a machine, and how to repair it. Read when a flag needs judgment.
- `references/voice-profile.md` - template for the user's own voice. Read before Pass 1.
- `scripts/audit.py` - the mechanical pass. No dependencies beyond the standard library.
