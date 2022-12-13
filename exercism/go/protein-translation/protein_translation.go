package protein

import "errors"

var protainMap = map[string]string{
	"AUG": "Methionine",
	"UUU": "Phenylalanine",
	"UUC": "Phenylalanine",
	"UUA": "Leucine", "UUG": "Leucine",
	"UCU": "Serine", "UCC": "Serine", "UCA": "Serine", "UCG": "Serine",
	"UAU": "Tyrosine", "UAC": "Tyrosine",
	"UGU": "Cysteine", "UGC": "Cysteine",
	"UGG": "Tryptophan",
	"UAA": "STOP", "UAG": "STOP", "UGA": "STOP",
}
var ErrInvalidBase = errors.New("ErrInvalidBase")
var ErrStop = errors.New("ErrStop")

func FromRNA(rna string) ([]string, error) {
	var result []string

	for n := 0; n <= len(rna)-3; n += 3 {
		protain, ok := FromCodon(rna[n : n+3])

		if ok == ErrInvalidBase {
			return result, ErrInvalidBase
		} else if ok == ErrStop {
			return result, nil
		}
		result = append(result, protain)
	}
	return result, nil
}

func FromCodon(codon string) (string, error) {
	protain, ok := protainMap[codon]
	if !ok {
		return "", ErrInvalidBase
	} else if protain == "STOP" {
		return "", ErrStop
	} else {
		return protain, nil
	}
}
