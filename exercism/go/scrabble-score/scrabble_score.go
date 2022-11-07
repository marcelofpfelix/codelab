package scrabble

import (
	"strings"
	"unicode"
)

var POINT_MAP = map[string]int{
	"aeioulnrst": 1,
	"dg":         2,
	"bcmp":       3,
	"fhvwy":      4,
	"k":          5,
	"jx":         8,
	"qz":         10,
}

// alterntive would be a alphabet-size slice with the values,
// or a switch case
func Score(word string) int {

	score := 0
	for _, c := range strings.ToLower(word) {
		for x, y := range POINT_MAP {

			if strings.Contains(x, string(c)) && unicode.IsLetter(c) {
				//fmt.Print(string(c), x, y, "\n")
				score += y
				break
			}
		}
	}
	return score
}
