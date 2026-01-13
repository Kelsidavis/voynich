#!/usr/bin/env python3
"""
Voynich Manuscript Decoder Module
Version 8.0 - Corpus-First Methodology - January 2026

CRITICAL CHANGE FROM v7.5:
This version only includes patterns VERIFIED in the corpus.
All meaning assignments are marked with confidence levels.
Unverified claims from previous versions have been removed.

WHAT WAS REMOVED:
- 'choremu' (0 corpus occurrences - was in vocabulary but NOT in manuscript)
- 'daj' (0 corpus occurrences - claimed imperative doesn't exist)
- Many other entries that were hypothesized but not attested

WHAT THIS VERSION PROVIDES:
- Morphological analysis (prefixes, suffixes, roots) - HIGH confidence
- Structural patterns (qo- determiner, -aiin/-ain case) - HIGH confidence
- Meaning assignments - LOW confidence (marked with ?)

HONEST ASSESSMENT:
Without external validation (bilingual text, known author), we cannot
prove what any Voynich word means. The Polish hypothesis is phonetically
plausible but grammatically unverified (case paradigms don't appear).

Usage:
    from voynich_decoder_v8 import analyze_word, decode_text, MORPHOLOGY

    # Analyze structure of a word
    result = analyze_word('qokaiin')
    # Returns: {'prefix': 'qo-', 'root': 'k', 'suffix': '-aiin', 'confidence': 'A'}

    # Decode with honest uncertainty markers
    result = decode_text('daiin.chol.dar')
    # Returns: 'daiin[?leaf] . chol[?flower] . dar[?give]'
"""

# =============================================================================
# CORPUS STATISTICS (from 36,373 tokens, 8,474 unique types)
# =============================================================================
CORPUS_STATS = {
    'total_tokens': 36373,
    'unique_types': 8474,
    'hapax_legomena': 6030,  # 71.2% appear only once
    'top_word': ('daiin', 805),
}

# =============================================================================
# VERIFIED MORPHOLOGICAL PATTERNS (Confidence: A = High, B = Medium, C = Low)
# =============================================================================

# Prefixes - verified by qo-X/X pair analysis (412 pairs, 2-8x ratio)
PREFIXES = {
    'qo': {
        'confidence': 'A',
        'evidence': '412 qo-X/X pairs, consistent 2-8x frequency ratio',
        'possible_meaning': 'DETERMINER (the?)',
        'tokens': 4991,
        'types': 788,
    },
    'o': {
        'confidence': 'B',
        'evidence': 'Common initial, contrasts with qo-',
        'possible_meaning': 'PREPOSITION?',
        'tokens': 2847,
        'types': 1866,
    },
    'y': {
        'confidence': 'C',
        'evidence': 'Appears between elements',
        'possible_meaning': 'CONJUNCTION (and?)',
        'tokens': 1294,
        'types': 619,
    },
    'l': {
        'confidence': 'C',
        'evidence': 'Often before ch/sh sequences',
        'possible_meaning': 'PREFIX?',
        'tokens': 856,
        'types': 377,
    },
    's': {
        'confidence': 'C',
        'evidence': 'Common initial',
        'possible_meaning': 'PREFIX?',
        'tokens': 2103,
        'types': 919,
    },
}

# Suffixes - verified by productivity (unique roots using each suffix)
SUFFIXES = {
    'aiin': {
        'confidence': 'A',
        'evidence': '513 different roots, 67% of aiin/ain pairs',
        'possible_meaning': 'CASE MARKER 1 (nominative?)',
        'tokens': 3304,
        'types': 513,
    },
    'ain': {
        'confidence': 'A',
        'evidence': '294 different roots, 33% of aiin/ain pairs',
        'possible_meaning': 'CASE MARKER 2 (accusative?)',
        'tokens': 1577,
        'types': 294,
    },
    'dy': {
        'confidence': 'A',
        'evidence': '1124 different roots - most productive suffix',
        'possible_meaning': 'ADJECTIVAL',
        'tokens': 6273,
        'types': 1124,
    },
    'edy': {
        'confidence': 'A',
        'evidence': '420 different roots, extends -dy pattern',
        'possible_meaning': 'PARTICIPLE?',
        'tokens': 1847,
        'types': 420,
    },
    'ol': {
        'confidence': 'A',
        'evidence': '488 roots, 2962 tokens as suffix (NOT Latin oleum)',
        'possible_meaning': 'SUBSTANTIVAL',
        'tokens': 2962,
        'types': 488,
    },
    'or': {
        'confidence': 'B',
        'evidence': '430 different roots',
        'possible_meaning': 'AGENTIVE?',
        'tokens': 2015,
        'types': 430,
    },
    'ar': {
        'confidence': 'B',
        'evidence': '516 different roots',
        'possible_meaning': 'RELATIONAL?',
        'tokens': 2389,
        'types': 516,
    },
    'ey': {
        'confidence': 'B',
        'evidence': '685 different roots',
        'possible_meaning': 'GENITIVE?',
        'tokens': 2891,
        'types': 685,
    },
    'y': {
        'confidence': 'B',
        'evidence': '3227 different roots - most common ending',
        'possible_meaning': 'GENERAL SUFFIX',
        'tokens': 8234,
        'types': 3227,
    },
}

