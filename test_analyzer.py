from analyzer import validate_sequence, gc_content, transcribe, reverse_complement, nucleotide_counts

def test_validate_cleans_input():
    assert validate_sequence("atgc gatc") == "ATGCGATC"

def test_validate_rejects_invalid_letters():
    assert validate_sequence("ATGX") is None

def test_validate_rejects_empty():
    assert validate_sequence("") is None

def test_gc_content_half():
    assert gc_content("ATGC") == 50.0

def test_gc_content_all_gc():
    assert gc_content("GGGG") == 100.0

def test_gc_content_no_gc():
    assert gc_content("ATAT") == 0.0

def test_gc_content_empty():
    assert gc_content("") == 0.0

def test_transcribe():
    assert transcribe("ATGC") == "AUGC"

def test_reverse_complement():
    assert reverse_complement("ATGC") == "GCAT"

def test_reverse_complement_longer():
    assert reverse_complement("AGCTTAAGCC") == "GGCTTAAGCT"

def test_reverse_complement_palindrome():
    # GAATTC is a real enzyme cut site and equals its own reverse complement
    assert reverse_complement("GAATTC") == "GAATTC"

def test_nucleotide_counts():
    assert nucleotide_counts("AGCTTAAGCC") == {"A": 3, "T": 2, "C": 3, "G": 2}

def test_nucleotide_counts_missing_bases():
    assert nucleotide_counts("AAAA") == {"A": 4, "T": 0, "C": 0, "G": 0}