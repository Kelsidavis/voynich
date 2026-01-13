#!/usr/bin/env python3
"""
Run blind decoding on sampled labels using CANDIDATES.csv.

This script implements the blind decoding phase defined in BLIND_TEST_PLAN.md.
It reads blind_inputs.csv and attempts to match roots from CANDIDATES.csv
WITHOUT access to section information.
"""

import csv
import re
import os
from pathlib import Path
from datetime import datetime


def load_candidates(candidates_path: str) -> list:
    """
    Load candidate roots from CANDIDATES.csv.

    Returns: list of dicts with root, gloss, domain info
    """
    candidates = []
    with open(candidates_path, 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Only use strict exact matches for confirmatory test
            if row['match_type'] == 'exact':
                candidates.append({
                    'root': row['root'],
                    'language': row['language'],
                    'gloss': row['gloss'],
                    'domain': row['domain'],
                    'confidence': row['confidence']
                })
    return candidates


def find_matches(eva_text: str, candidates: list) -> list:
    """
    Find all candidate roots that appear in the EVA text.

    Uses substring matching: root must appear as substring within any token.

    Returns: list of matched candidates
    """
    matches = []
    tokens = eva_text.lower().split('.')

    for candidate in candidates:
        root = candidate['root'].lower()
        # Check if root appears in any token
        for token in tokens:
            if root in token:
                matches.append(candidate)
                break  # Only count each candidate once per label

    return matches


def decode_blind_inputs(blind_inputs_path: str, candidates_path: str, output_path: str):
    """
    Decode blind inputs and write results.
    """
    candidates = load_candidates(candidates_path)
    print(f"Loaded {len(candidates)} exact-match candidates")

    results = []

    with open(blind_inputs_path, 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            blind_id = row['blind_id']
            eva_text = row['eva_text']

            matches = find_matches(eva_text, candidates)

            if matches:
                matched_roots = ','.join([m['root'] for m in matches])
                glosses = ','.join([m['gloss'] for m in matches])
                domains = ','.join([m['domain'] for m in matches])
            else:
                matched_roots = ''
                glosses = ''
                domains = ''

            results.append({
                'blind_id': blind_id,
                'eva_text': eva_text,
                'matched_roots': matched_roots,
                'glosses': glosses,
                'domains': domains,
                'transform_used': 'none'  # Strict matching only
            })

    # Write results
    with open(output_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=[
            'blind_id', 'eva_text', 'matched_roots', 'glosses', 'domains', 'transform_used'
        ])
        writer.writeheader()
        writer.writerows(results)

    # Print summary
    matches_found = sum(1 for r in results if r['matched_roots'])
    print(f"\nDecoding complete:")
    print(f"  Total labels: {len(results)}")
    print(f"  Labels with matches: {matches_found}")
    print(f"  Labels without matches: {len(results) - matches_found}")
    print(f"\nOutput: {output_path}")

    return results


def main():
    repo_root = Path(__file__).parent.parent

    # Find the most recent run directory
    blind_test_dir = repo_root / 'evidence' / 'blind_test'
    run_dirs = sorted(blind_test_dir.glob('run_*'), reverse=True)

    if not run_dirs:
        print("No blind test runs found. Run extract_blind_labels.py first.")
        return

    run_dir = run_dirs[0]
    print(f"Using run directory: {run_dir}")

    blind_inputs_path = run_dir / 'blind_inputs.csv'
    candidates_path = repo_root / 'evidence' / 'CANDIDATES.csv'
    output_path = run_dir / 'blind_decodes.csv'

    if not blind_inputs_path.exists():
        print(f"Error: {blind_inputs_path} not found")
        return

    if not candidates_path.exists():
        print(f"Error: {candidates_path} not found")
        return

    decode_blind_inputs(str(blind_inputs_path), str(candidates_path), str(output_path))


if __name__ == '__main__':
    main()
