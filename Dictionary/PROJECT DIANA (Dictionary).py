def dictionary():
    dictionary={
                "hamper":'thwart',
                "buttress":"support",
                "amalgamate":"combine",
                'emancipate': "liberate"

                }
    while True:
        search = input("Enter word: ")

        for word in dictionary:
            if search in word.casefold():
                return dictionary[word]
        return "Word not in dictionary"

dictionary()