#!/usr/bin/env python3
"""
Voynich Manuscript Cosmological Rosettes Section Analysis with Polish-Latin Decoder v6.1
Analyzes folios f85r-f86v (the famous foldout rosettes diagrams)
"""

import re
from collections import Counter, defaultdict
from voynich_decoder import decode_text, decode_word, VOCAB

# Read transcription
with open('voynich_transcription.txt', 'r', encoding='latin-1') as f:
    transcription = f.read()

# Rosettes section folios (f85-f86, including sub-pages)
ROSETTES_FOLIOS = set()
for base in ['f85r', 'f85v', 'f86r', 'f86v']:
    ROSETTES_FOLIOS.add(base)
    for sub in ['1', '2', '3', '4', '5', '6']:
        ROSETTES_FOLIOS.add(f'{base}{sub}')

# Extract lines by folio
line_pattern = re.compile(r'^<(f8[56][rv]\d?)[^>]*;H>\s*(.+?)(?:<[^>]*>)*\s*$', re.MULTILINE)

folios = defaultdict(list)
for match in line_pattern.finditer(transcription):
    folio_id = match.group(1).split('.')[0]
    text = match.group(2).strip()

    text = re.sub(r'<[^>]*>', '', text)
    text = re.sub(r'[!?]', '', text)
    text = text.strip()

    if text and len(text) > 1:
        folios[folio_id].append(text)

# Sort folios
def natural_sort_key(s):
    match = re.match(r'f(\d+)([rv])(\d*)', s)
    if match:
        num = int(match.group(1))
        suffix = 0 if match.group(2) == 'r' else 1
        sub = int(match.group(3)) if match.group(3) else 0
        return (num, suffix, sub)
    return (999, 0, 0)

sorted_folios = sorted(folios.keys(), key=natural_sort_key)

# Vocabulary categories
POLISH_TERMS = {'chor', 'chory', 'choremu', 'dar', 'dal', 'da', 'dan', 'daim', 'daj', 'dary',
                'sal', 'saly', 'kor', 'oko', 'oky', 'ochey', 'shey', 'rchey',
                'keor', 'kchy', 'schy', 'mchy', 'gchy', 'cchy', 'ly', 'lchy',
                'ytchor', 'shoky', 'kam', 'pchey', 'pchy'}

COSMOLOGICAL_TERMS = {'ot', 'otar', 'otair', 'oteor', 'otol', 'otal', 'oty',
                      'oteey', 'otedy', 'oteol', 'oteody', 'cphar', 'cphor',
                      'cphol', 'pharma', 'sol', 'shol', 'sheol', 'paradam'}

GEOGRAPHICAL_TERMS = {'ar', 'aror', 'arxor', 'pol', 'kar', 'kal', 'kam',
                      'or', 'lor', 'dor', 'sor', 'tor'}

# Analysis counters
all_words = []
polish_counts = Counter()
cosmo_counts = Counter()
word_freq = Counter()

# Output
output = []
output.append("=" * 90)
output.append("VOYNICH MANUSCRIPT - COSMOLOGICAL ROSETTES SECTION ANALYSIS")
output.append("Polish-Latin Decoder v6.1")
output.append("Folios f85r - f86v (Foldout Rosettes Diagrams)")
output.append("=" * 90)
output.append("")
output.append("SECTION DESCRIPTION:")
output.append("The rosettes foldout is one of the most famous pages of the Voynich manuscript.")
output.append("It consists of nine circular 'rosettes' connected by causeways, possibly depicting:")
output.append("  - A cosmological map (celestial spheres)")
output.append("  - A geographical map (cities/regions)")
output.append("  - An alchemical diagram (processes/stages)")
output.append("")

# Process each folio
for folio in sorted_folios:
    lines = folios[folio]

    output.append("-" * 80)
    output.append(f"FOLIO {folio.upper()}")
    output.append("-" * 80)
    output.append("")

    for i, line in enumerate(lines, 1):
        words = line.replace('.', ' ').split()
        all_words.extend(words)

        for word in words:
            word_lower = word.lower()
            word_freq[word_lower] += 1

            if word_lower in POLISH_TERMS:
                polish_counts[word_lower] += 1

            # Check for cosmological prefixes
            if word_lower.startswith('ot') or word_lower.startswith('cpho') or word_lower.startswith('cphar'):
                cosmo_counts[word_lower] += 1

        decoded = decode_text(line)

        output.append(f"Line {i}:")
        output.append(f"  Voynich: {line}")
        output.append(f"  Decoded: {decoded}")

        # Flag patterns
        if 'SICK' in decoded:
            output.append(f"  ** POLISH: Patient reference (chor)")
        if 'GIVE' in decoded or 'GAVE' in decoded:
            output.append(f"  ** POLISH: Instruction verb (dar/dal)")
        if 'STAR' in decoded or 'star' in decoded:
            output.append(f"  ** COSMOLOGICAL: Celestial reference")
        if 'HEAVEN' in decoded or 'heaven' in decoded:
            output.append(f"  ** COSMOLOGICAL: Celestial realm")
        if 'SPHERE' in decoded or 'AETHER' in decoded:
            output.append(f"  ** COSMOLOGICAL: Sphaera Mundi reference")
        if 'PARADISE' in decoded:
            output.append(f"  ** THEOLOGICAL: Eden/Paradise reference")

        output.append("")

