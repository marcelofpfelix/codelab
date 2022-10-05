package meteorology

import "fmt"

type TemperatureUnit int

const (
	Celsius    TemperatureUnit = 0
	Fahrenheit TemperatureUnit = 1
)

// Add a String method to the TemperatureUnit type
func (sc TemperatureUnit) String() string {
	units := []string{"°C", "°F"}
	return units[sc]
}

type Temperature struct {
	degree int
	unit   TemperatureUnit
}

// Add a String method to the Temperature type
func (d Temperature) String() string {
	return fmt.Sprintf("%v %v", d.degree, d.unit)
}

type SpeedUnit int

const (
	KmPerHour    SpeedUnit = 0
	MilesPerHour SpeedUnit = 1
)

// Add a String method to SpeedUnit
func (sc SpeedUnit) String() string {
	units := []string{"km/h", "mph"}
	return units[sc]
}

type Speed struct {
	magnitude int
	unit      SpeedUnit
}

// Add a String method to Speed
func (d Speed) String() string {
	return fmt.Sprintf("%v %v", d.magnitude, d.unit)
}

type MeteorologyData struct {
	location      string
	temperature   Temperature
	windDirection string
	windSpeed     Speed
	humidity      int
}

// Add a String method to MeteorologyData
func (d MeteorologyData) String() string {
	return fmt.Sprintf("%v: %v, Wind %v at %v, %v%% Humidity", d.location, d.temperature, d.windDirection, d.windSpeed, d.humidity)
}
