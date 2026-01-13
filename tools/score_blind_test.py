#!/usr/bin/env python3
"""
Score blind test results and run shuffle baseline.

This script implements the reveal and scoring phase defined in BLIND_TEST_PLAN.md.
It joins decoded results with section information and computes hit rates.
"""

import csv
import random
from pathlib import Path
from collections import Counter
import statistics


# Section-domain scoring rubric from MATCHING_PROTOCOL.md
SECTION_HIT_DOMAINS = {
    'H': {'BOTANICAL', 'MEDICAL'},      # Herbal
    'Z': {'CELESTIAL'},                  # Zodiac
    'B': {'BODY', 'MEDICAL'},            # Biological
    'P': {'MEDICAL', 'BOTANICAL'},       # Pharmaceutical
}

SECTION_MISS_DOMAINS = {
    'H': {'CELESTIAL'},
    'Z': {'BOTANICAL', 'BODY'},
    'B': {'CELESTIAL', 'BOTANICAL'},
    'P': {'CELESTIAL'},
}


def score_label(section: str, domains: str) -> str:
    """
    Score a single label as HIT, MISS, or AMBIG.

    Args:
        section: H, Z, B, or P
        domains: comma-separated domain string (may be empty)

    Returns: 'HIT', 'MISS', or 'AMBIG'
    """
    if not domains:
        return 'AMBIG'

    domain_set = set(d.strip() for d in domains.split(','))

    # Check for hits first
    hit_domains = SECTION_HIT_DOMAINS.get(section, set())
    if domain_set & hit_domains:
        return 'HIT'

    # Check for misses
    miss_domains = SECTION_MISS_DOMAINS.get(section, set())
    if domain_set & miss_domains:
        return 'MISS'

    # Everything else is ambiguous (e.g., VERB, TEMPORAL)
    return 'AMBIG'


