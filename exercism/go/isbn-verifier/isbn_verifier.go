package isbn

import (
	"unicode"
)

func IsValidISBN(isbn string) bool {
	total := 0
	multi := 10

	for _, value := range isbn {
		if unicode.IsNumber(value) {
			// get rune value out of the ASCII
			total += int(value-'0') * multi
			multi--
		} else if value == '-' {
			continue
		} else if value == 'X' && multi == 1 {
			total += +10 * multi
			multi--
		} else {
			return false
		}
	}

	return total%11 == 0 && multi == 0
}
