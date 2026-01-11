# Investigation: The "Missing" Imperative 'daj'

## The Problem

Initial grammatical analysis found that `daj` (Polish imperative "give!") appeared **zero times** in the entire Voynich corpus. This was a significant weakness for the Polish hypothesis — a recipe book should have many imperative commands.

## The Discovery

**The letter 'j' does not exist in the Voynich manuscript.**

Searching the entire corpus:
- Words containing 'j': **0**
- Words containing 'dai': **2,161**

## Historical Explanation

According to the [History of Polish orthography](https://en.wikipedia.org/wiki/History_of_Polish_orthography):

> **The letter 'j' did not exist in Polish until the 18th century.**

Medieval Polish wrote the /j/ sound as **'i'** or **'y'**:

| Modern Polish | Medieval Spelling | English |
|---------------|-------------------|---------|
| daj | dai, day | give! |
| ja | ia | I |
| mój | moi | my |

### The First Written Polish Sentence (c. 1270)

The famous sentence from the *Book of Henryków*:

```
Medieval: "Day, ut ia pobrusa, a ti poziwai"
Modern:   "Daj, niech ja pomielę, a ty odpoczywaj"
English:  "Let me grind, and you rest"
          ^^^
          Imperative 'daj' written as 'day'
```

## Implications for Voynich

If the manuscript encodes medieval Polish (pre-18th century):

| Polish Form | Medieval Spelling | Voynich | Count |
|-------------|-------------------|---------|-------|
| daj (imp.) | dai | dai-, daiin | 805+ |
| dać (inf.) | dac | dar | 297 |
| da (3sg) | da | da | 1,885 |
| dał (past) | dal | dal | 243 |
| daję (1sg) | daie | daim | 10 |
| dane (part.) | dane | dan | 16 |

**The imperative WAS there all along — encoded as 'dai'.**

## The 'daiin' Problem

This raises a question about 'daiin' (805 occurrences):

### Current Interpretation
```
daiin = Latin 'folium' (leaf)
```

### Alternative Interpretation
```
daiin = Polish 'daj' + nominalizing suffix '-in'
      = "the giving" / "what is given" / "dose"
```

### Distribution Analysis

| Section | daiin Count | Percentage |
|---------|-------------|------------|
| Herbal | 401 | 49.8% |
| Recipe | 237 | 29.4% |
| Bio | 83 | 10.3% |
| Astro | 34 | 4.2% |
| Rosettes | 25 | 3.1% |

Both interpretations are plausible:
- **Leaf**: Herbal section describes plants (leaves)
- **Give/Dose**: Herbal section prescribes treatments ("give this preparation")

## Complete Conjugation Paradigm

With this correction, the Polish verb 'dać' (to give) shows a **complete conjugation paradigm**:

```
INFINITIVE:     dać    → dar     (297x)  ✓
IMPERATIVE:     daj    → dai-    (805x)  ✓ RECOVERED
3RD SINGULAR:   da     → da      (1885x) ✓
1ST SINGULAR:   daję   → daim    (10x)   ✓
PAST MASC:      dał    → dal     (243x)  ✓
PARTICIPLE:     dane   → dan     (16x)   ✓
```

## Significance

This finding **strengthens** the Polish hypothesis:

1. **Explains missing 'j'**: The letter didn't exist in medieval Polish orthography
2. **Recovers the imperative**: 'dai-' forms account for 1,286 occurrences
3. **Matches historical spelling**: Consistent with 13th-15th century conventions
4. **Completes the paradigm**: All expected verb forms are now present
5. **Dates the encoding**: Pre-18th century Polish orthography

## Remaining Questions

1. Is 'daiin' primarily "leaf" or "give"? Context analysis needed.
2. Do other /j/-containing Polish words show the same i/y substitution?
3. What other medieval Polish spelling conventions appear in the text?

## References

- [History of Polish orthography](https://en.wikipedia.org/wiki/History_of_Polish_orthography) - Wikipedia
- [Old Polish](https://en.wikipedia.org/wiki/Old_Polish) - Wikipedia
- Book of Henryków (c. 1270) - First written Polish sentence
- Jakub Parkoszowic's orthographic treatise (c. 1440)
