# Matching Protocol (Pre-Registered)

This protocol defines how candidate cognates are identified and evaluated.
It is designed to minimize selection bias and to make results reproducible.

## 1. Scope

- **Target**: Voynich EVA transcription tokens and token substrings (roots).
- **Primary comparison language**: Basque.
- **Secondary comparison languages** (contact-layer candidates): Turkish, Hungarian, Hebrew.
- **Negative controls**: at least 3 unrelated languages (chosen before running tests).

## 2. Token / Root Extraction Rules

We define a "root candidate" as:
- a contiguous substring of a token of length 3–4 characters (default), OR
- a full token if token length <= 6.

We exclude:
- tokens containing only EVA structural prefixes/suffixes under study (e.g., pure "qo-" forms),
- tokens shorter than 2 characters,
- tokens occurring fewer than N times (default N=3) unless manually flagged as label-only.

## 3. Matching Rules (No Wiggle)

For a root candidate R and a dictionary form D:

**Allowed matches:**
- Exact match only (R == D), OR
- One of these pre-registered transformations (choose ONE set and freeze it):
  - **Option A** (STRICT): None (exact only)
  - **Option B**: Single final vowel normalization: {a,e,i,o,u} treated as equivalent at final character only.

**Current selection: Option A (STRICT)**

**Disallowed:**
- arbitrary phonetic equivalence (e.g., l~r, t~d, k~g) unless explicitly pre-registered.
- edit distance > 1
- semantic broadening beyond the dictionary headword.

## 4. Semantic Assignment

Every match must use a fixed reference gloss taken from a dictionary source.
No post-hoc glossing is allowed (e.g., "could mean X or Y depending on context").

Each matched root receives:
- a single **gloss label** (e.g., FLOWER, FOOT, BLOOD)
- a **domain label** (BOTANICAL, BODY, MEDICAL, TEMPORAL, CELESTIAL, OTHER)

### Domain Labels

| Domain | Definition |
|--------|------------|
| BOTANICAL | Plants, flowers, herbs, agricultural terms |
| BODY | Anatomy, body parts |
| MEDICAL | Healing, illness, blood, treatments |
| TEMPORAL | Time words (now, then, when) |
| CELESTIAL | Stars, planets, astronomical terms |
| VERB | Action words (enter, sell, bring) |
| OTHER | Does not fit above categories |

## 5. Testing Plan

### 5.1 In-Sample Discovery (Exploratory)
Used only to propose candidates. Results here are NOT evidence.

### 5.2 Out-of-Sample Blind Test (Confirmatory)
- Freeze the candidate list and all rules above.
- Randomly sample K labels from each section (default K=5 per section, 20 total).
- Decode without looking at illustrations or section titles.
- After decoding, reveal section and score "domain appropriateness."

## 6. Scoring

A decoded label is scored as:
- **HIT**: domain matches section (e.g., BOTANICAL in herbal folios)
- **MISS**: domain conflicts strongly with section
- **AMBIG**: too generic to classify (e.g., ENTER, THE, NOW) or no match found

### Section-Domain Mapping

| Section | Expected Domains (HIT) | Conflicting Domains (MISS) |
|---------|------------------------|---------------------------|
| H (Herbal) | BOTANICAL, MEDICAL | CELESTIAL |
| Z (Zodiac) | CELESTIAL | BOTANICAL, BODY |
| B (Biological) | BODY, MEDICAL | CELESTIAL, BOTANICAL |
| P (Pharmaceutical) | MEDICAL, BOTANICAL | CELESTIAL |

**Primary metric:**
- Hit Rate = HIT / (HIT + MISS)

**Secondary metrics:**
- Coverage = (HIT + MISS + AMBIG) / total labels sampled
- Ambiguity Rate = AMBIG / decoded

## 7. Negative Controls

Run the same matching procedure against control language dictionaries.
If controls produce similar hit rates or similar match counts, the method is underconstrained.

**Designated control languages:**
1. Finnish (Uralic, typologically similar to Basque)
2. Welsh (Celtic, European language isolate comparison)
3. Swahili (Bantu, geographically/historically implausible)

## 8. Reporting Requirements

Every report must include:
- the frozen protocol version (git hash)
- sampled label IDs
- full match tables (including rejected candidates)
- control results
- shuffle baseline statistics

---

*Protocol version: 1.0*
*Frozen: January 2026*
*Matching rule: Option A (STRICT - exact only)*
*Minimum root length: 3 characters*
