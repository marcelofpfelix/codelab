package prime

import "errors"

// Nth returns the nth prime number. An error must be returned if the nth prime number can't be calculated ('n' is equal or less than zero)
func Nth(n int) (int, error) {
	if n <= 0 {
		return 0, errors.New("there is no zeroth prime")
	}

	// slice starting with 2, since 2 is the first prime number
	primes := []int{2}
	index := 3
	for len(primes) < n {
		isPrime := true
		// check if index is divisible by any prime number
		for _, prime := range primes {
			// if index is divisible by any prime number, it is not prime
			if index%prime == 0 {
				isPrime = false
				break
			}
		}
		if isPrime {
			primes = append(primes, index)
		}
		index += 2
	}

	return primes[n-1], nil
}
