package space

type Planet string

const period = 31557600.0

// Given an age in seconds, calculate how old someone would be on
// our Planets
var coef = map[Planet]float64{
	"Earth":   1.0,
	"Mercury": 0.2408467,
	"Venus":   0.61519726,
	"Mars":    1.8808158,
	"Jupiter": 11.862615,
	"Saturn":  29.447498,
	"Uranus":  84.016846,
	"Neptune": 164.79132}

func Age(seconds float64, planet Planet) float64 {

	// convert to lower case: Planet(strings.ToLower(string(planet)))
	if coefficient, OK := coef[planet]; OK {
		return seconds / (period * coefficient)
	}
	return -1
}
