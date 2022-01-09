package twofer

import "fmt"

func ShareWith(name string) string {

	if name == "" {
		name = "you"
	}

	// alternative "One for" + name + ", one for me."
	return fmt.Sprintf("One for %s, one for me.", name)
}
