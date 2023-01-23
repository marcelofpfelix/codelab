package atbash

import (
	"bytes"
	"strings"
	"unicode"
)

func Atbash(s string) string {
	var ciphertext bytes.Buffer

	for _, char := range strings.ToLower(s) {
		if unicode.IsLetter(char) {
			ciphertext.WriteRune('a' + 'z' - char)
		} else if unicode.IsDigit(char) {
			ciphertext.WriteRune(char)
		}
		if (ciphertext.Len()+1)%6 == 0 {
			ciphertext.WriteRune(' ')
		}
	}
	// remove any trailing space that was inserted
	return strings.TrimRight(ciphertext.String(), " ")
}
