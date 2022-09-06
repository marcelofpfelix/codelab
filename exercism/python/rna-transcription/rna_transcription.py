"""
RNA
"""


def to_rna(dna_strand):
    """
    Given a DNA strand, return its RNA complement (per RNA transcription).

        arg dna_strand: (string) the DNA strand
        return: (string) the RNA complement
    """

    return dna_strand.translate(str.maketrans("GCTA", "CGAU"))

    # alternative:
    # rna = ''.join(map(lambda char:
    # {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}.get(char, ''), text))