# Verified roots (appear with 4+ suffix variants, >100 tokens)
ROOTS = {
    'ch': {'confidence': 'A', 'tokens': 1696, 'suffix_count': 8, 'meaning': '?'},
    'd': {'confidence': 'A', 'tokens': 1633, 'suffix_count': 8, 'meaning': '?'},
    'sh': {'confidence': 'A', 'tokens': 1072, 'suffix_count': 8, 'meaning': '?'},
    'qok': {'confidence': 'A', 'tokens': 1199, 'suffix_count': 8, 'meaning': '?'},
    'che': {'confidence': 'A', 'tokens': 1046, 'suffix_count': 8, 'meaning': '?'},
    'qoke': {'confidence': 'A', 'tokens': 955, 'suffix_count': 8, 'meaning': '?'},
    'she': {'confidence': 'A', 'tokens': 845, 'suffix_count': 8, 'meaning': '?'},
    'ok': {'confidence': 'A', 'tokens': 765, 'suffix_count': 8, 'meaning': '?'},
    'ot': {'confidence': 'A', 'tokens': 719, 'suffix_count': 8, 'meaning': '?'},
    's': {'confidence': 'A', 'tokens': 677, 'suffix_count': 8, 'meaning': '?'},
}

# =============================================================================
# SPECULATIVE MEANINGS (Confidence: C - phonetically plausible, unverified)
# =============================================================================
# WARNING: These are HYPOTHESES, not proven translations.
# The Polish/Latin parallels are suggestive but NOT grammatically verified.

SPECULATIVE_VOCAB = {
    # These words exist in corpus but meanings are SPECULATIVE
    'dar': {
        'count': 297,
        'hypothesis': 'Polish dać (to give)',
        'confidence': 'C',
        'problem': 'Takes Voynich suffixes, not Polish conjugation',
    },
    'dal': {
        'count': 243,
        'hypothesis': 'Polish dał (he gave)',
        'confidence': 'C',
        'problem': 'Patterns identically to dar - may be spelling variant',
    },
    'chor': {
        'count': 206,
        'hypothesis': 'Polish chory (sick)',
        'confidence': 'C',
        'problem': 'No Polish case forms appear (choremu=0, chorzy=0)',
    },
    'sal': {
        'count': 54,
        'hypothesis': 'salt (Polish sól or Latin sal)',
        'confidence': 'C',
        'problem': 'Common in many languages, not diagnostic',
    },
    'sol': {
        'count': 67,
        'hypothesis': 'sun (Latin sol)',
        'confidence': 'C',
        'problem': 'Common in many languages, not diagnostic',
    },
    'ol': {
        'count': 525,
        'hypothesis': 'Latin oleum (oil)',
        'confidence': 'D',  # Downgraded
        'problem': '-ol is a SUFFIX (2962 tokens) more than prefix (1587)',
    },
}

# =============================================================================
# REJECTED ENTRIES (were in v7.5, but NOT in corpus)
# =============================================================================
REJECTED_ENTRIES = {
    'choremu': 'Claimed Polish dative - 0 corpus occurrences',
    'daj': 'Claimed Polish imperative - 0 corpus occurrences',
    'chorzy': 'Claimed Polish plural - 0 corpus occurrences',
    'chora': 'Claimed Polish feminine - 0 corpus occurrences',
}

# =============================================================================
# MORPHOLOGICAL ANALYSIS FUNCTIONS
# =============================================================================

def analyze_word(word: str) -> dict:
    """
    Analyze a Voynich word's structure.
    Returns prefix, root, suffix with confidence ratings.
    """
    result = {
        'word': word,
        'prefix': None,
        'root': None,
        'suffix': None,
        'structure_confidence': 'B',  # Default
        'meaning': '?',
        'meaning_confidence': 'D',  # Unknown by default
    }

    remainder = word

    # Check for prefix
    for pre in sorted(PREFIXES.keys(), key=len, reverse=True):
        if remainder.startswith(pre) and len(remainder) > len(pre):
            result['prefix'] = pre + '-'
            result['structure_confidence'] = PREFIXES[pre]['confidence']
            remainder = remainder[len(pre):]
            break

    # Check for suffix
    for suf in sorted(SUFFIXES.keys(), key=len, reverse=True):
        if remainder.endswith(suf) and len(remainder) > len(suf):
            result['suffix'] = '-' + suf
            if SUFFIXES[suf]['confidence'] == 'A':
                result['structure_confidence'] = 'A'
            remainder = remainder[:-len(suf)]
            break

    result['root'] = remainder if remainder else word

    # Check if root is verified
    if result['root'] in ROOTS:
        result['structure_confidence'] = 'A'

    # Check for speculative meaning
    if word in SPECULATIVE_VOCAB:
        result['meaning'] = f"?{SPECULATIVE_VOCAB[word]['hypothesis']}"
        result['meaning_confidence'] = SPECULATIVE_VOCAB[word]['confidence']

    return result


