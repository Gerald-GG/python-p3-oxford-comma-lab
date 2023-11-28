def oxford_comma(words):
    if len(words) == 1:
        return words[0]
    elif len(words) == 2:
        return f"{words[0]} and {words[1]}"
    else:
        formatted_words = ', '.join(words[:-1])
        return f"{formatted_words}, and {words[-1]}"
result = oxford_comma(["fiddleheads", "okra", "kohlrabi"])
print(result)
