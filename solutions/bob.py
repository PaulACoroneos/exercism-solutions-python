def response(hey_bob):
    has_question_mark = hey_bob.strip().endswith('?')
    is_upper_case = hey_bob.isupper()

    if not has_question_mark and is_upper_case:
        return "Whoa, chill out!"
    if has_question_mark and not is_upper_case:
        return "Sure."
    if has_question_mark and is_upper_case:
        return "Calm down, I know what I'm doing!"
    if not hey_bob.strip():
        return "Fine. Be that way!"
    return 'Whatever.'