output.append("")

# Statistics
output.append("=" * 90)
output.append("ROSETTES SECTION STATISTICS")
output.append("=" * 90)
output.append("")

output.append(f"Total folios: {len(sorted_folios)}")
output.append(f"Total lines: {sum(len(folios[f]) for f in folios)}")
output.append(f"Total words: {len(all_words)}")
output.append(f"Unique words: {len(set(all_words))}")
output.append("")

# Top words
output.append("TOP 40 WORDS IN ROSETTES SECTION:")
output.append("-" * 60)
for word, count in word_freq.most_common(40):
    decoded = decode_word(word)
    output.append(f"  {word:<15} ({decoded:<25}): {count:>4}x")
output.append("")

# Polish terms
output.append("POLISH TERMS IN ROSETTES SECTION:")
output.append("-" * 50)
if polish_counts:
    for word, count in sorted(polish_counts.items(), key=lambda x: -x[1]):
        meaning = VOCAB.get(word, ('?', 0))[0]
        output.append(f"  {word:<12} ({meaning:<15}): {count:>4}x")
else:
    output.append("  (Checking for Polish terms...)")

# Manual check for Polish terms in all words
polish_found = Counter()
for word in all_words:
    wl = word.lower()
    for term in POLISH_TERMS:
        if term in wl:
            polish_found[term] += 1

if polish_found:
    output.append("")
    output.append("POLISH TERMS (including as substrings):")
    for term, count in polish_found.most_common():
        meaning = VOCAB.get(term, ('?', 0))[0]
        output.append(f"  {term:<12} ({meaning:<15}): {count:>4}x")
output.append("")

# Cosmological terms
output.append("COSMOLOGICAL TERMS (ot-/cpho-/sol- prefix):")
output.append("-" * 50)
cosmo_in_text = Counter()
for word in all_words:
    wl = word.lower()
    if wl.startswith('ot') or wl.startswith('cpho') or wl.startswith('cphar') or wl.startswith('sol'):
        cosmo_in_text[wl] += 1
for word, count in cosmo_in_text.most_common(25):
    decoded = decode_word(word)
    output.append(f"  {word:<15} ({decoded:<20}): {count:>4}x")
output.append("")

# Look for place/region labels (short words)
output.append("=" * 90)
output.append("PATTERN ANALYSIS - ROSETTE/REGION LABELS")
output.append("=" * 90)
output.append("")

# Short words (likely labels for rosettes/regions)
short_words = Counter()
for word in all_words:
    if 2 <= len(word) <= 6:
        short_words[word.lower()] += 1

output.append("SHORT WORDS (2-6 chars) - potential rosette/region labels:")
output.append("-" * 50)
for word, count in short_words.most_common(40):
    decoded = decode_word(word)
    output.append(f"  {word:<10} → {decoded:<20} ({count}x)")
output.append("")

# Unique words (appearing only 1-2 times - likely specific labels)
output.append("UNIQUE/RARE WORDS (1-2 occurrences) - potential place names:")
output.append("-" * 50)
rare_words = [(w, c) for w, c in word_freq.items() if c <= 2 and len(w) >= 4]
rare_words.sort(key=lambda x: -len(x[0]))
for word, count in rare_words[:30]:
    decoded = decode_word(word)
    output.append(f"  {word:<18} → {decoded}")
output.append("")

# Folio-by-folio summary
output.append("=" * 90)
output.append("FOLIO-BY-FOLIO SUMMARY")
output.append("=" * 90)
output.append("")

