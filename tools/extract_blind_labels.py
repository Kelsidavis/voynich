#!/usr/bin/env python3
"""
Extract label samples for blind testing from Voynich EVA transcription.

This script implements the deterministic sampling procedure defined in
BLIND_TEST_PLAN.md. It produces blind_inputs.csv with hashed locators
to ensure blindness during decoding.
"""

import hashlib
import csv
import re
import random
import os
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# Configuration
SAMPLES_PER_SECTION = 5
SEED = 2026  # Fixed seed for reproducibility
MIN_TOKEN_LENGTH = 2


def hash_locator(locator: str) -> str:
    """Generate 8-char hash of locator for blindness."""
    return hashlib.sha256(locator.encode()).hexdigest()[:8]


def extract_eva_tokens(text: str) -> list:
    """Extract alphabetic EVA tokens from a line."""
    # Remove special markers and fillers
    cleaned = re.sub(r'[!%*{}]', '', text)
    cleaned = re.sub(r'<[^>]+>', '', cleaned)
    # Split on . and , and =
    tokens = re.split(r'[.,=\s]+', cleaned)
    # Keep only alphabetic tokens
    return [t for t in tokens if t and re.match(r'^[a-z]+$', t) and len(t) >= MIN_TOKEN_LENGTH]


def parse_transcription(filepath: str) -> dict:
    """
    Parse the IVTFF transcription file into sections with labels.

    Returns: dict mapping section -> list of (locator, eva_text) tuples
    """
    sections = defaultdict(list)
    current_section = None
    current_folio = None

    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            line = line.rstrip()

            # Skip comments and empty lines
            if line.startswith('#') or not line.strip():
                continue

            # Detect folio header with section info
            # Format: <f1r>          <! $I=H $Q=A $P=A $L=A $H=1 $X=V>
            folio_match = re.match(r'^<(f\d+[rv]\d?)>', line)
            if folio_match:
                current_folio = folio_match.group(1)
                section_match = re.search(r'\$I=([HZBPC])', line)
                if section_match:
                    current_section = section_match.group(1)
                continue

            # Detect label lines
            # Format: <f57v.1,@L0;H>     dairol
            label_match = re.match(r'^<([^>]+),@L[^;]*;([A-Z])>\s*(.+)$', line)
            if label_match and current_section:
                locator = label_match.group(1)
                transcriber = label_match.group(2)
                text = label_match.group(3).strip()

                # Only use Takahashi (U) or other primary transcriptions
                if transcriber in ['U', 'H', 'V']:
                    tokens = extract_eva_tokens(text)
                    if tokens:  # Has at least one valid token
                        eva_text = '.'.join(tokens)
                        sections[current_section].append((locator, eva_text))

            # Also capture circular/radial lines from zodiac
            # Format: <f72r1.01,@Cr0;V> oteodar.dar.shy=
            circ_match = re.match(r'^<([^>]+),@C[^;]*;([A-Z])>\s*(.+)$', line)
            if circ_match and current_section:
                locator = circ_match.group(1)
                transcriber = circ_match.group(2)
                text = circ_match.group(3).strip()

                if transcriber in ['U', 'H', 'V'] and text.endswith('='):
                    tokens = extract_eva_tokens(text)
                    if tokens:
                        eva_text = '.'.join(tokens)
                        sections[current_section].append((locator, eva_text))

    return sections


def deterministic_sample(items: list, n: int, seed: int) -> list:
    """
    Deterministically sample n items using hash-based ordering.
    """
    if len(items) <= n:
        return items

    # Sort by hash of locator for deterministic ordering
    sorted_items = sorted(items, key=lambda x: hash_locator(x[0] + str(seed)))
    return sorted_items[:n]


def generate_blind_inputs(transcription_path: str, output_dir: str) -> str:
    """
    Generate blind_inputs.csv from transcription.

    Returns: path to the generated file
    """
    # Parse transcription
    sections = parse_transcription(transcription_path)

    # Sample from each section
    samples = []
    for section in ['H', 'Z', 'B', 'P']:
        section_samples = deterministic_sample(
            sections.get(section, []),
            SAMPLES_PER_SECTION,
            SEED
        )
        for locator, eva_text in section_samples:
            samples.append({
                'locator': locator,
                'section': section,  # Will be hidden in output
                'eva_text': eva_text
            })

    # Shuffle samples (deterministically)
    random.seed(SEED)
    random.shuffle(samples)

    # Generate blind IDs
    for i, sample in enumerate(samples):
        sample['blind_id'] = f'B{i+1:02d}'

    # Create output directory
    os.makedirs(output_dir, exist_ok=True)

    # Write blind_inputs.csv (without section info)
    blind_path = os.path.join(output_dir, 'blind_inputs.csv')
    with open(blind_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['blind_id', 'locator_hash', 'eva_text'])
        writer.writeheader()
        for sample in samples:
            writer.writerow({
                'blind_id': sample['blind_id'],
                'locator_hash': hash_locator(sample['locator']),
                'eva_text': sample['eva_text']
            })

    # Write key file (for reveal phase) - keep in separate location
    key_path = os.path.join(output_dir, '.reveal_key.csv')
    with open(key_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['blind_id', 'locator', 'section'])
        writer.writeheader()
        for sample in samples:
            writer.writerow({
                'blind_id': sample['blind_id'],
                'locator': sample['locator'],
                'section': sample['section']
            })

    print(f"Generated {len(samples)} blind samples")
    print(f"  H (Herbal): {len([s for s in samples if s['section'] == 'H'])}")
    print(f"  Z (Zodiac): {len([s for s in samples if s['section'] == 'Z'])}")
    print(f"  B (Biological): {len([s for s in samples if s['section'] == 'B'])}")
    print(f"  P (Pharmaceutical): {len([s for s in samples if s['section'] == 'P'])}")
    print(f"\nBlind inputs: {blind_path}")
    print(f"Reveal key: {key_path}")

    return blind_path


def main():
    # Paths relative to repository root
    repo_root = Path(__file__).parent.parent
    transcription_path = repo_root / 'data' / 'voynich_transcription.txt'

    # Create run directory with date
    run_date = datetime.now().strftime('%Y-%m-%d')
    output_dir = repo_root / 'evidence' / 'blind_test' / f'run_{run_date}'

    generate_blind_inputs(str(transcription_path), str(output_dir))


if __name__ == '__main__':
    main()
