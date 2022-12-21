"""
Protein Translation
"""

PROTAIN_MAP = {
  "Methionine": ["AUG"],
  "Phenylalanine": ["UUU", "UUC"],
  "Leucine": ["UUA", "UUG"],
  "Serine": ["UCU", "UCC", "UCA", "UCG"],
  "Tyrosine": ["UAU", "UAC"],
  "Cysteine": ["UGU", "UGC"],
  "Tryptophan": ["UGG"],
  "STOP": ["UAA", "UAG", "UGA"]
}


def proteins(strand):
    """
    Translate RNA sequences into proteins.
    """
    result = []
    # used to split the condons
    number = 3
    codons = [strand[i:i+number] for i in range(0, len(strand), number)]

    for codon in codons:
        if codon in PROTAIN_MAP['STOP']:
            break
        for protein, values in PROTAIN_MAP.items():
            if codon in values:
                result.append(protein)

    return result
