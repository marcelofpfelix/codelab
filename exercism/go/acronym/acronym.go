package acronym

import (
	"strings"
)

// Abbreviate should have a comment documenting it.
func Abbreviate(s string) string {
	// simple solution
	acr := ""
	// FieldsFunc could also be used
	s = strings.ReplaceAll(strings.ReplaceAll(s, "_", ""), "-", " ")

	words := strings.Fields(s)

	for _, word := range words {
		// strings.Join can be used
		acr += string([]rune(word)[0])
	}

	return strings.ToUpper(acr)
	// using a regex would result in a more elegant solution
	// re := regexp.MustCompile(`[\PL]*([\pL])[\pL']*[\PL]*`)
}
