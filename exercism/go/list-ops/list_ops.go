package listops

// IntList is an abstraction of a list of integers which we can define methods on
type IntList []int

// type binFunc func(x, y int) int

func (s IntList) Foldl(fn func(int, int) int, initial int) int {
	for _, iten := range s {
		initial = fn(initial, iten)
	}
	return initial
}

func (s IntList) Foldr(fn func(int, int) int, initial int) int {
	for i := len(s) - 1; i >= 0; i-- {
		initial = fn(s[i], initial)
	}
	return initial
}

func (s IntList) Filter(fn func(int) bool) IntList {
	list := IntList{}
	for _, iten := range s {
		if fn(iten) {
			list = append(list, iten)
		}
	}
	return list
}

func (s IntList) Length() int {
	return len(s)
}

func (s IntList) Map(fn func(int) int) IntList {
	list := IntList{}
	for _, iten := range s {
		list = append(list, fn(iten))
	}
	return list
}

func (s IntList) Reverse() IntList {
	list := IntList{}
	for i := len(s) - 1; i >= 0; i-- {
		list = append(list, s[i])
	}
	return list
}

func (s IntList) Append(lst IntList) IntList {
	// Append one slice to another
	return append(s, lst...)
	// The ... unpacks b. Without the dots, the code would
	// attempt to append the slice as a whole, which is invalid.
}

func (s IntList) Concat(lists []IntList) IntList {
	for _, iten := range lists {
		s = append(s, iten...)
	}
	return s
}
