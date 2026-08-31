# Public communication standard

Public work carries CodeVolt's name. When accuracy and speed conflict, accuracy wins.

## Check the facts

Before publication, the author and reviewer must:

1. Match every claim about completed work to an exact public issue, pull request, commit, release or file.
2. Open the source and confirm that it says what the draft claims. A link alone is not proof.
3. Recheck details that can change, including issue state, merge state, versions, dates, counts and maintainer decisions.
4. Run any command, test or example presented as working. Record the actual result.
5. Separate observed facts from CodeVolt's interpretation and from future intent.
6. State limits and uncertainty in plain language.
7. Remove a claim when the evidence is incomplete or ambiguous.

The independent reviewer reads the evidence, not just the draft. Numbers and declared totals are checked programmatically where possible. A merge confirms the upstream outcome only. It does not prove every conclusion CodeVolt may draw from it.

## Write like a person

The final copy should sound like a capable person explaining real work to another person.

Use ordinary words and specific details. Vary sentence length naturally. Match the tone of the channel and the maintainer. Keep technical terms when they are accurate and useful.

Remove common signs of generated copy before publication. These include chatbot greetings, canned introductions, inflated claims, vague authority, promotional language, artificial three part lists, repeated bold labels, decorative emojis, generic conclusions and rhetorical questions that answer themselves.

Do not use em dashes in public copy. Do not use dash led fragments to manufacture rhythm. Use a normal list only when it helps the reader follow instructions or compare facts. Keep required hyphens inside technical identifiers, commands and established compound terms.

These style rules apply to CodeVolt's own words. Reproduce quoted upstream text, command output, code and identifiers exactly, including punctuation from the source. Never edit a quotation to satisfy a style rule. If a quotation cannot be reproduced exactly, paraphrase it and remove the quotation marks.

Humanising does not mean adding fake mistakes, invented opinions, personal history or forced quirks. A named representative may use an approved personal voice without claiming work or experience they did not have.

Read the copy aloud. Rewrite any sentence that sounds generated, assembled, theatrical or more confident than the evidence.

## Review before posting

Consequential means any public copy that claims completed work or contribution credit, names another project, maintainer or person, states a number, date, version, count or state, describes CodeVolt's capability, security, customers or future direction, or is published outside this repository. Anything uncertain is treated as consequential.

One model family may draft or revise the copy. A different model family must check factual support, omissions, tone and generated writing patterns. The accountable human approves consequential public claims and any material about CodeVolt's identity, capability, security, customers or future direction.

The review record must name:

1. The evidence checked.
2. The authoring model or person.
3. The independent reviewer.
4. Corrections made after review.
5. Claims removed or limited.
6. The person who approved publication.

If the independent review is unavailable, consequential public copy waits. Passing `scripts/validate_public_content.py` does not mean the copy has been reviewed.

## Correct mistakes openly

If published copy is wrong, the accountable human owns the correction and makes it within one working day of confirming the error. Correct the public source in place where the channel allows editing. Where it does not, publish a visible correction that links the original and leave the original in place unless it is harmful. Do not delete silently. Record the correction and its cause in `CHANGELOG.md`, and update any dependent Field Note or social copy. Do not quietly preserve a stronger claim after its evidence has changed.
