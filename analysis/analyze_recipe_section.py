#!/usr/bin/env python3
"""
Voynich Manuscript Recipe/Pharmaceutical Section Analysis with Polish-Latin Decoder v6.1
Analyzes folios f88r-f116v (pharmaceutical/recipe section)
"""

import re
from collections import Counter, defaultdict
from voynich_decoder import decode_text, decode_word, VOCAB

# Read transcription
with open('voynich_transcription.txt', 'r', encoding='latin-1') as f:
    transcription = f.read()

# Recipe section folios (f88-f116)
RECIPE_FOLIOS = set()
for num in range(88, 117):
    RECIPE_FOLIOS.add(f'f{num}r')
    RECIPE_FOLIOS.add(f'f{num}v')

# Extract lines by folio
line_pattern = re.compile(r'^<(f\d+[rv]\d?)[^>]*;H>\s+(.+?)(?:\s*<[^>]*>)*\s*$', re.MULTILINE)

folios = defaultdict(list)
for match in line_pattern.finditer(transcription):
    full_folio_id = match.group(1)
    # Extract base folio (e.g., f88r from f88r.1)
    folio_id = full_folio_id.split('.')[0]
    # Check if it's in recipe section range
    folio_match = re.match(r'f(\d+)', folio_id)
    if folio_match:
        folio_num = int(folio_match.group(1))
        if 88 <= folio_num <= 116:
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

PHARMACEUTICAL_TERMS = {'ol', 'cheol', 'chol', 'fol', 'keol', 'olkeey', 'olkain',
                        'sal', 'saly', 'sar', 'sarar', 'mix', 'kol'}

BOTANICAL_TERMS = {'daiin', 'dain', 'cheol', 'chol', 'ol', 'kor', 'raiin',
                   'flos', 'flor', 'ar', 'aror', 'arxor'}

MEDICAL_TERMS = {'saiin', 'sain', 'sainar', 'chor', 'dor', 'dol', 'dolor',
                 'keor', 'sal', 'dar', 'dal'}

# Analysis counters
all_words = []
polish_counts = Counter()
pharma_counts = Counter()
botanical_counts = Counter()
medical_counts = Counter()
word_freq = Counter()

# Output
output = []
output.append("=" * 90)
output.append("VOYNICH MANUSCRIPT - RECIPE/PHARMACEUTICAL SECTION ANALYSIS")
output.append("Polish-Latin Decoder v6.1")
output.append("Folios f88r - f116v (Pharmaceutical/Recipe Section)")
output.append("=" * 90)
output.append("")
output.append("SECTION DESCRIPTION:")
output.append("The recipe/pharmaceutical section contains compound preparation instructions.")
output.append("Characterized by:")
output.append("  - Dense text with minimal illustrations")
output.append("  - Repeated structural patterns suggesting formulas")
output.append("  - High frequency of preparation verbs")
output.append("")

# Process each folio
folio_stats = {}
for folio in sorted_folios:
    lines = folios[folio]

    folio_words = []
    folio_polish = 0
    folio_pharma = 0
    folio_chor = 0
    folio_dar = 0

    output.append("-" * 80)
    output.append(f"FOLIO {folio.upper()}")
    output.append("-" * 80)
    output.append("")

    for i, line in enumerate(lines, 1):
        words = line.replace('.', ' ').split()
        all_words.extend(words)
        folio_words.extend(words)

        for word in words:
            word_lower = word.lower()
            word_freq[word_lower] += 1

            # Count Polish terms
            for term in POLISH_TERMS:
                if term in word_lower:
                    polish_counts[term] += 1
                    folio_polish += 1
                    if term == 'chor':
                        folio_chor += 1
                    if term in ['dar', 'dal']:
                        folio_dar += 1
                    break

            # Count pharmaceutical terms
            for term in PHARMACEUTICAL_TERMS:
                if term in word_lower:
                    pharma_counts[term] += 1
                    folio_pharma += 1
                    break

        decoded = decode_text(line)

        output.append(f"Line {i}:")
        output.append(f"  Voynich: {line}")
        output.append(f"  Decoded: {decoded}")

        # Flag patterns
        if 'SICK' in decoded:
            output.append(f"  ** POLISH: Patient reference (chor)")
        if 'GIVE' in decoded or 'GAVE' in decoded:
            output.append(f"  ** POLISH: Instruction verb (dar/dal)")
        if 'SALT' in decoded:
            output.append(f"  ** POLISH: Salt (sal/sól)")
        if 'OIL' in decoded:
            output.append(f"  ** PHARMACEUTICAL: Oil preparation")
        if 'HEAL' in decoded or 'heal' in decoded:
            output.append(f"  ** MEDICAL: Healing reference")
        if 'leaf' in decoded or 'LEAF' in decoded:
            output.append(f"  ** BOTANICAL: Plant reference")
        if 'flower' in decoded or 'FLOWER' in decoded:
            output.append(f"  ** BOTANICAL: Flower reference")
        if 'ROOT' in decoded:
            output.append(f"  ** BOTANICAL: Root reference")
        if 'BLOOD' in decoded or 'blood' in decoded:
            output.append(f"  ** MEDICAL: Blood reference")
        if 'mix' in decoded.lower():
            output.append(f"  ** PHARMACEUTICAL: Mixing instruction")

        output.append("")

    # Store folio stats
    folio_stats[folio] = {
        'words': len(folio_words),
        'lines': len(lines),
        'polish': folio_polish,
        'pharma': folio_pharma,
        'chor': folio_chor,
        'dar': folio_dar
    }

