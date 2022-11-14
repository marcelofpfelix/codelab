// triangle
package triangle

type Kind int

const (
	NaT Kind = iota // not a triangle
	Equ             // equilateral
	Iso             // isosceles
	Sca             // scalene
)

// Determine if a triangle is equilateral, isosceles, or scalene.
func KindFromSides(a, b, c float64) Kind {
	if a+b > c && b+c > a && c+a > b {
		if a == b && b == c {
			return Equ
		} else if a != b && b != c && a != c {
			return Sca
		}
		return Iso
	}
	return NaT
}
