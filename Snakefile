configfile: "config.yaml"

print(config)

rule all:
    input:
        expand("qc/{sample}_1_fastqc.html", sample=config["samples"]),
        expand("qc/{sample}_2_fastqc.html", sample=config["samples"]),
        expand("trimmed/{sample}_R1_trimmed.fastq.gz", sample=config["samples"]),
        expand("trimmed/{sample}_R2_trimmed.fastq.gz", sample=config["samples"]),
        "reference/salmon_index",
        expand("quant/{sample}/quant.sf", sample=config["samples"])

rule fastqc:
    input:
        r1="data/raw/{sample}_1.fastq.gz",
        r2="data/raw/{sample}_2.fastq.gz"
    output:
        r1_html="qc/{sample}_1_fastqc.html",
        r2_html="qc/{sample}_2_fastqc.html",
        r1_zip="qc/{sample}_1_fastqc.zip",
        r2_zip="qc/{sample}_2_fastqc.zip"
    log:
        "logs/fastqc/{sample}.log"
    conda:
        "envs/fastqc.yaml"
    shell:
        "fastqc {input.r1} {input.r2} -o qc > {log} 2>&1"

rule trimmomatic:
    input:
        r1="data/raw/{sample}_1.fastq.gz",
        r2="data/raw/{sample}_2.fastq.gz"
    output:
        r1_trim="trimmed/{sample}_R1_trimmed.fastq.gz",
        r2_trim="trimmed/{sample}_R2_trimmed.fastq.gz"
    params:
        adapters="/path/to/adapters.fa"  
    log:
        "logs/trimmomatic/{sample}.log"
    conda:
        "envs/trimmomatic.yaml"
    shell:
        "trimmomatic PE {input.r1} {input.r2} "
        "{output.r1_trim} /dev/null {output.r2_trim} /dev/null "
        "SLIDINGWINDOW:4:20 MINLEN:36 > {log} 2>&1"

rule salmon_index:
    input:
        fa="reference/Homo_sapiens.GRCh38.cdna.all.fa"
    output:
        directory("reference/salmon_index")
    conda:
        "envs/salmon.yaml"
    shell:
        "salmon index -t {input.fa} -i {output}"

rule salmon_quant:
    input:
        r1="trimmed/{sample}_R1_trimmed.fastq.gz",
        r2="trimmed/{sample}_R2_trimmed.fastq.gz",
        index="reference/salmon_index"
    output:
        quant="quant/{sample}/quant.sf"
    params:
        libtype="A" 
    conda:
        "envs/salmon.yaml"
    shell:
        "salmon quant -i {input.index} -l {params.libtype} "
        "-1 {input.r1} -2 {input.r2} -p 4 "
        "-o quant/{wildcards.sample}"


