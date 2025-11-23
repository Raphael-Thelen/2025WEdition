#!/usr/bin/env python3
import csv
import sys
from collections import defaultdict
import matplotlib.pyplot as plt

def read_csv(path):
    # Liest alle Zeilen ein und gruppiert nach variant
    data = defaultdict(list)
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            variant = row['variant']
            data[variant].append({
                'samples':   int(row['samples']),
                'mean':      float(row['mean_ns']),
                'min':       int(row['min_ns']),
                'max':       int(row['max_ns']),
                'stddev':    float(row['stddev_ns']),
                'ci95':      float(row['ci95_ns']),
            })
    return data

def plot_means(data, out_png):
    # Für jede variant den Mittelwert-Mittelwert und CI mitteln
    variants = []
    means = []
    errors = []
    for var, rows in data.items():
        variants.append(var)
        # Durchschnitt über alle runs, könnte aber auch letzter Eintrag reichen
        avg_mean = sum(r['mean'] for r in rows) / len(rows)
        avg_ci   = sum(r['ci95'] for r in rows) / len(rows)
        means.append(avg_mean)
        errors.append(avg_ci)

    plt.figure(figsize=(6,4))
    plt.bar(variants, means, yerr=errors, capsize=5, color=['C0','C1'])
    plt.ylabel('Mean latency [ns]')
    plt.title('Spinlock Latency Comparison')
    plt.tight_layout()
    plt.savefig(out_png)
    print(f"Saved mean plot to {out_png}")

def plot_histograms(data, out_png):
    plt.figure(figsize=(8,4))
    for i, (var, rows) in enumerate(data.items()):
        # sammle alle sample-Werte für Histogramm; hier verwenden wir Min..Max?
        # besser: simulieren wir per-run einzelne Messwerte nicht vorhanden => nutzen wir mean
        values = [r['mean'] for r in rows]
        plt.subplot(1, len(data), i+1)
        plt.hist(values, bins=30, color=f'C{i}', alpha=0.7)
        plt.title(var)
        plt.xlabel('Latency [ns]')
        plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig(out_png)
    print(f"Saved histogram to {out_png}")

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} results.csv")
        sys.exit(1)
    path = sys.argv[1]
    data = read_csv(path)
    plot_means(data, 'aw_means.png')
    plot_histograms(data, 'aw_hist.png')

if __name__ == '__main__':
    main()