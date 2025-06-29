# Transcriptomic Profiling for Early-Stage Ovarian Cancer Biomarker Discovery

# Project Overview

This project aims to identify novel biomarkers for early-stage ovarian cancer using RNA-Seq data. It uses a Snakemake workflow to automate and reproduce quality control, trimming, quantification, and differential expression analysis.

# Technologies Used

- Snakemake – Workflow management
- FastQC – Quality control
- Trimmomatic – Adapter trimming
- Salmon – Transcript-level quantification
- PyDESeq2 – Differential gene expression analysis
- mygene – Annotation of transcript IDs
- Seaborn/Matplotlib – Data visualization
- HPC environment (DGX Cluster) – Analysis infrastructure

# Data & Setup

Input Data
- 8 RNA-seq samples (SRA: SRR5815895–SRR5815900) from early-stage ovarian carcinoma.
- Reference transcriptome: `Homo_sapiens.GRCh38.cdna.all.fa` (used with Salmon).

# Directory Structure

CGPROJECT/
├── data/raw/ # Raw FASTQ files
├── trimmed/ # Trimmed FASTQs
├── qc/ # FastQC reports
├── reference/ # Transcriptome and Salmon index
├── quant/ # Salmon quantification outputs
├── de/ # DESeq2 results and plots
├── scripts/ # All Python/R scripts
├── envs/ # Conda YAMLs for reproducibility
├── Snakefile # Snakemake workflow
├── config.yaml # Sample configuration
