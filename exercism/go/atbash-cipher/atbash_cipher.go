package atbash

import "strings"

func Atbash(s string) string {
	panic("Please implement the Atbash function")
}


// 	a simple shift cipher that relies on transposing all the letters in the alphabet
//	using an integer key between `0` and `26`
func RotationalCipher(plain string, shiftKey int) string {


	// text_list[index]= chr(122-ord(char)+97)

	// sums the key using % 26
	cipher := func(char rune) rune {
		lower := 'a'
		upper := 'A'
		base := upper

		if char >= lower {
			base = lower
		}
		if char >= upper {
			return base + (char-base+rune(shiftKey))%26
		}
		return char
	}

	return strings.Map(cipher, plain)
}
