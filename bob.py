def response(hey_bob):
    hey_bob_stripped = hey_bob.strip()

    if hey_bob.isupper() and hey_bob.endswith("?"):
        return "Calm down, I know what I'm doing!"
    elif hey_bob.isupper():
        return "Whoa, chill out!"
    elif hey_bob.isspace() or hey_bob == "":
        return "Fine. Be that way!"
    elif hey_bob_stripped.endswith("?"):
        return "Sure."
    else:
        return "Whatever."
