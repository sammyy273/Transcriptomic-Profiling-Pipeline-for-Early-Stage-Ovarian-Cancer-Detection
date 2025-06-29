import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv("../de/deseq2_clean.csv")

lfc_thresh = 1
padj_thresh = 0.05

df["significance"] = "Not Significant"
df.loc[(df["padj"] < padj_thresh) & (df["log2FoldChange"] > lfc_thresh), "significance"] = "Upregulated"
df.loc[(df["padj"] < padj_thresh) & (df["log2FoldChange"] < -lfc_thresh), "significance"] = "Downregulated"

# Plot
plt.figure(figsize=(10, 7))
sns.scatterplot(
    data=df,
    x="log2FoldChange",
    y=-np.log10(df["padj"]),
    hue="significance",
    palette={"Upregulated": "red", "Downregulated": "blue", "Not Significant": "grey"},
    alpha=0.7,
    edgecolor=None
)

plt.title("Volcano Plot: Tumor vs Control")
plt.xlabel("Log2 Fold Change")
plt.ylabel("-log10 Adjusted P-Value")
plt.axvline(x=1, color="black", linestyle="--")
plt.axvline(x=-1, color="black", linestyle="--")
plt.axhline(y=-np.log10(padj_thresh), color="black", linestyle="--")
plt.tight_layout()
plt.savefig("de/volcano_plot.png", dpi=300)
print("Volcano plot saved at: de/volcano_plot.png")
