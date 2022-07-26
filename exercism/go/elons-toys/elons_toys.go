package elon

import "fmt"

// 'Drive()' method
func (car *Car) Drive() {
	if car.battery >= car.batteryDrain {
		car.battery -= car.batteryDrain
		car.distance += car.speed
	}
}

// 'DisplayDistance() string' method
func (car *Car) DisplayDistance() string {
	return fmt.Sprintf("Driven %d meters", car.distance)
}

// Output: "Battery at 100%"

// TODO: define the 'DisplayBattery() string' method
func (car *Car) DisplayBattery() string {
	return fmt.Sprintf("Battery at %d%%", car.battery)
}

// TODO: define the 'CanFinish(trackDistance int) bool' method
func (car *Car) CanFinish(trackDistance int) bool {
	return car.battery/car.batteryDrain*car.speed >= trackDistance
}
