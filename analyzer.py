def validate_sequence(seq):
    """Return the cleaned sequence if valid, otherwise None."""
    seq = seq.upper().replace(" ", "").replace("\n", "")
    if not seq:
        return None
    if set(seq) <= set("ATCG"):
        return seq
    return None


if __name__ == "__main__":
    print(validate_sequence("atgc gatc"))
    print(validate_sequence("ATGX"))