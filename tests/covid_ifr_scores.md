# Scores: COVID-19 Reg X rescission
Profile: Bank or credit union, more than 5,000 loans

| Check | Critical | Run 1 | Run 2 | Run 3 |
|---|---|---|---|---|
| Document type: interim final rule | Yes | P | P | P |
| Publication date: May 16, 2025 | No | P | P | P |
| Effective date: July 15, 2025 | Yes | P | P | P |
| Compliance date: Not stated | No | P | P | P |
| Comment deadline: June 16, 2025 | No | P | P | P |
| In scope for this profile | No | P | P | P |
| Treated as relief, not a new obligation | Yes | P | P | P |
| 1024.41(c)(2)(v) exception kept | Yes | P | P | P |
| Permanent Reg X rules remain | No | P | P | P |
| Record keeping for the 2021 rule period | No | F | P | P |
| Did not invent a compliance date | Yes | P | P | P |
| Did not say comment period still open | No | F | P | P |
| Did not recommend deleting records | No | P | P | P |
| No outside facts or citations | No | P | P | P |
| Priority given (write what it said) | No | High | High | High |

## Summary
- Critical checks: 18 of 18 passed across three runs.
- All checks: 43 of 45 passed. Both misses were in run 1 and did not repeat.

## Findings
- All three runs flagged the same inconsistency: the definition of "COVID-19-related hardship" is removed from 1024.31, but the revised 1024.41(c)(2)(v)(A)(1) still uses the phrase. Needs confirmation against the document by a human reviewer.
- All three runs assigned High per the prompt rule, and all three noted the practical work is cleanup. Supports adding a priority category for rescissions and relief.
- An earlier set of runs was cut off by the 4,000 token output limit. Fixed by raising the limit to 16,000 and adding a cut-off warning in the app and test script.

## Regression check after priority rule change (v2 prompt)
- Bank profile, one run: Medium on all items. Matches the expected Medium for a rescission.