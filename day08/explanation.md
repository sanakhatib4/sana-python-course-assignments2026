## Dataset Description (Day 08)

This folder contains datasets and analysis files derived from **Protein Binding Microarray (PBM)** experiments performed on different truncation variants of the transcription factor **MSN2**.

### Included datasets

For each MSN2 variant, the folder contains the **top enrichment results from three technical repeats**:

- **FL** – full-length MSN2  
- **IDR** – MSN2 variant lacking the DNA-binding domain  
- **DBD** – isolated DNA-binding domain  

Each repeat corresponds to an independent PBM measurement and includes enrichment values for DNA probes.

The files are used as input for downstream analysis using **NumPy** and **Pandas**.

---

### Analysis performed

Using the datasets, the following analyses were implemented:

- Loading and organizing replicate datasets with **pandas**
- Comparing technical repeats for each MSN2 variant
- Computing **pairwise correlations** between repeats
- Visualizing correlations to assess reproducibility
- Basic statistical inspection of enrichment distributions

These analyses help evaluate:
- consistency between technical replicates  
- differences between full-length, DBD-only, and non-DBD variants  
- robustness of DNA-binding signal across experiments  

---

### Notes

- Each dataset corresponds to a technical replicate from a PBM experiment.
- File naming reflects the MSN2 variant and repeat number.
- Correlation analysis focuses on reproducibility rather than biological interpretation.

