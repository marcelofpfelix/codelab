package diffsquares

/*
  using the partial sum:
    $sum_(n=1)^k n = 1/2 k (k + 1)$
  https://www.wolframalpha.com/input?i=sum+n%2C+n%3D1+to+infinity
*/
func SquareOfSum(n int) int {

	// return int(math.Pow(float64(n*(n+1)/2), 2))
	return (n * (n + 1) / 2) * (n * (n + 1) / 2)
}

/*
  using the partial sum:
    $sum_(n=1)^k n^2 = 1/6 k (k + 1) (2 k + 1)$
  https://www.wolframalpha.com/input?i=sum+n%5E2%2C+n%3D1+to+infinity
*/
func SumOfSquares(n int) int {

	return n * (n + 1) * (2*n + 1) / 6
}

func Difference(n int) int {
	return SquareOfSum(n) - SumOfSquares(n)
}
