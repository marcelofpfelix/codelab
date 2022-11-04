package collatzconjecture

import "errors"

func CollatzConjecture(number int) (int, error) {
	if number < 1 {
		return 0, errors.New("values less than 1 not valid Collatz Conjecture input")
	}
	count := 0

	for number != 1 {
		count += 1
		if number%2 != 0 {
			number = 3*number + 1
		} else {
			number /= 2
		}
	}
	return count, nil
}
