# CodeVolt field notes

Selected public checklists, templates and examples from CodeVolt's approach to small, bounded technical work.

- **Status:** Active and selectively maintained
- **Maintainer:** [@Rook-CodeVolt](https://github.com/Rook-CodeVolt)
- **Last substantive review:** 30 August 2026

## Purpose

This repository makes a small amount of CodeVolt's working method useful and inspectable without publishing customer work, private systems or operational details. The material is intended for people scoping, reviewing or handing over contained website and code changes.

It is not a live operations feed, a complete description of CodeVolt, a customer support system, or a security guarantee.

## Contents

- [`checklists/proposed-change-review.md`](checklists/proposed-change-review.md): bound a proposed change before reviewing it.
- [`checklists/one-file-fix.md`](checklists/one-file-fix.md): keep a genuinely contained fix contained.
- [`checklists/small-technical-handover.md`](checklists/small-technical-handover.md): hand over what changed, how it was checked and how to undo it.
- [`templates/public-work-note.md`](templates/public-work-note.md): prepare a restrained public note backed by public evidence.

## Use

Copy or adapt a checklist for your own work. The documents are intentionally short; apply judgement appropriate to the system and risk involved.

To validate this repository locally:

```bash
python3 scripts/validate_public_content.py .
```

The same check runs in GitHub Actions for proposed changes and updates to `main`.

## Publication boundary

Read [`PUBLICATION_POLICY.md`](PUBLICATION_POLICY.md) before proposing content. Never submit credentials, customer or personal data, private infrastructure details, raw logs, unpublished security findings, recovery material, or proprietary implementation details.

## Maintenance and changes

[`MAINTENANCE.md`](MAINTENANCE.md) defines the weekly assurance cadence, update triggers and no-artificial-activity rule. Documentation corrections are welcome through the repository's issue template. Material additions require evidence and review; work enquiries belong on [codevolt.co.uk](https://codevolt.co.uk).

## Security and support

- Security concern: follow [`SECURITY.md`](SECURITY.md); do not disclose it in a public issue.
- Documentation correction: follow [`CONTRIBUTING.md`](CONTRIBUTING.md).
- Work enquiry: use [codevolt.co.uk](https://codevolt.co.uk).

## Licence

The repository is available under the [MIT Licence](LICENSE). Examples are generalized and come with no warranty.
