# DNA Sequence Analyzer

A Python tool that validates a DNA sequence and computes GC content, RNA transcription and reverse complement.

## Features

- **Validation:** accepts only A, T, C, G (case-insensitive; spaces and new lines are ignored)
- **Nucleotide counts:** counts number of A, T, C, and G bases
- **GC content:** percentage of G and C bases in the sequence
- **Transcription:** converts DNA to RNA by replacing T with U
- **Reverse complement:** generates the opposite strand, read 5' to 3'
- **Codon translation:** translates DNA into protein

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
Base counts:        A=3 T=2 C=3 G=2
GC content:         50.0%
RNA transcript:     AGCUUAAGCC
Reverse complement: GGCTTAAGCT
Protein (frame 1):  SLS
```
Protein letters are standard one-letter amino acid codes ( e.g. M = Methionine, * = Stop codon ).

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

## Running Tests

```
python -m pip install pytest
python -m pytest
```

## How it Works

- DNA strands are antiparallel, so the opposite strand is the *reverse* complement, not just the complement.
- Transcription is shown in its simplified form: the RNA matches the coding strand with T replaced by U.

## Future Improvements

- A bar chart of nucleotide counts
- Motif search
- FASTA file input

## Author

Arushi
