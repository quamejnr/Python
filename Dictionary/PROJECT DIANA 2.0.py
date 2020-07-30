class Dictionary:

    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    @staticmethod
    def search():
        user_input = input("Enter word: ")
        for vocab in vocabs:
            if user_input.casefold() == vocab.word:
                return vocab.meaning
            elif user_input.casefold() == vocab.meaning:
                return vocab.word
        return "Word not in dictionary"


vocabs = [
        Dictionary("hamper", "thwart"),
        Dictionary("buttress", "support"),
        Dictionary("amalgamate", "combine"),
        Dictionary('emancipate', "liberate"),
        Dictionary("extirpate", "wipe out"),

]


print(Dictionary.search())
