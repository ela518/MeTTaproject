from metta_handler import load_metta_space, get_gene_synonyms, inject_summary
from llm_calls import summarize_biological_data
from utils import write_summary_file

OUTPUT_FILE = "output/summary_output.txt"
space = load_metta_space("/home/ela/metta/file.metta")


print("DEBUG: loaded atoms matching LLM request:")
print(space.run("(request-llm-summary $x)"))
bindings = space.run("""
    !(match &self
        (request-llm-summary (gene $id))
        $id)
""")

print("DEBUG: MeTTa variable bindings:")
print(bindings)

if not bindings or not bindings[0]:
    print("No LLM summary requests found.")
    exit()

gene_id = str(bindings[0][0])
print(f"Found gene ID from MeTTa request: {gene_id}")


synonyms = get_gene_synonyms(space, gene_id)

if synonyms:
    input_text = f"Summarize the biological significance of these gene synonyms: {', '.join(str(s) for s in synonyms)}"
    summary = summarize_biological_data(input_text)
    inject_summary(space, gene_id, summary)
    write_summary_file(gene_id, synonyms, summary, OUTPUT_FILE)
    print(f"Summary for {gene_id} saved to {OUTPUT_FILE}")
else:
    print(f"No synonyms found for gene {gene_id}")
