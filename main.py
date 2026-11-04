from analyzer import validate_sequence, gc_content, transcribe, reverse_complement, nucleotide_counts, translate, read_fasta


def main():
    print("=== DNA Sequence Analyzer ===")
    raw = input("Enter a DNA sequence or a FASTA file name: ").strip()

    if raw.lower().endswith((".fasta", ".fa")):
        filename = raw
        try:
            header, raw = read_fasta(filename)
        except FileNotFoundError:
            print(f"File not found: {filename}")
            return
        print(f"Loaded FASTA record: {header}")

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