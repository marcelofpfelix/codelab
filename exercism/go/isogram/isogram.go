package isogram

import (
	"strings"
	"unicode"
)

func IsIsogram(word string) bool {
	word = strings.ToLower(word)
	for i, c := range word {
		// if char c is alpha and if char is duplicated
		if unicode.IsLetter(c) && strings.ContainsRune(word[i+1:], c) {
			return false
		}
	}
	return true
}

// ContainsRune used to check the given string contains the specified rune or not in it.
// IsLetter returns true if rune r is a letter
