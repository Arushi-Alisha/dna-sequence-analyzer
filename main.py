from analyzer import validate_sequence, gc_content, transcribe, reverse_complement, nucleotide_counts, translate


def main():
    print("=== DNA Sequence Analyzer ===")
    raw = input("Enter a DNA sequence: ")

    seq = validate_sequence(raw)
    if seq is None:
        print("Invalid sequence. Use only A, T, C, G.")
        return

    print(f"\nSequence:           {seq}")
    print(f"Length:             {len(seq)} bases")

    counts = nucleotide_counts(seq)
    print(f"Base counts:        A={counts['A']} T={counts['T']} C={counts['C']} G={counts['G']}")
    print(f"GC content:         {gc_content(seq)}%")
    print(f"RNA transcript:     {transcribe(seq)}")
    print(f"Reverse complement: {reverse_complement(seq)}")
    print(f"Protein (frame 1):  {translate(seq)}")


if __name__ == "__main__":
    main()