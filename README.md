# DNA Sequence Analyzer

A Python tool that validates a DNA sequence and computes GC content, RNA transcription and reverse complement.

## Features

- **Validation:** accepts only A, T, C, G (case-insensitive; spaces and new lines are ignored)
- **GC content:** percentage of G and C bases in the sequence
- **Transcription:** converts DNA to RNA by replacing T with U
- **Reverse complement:** generates the opposite strand, read 5' to 3'

## Requirements

- Python 3.8 or higher (no external libraries needed)

## How to Run

```
git clone https://github.com/Arushi-Alisha?dna-sequence-analyzer.git
cd dna-sequence-analyzer
python main.py
```

## Sample Output

```
=== DNA Sequence Analyzer ===
Enter a DNA sequence: agcttaagcc

Sequence:           AGCTTAAGCC
Length:             10 bases
GC content:         50.0%
RNA transcript:     AGCUUAAGCC
Reverse complement: GGCTTAAGCT
```

Invalid input is rejected:

```
Enter a DNA sequence: ATGX
Invalid sequence. Use only A, T, C, G.
```

## Project Structure

```
dna-sequence-analyzer/
├── analyzer.py   # core functions (validation, GC content, transcription, reverse complement)
├── main.py       # command-line interface
└── README.md
```

## How it Works

- DNA strands are antiparallel, so the opposite strand is the *reverse* complement, not just the complement.
- Transcription is shown in its simplified form: the RNA matches the coding strand with T replaced by U.

## Future Improvements

- Nucleotide counts with a bar chart
- Codon translation to amino acids
- Motif search
- FASTA file input
- Unit tests with pytest

## Author

Arushi
