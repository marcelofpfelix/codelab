package summultiples

func SumMultiples(limit int, divisors ...int) int {
	sum := 0

	// // simple
	// for index := 1; index < limit; index++ {
	// 	for _, number := range divisors {
	// 		if number > 0 && index%number == 0 {
	// 			sum += index
	// 			break
	// 		}
	// 	}
	// }

	// improvement, using a map for duplicates
	// and increment by number
	duplicates := make(map[int]bool)
	for _, number := range divisors {
		if number != 0 {
			for index := number; index < limit; index += number {
				if !duplicates[index] {
					sum += index
					duplicates[index] = true
				}
			}
		}
	}

	return sum
}
