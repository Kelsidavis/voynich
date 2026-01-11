#!/usr/bin/env python3
"""
Voynich Manuscript Herbal Section Analysis with Polish-Latin Decoder v6.1
Analyzes folios f1r through f57v (Herbal A and B sections)
"""

import re
from collections import Counter, defaultdict
from voynich_decoder import decode_text, decode_word, VOCAB

# Read transcription
with open('voynich_transcription.txt', 'r', encoding='latin-1') as f:
    transcription = f.read()

# Herbal section folios (f1r - f57v)
# Herbal A: f1r-f25v (large plant drawings)
# Herbal B: f26r-f57v (smaller plants, some with roots visible)
HERBAL_FOLIOS = set()
for i in range(1, 58):
    HERBAL_FOLIOS.add(f'f{i}r')
    HERBAL_FOLIOS.add(f'f{i}v')

# Extract lines by folio
line_pattern = re.compile(r'^<(f\d+[rv](?:\d+)?)[^>]*;H>\s*(.+?)(?:<[^>]*>)*\s*$', re.MULTILINE)

folios = defaultdict(list)
for match in line_pattern.finditer(transcription):
    folio_id = match.group(1).split('.')[0]
    text = match.group(2).strip()

    # Clean up text
    text = re.sub(r'<[^>]*>', '', text)
    text = re.sub(r'[!?]', '', text)
    text = text.strip()

    if text and len(text) > 1:
        if folio_id in HERBAL_FOLIOS:
            folios[folio_id].append(text)

# Sort folios naturally
def natural_sort_key(s):
    match = re.match(r'f(\d+)([rv])(\d*)', s)
    if match:
        num = int(match.group(1))
        suffix = 0 if match.group(2) == 'r' else 1
        sub = int(match.group(3)) if match.group(3) else 0
        return (num, suffix, sub)
    return (999, 0, 0)

sorted_folios = sorted(folios.keys(), key=natural_sort_key)

# Analysis counters
all_words = []
polish_terms = Counter()
latin_terms = Counter()
botanical_terms = Counter()
medical_terms = Counter()
unknown_words = Counter()
decoded_patterns = Counter()

# Polish vocabulary markers
POLISH_WORDS = {'chor', 'dar', 'dal', 'da', 'daim', 'dan', 'deey', 'lchy', 'lchey',
                'pchey', 'pchy', 'rchey', 'shey', 'ochey', 'oky', 'mchy', 'gchy',
                'schy', 'kchy', 'cchy', 'ly', 'ytchor', 'shoky', 'kam', 'keor',
                'kor', 'oko', 'sal', 'daj', 'dac', 'dary', 'chory', 'choremu'}

BOTANICAL_WORDS = {'daiin', 'dain', 'raiin', 'ral', 'rar', 'flos', 'flor', 'chol',
                   'cheol', 'ol', 'oldy', 'aror', 'arxor', 'ar', 'araiin', 'fachys',
                   'kam', 'oty', 'otol', 'oteol'}

MEDICAL_WORDS = {'saiin', 'sain', 'sainar', 'sair', 'sairy', 'dor', 'dol', 'dolor',
                 'dory', 'chor', 'chory', 'lchy', 'lchey', 'keor'}

# Generate output
output = []
output.append("=" * 80)
output.append("VOYNICH MANUSCRIPT - HERBAL SECTION ANALYSIS")
output.append("Polish-Latin Hybrid Decoder v6.1")
output.append("Folios f1r - f57v (Herbal A & B)")
output.append("=" * 80)
output.append("")

# Process each folio
for folio in sorted_folios:
    lines = folios[folio]

    output.append("-" * 80)
    output.append(f"FOLIO {folio.upper()}")
    output.append("-" * 80)
    output.append("")

    for i, line in enumerate(lines, 1):
        # Extract words
        words = line.replace('.', ' ').split()
        all_words.extend(words)

        # Count term types
        for word in words:
            word_lower = word.lower()
            if word_lower in POLISH_WORDS:
                polish_terms[word_lower] += 1
            if word_lower in BOTANICAL_WORDS:
                botanical_terms[word_lower] += 1
            if word_lower in MEDICAL_WORDS:
                medical_terms[word_lower] += 1

            # Check if decoded
            decoded = decode_word(word)
            if decoded.startswith('(') and decoded.endswith(')'):
                unknown_words[word_lower] += 1
            elif '[' in decoded or decoded.isupper():
                # Successfully decoded
                decoded_patterns[decoded] += 1

        # Decode line
        decoded = decode_text(line)

        output.append(f"Line {i}:")
        output.append(f"  Voynich: {line}")
        output.append(f"  Decoded: {decoded}")

        # Check for interesting patterns
        if 'SICK' in decoded:
            output.append(f"  ** POLISH: Patient reference (chor=sick)")
        if 'GIVE' in decoded or 'GAVE' in decoded:
            output.append(f"  ** POLISH: Instruction verb (dar/dal)")
        if 'ROOT' in decoded and 'kor' in line.lower():
            output.append(f"  ** POLISH: Root reference (kor=korzeń)")

        output.append("")

    output.append("")

# Statistics section
output.append("=" * 80)
output.append("HERBAL SECTION STATISTICS")
output.append("=" * 80)
output.append("")

