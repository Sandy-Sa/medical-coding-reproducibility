import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Plot showing the distribution of ICD-9 and ICD-10 codes in MIMIC-IV


mimiciii_diagnoses = pd.read_csv(
    "/Users/full_of_bugs/data/mimic-data/mimic-iii-clinical-database-1.4/DIAGNOSES_ICD.csv.gz",
    compression="gzip",
)

sns.set_theme("paper", style="whitegrid", palette="colorblind", font_scale=1.5)

icd9_counts = mimiciii_diagnoses.ICD9_CODE.value_counts()

fig = plt.figure(figsize=(10, 5))
ax = sns.lineplot(
    x=np.linspace(0, len(icd9_counts) - 1, len(icd9_counts)),
    y=icd9_counts.values,
    label="ICD-9",
    linewidth=1.5,
)
ax.set(
    yscale="log",
    xlabel="Code index",
    ylabel="Frequency of code in MIMIC-III",
)
ax.hlines(10, 0, 16200, linestyles="dashed", label="100", color="gray")
plt.xlim(-50, 16200)
fig.savefig(
    "files/images/mimiciii_code_freq.png",
    dpi=600,
    bbox_inches="tight",
)
