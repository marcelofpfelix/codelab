package airportrobot

import "fmt"

// `LanguageName` which returns the name of the language (a `string`) that the robot is supposed to greet the visitor in.
// `Greet` which accepts a visitor's name (a `string`) and returns a `string` with the greeting message in a specific language.
type Greeter interface {
	LanguageName() string
	Greet(name string) string
}

//struct that implement the two methods that are needed for the struct
type Italian struct{}
type Portuguese struct{}

// accepts the name of the visitor and anything that implements the `Greeter` interface as arguments and returns the desired greeting string.
func SayHello(name string, g Greeter) string {
	return fmt.Sprintf("I can speak %s: %s", g.LanguageName(), g.Greet(name))
}

func (i Italian) LanguageName() string {
	return "Italian"
}

func (i Italian) Greet(name string) string {
	return fmt.Sprintf("Ciao %s!", name)
}

func (i Portuguese) LanguageName() string {
	return "Portuguese"
}

func (i Portuguese) Greet(name string) string {
	return fmt.Sprintf("Olá %s!", name)
}
