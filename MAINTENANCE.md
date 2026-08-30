# Maintenance

## Ownership

The accountable maintainer is the CodeVolt team through [@Rook-CodeVolt](https://github.com/Rook-CodeVolt).

## Cadence

A weekly assurance review checks:

1. Repository purpose, links and contact routes remain accurate.
2. New public material still satisfies [`PUBLICATION_POLICY.md`](PUBLICATION_POLICY.md).
3. GitHub Actions, secret scanning and push protection remain in the expected state.
4. Open corrections or security routes have not been neglected.
5. Public descriptions remain consistent with the CodeVolt team voice.
6. A representative checklist remains usable as written.

The review does not create a commit merely to update a date or activity graph. If nothing material changed, no repository change is required.

## Update triggers

Review immediately when CodeVolt changes its public services, contact route, public identity, publication policy, or publishes a relevant issue, pull request, release or generalized resource.

## Change process

- Use a focused branch and pull request for material changes.
- Run `python3 scripts/validate_public_content.py .`.
- State what evidence supports a factual claim and why publication is safe.
- Keep work enquiries and sensitive reports out of public issues.
- Record user-visible changes in [`CHANGELOG.md`](CHANGELOG.md).

## Archival

If the repository stops being maintained, archive it and update the README with the archival date, last supported state and replacement or reason. Do not leave it appearing current.
