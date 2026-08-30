# Proposed change review

Use this before deciding whether a proposed code or website change is ready to merge or deploy.

## 1. Name the boundary

- What exact behaviour is meant to change?
- Which files or components are expected to change?
- What is explicitly outside this job?

If the boundary cannot be stated plainly, stop and reduce the job before reviewing implementation detail.

## 2. Confirm the evidence

- Is the starting problem reproducible or otherwise observable?
- Does the proposed change address that evidence rather than a guess?
- Are assumptions and unavailable checks visible?

## 3. Inspect impact

- What uses the changed interface, file or setting?
- Could authentication, permissions, data handling or failure behaviour change?
- Does the diff contain unrelated edits, generated noise or unexplained dependencies?

## 4. Verify the result

- Run the smallest relevant check first, then the wider checks justified by the impact.
- Exercise the expected path and a representative failure path.
- Record the exact command or observation and its result.

## 5. Preserve recovery

- Is there a practical way to reverse the change?
- Are migrations, irreversible actions or deployment order called out?
- Does the handover state what changed, what did not, and what remains uncertain?

A checklist supports judgement; it is not a guarantee that a change is safe or complete.
