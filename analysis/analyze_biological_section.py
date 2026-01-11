#!/usr/bin/env python3
"""
Voynich Manuscript Biological/Nymph Section Analysis with Polish-Latin Decoder v6.1
Analyzes folios f75r through f84v (nude female figures, baths, tubes)
"""

import re
from collections import Counter, defaultdict
from voynich_decoder import decode_text, decode_word, VOCAB

# Read transcription
with open('voynich_transcription.txt', 'r', encoding='latin-1') as f:
    transcription = f.read()

# Biological/Nymph section folios (f75-f84)
BIO_FOLIOS = set()
for i in range(75, 85):
    BIO_FOLIOS.add(f'f{i}r')
    BIO_FOLIOS.add(f'f{i}v')

# Extract lines by folio
line_pattern = re.compile(r'^<(f\d+[rv]\d?)[^>]*;H>\s*(.+?)(?:<[^>]*>)*\s*$', re.MULTILINE)

folios = defaultdict(list)
for match in line_pattern.finditer(transcription):
    folio_id = match.group(1).split('.')[0]
    text = match.group(2).strip()

    text = re.sub(r'<[^>]*>', '', text)
    text = re.sub(r'[!?]', '', text)
    text = text.strip()

    if text and len(text) > 1:
        base_folio = re.match(r'f(\d+)[rv]', folio_id)
        if base_folio:
            num = int(base_folio.group(1))
            if 75 <= num <= 84:
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

BODY_TERMS = {'or', 'cor', 'chy', 'keor', 'oko', 'oky', 'ochey', 'shey', 'rchey',
              'chey', 'cheor', 'chor', 'kar', 'kal'}

WATER_TERMS = {'she', 'shey', 'sho', 'shol', 'sheol', 'shedy', 'sheey', 'sheody',
               'shar', 'shor', 'shy', 'shem'}

FLOW_TERMS = {'qokeey', 'okeey', 'keey', 'cheey', 'qokeedy', 'okeedy', 'chedy',
              'qokain', 'okain', 'kain'}

# Analysis counters
all_words = []
polish_counts = Counter()
body_counts = Counter()
water_counts = Counter()
flow_counts = Counter()
word_freq = Counter()

# Output
output = []
output.append("=" * 90)
output.append("VOYNICH MANUSCRIPT - BIOLOGICAL/NYMPH SECTION ANALYSIS")
output.append("Polish-Latin Decoder v6.1")
output.append("Folios f75r - f84v (Female Figures, Baths, Tubes/Pipes)")
output.append("=" * 90)
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
            if word_lower in BODY_TERMS:
                body_counts[word_lower] += 1
            if word_lower in WATER_TERMS:
                water_counts[word_lower] += 1
            if word_lower in FLOW_TERMS:
                flow_counts[word_lower] += 1

        decoded = decode_text(line)

        output.append(f"Line {i}:")
        output.append(f"  Voynich: {line}")
        output.append(f"  Decoded: {decoded}")

        # Flag patterns
        if 'SICK' in decoded:
            output.append(f"  ** POLISH: Patient reference (chor)")
        if 'GIVE' in decoded or 'GAVE' in decoded:
            output.append(f"  ** POLISH: Instruction verb (dar/dal)")
        if 'water' in decoded.lower() or 'WATER' in decoded:
            output.append(f"  ** WATER/BATH: Hydrotherapy reference")
        if 'flow' in decoded.lower():
            output.append(f"  ** FLOW: Bodily fluid/circulation")
        if 'BLOOD' in decoded or 'blood' in decoded:
            output.append(f"  ** BODY: Blood reference")
        if 'EYES' in decoded or 'EYE' in decoded:
            output.append(f"  ** BODY: Eye reference")

        output.append("")

output.append("")

# Statistics
output.append("=" * 90)
output.append("BIOLOGICAL SECTION STATISTICS")
output.append("=" * 90)
output.append("")

output.append(f"Total folios: {len(sorted_folios)}")
output.append(f"Total lines: {sum(len(folios[f]) for f in folios)}")
output.append(f"Total words: {len(all_words)}")
output.append(f"Unique words: {len(set(all_words))}")
output.append("")

