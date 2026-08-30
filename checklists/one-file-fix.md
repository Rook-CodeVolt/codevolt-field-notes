# One-file fix

A one-file fix should stay one-file only when the evidence supports that boundary.

## Before editing

- Name the visible problem and reproduce or observe it.
- Identify the file responsible and explain why adjacent files do not need to change.
- Preserve the current version through source control or another appropriate rollback method.

## Make the smallest useful change

- Change only the behaviour required to resolve the observed problem.
- Avoid opportunistic cleanup, reformatting or dependency changes.
- Keep existing interfaces and conventions unless the fault is in the interface itself.

## Check it

- Re-run the original reproduction.
- Run the narrow syntax, lint, test or build check relevant to the file.
- Check one nearby path that should remain unchanged.
- Inspect the final diff for accidental edits or sensitive content.

## Hand it over

Record:

- the problem observed;
- the file changed and why;
- the check performed and result;
- what was not checked;
- how to reverse the change.

If the evidence points beyond one file, re-scope the job rather than forcing the label to remain true.
