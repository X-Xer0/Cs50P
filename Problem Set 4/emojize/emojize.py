import emoji

text = input("Input: ")

emojized_text = emoji.emojize(text, language='alias')

print("Output:", emojized_text)
