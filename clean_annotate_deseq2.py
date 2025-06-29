import os
import pandas as pd

# Load the CSV
df = pd.read_csv("de/deseq2_results.csv")

print(f"Original rows: {df.shape[0]}")

if "#NAME?" in df.columns:
    df = df.drop(columns=["#NAME?"])

# Clean: baseMean > 0 and padj not null
df_clean = df[(df["baseMean"] > 0) & (df["padj"].notna())]

print(f"Cleaned rows: {df_clean.shape[0]}")

# Make sure the output directory exists
output_dir = "../de"
os.makedirs(output_dir, exist_ok=True)

# Save cleaned file
output_path = os.path.join(output_dir, "deseq2_clean.csv")
df_clean.to_csv(output_path, index=False)

print(f"Cleaned file saved at: {output_path}")


