package wordy

import (
	"regexp"
	"strconv"
)

func Answer(question string) (int, bool) {

	// validate syntax
	if match, _ := regexp.MatchString(`What is -?\d+(?: (?:plus|minus|divided by|multiplied by) -?\d+)*\?`, question); !match {
		return 0, false
	}

	// gets the opetators and integers in a slice
	re1 := regexp.MustCompile(`(plus|minus|divided|multiplied)`)
	operators := re1.FindAllString(question, -1)
	re2 := regexp.MustCompile(`-?\d+`)
	numbers := re2.FindAllString(question, -1)

	// returns error if numbers and operators mismatch
	if len(operators) != len(numbers)-1 {
		return 0, false
	}
	sum, _ := strconv.Atoi(numbers[0])
	for i, o := range operators {
		n, _ := strconv.Atoi(numbers[i+1])
		switch o {
		case "plus":
			sum += n
		case "minus":
			sum -= n
		case "divided":
			sum /= n
		case "multiplied":
			sum *= n
		}
	}
	return sum, true
}
