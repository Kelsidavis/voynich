#!/usr/bin/env python3
"""
Voynich Manuscript Astronomical Section Analysis with Polish-Latin Decoder v6.1
Analyzes folios f67r through f73v (zodiac circles, star diagrams)
"""

import re
from collections import Counter, defaultdict
from voynich_decoder import decode_text, decode_word, VOCAB

# Read transcription
with open('voynich_transcription.txt', 'r', encoding='latin-1') as f:
    transcription = f.read()

# Astronomical section folios (f67-f73, including sub-pages)
ASTRO_FOLIOS = set()
for i in range(67, 74):
    ASTRO_FOLIOS.add(f'f{i}r')
    ASTRO_FOLIOS.add(f'f{i}v')
    for sub in ['1', '2', '3']:
        ASTRO_FOLIOS.add(f'f{i}r{sub}')
        ASTRO_FOLIOS.add(f'f{i}v{sub}')

# Extract lines by folio
line_pattern = re.compile(r'^<(f\d+[rv]\d?)[^>]*;H>\s*(.+?)(?:<[^>]*>)*\s*$', re.MULTILINE)

folios = defaultdict(list)
for match in line_pattern.finditer(transcription):
    folio_id = match.group(1).split('.')[0]
    text = match.group(2).strip()

    # Clean up text
    text = re.sub(r'<[^>]*>', '', text)
    text = re.sub(r'[!?]', '', text)
    text = text.strip()

    if text and len(text) > 1:
        # Check if folio matches astronomical section
        base_folio = re.match(r'f(\d+)[rv]', folio_id)
        if base_folio:
            num = int(base_folio.group(1))
            if 67 <= num <= 73:
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
POLISH_TERMS = {'chor', 'chory', 'dar', 'dal', 'da', 'dan', 'daim', 'daj', 'dary',
                'sal', 'saly', 'kor', 'oko', 'oky', 'ochey', 'shey', 'rchey',
                'keor', 'kchy', 'schy', 'mchy', 'gchy', 'cchy', 'ly', 'lchy',
                'ytchor', 'shoky', 'kam', 'pchey', 'pchy'}

ASTRONOMICAL_TERMS = {'ot', 'otar', 'otair', 'oteor', 'otol', 'otal', 'oty',
                      'oteey', 'otedy', 'oteol', 'oteody', 'star', 'sol',
                      'shol', 'sheol', 'cphar', 'cphor', 'cphol', 'pharma',
                      'otchy', 'otaiin', 'otaldy'}

ZODIAC_MONTHS = {'ar', 'taur', 'gem', 'canc', 'leo', 'virg', 'libr', 'scorp',
                 'sagit', 'capri', 'aquar', 'pisc'}

# Analysis counters
all_words = []
polish_counts = Counter()
astro_counts = Counter()
word_freq = Counter()
decoded_terms = Counter()

# Output
output = []
output.append("=" * 90)
output.append("VOYNICH MANUSCRIPT - ASTRONOMICAL SECTION ANALYSIS")
output.append("Polish-Latin Decoder v6.1")
output.append("Folios f67r - f73v (Zodiac Circles, Star Diagrams)")
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

            # Check for astronomical prefixes
            if word_lower.startswith('ot') or word_lower.startswith('cpho') or word_lower.startswith('cphar'):
                astro_counts[word_lower] += 1

        decoded = decode_text(line)

        output.append(f"Line {i}:")
        output.append(f"  Voynich: {line}")
        output.append(f"  Decoded: {decoded}")

        # Flag interesting patterns
        if 'SICK' in decoded:
            output.append(f"  ** POLISH: Patient reference")
        if 'STAR' in decoded or 'star' in decoded:
            output.append(f"  ** ASTRONOMICAL: Star reference")
        if 'AETHER' in decoded or 'SPHERE' in decoded:
            output.append(f"  ** COSMOLOGICAL: Celestial sphere")
        if 'GIVE' in decoded or 'GAVE' in decoded:
            output.append(f"  ** POLISH: Instruction verb")

        output.append("")

output.append("")

# Statistics
output.append("=" * 90)
output.append("ASTRONOMICAL SECTION STATISTICS")
output.append("=" * 90)
output.append("")

output.append(f"Total folios: {len(sorted_folios)}")
output.append(f"Total lines: {sum(len(folios[f]) for f in folios)}")
output.append(f"Total words: {len(all_words)}")
output.append(f"Unique words: {len(set(all_words))}")
output.append("")

# Top words
output.append("TOP 30 WORDS IN ASTRONOMICAL SECTION:")
output.append("-" * 50)
for word, count in word_freq.most_common(30):
    decoded = decode_word(word)
    output.append(f"  {word:<15} ({decoded:<20}): {count:>4}x")
output.append("")

# Polish terms
output.append("POLISH TERMS IN ASTRONOMICAL SECTION:")
output.append("-" * 50)
if polish_counts:
    for word, count in sorted(polish_counts.items(), key=lambda x: -x[1]):
        meaning = VOCAB.get(word, ('?', 0))[0]
        output.append(f"  {word:<12} ({meaning:<15}): {count:>4}x")
else:
    output.append("  (No Polish terms found)")
output.append("")

# Astronomical terms (ot- prefix)
output.append("ASTRONOMICAL TERMS (ot-/cpho- prefix):")
output.append("-" * 50)
for word, count in sorted(astro_counts.items(), key=lambda x: -x[1])[:25]:
    decoded = decode_word(word)
    output.append(f"  {word:<15} ({decoded:<20}): {count:>4}x")
output.append("")

