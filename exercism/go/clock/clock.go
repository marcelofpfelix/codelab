package clock

//package main

import "fmt"

// could also be done with: type Clock int
type Clock struct {
	hour    int
	minutes int
}

func New(h, m int) Clock {
	// go doesn't do an Euclidean division like python
	// so 1440 is used for negative numbers
	dayMinutes := 1440
	hourMinutes := 60

	minutes := (h*hourMinutes + m) % dayMinutes
	if minutes < 0 {
		minutes += dayMinutes
	}
	return Clock{
		minutes / hourMinutes,
		minutes % hourMinutes,
	}
}

func (c Clock) Add(m int) Clock {
	return New(c.hour, c.minutes+m)
}

func (c Clock) Subtract(m int) Clock {
	return New(c.hour, c.minutes-m)
}

func (c Clock) String() string {
	return fmt.Sprintf("%02d:%02d", c.hour, c.minutes)
}