# Top words
output.append("TOP 40 WORDS IN BIOLOGICAL SECTION:")
output.append("-" * 60)
for word, count in word_freq.most_common(40):
    decoded = decode_word(word)
    output.append(f"  {word:<15} ({decoded:<25}): {count:>4}x")
output.append("")

# Polish terms
output.append("POLISH TERMS IN BIOLOGICAL SECTION:")
output.append("-" * 50)
if polish_counts:
    for word, count in sorted(polish_counts.items(), key=lambda x: -x[1]):
        meaning = VOCAB.get(word, ('?', 0))[0]
        output.append(f"  {word:<12} ({meaning:<15}): {count:>4}x")
else:
    output.append("  (No Polish terms found)")
output.append("")

# Body terms
output.append("BODY-RELATED TERMS:")
output.append("-" * 50)
for word, count in sorted(body_counts.items(), key=lambda x: -x[1])[:20]:
    decoded = decode_word(word)
    output.append(f"  {word:<12} ({decoded:<20}): {count:>4}x")
output.append("")

# Water terms
output.append("WATER/BATH TERMS (she-/sho- prefix):")
output.append("-" * 50)
water_in_text = Counter()
for word in all_words:
    wl = word.lower()
    if wl.startswith('she') or wl.startswith('sho') or wl.startswith('shy'):
        water_in_text[wl] += 1
for word, count in water_in_text.most_common(20):
    decoded = decode_word(word)
    output.append(f"  {word:<15} ({decoded:<20}): {count:>4}x")
output.append("")

# Flow terms
output.append("FLOW/CIRCULATION TERMS:")
output.append("-" * 50)
flow_in_text = Counter()
for word in all_words:
    wl = word.lower()
    if 'keey' in wl or 'keed' in wl or 'kain' in wl:
        flow_in_text[wl] += 1
for word, count in flow_in_text.most_common(20):
    decoded = decode_word(word)
    output.append(f"  {word:<15} ({decoded:<20}): {count:>4}x")
output.append("")

# Pattern analysis
output.append("=" * 90)
output.append("PATTERN ANALYSIS - NYMPH LABELS & BODY REFERENCES")
output.append("=" * 90)
output.append("")

# Short words (likely figure labels)
short_words = Counter()
for word in all_words:
    if 2 <= len(word) <= 5:
        short_words[word.lower()] += 1

output.append("SHORT WORDS (2-5 chars) - potential figure labels:")
output.append("-" * 50)
for word, count in short_words.most_common(35):
    decoded = decode_word(word)
    output.append(f"  {word:<8} → {decoded:<20} ({count}x)")
output.append("")

# Look for body part patterns
output.append("BODY PART VOCABULARY:")
output.append("-" * 50)
body_vocab = {
    'or': 'heart (Latin cor)',
    'chy': 'blood (Latin sanguis)',
    'cheor': 'flower-heart / blood-heart',
    'keor': 'BLOOD (Polish krew)',
    'oko': 'EYE (Polish oko)',
    'oky': 'EYES (Polish oczy)',
    'ochey': 'EYES (Polish oczy)',
    'shey': 'OF-NECK (Polish szyi)',
    'rchey': 'OF-HAND (Polish ręki)',
    'kar': 'vessel/body',
    'kal': 'vessel',
    'kam': 'BATHE (Polish kąpać)',
}
for word, meaning in body_vocab.items():
    count = word_freq.get(word, 0)
    output.append(f"  {word:<10}: {meaning:<30} ({count}x)")
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
    she_count = sum(1 for w in words if w.lower().startswith('she') or w.lower().startswith('sho'))
    chy_count = sum(1 for w in words if 'chy' in w.lower() or 'che' in w.lower())

    output.append(f"{folio.upper():8}: {len(lines):3} lines, {len(words):4} words | "
                  f"chor: {chor_count:2}, dar/dal: {dar_count:2}, she-: {she_count:2}, che/chy: {chy_count:2}")

output.append("")

# Look for chor (sick) contexts
output.append("=" * 90)
output.append("'CHOR' (SICK) IN BIOLOGICAL SECTION")
output.append("=" * 90)
output.append("")

chor_lines = []
for folio in sorted_folios:
    for line in folios[folio]:
        if 'chor' in line.lower():
            chor_lines.append((folio, line))

