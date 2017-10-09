def mutate_string(string, position, character):
    sl = list(string)
    sl[position] = character
    return "".join(sl)
