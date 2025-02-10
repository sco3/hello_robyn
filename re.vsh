import regex

text := 'model name: asdf'
query := r'model name:(.+)'
mut re := regex.regex_opt(query)!
start, end := re.match_string(text)
mut gi := 0
for gi < re.groups.len {
    if re.groups[gi] >= 0 {
        println('${gi / 2} :[${text[re.groups[gi]..re.groups[gi + 1]]}]')
    }
    gi += 2
}
