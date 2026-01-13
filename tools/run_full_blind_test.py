#!/usr/bin/env python3
"""
Run the complete blind test pipeline.

This script executes all three phases:
1. Extract blind labels from transcription
2. Decode blindly using CANDIDATES.csv
3. Reveal sections and score results

Usage: python run_full_blind_test.py
"""

import os
import sys
from pathlib import Path

# Add tools directory to path for imports
tools_dir = Path(__file__).parent
sys.path.insert(0, str(tools_dir))

from extract_blind_labels import generate_blind_inputs
from run_blind_decode import decode_blind_inputs, load_candidates
from score_blind_test import reveal_and_score, run_shuffle_baseline, generate_report
from datetime import datetime


def main():
    repo_root = tools_dir.parent

    print("=" * 60)
    print("VOYNICH BLIND TEST PIPELINE")
    print("=" * 60)

    # Check prerequisites
    transcription_path = repo_root / 'data' / 'voynich_transcription.txt'
    candidates_path = repo_root / 'evidence' / 'CANDIDATES.csv'

    if not transcription_path.exists():
        print(f"Error: Transcription not found at {transcription_path}")
        return 1

    if not candidates_path.exists():
        print(f"Error: Candidates not found at {candidates_path}")
        return 1

    # Create run directory
    run_date = datetime.now().strftime('%Y-%m-%d')
    run_dir = repo_root / 'evidence' / 'blind_test' / f'run_{run_date}'
    os.makedirs(run_dir, exist_ok=True)

    print(f"\nRun directory: {run_dir}\n")

    # Phase 1: Extract
    print("-" * 60)
    print("PHASE 1: EXTRACT BLIND LABELS")
    print("-" * 60)
    blind_inputs_path = generate_blind_inputs(
        str(transcription_path),
        str(run_dir)
    )

    # Phase 2: Decode
    print("\n" + "-" * 60)
    print("PHASE 2: BLIND DECODING")
    print("-" * 60)
    decode_blind_inputs(
        str(run_dir / 'blind_inputs.csv'),
        str(candidates_path),
        str(run_dir / 'blind_decodes.csv')
    )

    # Phase 3: Score
    print("\n" + "-" * 60)
    print("PHASE 3: REVEAL & SCORE")
    print("-" * 60)
    stats, results = reveal_and_score(
        str(run_dir / 'blind_decodes.csv'),
        str(run_dir / '.reveal_key.csv'),
        str(run_dir)
    )

    # Run baseline
    print("\n" + "-" * 60)
    print("PHASE 4: BASELINE COMPARISON")
    print("-" * 60)
    baseline = run_shuffle_baseline(results)

    if baseline.get('mean') is not None:
        print(f"Shuffled baseline mean: {baseline['mean']:.3f}")
        print(f"Shuffled baseline std: {baseline['std']:.3f}")

    # Write baseline
    import csv
    baseline_path = run_dir / 'shuffled_baseline.csv'
    with open(baseline_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['shuffle_num', 'hit_rate'])
        for i, rate in enumerate(baseline.get('hit_rates', [])):
            writer.writerow([i+1, rate])

    # Generate report
    generate_report(stats, baseline, str(run_dir))

    # Final summary
    print("\n" + "=" * 60)
    print("PIPELINE COMPLETE")
    print("=" * 60)
    print(f"\nAll outputs in: {run_dir}")
    print("\nFiles generated:")
    for f in sorted(run_dir.glob('*')):
        if not f.name.startswith('.'):
            print(f"  {f.name}")

    return 0


if __name__ == '__main__':
    sys.exit(main())
