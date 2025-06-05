from hyperon import MeTTa

def load_metta_space(filepath: str) -> MeTTa:
    space = MeTTa()
    space._loaded_atoms = []

    with open(filepath, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if not line or line.startswith(";"):
                continue
            print(f"LOADING: {line}")
            result = space.run(line)
            space._loaded_atoms.append(line)

    print("DEBUG: _loaded_atoms =", space._loaded_atoms)
    return space


def get_gene_synonyms(space, gene_id):
    print(f"DEBUG: scanning _loaded_atoms for synonyms of gene {gene_id}")
    for raw in space._loaded_atoms:
        if raw.startswith(f"(synonyms (gene {gene_id})"):
            print("DEBUG: matched raw synonym line:", raw)
            parts = raw.strip("()").split()[3:]
            return parts
    print("DEBUG: no synonym line matched")
    return []

    for atom in atoms:
        if str(atom).startswith(f"(synonyms (gene {gene_id})"):
            print("DEBUG: matched synonym atom:", atom)
            return atom.get_children()[2:]  
    
    print("DEBUG: no synonym atom matched")
    return []


def inject_summary(space: MeTTa, gene_id: str, summary: str):
    space.run(f'(summary (gene {gene_id}) "{summary}")')