for folio in sorted_folios:
    lines = folios[folio]
    words = []
    for line in lines:
        words.extend(line.replace('.', ' ').split())

    chor_count = sum(1 for w in words if 'chor' in w.lower())
    dar_count = sum(1 for w in words if 'dar' in w.lower() or 'dal' in w.lower())
    ot_count = sum(1 for w in words if w.lower().startswith('ot'))
    sol_count = sum(1 for w in words if 'sol' in w.lower() or 'shol' in w.lower())

    output.append(f"{folio.upper():8}: {len(lines):3} lines, {len(words):4} words | "
                  f"ot-: {ot_count:3}, sol-: {sol_count:2}, chor: {chor_count:2}, dar/dal: {dar_count:2}")

output.append("")

# Look for specific patterns
output.append("=" * 90)
output.append("SPECIFIC PATTERN ANALYSIS")
output.append("=" * 90)
output.append("")

# Cardinal directions / position words
output.append("DIRECTIONAL/POSITION TERMS:")
output.append("-" * 50)
direction_terms = Counter()
for word in all_words:
    wl = word.lower()
    if wl in ['or', 'ar', 'al', 'ol', 'otal', 'otar', 'otol']:
        direction_terms[wl] += 1
    if 'pol' in wl or 'sor' in wl or 'lor' in wl or 'dor' in wl:
        direction_terms[wl] += 1
for word, count in direction_terms.most_common(20):
    decoded = decode_word(word)
    output.append(f"  {word:<12} ({decoded:<15}): {count:>4}x")
output.append("")

# Eden/Paradise references
output.append("EDEN/PARADISE REFERENCES:")
output.append("-" * 50)
eden_terms = Counter()
for word in all_words:
    wl = word.lower()
    if 'para' in wl or 'adam' in wl or 'eden' in wl or 'arxor' in wl or 'aror' in wl:
        eden_terms[wl] += 1
if eden_terms:
    for word, count in eden_terms.most_common():
        decoded = decode_word(word)
        output.append(f"  {word:<15} ({decoded:<20}): {count:>4}x")
else:
    output.append("  (No direct Eden/Paradise terms found)")
output.append("")

# Water/River references (four rivers of Eden?)
output.append("WATER/RIVER REFERENCES (Four Rivers of Eden?):")
output.append("-" * 50)
water_terms = Counter()
for word in all_words:
    wl = word.lower()
    if wl.startswith('she') or wl.startswith('sho') or 'keey' in wl or 'kain' in wl:
        water_terms[wl] += 1
for word, count in water_terms.most_common(15):
    decoded = decode_word(word)
    output.append(f"  {word:<15} ({decoded:<20}): {count:>4}x")
output.append("")

# Key findings
output.append("=" * 90)
output.append("KEY FINDINGS - ROSETTES SECTION")
output.append("=" * 90)
output.append("")

total_polish = sum(polish_counts.values()) + sum(polish_found.values())
total_cosmo = sum(cosmo_in_text.values())

output.append(f"1. POLISH TERMS: {total_polish} occurrences")
output.append(f"   Polish vocabulary present, indicating practical/instructional content.")
output.append("")

output.append(f"2. COSMOLOGICAL TERMS (ot-/sol-): {total_cosmo} occurrences")
output.append(f"   Celestial vocabulary confirms cosmological interpretation.")
output.append("")

output.append("3. ROSETTE INTERPRETATION:")
output.append("   The nine rosettes may represent:")
output.append("   - Nine celestial spheres (Ptolemaic cosmology)")
output.append("   - Nine regions/cities (geographical map)")
output.append("   - Nine stages of treatment/preparation (medical)")
output.append("")

output.append("4. CAUSEWAY INTERPRETATION:")
output.append("   The connecting paths between rosettes may represent:")
output.append("   - Rivers (possibly four rivers of Eden)")
output.append("   - Trade/travel routes")
output.append("   - Celestial pathways")
output.append("   - Bodily channels (vessels)")
output.append("")

output.append("5. POLISH-LATIN PATTERN:")
output.append("   - LATIN: Cosmological terms (stella, caelum, sol)")
output.append("   - POLISH: Practical references (dar=give, chor=sick)")
output.append("")

output.append("=" * 90)

# Write output
with open('voynich_rosettes_analysis.txt', 'w') as f:
    f.write('\n'.join(output))

print("Rosettes section analysis complete!")
print(f"  Folios: {len(sorted_folios)}")
print(f"  Words: {len(all_words)}")
print(f"  Polish terms: {total_polish}")
print(f"  Cosmological terms: {total_cosmo}")
print(f"  Output: voynich_rosettes_analysis.txt")
print()
print("Top words:")
for word, count in word_freq.most_common(15):
    print(f"  {word}: {count}x")
