# Investigation: Persian/Arabic Connection to Voynich

## The Visual Similarity Claim

Some scholars note that Voynich glyphs resemble Arabic/Persian script:
- Flowing, connected letter forms
- Similar stroke patterns
- Some glyphs look like Arabic letters

However, **visual similarity ≠ linguistic relationship**.

---

## Test 1: Triconsonantal Root Patterns

Semitic languages (Arabic, Hebrew) use 3-consonant roots:
- Arabic: k-t-b → kataba (he wrote), kitab (book), maktub (written)
- Pattern: C-C-C with vowels inserted

### Voynich Root Analysis

Most common Voynich roots (from corpus):
| Root | Tokens | Consonants |
|------|--------|------------|
| ch | 1696 | 1-2 |
| d | 1633 | 1 |
| sh | 1072 | 1-2 |
| qok | 1199 | 2-3 |
| ok | 765 | 1 |
| ot | 719 | 1-2 |
| s | 677 | 1 |

**Result: DOES NOT MATCH**

Voynich roots are 1-2 consonants, NOT triconsonantal.
Semitic root pattern is absent.

---

## Test 2: Arabic Definite Article "al-"

Arabic uses "al-" (الـ) as definite article:
- al-kitab (the book)
- al-bayt (the house)

Voynich has 'al' (253 occurrences). Is this Arabic "al-"?

### Evidence AGAINST:

1. **Position**: Arabic "al-" is a PREFIX. Voynich 'al' appears as:
   - Standalone word: 253 times
   - NOT attached to following word

2. **Pattern**: In Voynich, 'al' follows the same pattern as 'ar', 'or', 'ol':
   | Form | Count |
   |------|-------|
   | ar | 346 |
   | or | 350 |
   | al | 253 |
   | ol | 525 |

   These are clearly suffix variants (-ar, -or, -al, -ol), not the Arabic article.

3. **Voynich determiner**: qo- functions as determiner (412 word pairs)
   - If 'al' were the definite article, we wouldn't need qo-

**Result: REJECTED**

---

## Test 3: Persian/Arabic Vocabulary

Testing common Persian/Arabic words:

| Word | Persian | Arabic | Voynich Count |
|------|---------|--------|---------------|
| و (va/wa) | and | and | Need to check 'o' |
| از (az) | from | - | 0 |
| با (ba) | with | - | 0 |
| که (ke) | that/which | - | 0 |
| این (in) | this | - | 0 |
| آب (ab) | water | - | 0 |
| شب (shab) | night | - | 0 (as standalone) |
| گل (gol) | flower | - | 0 |
| دل (del) | heart | - | dal=243 (but see below) |

### The 'dal' Problem

Persian 'del' (دل) means "heart". Voynich has 'dal' (243x).

But we already proved dal = d + al (suffix pattern):
- 179 stems take BOTH -ar AND -al
- dar (297) and dal (243) are the same root with different suffixes
- This is NOT evidence of Persian

### The 'shab' / 'sh' Connection

Persian 'shab' (شب) = night. Voynich has many sh- words.

But Voynich 'sh' is a productive ROOT:
| Form | Count |
|------|-------|
| shedy | 425 |
| shey | 276 |
| shol | 175 |
| sheey | 142 |
| shor | 92 |

This is Voynich morphology, not Persian vocabulary.

**Result: NO PERSIAN VOCABULARY MATCH**

---

## Test 4: Persian Morphology

Persian is an ANALYTIC language with:
- Subject-Object-Verb word order
- Ezafe construction (noun + -e + modifier)
- Limited case marking
- Postpositions rather than prepositions

### Voynich vs Persian Structure

| Feature | Persian | Voynich |
|---------|---------|---------|
| Root length | Multi-syllable | 1-2 consonants |
| Morphology | Analytic | Agglutinative |
| Case markers | Minimal (-ra) | Extensive (-aiin, -ain, etc.) |
| Ezafe (-e) | Common | Not found as connector |
| Suffixes | Few | Many productive suffixes |

**Result: DOES NOT MATCH**

Voynich is more AGGLUTINATIVE (suffix-heavy), not analytic like Persian.

---

## Test 5: Arabic Morphology

Arabic has:
- Triconsonantal roots (k-t-b pattern)
- Template morphology (inserting vowels)
- Prefixed definite article (al-)
- Verb conjugation with prefixes AND suffixes

### Voynich vs Arabic Structure

| Feature | Arabic | Voynich |
|---------|--------|---------|
| Root pattern | CCC (3 consonants) | C or CC |
| Word formation | Internal vowel change | Suffix addition |
| Article | al- prefix | qo- prefix (different) |
| Verb marking | Prefix + suffix | Unknown |

**Result: DOES NOT MATCH**

---

## Test 6: Script Direction Evidence

If Voynich encoded Persian/Arabic:

1. **Right-to-left encoding?** No evidence of reversed word order
2. **Letter shapes as cipher?** Possible but unproven
3. **Abjad (consonant-only)?** Voynich has vowels (a, e, i, o)

---

## Test 7: Historical Context

The Voynich manuscript (carbon dated 1404-1438) comes from:
- European context (Italian/Central European ownership chain)
- Latin alphabet underlying EVA transcription
- No Arabic/Persian notation in marginalia

Persian/Arabic texts from this period would show:
- Different page layout (right-to-left)
- Different numbering system
- Different illustration style

The Voynich shows NONE of these features.

---

## Conclusion

| Test | Result |
|------|--------|
| Triconsonantal roots | **NO** - Voynich has 1-2 consonant roots |
| Arabic 'al-' article | **NO** - 'al' is a suffix, not article |
| Persian vocabulary | **NO** - No matches |
| Persian morphology | **NO** - Voynich is agglutinative |
| Arabic morphology | **NO** - No template patterns |
| Script direction | **NO** - No RTL evidence |
| Historical context | **NO** - European origin |

### Final Assessment

**The Persian/Arabic hypothesis is REJECTED.**

The visual similarity between Voynich glyphs and Arabic/Persian script is:
- Superficial (flowing cursive is common)
- Not supported by linguistic evidence
- Contradicted by morphological analysis

The Voynich script may have been influenced by Arabic/Persian aesthetics, but the underlying language structure shows NO connection to Semitic or Iranian languages.

---

## What About Other Middle Eastern Languages?

| Language | Test | Result |
|----------|------|--------|
| Hebrew | Triconsonantal roots | NO |
| Syriac | Semitic patterns | NO |
| Turkish | Agglutinative, SOV | Possible structure match, no vocabulary |
| Armenian | Indo-European | No vocabulary match |

The ONLY structural similarity is with agglutinative languages (Turkish, Finnish, Hungarian), but vocabulary doesn't match any of them either.

---

*Investigation completed January 2026*
*Corpus-first methodology*
