package logs

var appRune = map[rune]string{
	'❗': "recommendation",
	'🔍': "search",
	'☀': "weather",
}

// Application identifies the application emitting the given log.
func Application(log string) string {
	for _, rune := range log {
		app, exists := appRune[rune]
		// if app, exists := appRune[rune]; exists {
		if exists {
			return app
		}
	}
	return "default"
}

// Replace replaces all occurrences of old with new, returning the modified log
// to the caller.
func Replace(log string, oldRune, newRune rune) string {
	runeStr := []rune(log)
	for index, rune := range runeStr {

		if rune == oldRune {
			runeStr[index] = newRune
		}
	}
	// return strings.ReplaceAll(log, string(oldRune), string(newRune))
	return string(runeStr)
}

// WithinLimit determines whether or not the number of characters in log is
// within the limit.
func WithinLimit(log string, limit int) bool {
	runeStr := []rune(log)
	return len(runeStr) <= limit
	// 	return utf8.RuneCountInString(log) <= limit
}