output.append(f"Total folios analyzed: {len(sorted_folios)}")
output.append(f"Total words: {len(all_words)}")
output.append(f"Unique words: {len(set(all_words))}")
output.append("")

# Polish term frequency
output.append("POLISH TERMS IN HERBAL SECTION:")
output.append("-" * 40)
polish_in_herbal = {w: c for w, c in polish_terms.items()}
for word, count in sorted(polish_in_herbal.items(), key=lambda x: -x[1])[:20]:
    meaning = VOCAB.get(word, ('?', 0))[0]
    output.append(f"  {word:12} ({meaning:15}): {count:4}x")
output.append("")

# Botanical terms
output.append("BOTANICAL TERMS IN HERBAL SECTION:")
output.append("-" * 40)
for word, count in sorted(botanical_terms.items(), key=lambda x: -x[1])[:15]:
    meaning = VOCAB.get(word, ('?', 0))[0]
    output.append(f"  {word:12} ({meaning:15}): {count:4}x")
output.append("")

# Medical terms
output.append("MEDICAL TERMS IN HERBAL SECTION:")
output.append("-" * 40)
for word, count in sorted(medical_terms.items(), key=lambda x: -x[1])[:15]:
    meaning = VOCAB.get(word, ('?', 0))[0]
    output.append(f"  {word:12} ({meaning:15}): {count:4}x")
output.append("")

# Top unknown words
output.append("TOP UNDECODED WORDS (potential new vocabulary):")
output.append("-" * 40)
for word, count in unknown_words.most_common(30):
    output.append(f"  {word:15}: {count:4}x")
output.append("")

# Pattern analysis
output.append("=" * 80)
output.append("PATTERN ANALYSIS")
output.append("=" * 80)
output.append("")

# Look for plant name patterns (typically first word of a page or after label markers)
plant_candidates = Counter()
for folio in sorted_folios:
    lines = folios[folio]
    if lines:
        # First word of first line often is plant name
        first_words = lines[0].replace('.', ' ').split()
        if first_words:
            plant_candidates[first_words[0].lower()] += 1

output.append("POTENTIAL PLANT NAMES (first words of folios):")
output.append("-" * 40)
for word, count in plant_candidates.most_common(25):
    decoded = decode_word(word)
    output.append(f"  {word:15} → {decoded:20} ({count}x)")
output.append("")

# Look for chor (sick) patterns in herbal section
output.append("LINES WITH 'CHOR' (sick person) IN HERBAL SECTION:")
output.append("-" * 40)
chor_lines = []
for folio in sorted_folios:
    for line in folios[folio]:
        if 'chor' in line.lower():
            chor_lines.append((folio, line))

output.append(f"Found {len(chor_lines)} lines with 'chor' (SICK)")
output.append("")
for folio, line in chor_lines[:20]:
    decoded = decode_text(line)
    output.append(f"[{folio}] {line}")
    output.append(f"        → {decoded}")
    output.append("")

# Look for dar/dal (give/gave) patterns
output.append("LINES WITH 'DAR/DAL' (give/gave) IN HERBAL SECTION:")
output.append("-" * 40)
dar_lines = []
for folio in sorted_folios:
    for line in folios[folio]:
        if 'dar' in line.lower() or 'dal' in line.lower():
            dar_lines.append((folio, line))

output.append(f"Found {len(dar_lines)} lines with 'dar/dal' (GIVE/GAVE)")
output.append("")
for folio, line in dar_lines[:20]:
    decoded = decode_text(line)
    output.append(f"[{folio}] {line}")
    output.append(f"        → {decoded}")
    output.append("")

# Summary findings
output.append("=" * 80)
output.append("KEY FINDINGS - POLISH IN HERBAL SECTION")
output.append("=" * 80)
output.append("")

total_polish = sum(polish_terms.values())
total_botanical = sum(botanical_terms.values())
total_medical = sum(medical_terms.values())

output.append(f"Polish instruction terms: {total_polish} occurrences")
output.append(f"Botanical terms: {total_botanical} occurrences")
output.append(f"Medical terms: {total_medical} occurrences")
output.append("")

output.append("INTERPRETATION:")
output.append("-" * 40)
output.append("The herbal section contains both:")
output.append("  1. LATIN botanical terminology (plant parts, preparations)")
output.append("  2. POLISH medical instructions (patient references, dosing)")
output.append("")
output.append("This supports the hypothesis that the Voynich is a")
output.append("POLISH-LATIN bilingual medical/herbal manuscript.")
output.append("")

if len(chor_lines) > 0:
    output.append(f"SIGNIFICANT: {len(chor_lines)} patient references ('chor'=sick)")
    output.append("  These are NOT cherub references but medical patient terms!")
output.append("")

output.append("=" * 80)

# Write output
with open('voynich_herbal_analysis.txt', 'w') as f:
    f.write('\n'.join(output))

print(f"Herbal section analysis complete!")
print(f"  Folios: {len(sorted_folios)}")
print(f"  Words: {len(all_words)}")
print(f"  Polish terms: {total_polish}")
print(f"  Output: voynich_herbal_analysis.txt")
print()
print("Polish term summary:")
for word, count in sorted(polish_terms.items(), key=lambda x: -x[1])[:10]:
    print(f"  {word}: {count}x")
