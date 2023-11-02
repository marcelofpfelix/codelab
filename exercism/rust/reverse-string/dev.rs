fn reverse_string(s: &str) -> String {
    if s.is_empty() {
        return s.to_string();
    }

    let mut i = 0;
    let mut j = s.chars().count() - 1;
    let mut chars: Vec<char> = s.chars().collect();

    while i < j {
        let temp = chars[i];
        chars[i] = chars[j];
        chars[j] = temp;
        i += 1;
        j -= 1;
    }

    chars.into_iter().collect()
}

fn main() {
    let str = String::from("子猫");

    let rev_str = reverse_string(&str);

    println!("Reversed string: {}", rev_str);
}


// func Reverse(input string) string {
// 	runes := []rune(input)

// 	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
// 		runes[i], runes[j] = runes[j], runes[i]
// 	}
// 	return string(runes)
// }