output.append("")

# Statistics
output.append("=" * 90)
output.append("RECIPE SECTION STATISTICS")
output.append("=" * 90)
output.append("")

output.append(f"Total folios: {len(sorted_folios)}")
output.append(f"Total lines: {sum(len(folios[f]) for f in folios)}")
output.append(f"Total words: {len(all_words)}")
output.append(f"Unique words: {len(set(all_words))}")
output.append("")

# Top words
output.append("TOP 50 WORDS IN RECIPE SECTION:")
output.append("-" * 60)
for word, count in word_freq.most_common(50):
    decoded = decode_word(word)
    output.append(f"  {word:<18} ({decoded:<25}): {count:>4}x")
output.append("")

# Polish terms
output.append("POLISH TERMS IN RECIPE SECTION:")
output.append("-" * 50)
polish_found = Counter()
for word in all_words:
    wl = word.lower()
    for term in POLISH_TERMS:
        if term == wl or (len(term) >= 3 and term in wl):
            polish_found[term] += 1

if polish_found:
    for term, count in polish_found.most_common():
        meaning = VOCAB.get(term, ('?', 0))[0]
        output.append(f"  {term:<12} ({meaning:<15}): {count:>4}x")
output.append("")

# Pharmaceutical terms
output.append("PHARMACEUTICAL TERMS (ol/sal/cheol):")
output.append("-" * 50)
pharma_found = Counter()
for word in all_words:
    wl = word.lower()
    if 'ol' in wl or 'sal' in wl or 'cheol' in wl or 'chol' in wl:
        pharma_found[wl] += 1
for word, count in pharma_found.most_common(30):
    decoded = decode_word(word)
    output.append(f"  {word:<18} ({decoded:<20}): {count:>4}x")
output.append("")

# Healing/Medical terms
output.append("HEALING/MEDICAL TERMS (saiin/chor/keor):")
output.append("-" * 50)
medical_found = Counter()
for word in all_words:
    wl = word.lower()
    if 'saiin' in wl or 'sain' in wl or 'chor' in wl or 'keor' in wl:
        medical_found[wl] += 1
for word, count in medical_found.most_common(20):
    decoded = decode_word(word)
    output.append(f"  {word:<18} ({decoded:<20}): {count:>4}x")
output.append("")

# Botanical terms
output.append("BOTANICAL TERMS (daiin/cheol/kor):")
output.append("-" * 50)
botanical_found = Counter()
for word in all_words:
    wl = word.lower()
    if 'daiin' in wl or 'dain' in wl or 'cheol' in wl or 'kor' in wl or 'raiin' in wl:
        botanical_found[wl] += 1
for word, count in botanical_found.most_common(20):
    decoded = decode_word(word)
    output.append(f"  {word:<18} ({decoded:<20}): {count:>4}x")
output.append("")

# Flow/preparation terms
output.append("FLOW/PREPARATION TERMS (qokeey/keey/kain):")
output.append("-" * 50)
flow_found = Counter()
for word in all_words:
    wl = word.lower()
    if 'keey' in wl or 'kain' in wl or 'keedy' in wl:
        flow_found[wl] += 1