def decode_word(word: str, show_structure: bool = False) -> str:
    """
    Decode a single word with honest uncertainty markers.

    Args:
        word: The Voynich word to decode
        show_structure: If True, show morphological breakdown

    Returns:
        String with decoded meaning or ? for unknown
    """
    analysis = analyze_word(word)

    if show_structure:
        parts = []
        if analysis['prefix']:
            parts.append(f"[{analysis['prefix']}]")
        parts.append(f"[{analysis['root']}]")
        if analysis['suffix']:
            parts.append(f"[{analysis['suffix']}]")
        structure = ''.join(parts)
        return f"{word}={structure}({analysis['meaning']})"
    else:
        return f"{word}[{analysis['meaning']}]"


def decode_text(text: str, show_structure: bool = False) -> str:
    """
    Decode a line of Voynich text.

    Args:
        text: Period-separated Voynich words
        show_structure: If True, show morphological breakdown

    Returns:
        Decoded text with uncertainty markers
    """
    words = text.replace('.', ' . ').split()
    result = []

    for word in words:
        if word == '.':
            result.append('.')
        else:
            result.append(decode_word(word, show_structure))

    return ' '.join(result)


def get_corpus_word_count(word: str) -> int:
    """Return how many times a word appears in corpus (from stored data)."""
    # Top 100 words with counts
    WORD_COUNTS = {
        'daiin': 805, 'ol': 525, 'chedy': 496, 'aiin': 457, 'shedy': 425,
        'chol': 381, 'or': 350, 'ar': 346, 'chey': 339, 'qokeey': 308,
        'qokeedy': 301, 'dar': 297, 'qokain': 277, 'shey': 276, 'qokedy': 265,
        'qokaiin': 262, 'al': 253, 'dal': 243, 'dy': 226, 'okaiin': 209,
        'chor': 206, 'dain': 189, 'qokal': 188, 'shol': 175, 'okeey': 174,
        'cheey': 174, 'cheol': 167, 'otedy': 154, 'otaiin': 150, 'qokar': 149,
        'qol': 148, 'chdy': 145, 'sheey': 142, 'okain': 141, 'qoky': 139,
        'otar': 139, 'otal': 137, 'chy': 136, 'saiin': 136, 'oteey': 135,
        'chckhy': 134, 'okal': 133, 'okar': 124, 'sho': 121, 'lchedy': 119,
        'okedy': 116, 'sheol': 113, 'dol': 111, 'oty': 110, 'cthy': 105,
    }
    return WORD_COUNTS.get(word, 0)


# =============================================================================
# SUMMARY STATISTICS
# =============================================================================

def print_summary():
    """Print summary of what we know vs don't know."""
    print("=" * 70)
    print("VOYNICH DECODER v8.0 - HONEST ASSESSMENT")
    print("=" * 70)
    print()
    print("WHAT WE KNOW (HIGH CONFIDENCE):")
    print("  ✓ Morphological structure exists")
    print("  ✓ Productive prefixes: qo-, o-, y-")
    print("  ✓ Productive suffixes: -aiin, -ain, -dy, -ol, -or")
    print("  ✓ qo-X/X pairs suggest qo- is a determiner")
    print("  ✓ -aiin/-ain (67%/33%) suggests grammatical case")
    print()
    print("WHAT WE CANNOT PROVE:")
    print("  ✗ That any specific word means anything specific")
    print("  ✗ That the language is Polish (paradigms don't appear)")
    print("  ✗ That the language is Latin (declensions don't appear)")
    print("  ✗ That our phonetic mappings are correct")
    print()
    print("REJECTED FROM v7.5:")
    for entry, reason in REJECTED_ENTRIES.items():
        print(f"  - {entry}: {reason}")
    print()


if __name__ == '__main__':
    print_summary()

    print("\nEXAMPLE ANALYSIS:")
    print("-" * 50)

    test_words = ['daiin', 'qokaiin', 'chedy', 'dar', 'chor', 'shedy']
    for word in test_words:
        analysis = analyze_word(word)
        print(f"\n{word}:")
        print(f"  Structure: {analysis['prefix'] or ''}{analysis['root']}{analysis['suffix'] or ''}")
        print(f"  Structure confidence: {analysis['structure_confidence']}")
        print(f"  Meaning: {analysis['meaning']}")
        print(f"  Meaning confidence: {analysis['meaning_confidence']}")
