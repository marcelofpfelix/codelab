/*
  convert a number into a string that contains raindrop sounds
*/
package raindrops

import "strconv"

// compatible with the tests.
const TestVersion = 1

// Convert translate a number to its raindrops string representation.
func Convert(number int) (sound string) {
	// alternatives
	// var sound string
	// string := ""

	if number%3 == 0 {
		sound += "Pling"
	}
	if number%5 == 0 {
		sound += "Plang"
	}
	if number%7 == 0 {
		sound += "Plong"
	}
	if sound == "" {
		// convert to string
		sound = strconv.Itoa(number)
	}
	return
}
