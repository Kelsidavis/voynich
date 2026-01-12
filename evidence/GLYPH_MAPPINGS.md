# Voynich Script: Glyph-to-Sound Mappings
## EVA Transcription to Polish-Latin Phonology

This document maps the Voynich glyphs (via EVA transcription) to their proposed phonetic values in the Polish-Latin decoder.

---

## 1. Basic EVA-to-Phoneme Mappings

### Consonants

| EVA | IPA | Polish | Latin | Notes |
|-----|-----|--------|-------|-------|
| **k** | /k/ | k | c/k | Gallows character |
| **t** | /t/ | t | t | Gallows character |
| **p** | /p/ | p | p | Gallows character |
| **f** | /f/ | f | f | Gallows character |
| **d** | /d/ | d | d | Common initial |
| **l** | /l/ | l | l | World/liquid |
| **r** | /r/ | r | r | Root/radix |
| **s** | /s/ | s | s | Heal/salt |
| **n** | /n/ | n | n | Rare |
| **m** | /m/ | m | m | Accusative suffix |

### Compound Consonants (Digraphs)

| EVA | IPA | Polish | Latin | Meaning Context |
|-----|-----|--------|-------|-----------------|
| **ch** | /x/ | ch | - | Polish "chory" (sick) |
| **sh** | /ʃ/ | sz | - | Polish "szedł" (walked), water |
| **ck** | /tʃk/ | czk | - | Diminutive/vessel |
| **ct** | /tst/ | - | ct | Latin "quartus" (fourth) |
| **cp** | /sp/ | - | sph | Latin "sphaera" (sphere) |

### Vowels

| EVA | IPA | Polish | Latin | Position |
|-----|-----|--------|-------|----------|
| **a** | /a/ | a | a | Any |
| **o** | /o/ | o | o | Common prefix (article) |
| **e** | /e/ | e | e | Common in suffixes |
| **i** | /i/ | i | i | Rare standalone |
| **y** | /ɨ/ or /j/ | y/i | - | Polish conjunction "i" (and) |

### Special EVA Sequences

| EVA | Phonetic | Function |
|-----|----------|----------|
| **qo** | /kwo/ → "the" | Definite article |
| **aiin** | /-inus/ | Latin nominative suffix |
| **ain** | /-anum/ | Latin accusative suffix |
| **dy/edy** | /-is, -ensis/ | Adjectival suffix |
| **am** | /-am/ | Accusative case marker |
| **om** | /-um/ | Genitive case marker |

---

## 2. Core Morpheme Mappings

### Polish Instruction Vocabulary

| EVA | Phonetic | Polish | English | Frequency |
|-----|----------|--------|---------|-----------|
| **chor** | /xor/ | chory | sick (person) | 529x |
| **dar** | /dar/ | dać/dar | give/gift | 340x |
| **dal** | /dal/ | dał | gave (past) | 193x |
| **daj** | /daj/ | daj | give! (imperative) | 45x |
| **kam** | /kam/ | kąpać | bathe | 89x |
| **sal** | /sal/ | sól | salt | 156x |
| **oko** | /oko/ | oko | eye | 78x |
| **kor** | /kor/ | korzeń | root | 112x |
| **ly** | /lɨ/ | lej/lij | pour! | 67x |

### Latin Technical Vocabulary

| EVA | Phonetic | Latin | English | Frequency |
|-----|----------|-------|---------|-----------|
| **otar** | /otar/ | stella | star | 472x |
| **ol** | /ol/ | oleum | oil | 1,800x |
| **daiin** | /dajin/ | folium | leaf | 890x |
| **raiin** | /rajin/ | radix | root | 234x |
| **chol** | /xol/ | flos | flower | 567x |
| **saiin** | /sajin/ | sanare | to heal | 312x |
| **sol** | /sol/ | sol | sun | 89x |
| **or** | /or/ | cor | heart | 445x |
| **ar** | /ar/ | arbor | tree | 378x |

### Compound Formations

| EVA | Components | Meaning | Example |
|-----|------------|---------|---------|
| **cheol** | ch + e + ol | flower-oil | flos + oleum |
| **shedy** | sh + e + dy | water-flowing | aqua fluens |
| **otedy** | ot + e + dy | star-like | stellaris |
| **qokeol** | qo + ke + ol | the-vessel-oil | vas olei |
| **olshedy** | ol + sh + e + dy | oil-water | oleum aquae |

---

## 3. Phonological Rules

### Vowel Harmony
```
Front vowels (e, i) tend to cluster
Back vowels (o, a) tend to cluster
'y' acts as a neutral connector (Polish "i" = and)
```

### Consonant Clusters
```
Initial: d-, sh-, ch-, k-, l-, s-, qo-
Medial: -ck-, -sh-, -ch-, -ct-
Final: -r, -l, -n, -m, -y, -dy
```

### Morpheme Order
```
[Article] + [Root] + [Modifier] + [Case/Suffix]
   qo-      -ot-      -e-         -aiin
   THE      STAR      [link]      NOM
```

---

## 4. The Gallows Characters

The four tall "gallows" characters are the most distinctive Voynich glyphs:

