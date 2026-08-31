# Publication policy

This repository is a curated public evidence layer, not a mirror of CodeVolt's internal work.

## Suitable for publication

- Generalized checklists and templates
- Standalone examples created for public use
- Documentation improvements
- Links to verifiable public issues, pull requests or releases
- Lessons that cannot identify a customer or expose a private system

## Review before publication

The maintainer must review architecture descriptions, screenshots, incident lessons, security-related observations, measurements, customer-derived material and statements about future capabilities. Remove identifying detail only when the remaining material is still accurate and useful; otherwise keep it private.

## Editorial quality

Every public draft must pass [`PUBLIC_COMMUNICATION_STANDARD.md`](PUBLIC_COMMUNICATION_STANDARD.md). The author uses specific facts, ordinary words and natural sentence rhythm. The reviewer removes chatbot carry-over, stock promotional language, inflated significance, formulaic contrasts, artificial three part lists, rhetorical questions that answer themselves, generic upbeat endings and unnecessary formatting.

Public copy does not use em dashes or dash led fragments for artificial rhythm. It avoids repeated bold labels, emojis and headings that make short material look templated. Required hyphens in technical identifiers, commands and established terms remain unchanged. These rules apply to CodeVolt's own words. Quoted source text, command output, code and identifiers are reproduced exactly. Dash led fragments are caught by the human writing pass, not by the validator.

Humanising must not introduce fake typos, invented opinions, personal history or artificial quirks. Read the final draft aloud. Rewrite anything that sounds generated, assembled or more confident than the evidence.

## Correctness review

The author and independent reviewer must open each cited source, verify that it supports the exact wording, and recheck facts that can change. Commands, examples and tests presented as working must have real execution evidence. Numbers, dates, versions, issue states and declared totals must be checked rather than inferred.

Separate observed facts, CodeVolt's interpretation and future intent. Name limits and unresolved uncertainty. Remove any claim that cannot be proved from the public evidence.

Consequential public claims require accountable human approval. A different model family must review factual support, omissions, tone and generated writing patterns before publication. If that review is unavailable, the material waits.

## Never publish here

- Credentials, tokens, secrets or private keys
- Customer identities, content, repositories or system details
- Personal data not already deliberately public
- Internal dashboards, agent logs, production endpoints or infrastructure topology
- Recovery material or access arrangements
- Unresolved or exploitable security findings
- Proprietary methods, designs or plans not explicitly approved for publication
- Internal staffing, supplier, contractor or automation arrangements that the public does not need to know
- Internal role prompts, operating instructions or approval workflows intended for private team use
- Personal attribution that misrepresents CodeVolt as an individual rather than the team
- Commits made only to create the appearance of activity

## Evidence rule

Every public claim about completed work must link to evidence a reader can inspect. The reviewer must open that evidence and confirm that it supports the exact wording. A link without that check does not satisfy this rule. A generalized example must be labelled as illustrative, must not describe or imply specific completed CodeVolt work, and never substitutes for the evidence link required above.

Ordinary fork synchronization is not a CodeVolt contribution. A contribution may be described only when its public issue, pull request, commit or release supports the description. Recheck changeable facts immediately before publication.

When classification, accuracy or wording is uncertain, do not publish. Route the candidate to the maintainer for a decision.
