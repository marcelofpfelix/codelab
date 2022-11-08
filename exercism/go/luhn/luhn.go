package luhn

import (
	"strings"
	"unicode"
)

// Luhn algorithm checksum formula used to validate a variety of identification
// numbers, such as credit cards
func Valid(id string) bool {
	total := 0
	index := 1

	id = strings.ReplaceAll(id, " ", "")

	parity := len(id) % 2

	for _, value := range id {
		if unicode.IsNumber(value) {
			if index%2 == parity {
				total += int(value - '0')
			} else if int(value-'0') > 4 {
				total += 2*int(value-'0') - 9
			} else {
				total += 2 * int(value-'0')
			}
		} else {
			return false
		}
		index++
	}
	return total%10 == 0 && index > 2
}