for word, count in flow_found.most_common(20):
    decoded = decode_word(word)
    output.append(f"  {word:<18} ({decoded:<20}): {count:>4}x")
output.append("")

# Folio-by-folio summary
output.append("=" * 90)
output.append("FOLIO-BY-FOLIO SUMMARY")
output.append("=" * 90)
output.append("")
output.append(f"{'FOLIO':<10} {'LINES':>6} {'WORDS':>6} {'OL(oil)':>8} {'SAL(salt)':>10} {'CHOR':>6} {'DAR/DAL':>8}")
output.append("-" * 60)

for folio in sorted_folios:
    stats = folio_stats[folio]
    words = []
    for line in folios[folio]:
        words.extend(line.replace('.', ' ').split())

    ol_count = sum(1 for w in words if 'ol' in w.lower() and len(w) <= 6)
    sal_count = sum(1 for w in words if 'sal' in w.lower())
    chor_count = sum(1 for w in words if 'chor' in w.lower())
    dar_count = sum(1 for w in words if 'dar' in w.lower() or 'dal' in w.lower())

    output.append(f"{folio.upper():<10} {stats['lines']:>6} {stats['words']:>6} {ol_count:>8} {sal_count:>10} {chor_count:>6} {dar_count:>8}")

output.append("")

# Recipe patterns analysis
output.append("=" * 90)
output.append("RECIPE PATTERN ANALYSIS")
output.append("=" * 90)
output.append("")

# Look for repeated formula patterns
output.append("CHOR (sick) LINES - Patient references in recipes:")
output.append("-" * 50)
chor_lines = []
for folio in sorted_folios:
    for line in folios[folio]:
        if 'chor' in line.lower():
            decoded = decode_text(line)
            chor_lines.append((folio, line, decoded))

for folio, line, decoded in chor_lines[:15]:  # First 15 examples
    output.append(f"[{folio}] {line}")
    output.append(f"        → {decoded}")
    output.append("")

output.append(f"Total CHOR lines: {len(chor_lines)}")
output.append("")

# DAR/DAL instruction patterns
output.append("DAR/DAL (give) INSTRUCTION PATTERNS:")
output.append("-" * 50)
dar_lines = []
for folio in sorted_folios:
    for line in folios[folio]:
        line_lower = line.lower()
        if 'dar' in line_lower or 'dal' in line_lower:
            dar_lines.append((folio, line))

output.append(f"Total DAR/DAL lines: {len(dar_lines)}")
output.append("")

# Sample dar/dal lines
output.append("Sample DAR/DAL lines:")
for folio, line in dar_lines[:10]:
    decoded = decode_text(line)
    output.append(f"[{folio}] {line}")
    output.append(f"        → {decoded}")
    output.append("")

# OL (oil) preparation patterns
output.append("OL (oil) PREPARATION PATTERNS:")
output.append("-" * 50)
ol_lines = []
for folio in sorted_folios:
    for line in folios[folio]:
        words = line.replace('.', ' ').split()
        if any('ol' in w.lower() and len(w) <= 4 for w in words):
            ol_lines.append((folio, line))

output.append(f"Total OL (oil) lines: {len(ol_lines)}")
output.append("")

# SAL (salt) preparation patterns
output.append("SAL (salt) PREPARATION PATTERNS:")
output.append("-" * 50)
sal_lines = []
for folio in sorted_folios:
    for line in folios[folio]:
        if 'sal' in line.lower():
            sal_lines.append((folio, line))

output.append(f"Total SAL (salt) lines: {len(sal_lines)}")
output.append("Sample SAL lines:")
for folio, line in sal_lines[:8]:
    decoded = decode_text(line)
    output.append(f"[{folio}] {line}")
    output.append(f"        → {decoded}")
    output.append("")

# Comparison to other sections
output.append("=" * 90)
output.append("COMPARISON TO OTHER SECTIONS")
output.append("=" * 90)
output.append("")

total_words = len(all_words)
polish_total = sum(polish_found.values())
ol_total = sum(1 for w in all_words if 'ol' in w.lower() and len(w) <= 6)
sal_total = sum(1 for w in all_words if 'sal' in w.lower())
chor_total = len(chor_lines)
dar_total = len(dar_lines)

