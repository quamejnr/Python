def counting_words(file):
    with open(file, 'r') as f:
        words = f.read()

    count = {}
    new_words = sorted(words.lower().split())
    for word in new_words:
        count.setdefault(word, 0)
        count[word] += 1

    with open('new_alice.txt', 'w') as nf:
        nf.write("Words\tCount\n"
                 "============\n")
        for k, v in count.items():
            nf.write(f"{k}\t{v}")
