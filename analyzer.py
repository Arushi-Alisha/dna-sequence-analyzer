def validate_sequence(seq):
    """Return the cleaned sequence if valid, otherwise None."""
    seq = seq.upper().replace(" ", "").replace("\n", "")
    if not seq:
        return None
    if set(seq) <= set("ATCG"):
        return seq
    return None

def gc_content(seq):
    """Return GC percentage of a valid sequence."""
    if not seq:
        return 0.0
    gc = seq.count("G") + seq.count("C")
    return round(gc / len(seq) * 100, 2)

def transcribe(seq):
    """Convert DNA to RNA by replacing T with U."""
    return seq.replace("T", "U")

def reverse_complement(seq):
    """Return the reverse complement of a DNA sequence."""
    complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join(complement[base] for base in reversed(seq))

def nucleotide_counts(seq):
    """Return a dictionary with the count of each base."""
    return {base: seq.count(base) for base in "ATCG"}

# One - letter amino acid codes (standard IUPAC). * = stop codon.
CODON_TABLE = {
    "TTT": "F", "TTC": "F", "TTA": "L", "TTG": "L",
    "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "ATT": "I", "ATC": "I", "ATA": "I", "ATG": "M",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "TAT": "Y", "TAC": "Y", "TAA": "*", "TAG": "*",
    "CAT": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "AAT": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "GAT": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "TGT": "C", "TGC": "C", "TGA": "*", "TGG": "W",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "AGT": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",
}

def translate(seq):
    """Translate DNA into a protein string, reading from the first base."""
    protein = ""
    for i in range(0, len(seq) - 2, 3):
        codon = seq[i:i + 3]
        protein += CODON_TABLE[codon]
    return protein


def parse_fasta(text):
    """Parse FASTA text and return (header, sequence) for the first record."""
    header = ""
    parts = []
    found_header = False
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith(">"):
            if found_header:
                break
            found_header = True
            header = line[1:].strip()
        else:
            parts.append(line)
    return header, "".join(parts)

def read_fasta(filename):
    """Read a FASTA file and return (header, sequence)."""
    with open(filename) as f:
        return parse_fasta(f.read())


if __name__ == "__main__":
    print(validate_sequence("atgc gatc"))
    print(validate_sequence("ATGX"))
    print(gc_content("ATGC"))
    print(transcribe("ATGC"))
    print(reverse_complement("ATGC"))