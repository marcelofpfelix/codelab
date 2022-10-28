package anagram

import (
	"sort"
	"strings"
)

func Sorted(word string) string {
	s := []rune(word)
	sort.Slice(s, func(i int, j int) bool { return s[i] < s[j] })

	return string(s)
}

func Detect(subject string, candidates []string) []string {

	var values []string

	subject = strings.ToLower(subject)
	test_subject := Sorted(strings.ToLower(subject))

	for _, candidate := range candidates {
		test_candidate := strings.ToLower(candidate)

		if test_subject == Sorted(test_candidate) && subject != test_candidate {
			values = append(values, candidate)
		}
	}

	return values

}