def reveal_and_score(decodes_path: str, reveal_key_path: str, output_dir: str) -> dict:
    """
    Join decoded results with section info and score.

    Returns: dict with scoring statistics
    """
    # Load reveal key
    key_map = {}
    with open(reveal_key_path, 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            key_map[row['blind_id']] = {
                'locator': row['locator'],
                'section': row['section']
            }

    # Load decodes and join
    results = []
    with open(decodes_path, 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            blind_id = row['blind_id']
            key_info = key_map.get(blind_id, {})

            section = key_info.get('section', '')
            domains = row['domains']
            score = score_label(section, domains)

            results.append({
                'blind_id': blind_id,
                'locator': key_info.get('locator', ''),
                'section': section,
                'eva_text': row['eva_text'],
                'matched_roots': row['matched_roots'],
                'glosses': row['glosses'],
                'domains': domains,
                'score': score
            })

    # Write revealed results
    revealed_path = Path(output_dir) / 'revealed.csv'
    with open(revealed_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=[
            'blind_id', 'locator', 'section', 'eva_text',
            'matched_roots', 'glosses', 'domains', 'score'
        ])
        writer.writeheader()
        writer.writerows(results)

    # Write scored results
    scored_path = Path(output_dir) / 'scored_results.csv'
    with open(scored_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=[
            'blind_id', 'section', 'domains', 'score'
        ])
        writer.writeheader()
        for r in results:
            writer.writerow({
                'blind_id': r['blind_id'],
                'section': r['section'],
                'domains': r['domains'],
                'score': r['score']
            })

    # Calculate statistics
    score_counts = Counter(r['score'] for r in results)
    hits = score_counts.get('HIT', 0)
    misses = score_counts.get('MISS', 0)
    ambig = score_counts.get('AMBIG', 0)
    non_ambig = hits + misses

    stats = {
        'total': len(results),
        'hits': hits,
        'misses': misses,
        'ambig': ambig,
        'hit_rate': hits / non_ambig if non_ambig > 0 else None,
        'non_ambig': non_ambig
    }

    print(f"\nScoring complete:")
    print(f"  Total labels: {stats['total']}")
    print(f"  HIT: {hits}")
    print(f"  MISS: {misses}")
    print(f"  AMBIG: {ambig}")
    if stats['hit_rate'] is not None:
        print(f"  Hit rate: {stats['hit_rate']:.3f} ({hits}/{non_ambig})")
    else:
        print(f"  Hit rate: N/A (no non-ambiguous results)")

    print(f"\nOutput: {revealed_path}")
    print(f"        {scored_path}")

    return stats, results


def run_shuffle_baseline(results: list, n_shuffles: int = 1000) -> dict:
    """
    Run shuffle baseline to establish expected hit rates by chance.
    """
    if not results:
        return {}

    # Get the actual scores for labels that have domains
    scored_labels = [(r['section'], r['domains']) for r in results if r['domains']]

    if not scored_labels:
        return {'mean': None, 'std': None, 'n_shuffles': n_shuffles}

    # Separate sections and domains
    sections = [s for s, d in scored_labels]
    domains_list = [d for s, d in scored_labels]

    hit_rates = []
    random.seed(2026)

    for _ in range(n_shuffles):
        # Shuffle sections relative to domains
        shuffled_sections = sections.copy()
        random.shuffle(shuffled_sections)

        # Score the shuffled version
        hits = 0
        misses = 0
        for section, domains in zip(shuffled_sections, domains_list):
            score = score_label(section, domains)
            if score == 'HIT':
                hits += 1
            elif score == 'MISS':
                misses += 1

        if hits + misses > 0:
            hit_rates.append(hits / (hits + misses))

    if hit_rates:
        mean_rate = statistics.mean(hit_rates)
        std_rate = statistics.stdev(hit_rates) if len(hit_rates) > 1 else 0
    else:
        mean_rate = None
        std_rate = None

    return {
        'mean': mean_rate,
        'std': std_rate,
        'n_shuffles': n_shuffles,
        'hit_rates': hit_rates
    }


def generate_report(stats: dict, baseline: dict, output_dir: str):
    """
    Generate the run report markdown file.
    """
    import subprocess
    from datetime import datetime

    # Try to get git hash
    try:
        git_hash = subprocess.check_output(
            ['git', 'rev-parse', 'HEAD'],
            cwd=output_dir,
            stderr=subprocess.DEVNULL
        ).decode().strip()[:8]
    except:
        git_hash = 'unknown'

    report_path = Path(output_dir) / 'RUN_REPORT.md'

    with open(report_path, 'w') as f:
        f.write("# Blind Test Run Report\n\n")
        f.write(f"**Date**: {datetime.now().strftime('%Y-%m-%d')}\n")
        f.write(f"**Protocol version**: {git_hash}\n\n")

        f.write("## Sample Statistics\n")
        f.write(f"- Total labels sampled: {stats['total']}\n")
        f.write(f"- Labels with matches: {stats['total'] - stats['ambig']}\n")
        f.write(f"- Labels without matches: {stats['ambig']}\n\n")

        f.write("## Scoring Results\n")
        f.write(f"- HIT: {stats['hits']}\n")
        f.write(f"- MISS: {stats['misses']}\n")
        f.write(f"- AMBIG: {stats['ambig']}\n")
        if stats['hit_rate'] is not None:
            f.write(f"- Hit Rate: {stats['hit_rate']:.3f} ({stats['hits']}/{stats['non_ambig']})\n\n")
        else:
            f.write("- Hit Rate: N/A (insufficient non-ambiguous results)\n\n")

        f.write("## Baseline Comparison\n")
        if baseline.get('mean') is not None:
            f.write(f"- Shuffled mean hit rate: {baseline['mean']:.3f}\n")
            f.write(f"- Shuffled std dev: {baseline['std']:.3f}\n")

            if stats['hit_rate'] is not None and baseline['std'] > 0:
                z_score = (stats['hit_rate'] - baseline['mean']) / baseline['std']
                f.write(f"- Z-score: {z_score:.2f}\n")

                if z_score >= 2:
                    conclusion = "**SUPPORTED** - Hit rate significantly above baseline"
                elif stats['non_ambig'] < 5:
                    conclusion = "**UNDERPOWERED** - Insufficient non-ambiguous results (n < 5)"
                else:
                    conclusion = "**NOT SUPPORTED** - Hit rate not significantly above baseline"
            else:
                conclusion = "**UNDERPOWERED** - Cannot compute significance"
        else:
            f.write("- Baseline: N/A (no matched labels to shuffle)\n")
            conclusion = "**UNDERPOWERED** - No matches found; expand candidate list"

        f.write(f"\n## Conclusion\n\n{conclusion}\n")

        f.write("\n## Interpretation\n\n")
        if stats['ambig'] == stats['total']:
            f.write("All labels scored AMBIG, meaning no candidate roots were found in the sampled labels. ")
            f.write("This indicates the candidate list is too small or the root lengths are too restrictive. ")
            f.write("**Recommendation**: Expand CANDIDATES.csv with additional strict roots.\n")
        elif stats['non_ambig'] < 5:
            f.write(f"Only {stats['non_ambig']} labels had domain assignments, which is insufficient for ")
            f.write("statistical significance testing (minimum n=5 required). ")
            f.write("**Recommendation**: Expand CANDIDATES.csv to increase coverage.\n")

    print(f"\nReport: {report_path}")


def main():
    repo_root = Path(__file__).parent.parent

    # Find the most recent run directory
    blind_test_dir = repo_root / 'evidence' / 'blind_test'
    run_dirs = sorted(blind_test_dir.glob('run_*'), reverse=True)

    if not run_dirs:
        print("No blind test runs found.")
        return

    run_dir = run_dirs[0]
    print(f"Using run directory: {run_dir}")

    decodes_path = run_dir / 'blind_decodes.csv'
    reveal_key_path = run_dir / '.reveal_key.csv'

    if not decodes_path.exists():
        print(f"Error: {decodes_path} not found. Run run_blind_decode.py first.")
        return

    if not reveal_key_path.exists():
        print(f"Error: {reveal_key_path} not found.")
        return

    # Run scoring
    stats, results = reveal_and_score(
        str(decodes_path),
        str(reveal_key_path),
        str(run_dir)
    )

    # Run baseline
    print("\nRunning shuffle baseline (1000 iterations)...")
    baseline = run_shuffle_baseline(results)

    if baseline.get('mean') is not None:
        print(f"  Baseline mean: {baseline['mean']:.3f}")
        print(f"  Baseline std: {baseline['std']:.3f}")

    # Write baseline results
    baseline_path = run_dir / 'shuffled_baseline.csv'
    with open(baseline_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['shuffle_num', 'hit_rate'])
        for i, rate in enumerate(baseline.get('hit_rates', [])):
            writer.writerow([i+1, rate])

    print(f"\nBaseline: {baseline_path}")

    # Generate report
    generate_report(stats, baseline, str(run_dir))


if __name__ == '__main__':
    main()
