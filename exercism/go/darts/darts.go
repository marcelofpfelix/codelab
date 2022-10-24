package darts

func Score(x, y float64) int {

	throw := (x * x) + (y * y)
	if throw > 100 {
		return 0
	}
	if throw > 25 {
		return 1
	}
	if throw > 1 {
		return 5
	}
	return 10

	// radius is a power of 2, to simplify.
	// math.Hypot(x, y) could also be used
}
