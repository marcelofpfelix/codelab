package thefarm

import (
	"errors"
	"fmt"
)

// See types.go for the types defined for this exercise.

// Define the SillyNephewError type here.
type SillyNephewError struct {
	amount int
}

func (e *SillyNephewError) Error() string {
	return fmt.Sprintf("silly nephew, there cannot be %d cows", e.amount)
}

// DivideFood computes the fodder amount per cow for the given cows.
func DivideFood(weightFodder WeightFodder, cows int) (float64, error) {
	fodder, err := weightFodder.FodderAmount()

	if cows == 0 {
		return 0, errors.New("division by zero")
	}
	if cows <= 0 {
		return 0, &SillyNephewError{cows}
	}
	if err != nil && err != ErrScaleMalfunction {
		return 0, err
	}
	if fodder < 0.0 {
		return 0, errors.New("negative fodder")
	}
	if err == ErrScaleMalfunction {
		if fodder > 0 {
			fodder *= 2
		}
	}
	return fodder / float64(cows), nil
}
