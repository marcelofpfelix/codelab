package proverb

import "fmt"

// Given a list of inputs, generate the relevant proverb
func Proverb(rhyme []string) []string {
	data := []string{}
	if len(rhyme) > 0 {
		for index := 0; index < len(rhyme)-1; index++ {
			data = append(data, fmt.Sprintf("For want of a %s the %s was lost.", rhyme[index], rhyme[index+1]))
		}
		data = append(data, fmt.Sprintf("And all for the want of a %s.", rhyme[0]))
	}

	return data
}
