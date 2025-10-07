text = input("Введіть текст латинськими літерами: ").lower()

letters = set(text)
more_than_one = {ch for ch in letters if text.count(ch) >= 2}
only_one = {ch for ch in letters if text.count(ch) == 1}

print("Літери, які зустрічаються >= 2 разів:", more_than_one)
print("Літери, які зустрічаються 1 раз:", only_one)
