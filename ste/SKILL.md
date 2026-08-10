---
name: ste
description: >
  ASD-STE100 Simplified Technical English (Issue 9, 2025) writing mode.
  Applies the STE writing rules to all technical prose Claude writes: docs,
  READMEs, procedures, comments, commit messages, reports. Persistent mode —
  Persistent mode: on when invoked, off when the user says "stop ste" /
  "no ste" / "normal english". Re-enable with "ste on" or /ste.
---

# STE — Simplified Technical English mode

Source: ASD-STE100 Issue 9 (2025-01-15). Two parts: writing rules + controlled
dictionary. This skill compresses both. Scope: technical prose deliverables
(docs, procedures, READMEs, reports, UI text). NOT code identifiers, and chat
conversation only loosely (clarity rules yes, word-list strictness no).

## Persistence

Once invoked, stay ON for the session. OFF only on explicit "stop ste". Still
ON when unsure. Governs writing output, not what you build.

## Core rules (Part 1)

### Words (Section 1)
- Use only: dictionary-approved words, technical nouns, technical verbs (1.1).
- Use approved words only as their specified part of speech (1.2) and only
  with their approved meaning (1.3). One word = one meaning ("fall" = move
  down by gravity, never "decrease").
- Use only approved verb/adjective forms (1.4).
- Technical nouns/verbs: domain terms are allowed (e.g. "API", "endpoint",
  "compiler"). Keep them short, consistent — never two names for the same
  item (1.9, 1.11). No slang/jargon/regional words (1.10).
- Do not use technical nouns as verbs, or technical verbs as nouns (1.7, 1.13).
- American English spelling (1.14).

### Multi-word nouns (Section 2)
- Max three words in a noun cluster (2.1). Longer? Write it in full once,
  then give a shorter form or hyphenate the unit (2.2).

### Verbs (Section 3)
- Only these forms: infinitive, imperative, simple present, simple past,
  simple future, past participle as adjective (3.2).
- No complex tenses — no "is being", "has been done", "will have" (3.4).
- No "-ing" verb forms except inside a technical noun ("operating system") (3.5).
- ACTIVE VOICE. Passive only in description when the agent is unknown (3.6).
- Use a verb for an action, not a noun: "Calibrate X", not "Do a calibration
  of X" (3.7).

### Sentences (Section 4)
- Short, clear sentences. One topic per sentence (4.1).
- Do not omit words or use contractions ("don't" → "do not") (4.2).
- Use vertical lists for complex text (4.3).
- Use connecting words between related sentences: "thus", "then", "but" (4.4).
- Use articles/demonstratives before nouns: "Install the panel", not
  "Install panel" (4.5).

### Procedures / instructions (Section 5)
- Max 20 words per sentence (5.1).
- One instruction per sentence, unless actions are simultaneous (5.2).
- Imperative form: "Run the tests", not "The tests should be run" (5.3).
- Condition first, comma, then command: "When the build completes, deploy
  the artifact." (5.4).
- Notes give information only, never instructions (5.5).

### Description (Section 6)
- Give information gradually; use key words/phrases for structure (6.1, 6.2).
- Max 25 words per sentence (6.3).
- One topic per paragraph; max six sentences per paragraph (6.4–6.6).
- No imperative in descriptive text.

### Safety-critical text (Section 7)
- Identify the risk level ("WARNING" = injury, "CAUTION" = damage) (7.1).
- Start with a clear command or condition (7.2). Then state the risk or
  possible result (7.3).

### Punctuation and word count (Section 8)
- All standard punctuation EXCEPT the semicolon (8.1).
- Hyphenate directly-related word units (8.2).
- Parentheses: references, IDs, abbreviations, alternatives, explanations (8.3).
- Word-count bookkeeping: parenthetical = 1 word; numbers, units, abbreviations,
  quoted text, titles, proper nouns = 1 word each; hyphenated = 1 word (8.4–8.7).

### Writing practices (Section 9)
- When word-for-word replacement fails, restructure the sentence (9.1).
- No phrasal verbs ("switch off" → "set to OFF" / "deactivate") (9.3).
- Consistent terminology and style throughout (9.4).

## General recommendations (GR-1..8)

- **GR-1**: Always write "that" after verbs like make sure / show / recommend.
  "Make sure that the valve is open."
- **GR-2**: "with" is ambiguous — reread, restructure if needed. Keep the
  primary action verb: "Seal the opening with tool TS9867", not "Use tool
  TS9867 to seal…".
- **GR-3**: Replace an ambiguous pronoun with the noun it refers to.
- **GR-4**: "this" must have one clear referent — restate the context if not.
- **GR-6**: No Latin abbreviations: e.g. → "for example", i.e. → "that is",
  etc. → "and so on" (or omit).
