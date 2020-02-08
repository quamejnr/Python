word = "banana"


def make_word(word):
    count = 0

    while len(word) > 0:
        new_word = ""
        for letter in word:
            new_word += letter
            yield new_word
            count +=1
        word = word[1:]


print(list(make_word(word)))


