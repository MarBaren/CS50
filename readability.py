from cs50 import get_string

# Vraag user om tekst
while True:
    text = get_string("Text: ")
    if len(text) > 0:
        break

# Tel de hoeveelheid letters
letters = 0
for char in text:
    if char.isalpha():
        letters += 1

print(f"{letters}")

# Tel de hoeveelheid woorden
words = text.count(" ") + 1

print(f"{words}")

# Tel de hoeveelheid zinnen
sentences = text.count(".") + text.count("!") + text.count("?")

print(f"{sentences}")

# Grade berekenen
L = letters / words * 100
S = sentences / words * 100
grade = round(0.0588 * L - 0.296 * S - 15.8)

# Grade printen
if grade < 1:
    print("Before Grade 1")
elif grade > 15:
    print("Grade 16+")
else:
    print(f"Grade {grade}")