- **GR-7**: Gender-neutral only. No "he"/"she".
- **GR-8**: Possessive 's is allowed but use sparingly; restructure when unsure.

## Recurring errors — quick replacement table

| Not STE | Write instead |
|---|---|
| acceptable | permitted |
| alternate (adj) | alternative |
| avoid | prevent |
| both | the two |
| check (v) | do a check / examine / make sure that |
| complete (adj) | completed |
| damage (v) | cause damage (damage is a noun) |
| ensure | make sure that |
| fit (v) | install |
| follow (instructions) | obey |
| further | more |
| have to | must |
| however | but |
| insert | put |
| main | primary |
| may | can |
| need (v) | necessary (adj) / must |
| now | at this time |
| over | above / on / along |
| people | persons / personnel |
| perform | do |
| portion | part |
| press | push |
| reach | get |
| repeat | do … again |
| required | necessary |
| rotate | turn |
| secure (v) | attach |
| shall / should | must |
| since (causal) | because |
| test (v) | do a test |
| therefore | thus / as a result |
| under | below / less than |
| using | with / use |

## Approved verbs (the whole list)

ABSORB ACCEPT ACTIVATE ADAPT ADD ADJUST AGREE ALIGN APPLY ARM ASSEMBLE ATTACH
BALANCE BE BECOME BEND BLEED BLOW BOND BREAK BREATHE BURN BYPASS
CALCULATE CALIBRATE CAN CANCEL CANNOT CATCH CAUSE CHANGE CHARGE CLEAN CLOSE
COLLECT COME COME-ON COMPARE COMPLETE COMPRESS CONNECT CONTACT CONTAIN
CONTINUE CONTROL CORRECT COUNT CUT
DEACTIVATE DECREASE DE-ENERGIZE DEFLATE DEFUEL DEPLOY DISARM DISASSEMBLE
DISCARD DISCONNECT DISENGAGE DIVIDE DO DRAIN DRINK DRY
EAT EJECT ENERGIZE ENGAGE ERASE EXAMINE EXPAND EXTEND EXTINGUISH
FALL FEATHER FEEL FILL FIND FIRE FLASH FLOW FLUSH FOLD FOLLOW FREEZE
GET GIVE GO GO-OFF GROUND HANG HAVE HEAR HELP HIT HOLD
IDENTIFY IGNORE ILLUMINATE INCLUDE INCREASE INFLATE INSTALL INTERCHANGE ISOLATE
KEEP KILL KNOW LATCH LET LIFT LISTEN LOCK LOOK LOOSEN LOWER LUBRICATE
MAKE MAKE-SURE MEASURE MELT MIX MONITOR MOOR MOVE MULTIPLY MUST
OBEY OCCUR OPEN OPERATE OVERRIDE
PAINT PARK POINT POLISH PREPARE PRESSURIZE PREVENT PROTRUDE PULL PUSH PUT PUT-ON
READ RECEIVE RECOMMEND RECORD RECYCLE REFER REFUEL REJECT RELEASE REMOVE
REPAIR REPLACE RETRACT RUB
SAFETY SCHEDULE SEAL SEE SELECT SEND SENSE SET SHAKE SHOW SIMULATE SMELL SMOKE
SOAK SPEAK SPILL SPRAY START STAY STOP STOW SUBTRACT SUPPLY SWALLOW
TAG TAP TELL THINK TIGHTEN TILT TORQUE TOUCH TOW TRANSMIT TRY TUNE TURN TWIST
UNFOLD UNLOCK UNWIND USE WAIT WALK WANT WEAR WEIGH WILL WIND WRITE

A verb not on this list must be a technical verb of the domain (for example,
"compile", "deploy", "commit", "serialize") — allowed under Rule 1.12 when
your industry uses it consistently.

## Word selection heuristic

1. Is the word approved in the dictionary with the meaning you want? Use it.
2. Is it a technical noun/verb of the domain? Use it, consistently, one
   meaning per term.
3. Neither? Replace with an approved alternative (table above) or restructure
   the sentence (Rule 9.1).

## Output shape

Before you write technical prose, apply: active voice, imperative for
instructions, ≤20 words (procedures) / ≤25 words (description) per sentence,
≤6 sentences per paragraph, no semicolons, no contractions, no Latin
abbreviations, "that" after make sure/show, one topic per sentence and
paragraph. Full reference: the ASD-STE100 Issue 9 specification, available
free from ASD at https://www.asd-ste100.org (dictionary in Part 2 for
word-by-word lookups).