output.append("VOCABULARY DISTRIBUTION IN RECIPE SECTION:")
output.append("-" * 50)
output.append(f"  Total words:        {total_words:>6}")
output.append(f"  Polish terms:       {polish_total:>6} ({polish_total/total_words*100:.1f}%)")
output.append(f"  OL (oil) words:     {ol_total:>6} ({ol_total/total_words*100:.1f}%)")
output.append(f"  SAL (salt) words:   {sal_total:>6} ({sal_total/total_words*100:.2f}%)")
output.append(f"  CHOR (sick) lines:  {chor_total:>6}")
output.append(f"  DAR/DAL lines:      {dar_total:>6}")
output.append("")

output.append("COMPARISON TO ADJACENT/OTHER SECTIONS:")
output.append("-" * 60)
output.append("                    Herbal      Astro       Bio         Rosettes    Recipe")
output.append("                    (f1-57)     (f67-73)    (f75-84)    (f85-86)    (f88-116)")
output.append("-" * 60)
output.append(f"  Words:            9,575       3,026       6,851       1,810       {total_words}")
output.append(f"  Polish %:         5.0%        4.1%        4.5%        28.7%       {polish_total/total_words*100:.1f}%")
output.append(f"  CHOR (sick):      147         6           10          12          {chor_total}")
output.append(f"  DAR/DAL:          151         67          133         105         {dar_total}")
output.append("")

# Key findings
output.append("=" * 90)
output.append("KEY FINDINGS - RECIPE/PHARMACEUTICAL SECTION")
output.append("=" * 90)
output.append("")

output.append("1. SECTION PURPOSE:")
output.append("   The recipe section contains COMPOUND PREPARATION instructions.")
output.append("   Focus is on HOW TO PREPARE medicines, not WHAT they treat.")
output.append("")

output.append("2. VOCABULARY PROFILE:")
output.append(f"   - Polish terms: {polish_total/total_words*100:.1f}% (lower than rosettes 28.7%)")
output.append(f"   - High OL (oil) frequency: {ol_total} occurrences")
output.append(f"   - DAR/DAL instructions: {dar_total} lines")
output.append(f"   - CHOR (sick) references: {chor_total} (moderate)")
output.append("")

output.append("3. RECIPE STRUCTURE:")
output.append("   Typical recipe pattern:")
output.append("   [ingredient] + [preparation verb] + [method] + [result]")
output.append("   'cheol' (flower-oil) + 'dar' (give) + 'qokeey' (the-flow) + 'saiin' (heal)")
output.append("")

output.append("4. KEY INGREDIENTS:")
output.append("   - OL (oil): base for preparations")
output.append("   - SAL (salt): preservative/active ingredient")
output.append("   - CHEOL (flower-oil): plant extract")
output.append("   - DAIIN (leaf): plant material")
output.append("")

output.append("5. RELATIONSHIP TO OTHER SECTIONS:")
output.append("   Recipe section receives input from:")
output.append("   - HERBAL: Which plants to use")
output.append("   - ASTRONOMICAL: When to prepare")
output.append("   - BIOLOGICAL: How to administer")
output.append("   - ROSETTES: Theoretical framework")
output.append("   - F87: Bridge from theory to practice")
output.append("")

output.append("6. POLISH-LATIN PATTERN:")
output.append("   - LATIN: Ingredient names (oleum, sal, flos)")
output.append("   - POLISH: Action verbs (dar=give, dal=gave)")
output.append("   - MIXED: Compound terms (cheol=flower-oil)")
output.append("")

output.append("=" * 90)

# Write output
with open('voynich_recipe_analysis.txt', 'w') as f:
    f.write('\n'.join(output))

print("Recipe section analysis complete!")
print(f"  Folios: {len(sorted_folios)}")
print(f"  Lines: {sum(len(folios[f]) for f in folios)}")
print(f"  Words: {len(all_words)}")
print(f"  Polish terms: {polish_total} ({polish_total/total_words*100:.1f}%)")
print(f"  CHOR (sick): {chor_total} lines")
print(f"  DAR/DAL: {dar_total} lines")
print(f"  Output: voynich_recipe_analysis.txt")
print()
print("Top words in recipe section:")
for word, count in word_freq.most_common(15):
    print(f"  {word}: {count}x")
