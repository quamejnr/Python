class Dictionary:

    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning


words = [
        Dictionary("hamper", "thwart"),
        Dictionary("buttress", "support"),
        Dictionary("amalgamate", "combine"),
        Dictionary('emancipate', "liberate"),
        Dictionary("extirpate", "wipe out"),

]

user_input = input("Enter word: ")
for word in words:
    if user_input == word.word:
        print(word.meaning)