output.append(f"Found {len(chor_lines)} lines with 'chor' (SICK)")
output.append("")
for folio, line in chor_lines[:15]:
    decoded = decode_text(line)
    output.append(f"[{folio}] {line}")
    output.append(f"        → {decoded}")
    output.append("")

# Look for kam (bathe) contexts
output.append("=" * 90)
output.append("'KAM' (BATHE) AND WATER REFERENCES")
output.append("=" * 90)
output.append("")

kam_lines = []
for folio in sorted_folios:
    for line in folios[folio]:
        if 'kam' in line.lower() or 'sheol' in line.lower() or 'shedy' in line.lower():
            kam_lines.append((folio, line))

output.append(f"Found {len(kam_lines)} lines with bath/water terms")
output.append("")
for folio, line in kam_lines[:15]:
    decoded = decode_text(line)
    output.append(f"[{folio}] {line}")
    output.append(f"        → {decoded}")
    output.append("")

# Unique vocabulary analysis
output.append("=" * 90)
output.append("SECTION-SPECIFIC VOCABULARY ANALYSIS")
output.append("=" * 90)
output.append("")

# Look for patterns unique to biological section
output.append("TERMS SUGGESTING BODILY PROCESSES:")
output.append("-" * 50)

process_terms = Counter()
for word in all_words:
    wl = word.lower()
    # Flow/circulation patterns
    if 'keey' in wl or 'keed' in wl:
        process_terms['flow/keey'] += 1
    # Blood patterns
    if 'chy' in wl and len(wl) <= 6:
        process_terms['blood/chy'] += 1
    # Water/washing
    if wl.startswith('she') or wl.startswith('sho'):
        process_terms['water/she-'] += 1
    # Body patterns
    if 'or' in wl and len(wl) <= 5:
        process_terms['heart/or'] += 1

for term, count in process_terms.most_common():
    output.append(f"  {term:<15}: {count:>4}x")
output.append("")

# Key findings
output.append("=" * 90)
output.append("KEY FINDINGS - BIOLOGICAL SECTION")
output.append("=" * 90)
output.append("")

total_polish = sum(polish_counts.values())
total_body = sum(body_counts.values())
total_water = sum(water_in_text.values())
total_flow = sum(flow_in_text.values())

output.append(f"1. POLISH TERMS: {total_polish} occurrences")
output.append(f"   Polish medical vocabulary present, indicating practical instructions.")
output.append("")

output.append(f"2. BODY TERMS: {total_body} occurrences")
output.append(f"   References to body parts support anatomical/physiological content.")
output.append("")

output.append(f"3. WATER/BATH TERMS (she-): {total_water} occurrences")
output.append(f"   High water vocabulary consistent with bathing/hydrotherapy imagery.")
output.append("")

output.append(f"4. FLOW/CIRCULATION TERMS: {total_flow} occurrences")
output.append(f"   Terms suggesting bodily fluids and circulation.")
output.append("")

output.append("5. INTERPRETATION:")
output.append("   The biological section appears to describe:")
output.append("   - Hydrotherapy / medicinal bathing")
output.append("   - Bodily circulation and fluids")
output.append("   - Female health / gynecological treatments")
output.append("   - The 'nymphs' may represent patients undergoing treatment")
output.append("   - Tubes/pipes may represent bodily vessels or treatment apparatus")
output.append("")

output.append("6. POLISH-LATIN PATTERN:")
output.append("   - LATIN: Anatomical terms (cor→or, sanguis→chy)")
output.append("   - POLISH: Treatment instructions (dar=give, kam=bathe)")
output.append("   - POLISH: Patient references (chor=sick person)")
output.append("")

output.append("=" * 90)

# Write output
with open('voynich_biological_analysis.txt', 'w') as f:
    f.write('\n'.join(output))

print("Biological section analysis complete!")
print(f"  Folios: {len(sorted_folios)}")
print(f"  Words: {len(all_words)}")
print(f"  Polish terms: {total_polish}")
print(f"  Water terms: {total_water}")
print(f"  Output: voynich_biological_analysis.txt")
print()
print("Top words:")
for word, count in word_freq.most_common(15):
    print(f"  {word}: {count}x")
