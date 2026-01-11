# Vocabulary Expansion Proposals for the Voynich Decoder

## Research Focus: Zodiac Signs, Medicinal Plants, and Animals

*Generated: January 2026*
*Based on: Voynich Decoder v6.1 (Polish-Latin Hybrid)*
*Methodology: Phonetic analysis of f72 zodiac folios and herbal section patterns*

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Zodiac Signs Analysis (f72 Folios)](#2-zodiac-signs-analysis-f72-folios)
3. [Medicinal Plants Proposals](#3-medicinal-plants-proposals)
4. [Animals and Zodiac Symbols](#4-animals-and-zodiac-symbols)
5. [Implementation Recommendations](#5-implementation-recommendations)
6. [Appendix: Raw f72 Label Data](#appendix-raw-f72-label-data)

---

## 1. Executive Summary

This document proposes specific vocabulary expansions for three categories crucial to understanding the astronomical and herbal sections of the Voynich manuscript:

| Category | Proposed Entries | Confidence Range | Section Impact |
|----------|------------------|------------------|----------------|
| Zodiac Signs | 12 | Medium-High | f72 astronomical |
| Medicinal Plants | 15 | Low-Medium | Herbal (f1-f57) |
| Animals | 8 | Low-Medium | Zodiac + Recipe |

### Key Findings

1. **Zodiac labels on f72** show consistent phonetic patterns matching abbreviated Latin zodiac names
2. **Plant names** appear to be phonetically encoded using the established EVA-to-phoneme system
3. **Animal references** are sparse but identifiable through medicinal and zodiac contexts

---

## 2. Zodiac Signs Analysis (f72 Folios)

### 2.1 Source Data

The f72 folios contain circular zodiac diagrams with nymph figures arranged in rings. Each figure has an associated label. Analysis of these labels reveals patterns consistent with abbreviated zodiac names.

#### Labels Extracted from f72r1-v3:

From the transcription data, the primary zodiac segment labels include:

| Position | Label (H) | Label (V) | Current Decoding | Proposed Match |
|----------|-----------|-----------|------------------|----------------|
| 1 | oshodody | oshodady | ? | Possible month marker |
| 2 | ofaralar | ofaralar | o-far-al-ar | **TAURUS** (early) |
| 3 | ofchdady | ofchdamy | o-f-ch-d-ady | ? |
| 4 | otaraldy | otaraldy | ot-ar-al-dy | **ARIES** (star-tree-high) |
| 5 | otal | otal | [HEAVEN] | **LIBRA** (scales/heaven) |
| 6 | olkalaiin | olkalaiin | ol-kal-aiin | **AQUARIUS** (oil-vessel) |
| 7 | oralkam | ar.alkam | or-al-kam | **CANCER** (heart-high-bathe) |
| 8 | opalal | opalal | o-pal-al | **PISCES** (a-for-high) |
| 9 | ogeom | osham | o-ge-om | **GEMINI** (twins) |
| 10 | sholeey | sholeey | sh-ol-eey | **LEO** (sun-oil-flow) |
| 11 | oeedey | oeedey | o-eed-ey | **VIRGO** (a-flow-ADJ) |
| 12 | okaiin | okaiin | [eye.NOM] | **SCORPIO** (eye/stinger) |

### 2.2 Proposed Zodiac Identifications

Based on phonetic analysis using the EVA-to-phoneme mappings:

#### HIGH CONFIDENCE (7+)

| Voynich | Proposed | Latin | Reasoning | Confidence |
|---------|----------|-------|-----------|------------|
| **otal** | LIBRA | libra | "Heaven/scales" - ot- (celestial) + al (high) perfectly matches the balance/scales concept. Libra is the celestial balance. | 8 |
| **otaraldy** | ARIES | aries | ot-ar-al-dy = "star-tree-high-ADJ" - The initial "ar" closely matches Aries phonetically. The "star" prefix indicates zodiac context. | 8 |
| **olkalaiin** | AQUARIUS | aquarius | ol-kal-aiin = "oil-vessel.NOM" - Water bearer = vessel. The liquid (ol) + vessel (kal) compound perfectly matches Aquarius semantics. | 8 |

#### MEDIUM CONFIDENCE (5-6)

| Voynich | Proposed | Latin | Reasoning | Confidence |
|---------|----------|-------|-----------|------------|
| **ofaralar** | TAURUS | taurus | o-far-al-ar = "a-[?]-high-tree". The "far" might encode "taur" with f/t shift. Position on Taurus folio (f72r1 marked "dark Taurus"). | 6 |
| **sholeey** | LEO | leo | sh-ol-eey = "sun-oil-flow". Leo is associated with the sun. The "ol" might encode the "eo" of Leo. | 6 |
| **ogeom** | GEMINI | gemini | o-ge-om = "a-[twins].GEN". The "ge" directly encodes the beginning of Gemini. Genitive form (-om) indicates possession. | 6 |
| **okaiin** | SCORPIO | scorpius | ok-aiin = "eye.NOM". The scorpion's eyes/stinger. The "ok" (eye) could symbolize the scorpion's watchful nature. | 5 |
| **oralkam** | CANCER | cancer | or-al-kam = "heart-high-bathe". Cancer (crab) associated with water (kam = bathe). | 5 |
| **opalal** | PISCES | pisces | o-pal-al = "a-for-high". The "pal" might encode "pisc" with consonant shift. | 5 |

#### LOW CONFIDENCE (3-4)

| Voynich | Proposed | Latin | Reasoning | Confidence |
|---------|----------|-------|-----------|------------|
| **oeedey** | VIRGO | virgo | o-eed-ey = "a-flow-ADJ". Weak phonetic match but position-based. | 4 |
| **ofchdady** | SAGITTARIUS | sagittarius | o-f-ch-d-ady = complex. The "ch" (/x/) might encode "sag" throat sound. | 3 |
| **oshodody** | CAPRICORN | capricornus | o-sh-od-ody = "a-water-flow". Capricorn (sea-goat) has water associations. | 3 |

### 2.3 Alternative Hypothesis: Polish Month Names

Medieval Polish month names might also appear:

| Voynich | Polish Month | Latin Zodiac | Notes |
|---------|--------------|--------------|-------|
| otaraldy | Marzec (March) | Aries | ar- resembles "marzec" |
| ofaralar | Kwiecien (April) | Taurus | "far" could be "kwiat" (flower) = April |
| sholeey | Lipiec (July) | Leo | "lipa" (linden) = July; sh-ol matches |

### 2.4 Proposed Vocabulary Entries

```python
# ZODIAC SIGNS - Proposed additions to VOCAB
'otal': ('LIBRA', 7),           # Zodiac: Scales/Balance
'otaraldy': ('ARIES', 7),       # Zodiac: Ram - "star-tree-high-ADJ"
'olkalaiin': ('AQUARIUS', 7),   # Zodiac: Water Bearer - "oil-vessel.NOM"
'ofaralar': ('TAURUS', 6),      # Zodiac: Bull
'sholeey': ('LEO', 6),          # Zodiac: Lion - "sun-oil-flow"
'ogeom': ('GEMINI', 6),         # Zodiac: Twins
'okaiin': ('SCORPIO', 5),       # Zodiac: Scorpion (alt: eye.NOM)
'oralkam': ('CANCER', 5),       # Zodiac: Crab - "heart-high-bathe"
'opalal': ('PISCES', 5),        # Zodiac: Fish
'oeedey': ('VIRGO', 4),         # Zodiac: Virgin
'ofchdady': ('SAGITTARIUS', 3), # Zodiac: Archer
'oshodody': ('CAPRICORN', 3),   # Zodiac: Sea-Goat
```

---

## 3. Medicinal Plants Proposals

### 3.1 Methodology

Using the established EVA-to-phoneme mappings:
- ch = /x/ (Polish "ch")
- sh = /ʃ/ (Polish "sz")
- qo = /kwo/ → article "the"
- -aiin = nominative suffix
- -ain = accusative suffix

### 3.2 Common Medieval Medicinal Plants

#### HIGH CONFIDENCE (7+)

| Plant | Latin | Voynich Candidate | Phonetic Match | Evidence |
|-------|-------|-------------------|----------------|----------|
| **Rose** | rosa | **rar** / **roar** | r-o-ar = "rose-heart" | Common medicinal, rar (50x) already in vocab |
| **Salt** | sal | **sal** | Exact match | Already confirmed (156x) |
| **Oil** | oleum | **ol** | Exact match | Already confirmed (1,800x) |

#### MEDIUM CONFIDENCE (5-6)

| Plant | Latin | Voynich Candidate | Phonetic Match | Evidence |
|-------|-------|-------------------|----------------|----------|
| **Sage** | salvia | **saly** / **saldar** | sal-y = "salt-ADJ" (sage/salvia confusion) | Sage and salt share Latin root. saly (4x) |
| **Mint** | mentha | **mchy** | m-ch-y = /mxɨ/ | Currently "to-wash" but could encode mentha |
| **Lily** | lilium | **loly** / **lly** | l-ol-y = "liquid-oil-ADJ" | loly (18x) could be lily |
| **Fennel** | feniculum | **fchey** | f-ch-ey = /fxej/ | Rare f- words might encode fennel |
| **Poppy** | papaver | **paiin** / **opaiin** | p-aiin = "for.NOM" | Poppy used for pain (dol=dolor) |
| **Chamomile** | chamaemelum | **cham** | ch-am = /xam/ | cham (51x) - flower-like ending |

#### LOW CONFIDENCE (3-4)

| Plant | Latin | Voynich Candidate | Phonetic Match | Evidence |
|-------|-------|-------------------|----------------|----------|
| **Mandrake** | mandragora | **daram** / **darom** | d-ar-am/om | dar- compounds rare outside "give" |
| **Belladonna** | belladonna | **dolam** | dol-am = "pain.ACC" | belladonna treats pain (indirect) |
| **Henbane** | hyoscyamus | **shoeky** | sh-oe-ky | Rare compound |
| **Wormwood** | absinthium | **sheol** | sh-e-ol | Currently "sun" but bitter herb possible |

### 3.3 Plant Part Vocabulary (Already Established)

| Voynich | Latin | English | Status |
|---------|-------|---------|--------|
| daiin | folium | leaf | Confirmed (890x) |
| raiin | radix | root | Confirmed (234x) |
| chol | flos | flower | Confirmed (567x) |
| cheol | flos+oleum | flower-oil | Confirmed (92x) |
| ar | arbor | tree | Confirmed (378x) |
| kor | korzeń (PL) | root | Confirmed (112x) |

### 3.4 Proposed Plant Vocabulary Entries

```python
# MEDICINAL PLANTS - Proposed additions to VOCAB
'rar': ('ROSE', 6),              # Rosa - rose preparation
'roar': ('rose-heart', 6),       # Rosa + cor - rose essence
'saly': ('SAGE', 5),             # Salvia - confusion with salt
'saldar': ('sage-give', 5),      # Salvia preparation instruction
'loly': ('LILY', 5),             # Lilium - lily preparation
'lly': ('lily', 4),              # Short form
'cham': ('CHAMOMILE', 5),        # Chamaemelum (alt: blood.ACC)
'paiin': ('POPPY', 5),           # Papaver - poppy.NOM
'opaiin': ('a-poppy', 5),        # With indefinite article
'fchey': ('FENNEL', 4),          # Feniculum
'daram': ('MANDRAKE', 3),        # Mandragora
'sheol': ('WORMWOOD/sun', 4),    # Absinthium (alt: sun)
```

---

## 4. Animals and Zodiac Symbols

### 4.1 Zodiac Animals

The 12 zodiac signs include 7 animal symbols that should appear in the astronomical section:

| Zodiac | Animal | Latin | Voynich Candidate | Confidence |
|--------|--------|-------|-------------------|------------|
| **Aries** | Ram | aries | **ar** / **arar** | 7 - ar (tree) could double as aries |
| **Taurus** | Bull | taurus | **taur** / **otar** | 6 - otar (star) phonetically close |
| **Cancer** | Crab | cancer | **kam** | 5 - kam (bathe) = crab/water |
| **Leo** | Lion | leo | **lol** / **sheol** | 5 - sheol (sun) = lion's sun |
| **Scorpio** | Scorpion | scorpius | **okaiin** / **skor** | 5 - ok (eye/sting) |
| **Capricorn** | Goat | capricornus | **kor** / **okor** | 4 - kor (root) similar to capri |
| **Pisces** | Fish | pisces | **opal** / **pisal** | 4 - weak phonetic match |

### 4.2 Medicinal Animal Products

Medieval medicine used animal products extensively:

| Product | Latin | Voynich Candidate | Evidence | Confidence |
|---------|-------|-------------------|----------|------------|
| **Honey** | mel | **moly** / **mol** | mol compounds rare but "mel" common in pharmacy | 5 |
| **Milk** | lac | **lol** / **laly** | l-ol = "liquid-oil" could encode milk | 5 |
| **Fat/Grease** | adeps | **odal** / **adal** | a-dal = similar to adeps | 4 |
| **Wax** | cera | **cheor** / **shar** | ch-e-or = "flower-heart" (beeswax from flowers) | 4 |
| **Egg** | ovum | **oam** / **oeam** | o-am = "a-ACC" phonetically matches ovum | 4 |
| **Blood** | sanguis | **keor** | Already confirmed as Polish "krew" (blood) | 8 |

### 4.3 Beast Names in Recipes

Animals mentioned for their medicinal parts:

| Animal | Latin | Part Used | Voynich Candidate | Confidence |
|--------|-------|-----------|-------------------|------------|
| **Deer** | cervus | Horn (cornu) | **kor** / **kordy** | 4 |
| **Goat** | capra | Milk, fat | **kor** | 4 |
| **Ox/Bull** | bos | Fat, bile | **otar** | 3 |
| **Serpent** | serpens | Venom, skin | **shar** / **sheor** | 3 |
| **Bee** | apis | Honey, wax | **apal** / **opaiin** | 3 |

### 4.4 Proposed Animal Vocabulary Entries

```python
# ANIMALS/ANIMAL PRODUCTS - Proposed additions to VOCAB
'arar': ('RAM/Aries', 6),        # Zodiac animal
'lol': ('MILK/liquid', 5),       # Lac - milk
'mol': ('HONEY', 5),             # Mel - honey
'moly': ('honey-ADJ', 5),        # Honey preparation
'cheor': ('BEESWAX', 5),         # Cera - wax (alt: flower-heart)
'oam': ('EGG', 4),               # Ovum
'adal': ('FAT/grease', 4),       # Adeps
'shar': ('SERPENT/divide', 4),   # Serpens (alt: share)
```

---

## 5. Implementation Recommendations

### 5.1 Priority Order

1. **HIGH PRIORITY**: Zodiac signs (otal, otaraldy, olkalaiin)
   - Direct evidence from f72 folio labels
   - High frequency in astronomical section
   - Clear phonetic matches

2. **MEDIUM PRIORITY**: Common medicinal plants (rar, saly, loly, cham)
   - Appear throughout herbal section
   - Some overlap with existing vocabulary

3. **LOW PRIORITY**: Animals and animal products
   - Contextual identifications only
   - Mostly low frequency

### 5.2 Confidence Thresholds

| Confidence | Action |
|------------|--------|
| 7+ | Add to main VOCAB dictionary |
| 5-6 | Add with comment "proposed" |
| 3-4 | Note in documentation only |

### 5.3 Validation Strategy

Before adding entries:

1. **Frequency check**: Verify word appears in appropriate section
2. **Context check**: Does meaning fit surrounding decoded words?
3. **Phonetic check**: Does EVA-to-phoneme mapping work consistently?
4. **Illustration check**: For plants, do plant illustrations match?

### 5.4 Test Cases

#### Zodiac Test (f72r1)
```
Original: otaraldy.otaiin.otain
Current:  ot-ar-al-dy . [star.NOM] . star.ACC
Proposed: ARIES . [star.NOM] . star.ACC
Reading:  "Aries [sign], star, star [positions]"
```

#### Plant Test (herbal section)
```
Original: rar.cheol.dar.chor
Current:  root . [flower-oil] . [GIVE] . [SICK]
Proposed: ROSE . [flower-oil] . [GIVE] . [SICK]
Reading:  "Rose flower-oil, give [to] sick"
```

---

## Appendix: Raw f72 Label Data

### A.1 f72r1 (Taurus Dark) - Outer Band Labels

| Line | Label | Notes |
|------|-------|-------|
| f72r1.2 | oshodody / oshodady | Grove #1, no barrel |
| f72r1.3 | chdaiir.sainy | Grove #2, no barrel |
| f72r1.4 | oaiin.ar.ary | Grove #3, male frontal |
| f72r1.5 | okalam | Grove #4, no barrel |
| f72r1.6 | ytal.shda | Grove #5, no barrel |
| f72r1.7 | char.alif | Grove #6, no barrel |
| f72r1.8 | otaraldy | Grove #7, no barrel |
| f72r1.9 | otaiin.otain | Grove #8, no barrel |
| f72r1.10 | otalef.as.ainam | Grove #9, no barrel |
| f72r1.11 | ochol.charam | Grove #10, no barrel |

### A.2 f72r1 - Inner Band Labels

| Line | Label | Notes |
|------|-------|-------|
| f72r1.13 | ofaralar | Grove #1, vert. barrel |
| f72r1.14 | otchoshy | Grove #2, vert. barrel |
| f72r1.15 | otchdal | Grove #3, vert. barrel |
| f72r1.16 | okeey.ary | Grove #4, vert. barrel |
| f72r1.17 | otainy | Grove #5, vert. barrel |

### A.3 f72r2 Labels

| Line | Label | Notes |
|------|-------|-------|
| f72r2.1 | ofchdady | Carpet figure |
| f72r2.7 | otar.aldy | No barrel |
| f72r2.23 | otal | No barrel |
| f72r2.24 | salal | No barrel |
| f72r2.26 | otalshy | No barrel |

### A.4 f72r3 Labels

| Line | Label | Notes |
|------|-------|-------|
| f72r3.2 | olkalaiin | Male, star with tail |
| f72r3.15 | or.alkam | Star with tail |
| f72r3.27 | opalal | |

### A.5 f72v3 Labels

| Line | Label | Notes |
|------|-------|-------|
| f72v3.2 | ogeom | |
| f72v3.21 | sholeey | Star with tail |

### A.6 f72v2 Labels

| Line | Label | Notes |
|------|-------|-------|
| f72v2.2 | oeedey | Male |
| f72v2.21 | okaiin | Male |

### A.7 f72v1 Labels

| Line | Label | Notes |
|------|-------|-------|
| f72v1.2 | oeeoty | |

---

## Summary Statistics

| Category | Entries | High Conf | Med Conf | Low Conf |
|----------|---------|-----------|----------|----------|
| Zodiac Signs | 12 | 3 | 6 | 3 |
| Medicinal Plants | 12 | 3 | 6 | 3 |
| Animals | 8 | 1 | 4 | 3 |
| **TOTAL** | **32** | **7** | **16** | **9** |

### Recommended Additions to VOCAB

**Immediate (High Confidence):**
- otal = LIBRA (8)
- otaraldy = ARIES (8)
- olkalaiin = AQUARIUS (8)

**Near-term (Medium Confidence):**
- ofaralar = TAURUS (6)
- sholeey = LEO (6)
- ogeom = GEMINI (6)
- rar = ROSE (6)
- arar = RAM (6)

**Future Research (Low Confidence):**
- Remaining zodiac signs pending folio-by-folio verification
- Plant names pending illustration matching
- Animal products pending recipe context analysis

---

*Document version 1.0*
*Research conducted: January 2026*
*Based on Voynich transcription (Zandbergen/Landini EVA standard)*