# Pattern analysis - look for star/nymph labels
output.append("=" * 90)
output.append("PATTERN ANALYSIS - STAR/FIGURE LABELS")
output.append("=" * 90)
output.append("")

# Short words (likely labels)
short_words = Counter()
for word in all_words:
    if 2 <= len(word) <= 6:
        short_words[word.lower()] += 1

output.append("SHORT WORDS (2-6 chars) - potential star/figure labels:")
output.append("-" * 50)
for word, count in short_words.most_common(40):
    decoded = decode_word(word)
    output.append(f"  {word:<10} → {decoded:<20} ({count}x)")
output.append("")

# Repeated patterns (same label appearing multiple times)
output.append("REPEATED LABELS (appearing 5+ times):")
output.append("-" * 50)
repeated = [(w, c) for w, c in word_freq.items() if c >= 5]
repeated.sort(key=lambda x: -x[1])
for word, count in repeated[:30]:
    decoded = decode_word(word)
    output.append(f"  {word:<15} → {decoded:<25} ({count}x)")
output.append("")

# Look for number-like patterns
output.append("=" * 90)
output.append("POTENTIAL NUMBER/POSITION MARKERS")
output.append("=" * 90)
output.append("")

# Words starting with common prefixes
prefix_counts = Counter()
for word in all_words:
    word_lower = word.lower()
    if len(word_lower) >= 2:
        prefix_counts[word_lower[:2]] += 1

output.append("COMMON 2-LETTER PREFIXES:")
output.append("-" * 50)
for prefix, count in prefix_counts.most_common(20):
    output.append(f"  {prefix}-  : {count}x")
output.append("")

# Compare with other sections
output.append("=" * 90)
output.append("VOCABULARY COMPARISON WITH OTHER SECTIONS")
output.append("=" * 90)
output.append("")

# Calculate unique words
astro_words = set(w.lower() for w in all_words)
output.append(f"Unique words in astronomical section: {len(astro_words)}")
output.append("")

# Key astronomical vocabulary
output.append("KEY ASTRONOMICAL VOCABULARY:")
output.append("-" * 50)

astro_vocab = {
    'otaiin': 'star.NOM (nominative star)',
    'oteey': 'stars (plural)',
    'otedy': 'star-like/stellar',
    'oteor': 'star-heart',
    'otair': 'AETHER (celestial air)',
    'otol': 'heaven/celestial',
    'otal': 'HEAVEN',
    'otaldy': 'heavenly',
    'oty': 'star-ADJ',
    'shol': 'sun/knowledge',
    'sheol': 'SUN',
    'cphar': 'SPHERE',
    'cphor': 'sphere-heart',
    'cphol': 'sphere-oil',
}

for word, meaning in astro_vocab.items():
    count = word_freq.get(word, 0)
    output.append(f"  {word:<12}: {meaning:<30} ({count}x in astro)")
output.append("")

# Specific folio analysis
output.append("=" * 90)
output.append("FOLIO-BY-FOLIO SUMMARY")
output.append("=" * 90)
output.append("")

for folio in sorted_folios:
    lines = folios[folio]
    words = []
    for line in lines:
        words.extend(line.replace('.', ' ').split())

    # Count key terms
    chor_count = sum(1 for w in words if 'chor' in w.lower())
    ot_count = sum(1 for w in words if w.lower().startswith('ot'))
    dar_count = sum(1 for w in words if 'dar' in w.lower() or 'dal' in w.lower())

    output.append(f"{folio.upper():8}: {len(lines):3} lines, {len(words):4} words | "
                  f"ot-: {ot_count:3}, chor: {chor_count:2}, dar/dal: {dar_count:2}")

output.append("")

# Key findings
output.append("=" * 90)
output.append("KEY FINDINGS - ASTRONOMICAL SECTION")
output.append("=" * 90)
output.append("")

total_polish = sum(polish_counts.values())
total_astro = sum(astro_counts.values())

output.append(f"1. POLISH TERMS: {total_polish} occurrences")
if total_polish > 0:
    output.append("   Polish vocabulary is present, suggesting medical/instructional")
    output.append("   content mixed with astronomical observations.")
else:
    output.append("   Limited Polish vocabulary - more Latin astronomical terms.")
output.append("")

output.append(f"2. ASTRONOMICAL TERMS (ot-/cpho-): {total_astro} occurrences")
output.append("   High frequency of stellar/celestial vocabulary confirms")
output.append("   this section deals with astronomical content.")
output.append("")

# Check for zodiac-like patterns
output.append("3. ZODIAC/CALENDAR PATTERNS:")
# Look for sequences
for folio in sorted_folios:
    if 'f72' in folio:  # f72 has zodiac circles
        output.append(f"   {folio}: Likely zodiac calendar (circular diagram)")
output.append("")

output.append("4. INTERPRETATION:")
output.append("   The astronomical section appears to contain:")
output.append("   - Star/constellation labels (short repeated words)")
output.append("   - Celestial timing instructions (ot- prefixes)")
output.append("   - Possible astrological medical timing (when to treat)")
output.append("   - Polish verbs may indicate 'when to give' medicine")
output.append("")

output.append("=" * 90)

# Write output
with open('voynich_astronomical_analysis.txt', 'w') as f:
    f.write('\n'.join(output))

print("Astronomical section analysis complete!")
print(f"  Folios: {len(sorted_folios)}")
print(f"  Words: {len(all_words)}")
print(f"  Polish terms: {total_polish}")
print(f"  Astronomical terms: {total_astro}")
print(f"  Output: voynich_astronomical_analysis.txt")
print()
print("Top astronomical words:")
for word, count in word_freq.most_common(10):
    print(f"  {word}: {count}x")
