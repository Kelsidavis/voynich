# Blind Test Run Report

**Date**: 2026-01-13
**Protocol version**: a34c468f

## Sample Statistics
- Total labels sampled: 20
- Labels with matches: 5
- Labels without matches: 15

## Scoring Results
- HIT: 4
- MISS: 1
- AMBIG: 15
- Hit Rate: 0.800 (4/5)

## Baseline Comparison
- Shuffled mean hit rate: 0.881
- Shuffled std dev: 0.098
- Z-score: -0.82

## Conclusion

**NOT SUPPORTED** - Hit rate not significantly above baseline

## Interpretation

### Test Results

The first blind test with strict exact-match candidates (n=9) found 5 matches across 20 sampled labels:

| blind_id | section | EVA text | matched | domains | score |
|----------|---------|----------|---------|---------|-------|
| B06 | H (Herbal) | otaim.dam.alam | dam, ota | MEDICAL, BOTANICAL | HIT |
| B09 | P (Pharma) | oldam | dam | MEDICAL | HIT |
| B13 | Z (Zodiac) | otalchy.tar.am.dy | ota | BOTANICAL | MISS |
| B16 | P (Pharma) | oldam | dam | MEDICAL | HIT |
| B20 | H (Herbal) | otaim.dam.alam | dam, ota | MEDICAL, BOTANICAL | HIT |

### Key Observations

1. **"dam" (Hebrew BLOOD)** appeared in pharmaceutical and herbal contexts, both appropriate for MEDICAL vocabulary. This is consistent with the hypothesis.

2. **"ota" (Basque GORSE)** produced one HIT in herbal (where botanical terms are expected) but also one MISS in zodiac. The zodiac MISS may be a false positive from the common "ot-" prefix pattern.

3. **Duplicate samples**: B06/B20 and B09/B16 are duplicates from different transcribers of the same folio positions. This reduces effective sample size to 3 unique matches.

4. **Low coverage**: Only 9 strict candidates found matches in 25% of labels. The test is underpowered.

### Why Results Are Not Significant

- Hit rate (80%) is below shuffled baseline mean (88%)
- Z-score of -0.82 indicates no significant difference from chance
- With only n=5 (or n=3 unique) non-ambiguous samples, variance is very high
- The "ota" false positive may be due to matching inside "ot-" prefix words

### Next Steps

1. **Deduplicate samples** - Modify extraction to avoid same-position duplicates
2. **Expand candidate list** - Add more strict (4+ char) candidates to increase coverage
3. **Review "ot-" words** - Consider whether "ota" should be excluded as overlapping with "ot-" prefix
4. **Run with larger sample** - 40-60 labels may provide better statistical power

### Status

**INCONCLUSIVE** - Test underpowered; needs expanded candidate list and deduplication.
