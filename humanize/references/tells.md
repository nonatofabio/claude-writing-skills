# Catalog of AI tells

Read this when `audit.py` flags something and the repair is not obvious. Each entry gives the tell, why it signals a machine, and what to do instead. Nothing here is a hard ban - context decides.

Much of the vocabulary evidence comes from Wikipedia's community-maintained page "Signs of AI writing", which editors assembled from thousands of flagged article revisions.

## Contents

1. Vocabulary
2. Sentence constructions
3. Openers and closers
4. Structure and formatting
5. Punctuation
6. Stance and hedging
7. Things wrongly flagged as AI

---

## 1. Vocabulary

The watchlist words are not bad words. They are words that appear far more often in generated text than in human text, because they are the safest choice in their slot.

**High signal** (rare in human prose, common in generated prose): delve, tapestry, testament, beacon, symphony, labyrinth, realm, myriad, plethora, multifaceted, pivotal, crucial, robust, seamless, vibrant, meticulous.

**Context dependent** (ordinary words that become tells when used as filler): leverage, foster, navigate, unlock, harness, elevate, landscape, journey, ecosystem, framework, holistic, underscore, showcase.

**Repair:** replace with the plain verb or noun that describes the actual action. *Leverage our infrastructure* becomes *use our servers*. *Navigate the regulatory landscape* becomes *comply with three conflicting rules*. If no plain replacement exists, the sentence was not saying anything and should go.

**Keep the word** when it is the technically correct term: leverage in finance, landscape in geography or ecology, framework in software, realm in Windows domain administration.

## 2. Sentence constructions

**The negative-parallel intensifier.** "It's not just X, it's Y." "This isn't about X. It's about Y." Generated text reaches for this whenever it wants emphasis it has not earned. Repair: state Y directly and drop X.

**The tricolon everywhere.** Three parallel items, three parallel clauses, three parallel paragraphs. One tricolon in a piece is rhetoric. Six is a machine. Repair: count them; keep the best one.

**Compound-adjective stacking.** "Production-grade, enterprise-ready, cloud-native platform." Repair: keep the one adjective that is load-bearing and prove it in the next sentence.

**The gerund summary tail.** "...ensuring scalability and improving performance." A clause bolted to the end that adds no information. Repair: delete from the comma onward, or promote it to its own sentence with a subject.

**Hollow appositives.** "Postgres, a powerful open-source database, ..." Repair: delete the appositive unless the reader genuinely needs it. If they do, make it specific: "Postgres, which has shipped a major release every autumn since 2011, ..."

## 3. Openers and closers

**Scene-setting openers:** "In today's fast-paced digital world", "In an era of", "As technology continues to evolve". Repair: delete the whole sentence and start at the second one.

**Permission openers:** "Let's be honest", "The truth is", "Here's the thing". These promise candour instead of delivering it. Repair: delete and let the candid sentence stand alone.

**Engagement bait:** "Read that again." "Let that sink in." "And that changes everything." Repair: delete.

**The redundant close:** a final paragraph that restates the piece, often opening with "In conclusion", "Ultimately", "At the end of the day", or "Whether you're a beginner or an expert". Repair: delete it. If the piece needs a landing, land it on the sharpest claim, a concrete next step, or an open question - not a summary.

**The unearned call to action:** "What's your experience? Let me know in the comments." Keep only if the user actually wants comments.

## 4. Structure and formatting

**Bold-colon lists.** Every bullet shaped `**Term:** definition`. Fine for a glossary; a tell everywhere else, because it converts an argument into a lookup table and hides the connective reasoning. Repair: convert to prose and add the connections between items that the list format let you skip.

**Symmetry.** Equal-length paragraphs, equal-length sections, a heading over every second paragraph. Human drafts are lumpy: one section runs long because the author cared about it. Repair: let the section the author cares about run long.

**Emoji section markers** in professional or technical writing. Repair: delete, unless the user's own voice profile shows them.

**Table of contents on a 700-word post.** Repair: delete.

**Summary boxes that duplicate the body.** TL;DR is fine when the reader may not read on; it is a tell when the body immediately repeats it in the same words.

## 5. Punctuation

**Em dashes.** Not banned. Human writers use them, and some use them heavily. The tell is *uniform* use: an em dash in most paragraphs, always in the same aside-inserting role, never a colon or parenthesis instead. Repair: vary the punctuation to match the relationship between clauses - colon when the second clause explains the first, semicolon when they balance, parentheses when the aside is truly optional.

**Colons introducing every list.** Repair: sometimes run the list into the sentence.

**The rhetorical question followed immediately by its answer.** "So what does this mean? It means..." Repair: cut the question.

**Curly quotes and Unicode artefacts** pasted into plain-text contexts (code comments, commit messages, terminal output) reveal a copy-paste from a chat window. Repair: normalize to ASCII in those contexts.

## 6. Stance and hedging

**Both-sidesing.** "While some argue X, others contend Y." The author is refusing to write. Repair: pick a side and defend it, or state precisely what evidence would settle it and note that the evidence does not exist yet.

**Stacked hedges.** "It could potentially be somewhat useful in certain cases." Repair: one hedge maximum per claim, and only where the uncertainty is real. "This usually works" is honest. "This may potentially sometimes work" is noise.

**Ungrounded superlatives.** "Revolutionary", "game-changing", "cutting-edge". Repair: replace with the measurement. "Cuts p99 latency from 400ms to 90ms" beats "revolutionary performance".

**Attribution to nobody.** "Experts agree", "Studies show", "It is widely believed". Repair: name the expert and the study, or cut the claim.

## 7. Things wrongly flagged as AI

Do not "fix" these:

- **Correct grammar and spelling.** Human writers are allowed to be careful. Never introduce errors to seem human.
- **Em dashes used well.** Emily Dickinson and half of modern nonfiction run on them.
- **Technical jargon in technical writing.** A paper for practitioners should say *idempotent*, not *safe to repeat*, when idempotent is the precise term. Orwell's rule 5 says use the everyday word *if you can*; often, in technical writing, you cannot.
- **Lists in reference documentation.** API docs are supposed to look like lookup tables.
- **Formality.** Legal and regulatory writing is formal because it must be, not because a machine wrote it.
- **Long sentences.** Length is not a tell. Uniform length is.
