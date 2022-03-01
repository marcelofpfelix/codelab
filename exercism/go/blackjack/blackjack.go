package blackjack

// ParseCard returns the integer value of a card following blackjack ruleset.
func ParseCard(card string) int {

	switch {
	case card == "ace":
		return 11
	case card == "king" || card == "queen" || card == "jack" || card == "ten":
		return 10
	case card == "nine":
		return 9
	case card == "eight":
		return 8
	case card == "seven":
		return 7
	case card == "six":
		return 6
	case card == "five":
		return 5
	case card == "four":
		return 4
	case card == "three":
		return 3
	case card == "two":
		return 2
	case card == "one":
		return 1
	default:
		return 0
	}

}

// IsBlackjack returns true if the player has a blackjack, false otherwise.
func IsBlackjack(card1, card2 string) bool {

	return ParseCard(card1)+ParseCard(card2) == 21
}

// LargeHand implements the decision tree for hand scores larger than 20 points.
func LargeHand(isBlackjack bool, dealerScore int) string {

	if isBlackjack {
		if dealerScore > 9 {
			return "S"
		}
		return "W"
	}
	return "P"
}

// SmallHand implements the decision tree for hand scores with less than 21 points.
func SmallHand(handScore, dealerScore int) string {

	if handScore > 16 {
		return "S"
	}
	if handScore < 12 {
		return "H"
	}
	if dealerScore > 6 {
		return "H"
	}
	return "S"
}
