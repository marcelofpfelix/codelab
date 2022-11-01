package flatten

// Take a nested list and return a single flattened list with all values except nil/null.
func Flatten(nested interface{}) []interface{} {

	//The second set of braces instantiates an instance of that type,
	// so []interface{}{} is an empty slice of empty interface
	result := []interface{}{}
	//result := make([]interface{}, 0)

	switch item := nested.(type) {
	// []interface{} is the type: a slice [] of empty interface
	case []interface{}:
		for _, value := range item {
			// ...pass a slice arg directly to a variadic functio
			// recursive call
			result = append(result, Flatten(value)...)
		}
	// an empty interface
	case interface{}:
		result = append(result, item)
	}
	return result
}
