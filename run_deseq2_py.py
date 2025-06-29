import pandas as pd
import numpy as np
from pydeseq2.dds import DeseqDataSet
from pydeseq2.ds import DeseqStats
import os

samples = ["SRR5815895", "SRR5815896", "SRR5815899", "SRR5815900"]
groups = ["Control", "Control", "Tumor", "Tumor"]

counts = {}
for sample in samples:
    file_path = f"../quant/{sample}/quant.sf"
    df = pd.read_csv(file_path, sep="\t")
    counts[sample] = df.set_index("Name")["NumReads"].round().astype(int)

count_matrix = pd.DataFrame(counts).T

metadata = pd.DataFrame({
    "condition": groups
}, index=samples)

dds = DeseqDataSet(
    counts=count_matrix,
    metadata=metadata,
    design_factors="condition"
)

dds.deseq2()

stat_res = DeseqStats(dds, contrast=["condition", "Tumor", "Control"])
stat_res.summary()

results_df = stat_res.results_df
results_df["-log10(padj)"] = -results_df["padj"].apply(lambda x: np.nan if pd.isna(x) else np.log10(x) * -1)

os.makedirs("de", exist_ok=True)
results_df.to_csv("de/deseq2_results.csv", index=False)

print("DE results saved to de/deseq2_results.csv")

