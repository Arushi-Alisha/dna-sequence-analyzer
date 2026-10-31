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


if __name__ == "__main__":
    print(validate_sequence("atgc gatc"))
    print(validate_sequence("ATGX"))
    print(gc_content("ATGC"))