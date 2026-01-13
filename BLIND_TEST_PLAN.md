# Blind Test Plan

## Goal

Test whether candidate roots produce section-appropriate semantics out-of-sample.
This is the confirmatory phase that transforms exploratory findings into falsifiable evidence.

## Freeze Point

Before sampling, freeze:
- Candidate root list (`evidence/CANDIDATES.csv`)
- Matching Protocol version (`MATCHING_PROTOCOL.md`)
- Decoder script version (`tools/run_blind_decode.py`)

**All freezes must be committed to git before test execution.**

## Sampling

### Label Pool Definition

Labels are extracted from EVA transcription lines meeting these criteria:
- Text type = `labels`, `circular-lines`, or `radial-lines`
- Line ends with `=` (complete label)
- Contains at least one alphabetic EVA token `[a-z]`
- Excludes lines containing only fillers (`!`, `%`, `*`)

### Section Distribution

Sample exactly **20 labels total**:
- 5 from Herbal pages (`$I=H`)
- 5 from Zodiac pages (`$I=Z`)
- 5 from Biological pages (`$I=B`)
- 5 from Pharmaceutical/Recipe pages (`$I=P`)

### Deterministic Sampling Rule

For each section:
1. Sort eligible label lines by locator string (folio.position)
2. Compute `hash(locator) mod N` using SHA-256
3. Select the first 5 unique hits in hash order

This guarantees:
- No cherry-picking
- No "interesting-looking" bias
- Reproducibility by anyone using the same file + seed

## Blindness Protocol

### Blind Phase

During decoding, the decoder receives ONLY:
- `blind_id` (e.g., B01, B02...)
- `eva_text` (the token string)

The decoder does NOT receive:
- Folio image
- Folio number
- Section identifier (H/Z/B/P)
- Page number
- Known label lists

### Implementation

```
blind_inputs.csv:
blind_id,locator_hash,eva_text
B01,a7f3c2d1,otaiin.okal=
B02,8b2e4f9c,qokaiin.dar=
...
```

The `locator_hash` is SHA-256(locator)[:8] - enough to rejoin later, not enough to reverse.

## Decode Output

For each label, record:

| Field | Description |
|-------|-------------|
| blind_id | B01, B02, etc. |
| matched_roots | Roots found (comma-separated) |
| glosses | Corresponding gloss labels |
| domains | Corresponding domain labels |
| transform_used | "none" for strict matching |

Save as: `blind_decodes.csv`

Empty matches are recorded with blank fields - this is data, not error.

## Reveal Phase

After ALL decoding is complete:

1. Join `blind_inputs.csv` back to transcription using locator hash
2. Add section metadata (H/Z/B/P)
3. Add text type
4. Save as: `revealed.csv`

**Critical**: No modifications to `blind_decodes.csv` are permitted after reveal.

## Scoring

Apply the rubric from MATCHING_PROTOCOL.md:

| Outcome | Rule |
|---------|------|
| HIT | Domain matches section |
| MISS | Domain conflicts strongly with section |
| AMBIG | No domain, no match, or too generic |

### Section-Domain Rubric

| Section | HIT domains | MISS domains |
|---------|-------------|--------------|
| H (Herbal) | BOTANICAL, MEDICAL | CELESTIAL |
| Z (Zodiac) | CELESTIAL | BOTANICAL, BODY |
| B (Biological) | BODY, MEDICAL | CELESTIAL, BOTANICAL |
| P (Pharmaceutical) | MEDICAL, BOTANICAL | CELESTIAL |

Save as: `scored_results.csv`

## Baseline Comparison

### Shuffle Test

1. Randomly shuffle section labels 1000 times
2. Re-score each shuffle using the same rubric
3. Record hit rates for each shuffle
4. Compute mean and standard deviation

Save as: `shuffled_baseline.csv`

### Significance Threshold

**Acceptance criteria:**
- Real hit rate must exceed shuffled mean by >= 2 standard deviations
- Minimum 5 non-ambiguous items required for statistical validity

### Interpretation Guide

| Result | Interpretation |
|--------|----------------|
| p < 0.05, n >= 5 | Signal detected - hypothesis supported |
| p >= 0.05, n >= 5 | No signal - hypothesis not supported |
| n < 5 | Test underpowered - expand candidate list |

## Output Directory Structure

```
evidence/blind_test/run_YYYY-MM-DD/
├── blind_inputs.csv      # Blinded sample
├── blind_decodes.csv     # Decode results (no section info)
├── revealed.csv          # With section info added
├── scored_results.csv    # HIT/MISS/AMBIG scores
├── shuffled_baseline.csv # 1000 shuffle results
└── RUN_REPORT.md         # Summary statistics
```

## Run Report Template

```markdown
# Blind Test Run Report

**Date**: YYYY-MM-DD
**Protocol version**: [git hash]
**Candidate list version**: [git hash]

## Sample Statistics
- Total labels sampled: 20
- Section distribution: H=5, Z=5, B=5, P=5

## Match Results
- Total matches: X/20
- Domains found: [list]

## Scoring Results
- HIT: X
- MISS: Y
- AMBIG: Z
- Hit Rate: X/(X+Y) = P%

## Baseline Comparison
- Shuffled mean hit rate: M%
- Shuffled std dev: S%
- Z-score: (P - M) / S
- p-value: [calculated]

## Conclusion
[SUPPORTED / NOT SUPPORTED / UNDERPOWERED]
```

---

*Plan version: 1.0*
*Frozen: January 2026*