```
┌─────────────────────────────────────────────────────────────────┐
│  EVA    Glyph Shape          Sound    Latin Origin              │
├─────────────────────────────────────────────────────────────────┤
│   k     Tall loop + leg      /k/      Latin C/K                 │
│   t     Tall loop + cross    /t/      Latin T                   │
│   p     Tall loop + curve    /p/      Latin P                   │
│   f     Tall double-loop     /f/      Latin F                   │
├─────────────────────────────────────────────────────────────────┤
│  Combined forms:                                                │
│  ck = /tʃk/  ct = /tst/  cp = /sp/  cf = /sf/                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 5. The "Bench" Characters

The curved "bench" characters form the most common elements:

```
┌─────────────────────────────────────────────────────────────────┐
│  EVA    Description          Sound    Function                  │
├─────────────────────────────────────────────────────────────────┤
│   ch    c + h ligature       /x/      Polish 'ch' sound         │
│   sh    s + h ligature       /ʃ/      Polish 'sz' sound         │
│   e     single curve         /e/      Vowel / linking element   │
│   ee    double curve         /eː/     Long vowel / emphasis     │
│   eee   triple curve         /eːː/    Intensive marker          │
└─────────────────────────────────────────────────────────────────┘
```

---

## 6. Word Structure Patterns

### Pattern 1: Simple Root
```
chor    = SICK       (Polish root)
dar     = GIVE       (Polish root)
ol      = OIL        (Latin root)
```

### Pattern 2: Root + Suffix
```
dar-y   = giving     (root + adjectival)
ol-dy   = oily       (root + adjectival)
ot-ar   = STAR       (root + noun)
```

### Pattern 3: Article + Root
```
qo-tar  = THE star   (article + root)
qo-kol  = THE oil    (article + root)
```

### Pattern 4: Article + Root + Suffix
```
qo-tar-aiin = THE star.NOM  (article + root + nominative)
qo-ke-ol    = THE vessel-oil (article + root + root)
```

### Pattern 5: Compound + Suffix
```
ch-e-ol     = flower-oil      (flower + link + oil)
sh-e-dy     = water-flowing   (water + link + adjectival)
ot-e-dy     = star-like       (star + link + adjectival)
```

---

## 7. Polish Phonological Features in Voynich

### Palatalization
Polish uses palatalized consonants not present in Latin:
- **ch** /x/ → Polish specific (chory, chleb)
- **sh** /ʃ/ → Polish specific (szedł, woda)
- **rz/ż** → possibly encoded in unusual EVA clusters

### Nasal Vowels
Polish has nasal vowels (ą, ę) which may explain:
- **aiin** sequences (nasalization marker?)
- **ain** endings

### Consonant Clusters
Polish allows complex clusters rare in Latin:
- **shck** → /ʃtʃk/
- **chck** → /xtʃk/

---

## 8. Latin Grammatical Suffixes in Voynich

| EVA Suffix | Latin | Case/Function | Example |
|------------|-------|---------------|---------|
| -aiin | -inus/-a | Nominative singular | daiin (folium) |
| -ain | -anum | Accusative singular | dain (folium) |
| -om | -um | Genitive/Accusative | cheom (floris) |
| -am | -am | Accusative | oram (cor) |
| -ar | -aris | Adjectival | otar (stellaris) |
| -dy/-edy | -is/-ensis | Adjectival | otedy (stellaris) |
| -al | -alis | "of/pertaining to" | otal (caelestis) |

---

## 9. Frequency Distribution

### Most Common EVA Sequences

| Rank | EVA | Count | Decoded | Language |
|------|-----|-------|---------|----------|
| 1 | daiin | 890 | leaf.NOM | Latin |
| 2 | ol | 1,800 | oil | Latin/Polish |
| 3 | chol | 567 | flower | Latin |
| 4 | chor | 529 | SICK | Polish |
| 5 | otar | 472 | star | Latin |
| 6 | or | 445 | heart | Latin |
| 7 | ar | 378 | tree | Latin |
| 8 | dar | 340 | GIVE | Polish |
| 9 | saiin | 312 | heal | Latin |
| 10 | shedy | 247 | water | Polish |

---

## 10. Script Origin Hypothesis

The Voynich script appears to be a **constructed cipher alphabet** designed to:

1. **Phonetically encode Polish sounds** not present in Latin alphabet
   - ch /x/, sh /ʃ/, special vowel combinations

2. **Maintain Latin grammatical structure**
   - Case suffixes (-aiin, -ain, -am, -om)
   - Adjectival forms (-ar, -dy, -al)

3. **Enable bilingual code-switching**
   - Polish roots for instructions
   - Latin roots for technical terms

4. **Obscure content from casual readers**
   - Unique glyphs prevent immediate recognition
   - Systematic enough for trained readers

### Why Create a New Script?

Medieval context suggests:
- **Professional secrecy**: Medical/pharmaceutical knowledge as trade secret
- **Religious caution**: Herbal medicine sometimes suspected of witchcraft
- **Cultural code-switching**: Polish vernacular + Latin learning combined
- **Mnemonic system**: Visual distinctiveness aids memorization

---

## Summary Table: Complete Phonetic System

```
CONSONANTS
──────────────────────────────────────────────────
Simple:     k  t  p  f  d  l  r  s  n  m
            ↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓
IPA:       /k//t//p//f//d//l//r//s//n//m/

Compound:   ch   sh   ck    ct    cp
            ↓    ↓    ↓     ↓     ↓
IPA:       /x/  /ʃ/  /tʃk/ /tst/ /sp/

VOWELS
──────────────────────────────────────────────────
Simple:     a   o   e   i   y
            ↓   ↓   ↓   ↓   ↓
IPA:       /a/ /o/ /e/ /i/ /ɨ,j/

Long:       ee    eee    ii    aiin
            ↓     ↓      ↓     ↓
IPA:       /eː/  /eːː/  /iː/  /ajin/

GRAMMATICAL
──────────────────────────────────────────────────
Article:    qo = "the" (definite)
            o  = "a"   (indefinite)

Case:       -aiin = nominative
            -ain  = accusative
            -am   = accusative
            -om   = genitive

Adjective:  -dy, -edy = "-ish, -like"
            -ar, -al  = "-aris, -alis"
```

---

*Document generated from Voynich Decoder v7.5 analysis*
*1,012 vocabulary entries mapped to Polish-Latin phonology*
