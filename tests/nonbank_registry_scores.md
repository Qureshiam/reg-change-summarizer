# Scores: Nonbank Registry rescission

## Nonbank profile (more than 5,000 loans)

| Check | Critical | Run 1 | Run 2 | Run 3 |
|---|---|---|---|---|
| Document type: final rule | Yes | P | P | P |
| Publication date: October 29, 2025 | No | P | P | P |
| Effective date: October 29, 2025 | Yes | P | P | P |
| Compliance date: Not stated | No | P | P | P |
| No comment deadline invented | No | P | P | P |
| Nonbank in scope, as relief | Yes | P | P | P |
| Did not apply the 5,000-loan test | Yes | P | P | P |
| NMLS cited in the Bureau's reasoning | No | P | P | P |
| Did not claim NMLS or state obligations changed | No | P | P | P |
| Did not invent a compliance date | Yes | P | P | P |
| Treated as relief, not a new obligation | Yes | P | P | P |
| Did not say registration is still required | No | P | P | P |
| Did not claim form contract proposal withdrawn | No | P | P | P |
| Did not recommend stopping order tracking | No | P | P | P |
| Priority given | No | High | High | High |

Critical checks: 18 of 18. All checks: 42 of 42.

## Bank profile (more than 5,000 loans)

| Check | Critical | Run 1 | Run 2 | Run 3 |
|---|---|---|---|---|
| Document type: final rule | Yes | P | P | P |
| Publication date: October 29, 2025 | No | P | P | P |
| Effective date: October 29, 2025 | Yes | P | P | P |
| Compliance date: Not stated | No | P | P | P |
| No comment deadline invented | No | P | P | P |
| Bank out of scope | Yes | P | P | P |
| Did not tell a bank it must act under this rule | Yes | P | P | P |
| Did not apply the 5,000-loan test | Yes | P | P | P |
| NMLS cited in the Bureau's reasoning | No | P | P | P |
| Did not claim NMLS or state obligations changed | No | P | P | P |
| Did not invent a compliance date | Yes | P | P | P |
| Treated as relief, not a new obligation | Yes | P | P | P |
| Did not say registration is still required | No | P | P | P |
| Did not claim form contract proposal withdrawn | No | P | P | P |
| Did not recommend stopping order tracking | No | P | P | P |
| Priority matches expected (None or Low) | No | F | F | F |

Critical checks: 21 of 21. All checks: 45 of 48. All three misses are the priority row.

## Findings
- Nonbank runs said "partly in scope," because relief only matters if the servicer had a covered order or registered. More precise than the original answer key, which said "in scope." Answer key updated.
- All six runs avoided claiming the separate form contract proposal was withdrawn, although news coverage reported both actions together.
- All six runs flagged drafting inconsistencies in the rule (Congressional Review Act timing; "proposed rule" wording in the cost analysis).
- Bank runs raised nonbank affiliates, subsidiaries, and CUSOs as possibly covered, and noted the profile does not say whether the institution is federally insured. Not in the answer key. Product idea: add an affiliates question to the servicer profile.
- Bank runs rated every item High for a rule that is out of scope, while noting the effort is minimal. Combined with the COVID test, this is the third case showing the priority rule needs separate handling for rescissions, relief, and out-of-scope rules.

## Regression check after priority rule change (v2 prompt)
- Nonbank profile, one run: Medium where registry processes were built, Low if never built. Matches the expected Medium.
- Bank profile, one run: None for all servicing areas, Low for affiliate confirmation steps. Matches the expected None.
- The priority failures from the original runs are resolved.