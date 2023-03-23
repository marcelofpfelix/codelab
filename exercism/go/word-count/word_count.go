package wordcount

import (
	"regexp"
	"strings"
)

type Frequency map[string]int

func WordCount(phrase string) Frequency {
	data := Frequency{}

	re := regexp.MustCompile(`[a-zA-Z0-9]+(['][a-zA-Z0-9]+)?`)
	for _, word := range re.FindAllString(strings.ToLower(phrase), -1) {
		data[word]++
	}

	return data
}
