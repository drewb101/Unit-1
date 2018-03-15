def analyze_text(text):
    text = "".join([i for i in text if i.isalpha()])
    ltrs = len(text)
    ltr_e = text.lower().count('e')
    prct = str((ltr_e / ltrs) * 100)

    message = ("The text contains {} alphabetic characters, of which {} ({}%) are 'e'." "".format(ltrs, ltr_e, prct))
    return message


print(analyze_text("How are you doing today?")