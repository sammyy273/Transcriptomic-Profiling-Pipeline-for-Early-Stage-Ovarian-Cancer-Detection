import pandas as pd

# Load the cleaned DESeq2 result
df = pd.read_csv("../de/deseq2_clean.csv")

# Filter for significant genes (padj < 0.05)
sig_df = df[df["padj"] < 0.05]

# Sort by absolute log2FoldChange
sig_df["abs_log2FC"] = sig_df["log2FoldChange"].abs()
top20 = sig_df.sort_values("abs_log2FC", ascending=False).head(20)

# Drop helper column
top20.drop(columns=["abs_log2FC"], inplace=True)

# Save to CSV
top20.to_csv("de/top20_deseq2_genes.csv", index=False)

print("Top 20 DEGs saved to de/top20_deseq2_genes.csv")
