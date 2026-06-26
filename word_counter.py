
with open("sample.txt", "r") as file:
    text = file.read()


print("===== File Content =====")
print(text)


total_characters = len(text)


words = text.split()
total_words = len(words)


lines = text.splitlines()
total_lines = len(lines)


sentence_count = 0
for char in text:
    if char in ".!?":
        sentence_count += 1


print("\n===== Report =====")
print("Total Characters :", total_characters)
print("Total Words      :", total_words)
print("Total Lines      :", total_lines)
print("Total Sentences  :", sentence_count)