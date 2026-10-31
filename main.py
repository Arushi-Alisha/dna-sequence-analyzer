from analyzer import validate_sequence, gc_content, transcribe, reverse_complement


def main():
    print("=== DNA Sequence Analyzer ===")
    raw = input("Enter a DNA sequence: ")

    seq = validate_sequence(raw)
    if seq is None:
        print("Invalid sequence. Use only A, T, C, G.")
        return

    print(f"\nSequence:           {seq}")
    print(f"Length:             {len(seq)} bases")
    print(f"GC content:         {gc_content(seq)}%")
    print(f"RNA transcript:     {transcribe(seq)}")
    print(f"Reverse complement: {reverse_complement(seq)}")


if __name__ == "__main__":
    main()