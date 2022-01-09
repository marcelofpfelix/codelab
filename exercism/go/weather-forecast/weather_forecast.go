// Package weather provides weather information.
package weather

// CurrentCondition the current weather condition.
var CurrentCondition string

// CurrentLocation the current city location.
var CurrentLocation string

// Forecast receives the location and weather condion and returns a string.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
