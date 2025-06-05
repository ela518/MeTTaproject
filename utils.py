def write_summary_file(gene_id: str, synonyms: list, summary: str, output_path: str):
    with open(output_path, "w") as f:
        f.write(f"Gene: {gene_id}\n")
        f.write(f"Synonyms: {', '.join(str(s) for s in synonyms)}\n\n")
        f.write(f"Summary: {summary}\n")
