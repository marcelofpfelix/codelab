package parsinglogfiles

import "regexp"

func IsValidLine(text string) bool {
	return regexp.MustCompile(`^\[(TRC|DBG|INF|WRN|ERR|FTL)\]`).MatchString(text)
}

func SplitLogLine(text string) []string {
	// -1 to return all substrings
	return regexp.MustCompile(`\<[~*=-]*\>`).Split(text, -1)
}

func CountQuotedPasswords(lines []string) int {
	re := regexp.MustCompile(`(?i)".*password.*"`)
	count := 0
	for _, line := range lines {
		if re.MatchString(line) {
			count++
		}
	}
	return count
}

func RemoveEndOfLineText(text string) string {
	return regexp.MustCompile(`end-of-line\d+`).ReplaceAllLiteralString(text, "")
}

func TagWithUserName(lines []string) []string {
	re := regexp.MustCompile(`User +([a-zA-Z\d]+)`)

	for i, line := range lines {

		// will return the user in slice[1]
		slice := re.FindStringSubmatch(line)
		if slice != nil {
			lines[i] = "[USR] " + slice[1] + " " + line
			// alternative: fmt.Sprintf("[USR] %s %s", slice[1], line)
		}
	}
	return lines
}
