from Questions import Question

question_prompts = [
    "What does Kwame love to sleep in? \n(a)Pyjamas \n(b)Birthday suit\n",
    "What is Kwame's favourite food? \n(a)Rice \n(b)Emo tuo\n"

]

questions = [
    Question(question_prompts[0], 'b'),
    Question(question_prompts[1], 'b'),
]


def test(questions):
    for question in questions:
        score = 0
        answer = input(question.prompt)
        if answer == question.answer:
            print("Correct\n")
            score += 1
        else:
            print("Wrong! the answer is " + question.answer+"\n")

    print('You got ' + str(score) + "/" + str(len(questions)) + " correct")


test(questions)
