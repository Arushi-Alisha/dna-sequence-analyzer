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


if __name__ == "__main__":
    print(validate_sequence("atgc gatc"))
    print(validate_sequence("ATGX"))
    print(gc_content("ATGC"))
    print(transcribe("ATGC"))
    print(reverse_complement("ATGC"))