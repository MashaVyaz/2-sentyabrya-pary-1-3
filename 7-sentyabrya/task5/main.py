class Dictionary:
    rus = "Питон"
    eng = "Python"

p = Dictionary()
print(getattr(Dictionary, "rus_word", False))
