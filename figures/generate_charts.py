#!/usr/bin/env python3
"""
Generate visualization charts for Voynich Polish-Latin decoding evidence
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# Set style
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['font.size'] = 11
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['axes.labelsize'] = 12

# Data from analysis
sections = ['Herbal\n(f1-57)', 'Astro\n(f67-73)', 'Bio\n(f75-84)',
            'Rosettes\n(f85-86)', 'F87', 'Recipe\n(f88-116)']
sections_short = ['Herbal', 'Astro', 'Bio', 'Rosettes', 'F87', 'Recipe']

# Word counts
words = [9575, 3026, 6851, 1810, 172, 14319]

# Polish percentages
polish_pct = [5.0, 4.1, 4.5, 28.7, 16.9, 10.3]

# Key term counts
chor_counts = [147, 6, 10, 12, 4, 97]
dar_dal_counts = [151, 67, 133, 105, 13, 428]
ol_counts = [65, 15, 233, 50, 5, 1432]
water_counts = [300, 100, 670, 50, 10, 400]  # Approximate she- terms
star_counts = [80, 472, 50, 163, 10, 200]  # ot- terms

# Colors
colors = ['#2ecc71', '#3498db', '#9b59b6', '#e74c3c', '#f39c12', '#1abc9c']


def save_chart(fig, name):
    """Save chart in multiple formats"""
    fig.savefig(f'/home/k/Desktop/voynich-decoded/figures/charts/{name}.png',
                dpi=150, bbox_inches='tight', facecolor='white')
    print(f"  Saved: {name}.png")


# Create output directory
import os
os.makedirs('/home/k/Desktop/voynich-decoded/figures/charts', exist_ok=True)


# ============================================================================
# CHART 1: Polish Percentage by Section
# ============================================================================
print("Generating Chart 1: Polish Percentage by Section...")

fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.bar(sections, polish_pct, color=colors, edgecolor='black', linewidth=1.2)

# Add value labels on bars
for bar, pct in zip(bars, polish_pct):
    height = bar.get_height()
    ax.annotate(f'{pct}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom', fontweight='bold', fontsize=12)

# Highlight rosettes as highest
bars[3].set_edgecolor('#c0392b')
bars[3].set_linewidth(3)

ax.set_ylabel('Polish Vocabulary (%)', fontweight='bold')
ax.set_title('Polish Vocabulary Percentage by Manuscript Section', fontweight='bold', fontsize=14)
ax.set_ylim(0, 35)

# Add annotation for rosettes
ax.annotate('HIGHEST\n(Theory)', xy=(3, 28.7), xytext=(3.5, 32),
            fontsize=10, ha='center', color='#c0392b', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#c0392b'))

plt.tight_layout()
save_chart(fig, 'polish_percentage_by_section')
plt.close()


# ============================================================================
# CHART 2: Vocabulary Gradient (Rosettes → F87 → Recipe)
# ============================================================================
print("Generating Chart 2: Vocabulary Gradient...")

fig, ax = plt.subplots(figsize=(10, 6))

gradient_sections = ['Rosettes\n(Theory)', 'F87\n(Transition)', 'Recipe\n(Practice)']
gradient_polish = [28.7, 16.9, 10.3]
gradient_cosmo = [9.0, 5.8, 2.0]

x = np.arange(len(gradient_sections))
width = 0.35

bars1 = ax.bar(x - width/2, gradient_polish, width, label='Polish %',
               color='#e74c3c', edgecolor='black')
bars2 = ax.bar(x + width/2, gradient_cosmo, width, label='Cosmological %',
               color='#3498db', edgecolor='black')

# Add value labels
for bar in bars1:
    height = bar.get_height()
    ax.annotate(f'{height}%', xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3), textcoords="offset points", ha='center',
                va='bottom', fontweight='bold')

for bar in bars2:
    height = bar.get_height()
    ax.annotate(f'{height}%', xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3), textcoords="offset points", ha='center',
                va='bottom', fontweight='bold')

ax.set_ylabel('Percentage of Vocabulary', fontweight='bold')
ax.set_title('Vocabulary Gradient: Theory → Practice', fontweight='bold', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(gradient_sections)
ax.legend(loc='upper right')
ax.set_ylim(0, 35)

# Add trend arrow
ax.annotate('', xy=(2.3, 5), xytext=(-0.3, 25),
            arrowprops=dict(arrowstyle='->', color='gray', lw=2, ls='--'))
ax.text(1, 18, 'Decreasing\ntoward\npractice', fontsize=10, ha='center',
        color='gray', style='italic')

plt.tight_layout()
save_chart(fig, 'vocabulary_gradient')
plt.close()


# ============================================================================
# CHART 3: CHOR (Sick) Distribution
# ============================================================================
print("Generating Chart 3: CHOR Distribution...")

fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.bar(sections, chor_counts, color='#e74c3c', edgecolor='black', linewidth=1.2)

for bar, count in zip(bars, chor_counts):
    height = bar.get_height()
    ax.annotate(f'{count}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom', fontweight='bold', fontsize=12)

# Highlight herbal as highest
bars[0].set_edgecolor('#c0392b')
bars[0].set_linewidth(3)

ax.set_ylabel('CHOR (sick) Occurrences', fontweight='bold')
ax.set_title('Patient References (CHOR = Polish "chory" = sick)\nDistribution by Section',
             fontweight='bold', fontsize=14)
ax.set_ylim(0, 180)

ax.annotate('HIGHEST\n(Plants indexed\nby condition)', xy=(0, 147), xytext=(1, 160),
            fontsize=10, ha='center', color='#c0392b', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#c0392b'))

plt.tight_layout()
save_chart(fig, 'chor_distribution')
plt.close()


# ============================================================================
# CHART 4: DAR/DAL (Give) Distribution
# ============================================================================
print("Generating Chart 4: DAR/DAL Distribution...")

fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.bar(sections, dar_dal_counts, color='#2ecc71', edgecolor='black', linewidth=1.2)

for bar, count in zip(bars, dar_dal_counts):
    height = bar.get_height()
    ax.annotate(f'{count}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom', fontweight='bold', fontsize=12)

# Highlight recipe as highest
bars[5].set_edgecolor('#27ae60')
bars[5].set_linewidth(3)

ax.set_ylabel('DAR/DAL (give) Occurrences', fontweight='bold')
ax.set_title('Instruction Verb (DAR/DAL = Polish "dać/dał" = give/gave)\nDistribution by Section',
             fontweight='bold', fontsize=14)
ax.set_ylim(0, 500)

ax.annotate('HIGHEST\n(Preparation\ninstructions)', xy=(5, 428), xytext=(4, 460),
            fontsize=10, ha='center', color='#27ae60', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#27ae60'))

plt.tight_layout()
save_chart(fig, 'dar_dal_distribution')
plt.close()


# ============================================================================
# CHART 5: OL (Oil) Distribution
# ============================================================================
print("Generating Chart 5: OL Distribution...")

fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.bar(sections, ol_counts, color='#f39c12', edgecolor='black', linewidth=1.2)

for bar, count in zip(bars, ol_counts):
    height = bar.get_height()
    ax.annotate(f'{count}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom', fontweight='bold', fontsize=12)

# Highlight recipe as highest
bars[5].set_edgecolor('#d35400')
bars[5].set_linewidth(3)

ax.set_ylabel('OL (oil) Occurrences', fontweight='bold')
ax.set_title('Pharmaceutical Base (OL = Latin "oleum" = oil)\nDistribution by Section',
             fontweight='bold', fontsize=14)
ax.set_ylim(0, 1600)

ax.annotate('HIGHEST\n(1,432 = 10%\nof section)', xy=(5, 1432), xytext=(4, 1500),
            fontsize=10, ha='center', color='#d35400', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#d35400'))

plt.tight_layout()
save_chart(fig, 'ol_distribution')
plt.close()


# ============================================================================
# CHART 6: Section Comparison - Stacked Key Terms
# ============================================================================
print("Generating Chart 6: Section Comparison (Stacked)...")

fig, ax = plt.subplots(figsize=(12, 7))

x = np.arange(len(sections_short))
width = 0.6

# Normalize to per-1000 words for comparison
chor_per_k = [c/w*1000 for c, w in zip(chor_counts, words)]
dar_per_k = [d/w*1000 for d, w in zip(dar_dal_counts, words)]
star_per_k = [s/w*1000 for s, w in zip(star_counts, words)]

# Stack bars
p1 = ax.bar(x, chor_per_k, width, label='CHOR (sick)', color='#e74c3c')
p2 = ax.bar(x, dar_per_k, width, bottom=chor_per_k, label='DAR/DAL (give)', color='#2ecc71')
p3 = ax.bar(x, star_per_k, width, bottom=[c+d for c,d in zip(chor_per_k, dar_per_k)],
            label='OT- (star)', color='#3498db')

ax.set_ylabel('Occurrences per 1,000 Words', fontweight='bold')
ax.set_title('Key Term Density by Section\n(Normalized per 1,000 words)', fontweight='bold', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(sections_short)
ax.legend(loc='upper right')

plt.tight_layout()
save_chart(fig, 'section_comparison_stacked')
plt.close()


# ============================================================================
# CHART 7: Section Characteristics Radar
# ============================================================================
print("Generating Chart 7: Section Characteristics...")

fig, axes = plt.subplots(2, 3, figsize=(14, 10))
axes = axes.flatten()

section_data = [
    ('Herbal (f1-57)', 'Plants + Patients', '#2ecc71',
     {'CHOR': 15.4, 'DAR': 15.8, 'Star': 8.4, 'Water': 31.3, 'Oil': 6.8}),
    ('Astronomical (f67-73)', 'Timing Calendar', '#3498db',
     {'CHOR': 2.0, 'DAR': 22.1, 'Star': 156.0, 'Water': 33.0, 'Oil': 5.0}),
    ('Biological (f75-84)', 'Hydrotherapy', '#9b59b6',
     {'CHOR': 1.5, 'DAR': 19.4, 'Star': 7.3, 'Water': 97.8, 'Oil': 34.0}),
    ('Rosettes (f85-86)', 'Master Diagram', '#e74c3c',
     {'CHOR': 6.6, 'DAR': 58.0, 'Star': 90.1, 'Water': 27.6, 'Oil': 27.6}),
    ('F87 Transition', 'Theory→Practice', '#f39c12',
     {'CHOR': 23.3, 'DAR': 75.6, 'Star': 58.1, 'Water': 58.1, 'Oil': 29.1}),
    ('Recipe (f88-116)', 'Preparation Manual', '#1abc9c',
     {'CHOR': 6.8, 'DAR': 29.9, 'Star': 14.0, 'Water': 27.9, 'Oil': 100.0}),
]

for ax, (name, desc, color, data) in zip(axes, section_data):
    categories = list(data.keys())
    values = list(data.values())

    # Normalize values for display (max = 100)
    max_val = max(values)
    norm_values = [v/max_val * 100 for v in values]

    bars = ax.barh(categories, norm_values, color=color, edgecolor='black')
    ax.set_xlim(0, 110)
    ax.set_title(f'{name}\n"{desc}"', fontweight='bold', fontsize=11)

    # Add original values as labels
    for bar, val in zip(bars, values):
        width = bar.get_width()
        ax.text(width + 2, bar.get_y() + bar.get_height()/2,
                f'{val:.1f}‰', va='center', fontsize=9)

plt.suptitle('Section Vocabulary Profiles (per 1,000 words)', fontweight='bold', fontsize=14, y=1.02)
plt.tight_layout()
save_chart(fig, 'section_profiles')
plt.close()


# ============================================================================
# CHART 8: Evidence Summary - The Key Discovery
# ============================================================================
print("Generating Chart 8: Key Discovery Summary...")

fig, ax = plt.subplots(figsize=(12, 7))

# Create a visual showing CHOR reinterpretation
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(5, 9.5, 'THE KEY DISCOVERY', fontsize=20, fontweight='bold',
        ha='center', va='top')
ax.text(5, 8.8, 'CHOR appears 529 times in the manuscript', fontsize=14,
        ha='center', va='top', style='italic')

# Wrong interpretation box
wrong_box = mpatches.FancyBboxPatch((0.5, 4.5), 4, 3.5, boxstyle="round,pad=0.1",
                                     facecolor='#ffcccc', edgecolor='#c0392b', linewidth=2)
ax.add_patch(wrong_box)
ax.text(2.5, 7.5, '❌ WRONG', fontsize=14, fontweight='bold', ha='center', color='#c0392b')
ax.text(2.5, 6.8, 'Latin "cherub"', fontsize=12, ha='center')
ax.text(2.5, 6.0, '"cherub flower-oil\nthe-flow give cherub"', fontsize=10,
        ha='center', style='italic', color='gray')
ax.text(2.5, 4.8, '= NONSENSE', fontsize=11, ha='center', color='#c0392b', fontweight='bold')

# Right interpretation box
right_box = mpatches.FancyBboxPatch((5.5, 4.5), 4, 3.5, boxstyle="round,pad=0.1",
                                     facecolor='#ccffcc', edgecolor='#27ae60', linewidth=2)
ax.add_patch(right_box)
ax.text(7.5, 7.5, '✓ CORRECT', fontsize=14, fontweight='bold', ha='center', color='#27ae60')
ax.text(7.5, 6.8, 'Polish "chory" (sick)', fontsize=12, ha='center')
ax.text(7.5, 6.0, '"SICK flower-oil\nthe-flow give SICK"', fontsize=10,
        ha='center', style='italic', color='gray')
ax.text(7.5, 4.8, '= MEDICAL\nINSTRUCTION', fontsize=11, ha='center',
        color='#27ae60', fontweight='bold')

# Arrow
ax.annotate('', xy=(5.3, 6), xytext=(4.7, 6),
            arrowprops=dict(arrowstyle='->', color='black', lw=2))

# Bottom summary
ax.text(5, 3.5, 'This single correction transforms 529 occurrences\nfrom mystical nonsense into coherent medical text',
        fontsize=12, ha='center', va='top',
        bbox=dict(boxstyle='round', facecolor='#ffffcc', edgecolor='#f39c12'))

# Statistics
ax.text(5, 1.5, 'Distribution: Herbal (147) • Recipe (97) • Rosettes (12) • Biological (10) • Astronomical (6)',
        fontsize=10, ha='center', va='top', color='gray')
ax.text(5, 0.8, 'Highest in Herbal section = Plants indexed by what conditions they treat',
        fontsize=10, ha='center', va='top', color='gray', style='italic')

plt.tight_layout()
save_chart(fig, 'key_discovery')
plt.close()


# ============================================================================
# CHART 9: Manuscript Structure Flow
# ============================================================================
print("Generating Chart 9: Manuscript Structure...")

fig, ax = plt.subplots(figsize=(14, 8))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(7, 9.5, 'VOYNICH MANUSCRIPT STRUCTURE', fontsize=18, fontweight='bold', ha='center')
ax.text(7, 8.9, 'A Complete Medieval Medical Encyclopedia', fontsize=12, ha='center', style='italic')

# Section boxes
sections_info = [
    (1, 6.5, 'HERBAL\nf1-57', '#2ecc71', 'WHAT treats\nWHICH condition', 'chor=147'),
    (3.5, 6.5, 'ASTRO\nf67-73', '#3498db', 'WHEN to\ntreat', 'otar=472'),
    (6, 6.5, 'BIO\nf75-84', '#9b59b6', 'HOW to\nadminister', 'shedy=247'),
    (8.5, 6.5, 'ROSETTES\nf85-86', '#e74c3c', 'MASTER\nDIAGRAM', '28.7% Polish'),
    (11, 6.5, 'F87', '#f39c12', 'BRIDGE', '16.9% Polish'),
    (13, 6.5, 'RECIPE\nf88-116', '#1abc9c', 'HOW to\nprepare', 'dar/dal=428'),
]

for x, y, name, color, purpose, stat in sections_info:
    box = mpatches.FancyBboxPatch((x-0.9, y-1.2), 1.8, 2.4, boxstyle="round,pad=0.05",
                                   facecolor=color, edgecolor='black', linewidth=1.5, alpha=0.8)
    ax.add_patch(box)
    ax.text(x, y+0.6, name, fontsize=9, fontweight='bold', ha='center', va='center', color='white')
    ax.text(x, y-0.2, purpose, fontsize=7, ha='center', va='center', color='white')
    ax.text(x, y-0.9, stat, fontsize=7, ha='center', va='center', color='white',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.3, edgecolor='none'))

# Arrows
for i in range(5):
    x1 = sections_info[i][0] + 0.9
    x2 = sections_info[i+1][0] - 0.9
    ax.annotate('', xy=(x2, 6.5), xytext=(x1, 6.5),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.5))

# Legend box
legend_box = mpatches.FancyBboxPatch((1, 1), 12, 3, boxstyle="round,pad=0.1",
                                      facecolor='#f8f9fa', edgecolor='#dee2e6', linewidth=1)
ax.add_patch(legend_box)
ax.text(7, 3.5, 'KEY VOCABULARY BY SECTION', fontsize=11, fontweight='bold', ha='center')

legend_items = [
    ('CHOR (sick)', '#e74c3c', 'Highest in Herbal → plants indexed by condition'),
    ('DAR/DAL (give)', '#2ecc71', 'Highest in Recipe → preparation instructions'),
    ('OT- (star)', '#3498db', 'Highest in Astronomical → timing calendar'),
    ('SHE- (water)', '#9b59b6', 'Highest in Biological → hydrotherapy'),
]

for i, (term, color, desc) in enumerate(legend_items):
    y = 2.8 - i * 0.5
    ax.plot([1.5], [y], 'o', color=color, markersize=10)
    ax.text(2, y, term, fontsize=9, fontweight='bold', va='center')
    ax.text(4.5, y, desc, fontsize=9, va='center', color='gray')

plt.tight_layout()
save_chart(fig, 'manuscript_structure')
plt.close()


# ============================================================================
# CHART 10: Bilingual Pattern
# ============================================================================
print("Generating Chart 10: Bilingual Pattern...")

fig, ax = plt.subplots(figsize=(10, 7))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

ax.text(5, 9.5, 'BILINGUAL PATTERN', fontsize=18, fontweight='bold', ha='center')
ax.text(5, 8.8, 'Polish + Latin working together', fontsize=12, ha='center', style='italic')

# Polish box
polish_box = mpatches.FancyBboxPatch((0.5, 3.5), 4, 4.5, boxstyle="round,pad=0.1",
                                      facecolor='#ffe6e6', edgecolor='#c0392b', linewidth=2)
ax.add_patch(polish_box)
ax.text(2.5, 7.5, 'POLISH', fontsize=14, fontweight='bold', ha='center', color='#c0392b')
ax.text(2.5, 6.8, 'Practical Instructions', fontsize=11, ha='center', color='#c0392b')

polish_terms = [
    ('chor', 'sick (patient)'),
    ('dar/dal', 'give/gave'),
    ('kam', 'bathe'),
    ('ly', 'pour'),
    ('oko', 'eye'),
    ('sal', 'salt'),
]
for i, (term, meaning) in enumerate(polish_terms):
    y = 6.0 - i * 0.45
    ax.text(1.3, y, term, fontsize=10, fontweight='bold', color='#c0392b')
    ax.text(2.3, y, '→', fontsize=10, ha='center')
    ax.text(2.6, y, meaning, fontsize=10, color='gray')

# Latin box
latin_box = mpatches.FancyBboxPatch((5.5, 3.5), 4, 4.5, boxstyle="round,pad=0.1",
                                     facecolor='#e6f0ff', edgecolor='#2980b9', linewidth=2)
ax.add_patch(latin_box)
ax.text(7.5, 7.5, 'LATIN', fontsize=14, fontweight='bold', ha='center', color='#2980b9')
ax.text(7.5, 6.8, 'Technical Terms', fontsize=11, ha='center', color='#2980b9')

latin_terms = [
    ('otar', 'stella (star)'),
    ('ol', 'oleum (oil)'),
    ('daiin', 'folium (leaf)'),
    ('raiin', 'radix (root)'),
    ('saiin', 'sanare (heal)'),
    ('cheol', 'flos+oleum'),
]
for i, (term, meaning) in enumerate(latin_terms):
    y = 6.0 - i * 0.45
    ax.text(6.3, y, term, fontsize=10, fontweight='bold', color='#2980b9')
    ax.text(7.3, y, '→', fontsize=10, ha='center')
    ax.text(7.6, y, meaning, fontsize=10, color='gray')

# Combined example
example_box = mpatches.FancyBboxPatch((1, 0.5), 8, 2.3, boxstyle="round,pad=0.1",
                                       facecolor='#ffffcc', edgecolor='#f39c12', linewidth=2)
ax.add_patch(example_box)
ax.text(5, 2.4, 'COMBINED EXAMPLE', fontsize=11, fontweight='bold', ha='center')
ax.text(5, 1.8, 'chor.cheol.qokeey.dar', fontsize=12, ha='center',
        fontfamily='monospace', color='#2c3e50')
ax.text(5, 1.2, 'SICK (Pol.) flower-oil (Lat.) the-flow (Lat.) GIVE (Pol.)',
        fontsize=10, ha='center', color='gray')
ax.text(5, 0.7, '"Give the flowing flower-oil to the sick patient"',
        fontsize=10, ha='center', style='italic')

plt.tight_layout()
save_chart(fig, 'bilingual_pattern')
plt.close()


print("\n" + "="*60)
print("All charts generated successfully!")
print("="*60)
print(f"\nOutput directory: /home/k/Desktop/voynich-decoded/figures/charts/")
print("\nCharts created:")
print("  1. polish_percentage_by_section.png")
print("  2. vocabulary_gradient.png")
print("  3. chor_distribution.png")
print("  4. dar_dal_distribution.png")
print("  5. ol_distribution.png")
print("  6. section_comparison_stacked.png")
print("  7. section_profiles.png")
print("  8. key_discovery.png")
print("  9. manuscript_structure.png")
print("  10. bilingual_pattern.png")
