package romannumerals

import (
	"fmt"
	"math"
	"strconv"
)

var symbol1 = []string{"I", "X", "C", "M"}
var symbol5 = []string{"V", "L", "D"}

//     get a digit from a number
func get_digit(number int, index int) int {
	return int(math.Mod(float64(number)/math.Pow(10, float64(index)), 10))
}

/*
convert Hindu–Arabic numeral system to roman

this version aims to be versatile, simply by adding
the ordered simbols to the list
while substracting values from
['M','CM',D','CD','C','XC','L','XL','X','IX','V','IV', 'I']
would also be a good alternative
*/
func ToRomanNumeral(input int) (string, error) {
	romano := ""

	if input <= 0 || input >= 4000 {
		return "", fmt.Errorf("number %d is not allowed", input)
	}

	// get the number of digits
	lenght := len(strconv.Itoa(input))

	for index := 0; index < lenght; index++ {
		digit := get_digit(input, index)
		letter := ""

		// 4 or 9
		if digit%5 == 4 {
			if digit%5 == 4 {
				letter += symbol1[index]
			}
			if digit > 5 {
				letter += symbol1[index+1]
			} else {
				letter += symbol5[index]
			}
		} else {
			// adds symbol5
			if digit > 4 {
				letter += symbol5[index]
				digit = digit - 5
			}
			// and then the remain symbol1
			for indexx := 0; indexx < digit; indexx++ {
				letter += symbol1[index]
			}
		}
		romano = letter + romano
	}
	return romano, nil
}
