package lasagna

// Implement a function `PreparationTime` that accepts a slice of layers as a `[]string` and the average preparation time per layer in minutes as an `int`.
// The function should return the estimate for the total preparation time based on the number of layers as an `int`.
// Go has no default values for functions.
// If the average preparation time is passed as `0` (the default initial value for an `int`), then the default value of `2` should be used.
func PreparationTime(layers []string, time int) int {
	if time == 0 {
		time = 2
	}

	return len(layers) * time
}

// Define the function `Quantities` that takes a slice of layers as parameter as a `[]string`.
// The function will then determine the quantity of noodles and sauce needed to make your meal.
// The result should be returned as two values of `noodles` as an `int` and `sauce` as a `float64`.
func Quantities(layers []string) (int, float64) {
	noodles := 0
	sauce := 0.0

	for _, layer := range layers {
		if layer == "noodles" {
			noodles += 50
		} else if layer == "sauce" {
			sauce += 0.2
		}
	}

	return noodles, sauce
}

// Write a function `AddSecretIngredient` that accepts two slices of ingredients of type `[]string` as parameters.
// The first parameter is the list your friend sent you, the second is the ingredient list of your own recipe.
// The last element in your ingredient list is always `"?"`. The function should replace it with the last item from your friends list.
func AddSecretIngredient(friendsList, myList []string) {
	myList[len(myList)-1] = friendsList[len(friendsList)-1]
}

// The function should return a slice of `float64` of the amounts needed for the desired number of portions.
// You want to keep the original recipe though.
// This means the `amounts` argument should not be modified in this function.
func ScaleRecipe(amounts []float64, quantities int) []float64 {
	var scaled []float64

	for _, qty := range amounts {
		scaled = append(scaled, qty/2*float64(quantities))
	}
	return scaled
}
