/// simply reverse order
pub fn reverse(input: &str) -> String {
    // the simple way
    // input.chars().rev().collect()

    if input.len() == 0 {
        return input.to_string();
    }
    let mut i = 0;
    // instead of input.len() to handle wide characters
    let mut j = input.chars().count() - 1;
    let mut chars: Vec<char> = input.chars().collect();

    while i < j {
        let temp = chars[i];
        chars[i] = chars[j];
        chars[j] = temp;
        i += 1;
        j -= 1;
    }

    chars.into_iter().collect()
}
