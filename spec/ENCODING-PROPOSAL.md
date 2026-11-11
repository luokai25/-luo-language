# Luo Character Encoding: Initial Proposal

**Status: provisional discussion only. Not an approved standard.**

Five bits can represent 32 values, so a compact fixed-width internal representation for 30 character identities is possible.

## Candidate mapping
This candidate maps register order to zero-based values:

| Character | Candidate 5-bit value |
|---|---|
| LUO-001 | 00000 |
| LUO-002 | 00001 |
| LUO-003 | 00010 |
| LUO-004 | 00011 |
| LUO-005 | 00100 |
| LUO-006 | 00101 |
| LUO-007 | 00110 |
| LUO-008 | 00111 |
| LUO-009 | 01000 |
| LUO-010 | 01001 |
| LUO-011 | 01010 |
| LUO-012 | 01011 |
| LUO-013 | 01100 |
| LUO-014 | 01101 |
| LUO-015 | 01110 |
| LUO-016 | 01111 |
| LUO-017 | 10000 |
| LUO-018 | 10001 |
| LUO-019 | 10010 |
| LUO-020 | 10011 |
| LUO-021 | 10100 |
| LUO-022 | 10101 |
| LUO-023 | 10110 |
| LUO-024 | 10111 |
| LUO-025 | 11000 |
| LUO-026 | 11001 |
| LUO-027 | 11010 |
| LUO-028 | 11011 |
| LUO-029 | 11100 |
| LUO-030 | 11101 |

A previous discussion also considered values 00001 through 11110 with 00000 as a separator. Neither scheme has been approved.

## Decisions still required
- Are values character identities, token IDs, or both?
- Should permanent text encoding use Unicode, a private-use development mapping, a dedicated encoding, or a layered scheme?
- How will Luo interoperate with operating systems, terminals, browsers, editors, and network protocols?
- How are grapheme boundaries, normalization, invalid sequences, and versioning handled?
- How are source files framed and identifiers separated?
- How will future additions be handled?

A 5-bit value can be a compact internal symbol ID. It is not a complete text encoding or file format. A real format must define framing, metadata, versioning, error handling, and interoperability. Do not freeze code points or binary format until the creator reviews the alternatives.
