// This is a "stub" file.  It's a little start on your solution.
// It's not a complete solution though; you have to write some code.

// Package acronym should have a package comment that summarizes what it's about.
// https://golang.org/doc/effective_go.html#commentary
package acronym

// Abbreviate should have a comment documenting it.
func Abbreviate(s string) string {
	// Write some code here to pass the test suite.
	// Then remove all the stock comments.
	// They're here to help you get started but they only clutter a finished solution.
	// If you leave them in, reviewers may protest!
	return ""
}

/*
   """
   simple acronym:
   a = words[0]
   words = words.replace("_", "").replace("- ", "")

   for index, char in enumerate(words):
       if char == ' ' or char == '-':
           a = a + words[index + 1]
   return a.upper()
   """

   # smart: get the words
   return ''.join(word[0].upper() for word in re.findall(r"[a-zA-Z']+", words))

*/
