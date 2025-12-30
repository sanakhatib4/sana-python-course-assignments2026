from pathlib import Path

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from scipy import stats


def sort_key(name: str) -> tuple[int, int, str]:
    name_upper = name.upper()
    repeat_order = 1 if "R1" in name_upper else 2 if "R2" in name_upper else 3 if "R3" in name_upper else 4
    type_order = 0 if "FL" in name_upper else 1
    return repeat_order, type_order, name_upper


def load_datasets(data_dir: Path, e_threshold: float = 0.35) -> dict[str, pd.DataFrame]:
    datasets: dict[str, pd.DataFrame] = {}
    for path in sorted(data_dir.glob("*.txt")):
        if "_GDN" in path.stem:
            continue
        df = pd.read_csv(path, sep="\t", usecols=["8-mer", "E-score", "Z-score"])
        df = df[df["E-score"] >= e_threshold]
        datasets[path.stem] = df
    return datasets


def regression_r2(x: pd.Series, y: pd.Series) -> float:
    # Use linear regression on aligned values; return R^2 or NaN if not enough points.
    if len(x) < 2:
        return np.nan
    _, _, r_value, _, _ = stats.linregress(x, y)
    return r_value**2


def compute_r2_matrix(datasets: dict[str, pd.DataFrame], column: str) -> pd.DataFrame:
    names = sorted(datasets.keys(), key=sort_key)
    r2_matrix = pd.DataFrame(np.nan, index=names, columns=names)

    for i, name_i in enumerate(names):
        for j, name_j in enumerate(names):
            if j < i:
                continue
            merged = datasets[name_i].merge(datasets[name_j], on="8-mer", suffixes=("_i", "_j"))
            r2 = regression_r2(merged[f"{column}_i"], merged[f"{column}_j"])
            r2_matrix.at[name_i, name_j] = r2
            r2_matrix.at[name_j, name_i] = r2
    return r2_matrix


def plot_heatmap(matrix: pd.DataFrame, title: str, ax: plt.Axes) -> None:
    sns.heatmap(
        matrix,
        annot=True,
        fmt=".2f",
        cmap="YlGnBu",
        vmin=0,
        vmax=1,
        linewidths=0.5,
        linecolor="white",
        cbar=True,
        cbar_kws={"shrink": 0.8},
        ax=ax,
    )
    ax.set_title(title)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
    ax.set_yticklabels(ax.get_yticklabels(), rotation=0)


def top_pairs(matrix: pd.DataFrame, label: str, n: int = 10) -> None:
    mask = ~np.eye(len(matrix), dtype=bool)
    values = matrix.to_numpy()[mask]
    idx = pd.MultiIndex.from_tuples(
        [
            (matrix.index[i], matrix.columns[j])
            for i in range(len(matrix))
            for j in range(len(matrix))
            if mask[i, j]
        ]
    )
    stacked = pd.Series(values, index=idx).dropna().sort_values(ascending=False)
    print(f"Top {n} {label} R² pairs:")
    for (i, j), value in stacked.head(n).items():
        print(f"  {i} vs {j}: {value:.3f}")


def main() -> None:
    data_dir = Path.cwd()
    datasets = load_datasets(data_dir)

    e_r2 = compute_r2_matrix(datasets, "E-score")
    z_r2 = compute_r2_matrix(datasets, "Z-score")

    fig, axes = plt.subplots(1, 2, figsize=(16, 7))
    plot_heatmap(e_r2, "Linear Regression R² (E-score)", ax=axes[0])
    plot_heatmap(z_r2, "Linear Regression R² (Z-score)", ax=axes[1])
    plt.tight_layout()
    plt.savefig("correlation_linear_regression_all.png", dpi=300, bbox_inches="tight")
    plt.close(fig)

    e_r2.to_csv("e_score_rsquared_all.csv")
    z_r2.to_csv("z_score_rsquared_all.csv")

    top_pairs(e_r2, "E-score")
    top_pairs(z_r2, "Z-score")


if __name__ == "__main__":
    main()
