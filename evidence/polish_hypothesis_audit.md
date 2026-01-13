# Polish Hypothesis Audit: Final Status

## Executive Summary

**The Polish hypothesis has collapsed completely.**

Every claimed Polish word either:
1. Doesn't exist in the corpus (0 occurrences)
2. Is actually a Voynich root + suffix combination
3. Is too rare and ambiguous to constitute evidence

---

## Complete Review of v7.5 Polish Claims

### Category 1: Not In Corpus (0 occurrences)

| Claim | v7.5 Meaning | Corpus Count | Status |
|-------|--------------|--------------|--------|
| choremu | to the sick (dative) | 0 | **REJECTED** |
| daj | give! (imperative) | 0 | **REJECTED** |
| chorzy | sick ones (plural) | 0 | **REJECTED** |
| chora | sick (feminine) | 0 | **REJECTED** |
| chorego | sick (genitive) | 0 | **REJECTED** |

These words were in the vocabulary file but **do not exist in the manuscript**.

### Category 2: Root + Suffix Patterns

| Claim | v7.5 Meaning | Actual Structure | Evidence | Status |
|-------|--------------|------------------|----------|--------|
| dar | dać (give) | d + ar | 179 stems take both -ar/-al | **REJECTED** |
| dal | dał (gave) | d + al | Same root as dar | **REJECTED** |
| chor | chory (sick) | ch + or | 174 stems take both -or/-ol | **REJECTED** |
| chol | flower | ch + ol | Same root as chor | **REJECTED** |
| sal | sól (salt) | s + al | 's' is productive root | **REJECTED** |
| sol | słońce (sun) | s + ol | 's' is productive root | **REJECTED** |
| kor | korzeń (root) | k + or | 'k' is productive root | **REJECTED** |
| kam | kąpać (bathe) | k + am | 'k' is productive root | **REJECTED** |
| ly | lej (pour) | l + y | 'l' is productive root | **REJECTED** |
| dan | dane (given) | d + an | 'd' is productive root | **REJECTED** |
| dam | dam (I give) | d + am | 'd' is productive root | **REJECTED** |
| oky | oczy (eyes) | ok + y | 'ok' is productive root | **REJECTED** |

### Category 3: Ambiguous (Too rare to be evidence)

| Claim | v7.5 Meaning | Count | Analysis | Status |
|-------|--------------|-------|----------|--------|
| oko | eye | 8 | Could be ok + o | **INSUFFICIENT** |
| chory | sick | 10 | Could be ch + or + y | **INSUFFICIENT** |

### Category 4: What Survives

**Nothing.**

---

## The Critical Discovery

The discovery that destroyed the Polish hypothesis:

```
174+ stems take BOTH -or and -ol suffixes
179+ stems take BOTH -ar and -al suffixes
```

Examples:
| Stem | -or form | -ol form |
|------|----------|----------|
| ch | chor (206) | chol (381) |
| sh | shor (92) | shol (175) |
| d | dor (70) | dol (111) |
| s | sor (54) | sol (67) |
| k | kor (25) | kol (37) |

This proves -or, -ol, -ar, -al are **productive grammatical suffixes**, not meaning-bearing parts of words.

Therefore:
- 'chor' is NOT Polish 'chory' — it's 'ch' + '-or'
- 'dar' is NOT Polish 'dać' — it's 'd' + '-ar'
- 'sal' is NOT Polish/Latin 'salt' — it's 's' + '-al'

---

## Why the Hypothesis Failed

The v7.5 decoder's methodology was flawed:

1. **Phonetic matching without morphological analysis**
   - Words were matched to Polish by sound alone
   - No checking whether they follow Voynich or Polish grammar

2. **Confirmation bias**
   - Words that "sounded Polish" were collected
   - Contradicting evidence (suffix patterns) was ignored

3. **Invented attestations**
   - 'choremu' was in the vocabulary but not in the corpus
   - Claims were made about words that don't exist

4. **Circular reasoning**
   - Assumed Polish → found "Polish words" → claimed proof of Polish

---

## What Remains True

The Voynich manuscript does have:

1. ✓ Regular morphological structure
2. ✓ Productive prefixes (qo-, o-, y-)
3. ✓ Productive suffixes (-aiin, -ain, -ar, -al, -or, -ol, -dy, -edy)
4. ✓ Section-based vocabulary variation
5. ✓ Systematic encoding of *something*

What we cannot claim:

1. ✗ That the language is Polish
2. ✗ That the language is Latin
3. ✗ That any specific word has any specific meaning
4. ✗ That our phonetic mappings are correct

---

## Conclusion

The Polish-Latin bilingual hypothesis, as implemented in v7.5, is **not supported by corpus evidence**.

The decoder produced plausible-sounding translations through:
- Superficial phonetic similarity
- Ignoring contradicting morphological patterns
- Including non-existent words in the vocabulary

This is linguistic pareidolia, not decipherment.

The Voynich manuscript remains **undeciphered**.

---

*Audit completed January 2026*
*Corpus-first methodology*
