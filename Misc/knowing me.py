from Questions import Question


def knowing_me():

    user_name = input("Enter your name: ")
    user_name1 = "Kwame"

    question_prompts1 = [
        "What does " + user_name1 + " love to sleep in? \n(a)Pyjamas \n(b)Birthday suit",
        "What is " + user_name1 + "'s favourite food? \n(a)Rice \n(b)Emo tuo"

    ]

    question_prompts2 = [
        "What do you love to sleep in? \n(a)Pyjamas \n(b)Birthday suit\n",
        "What is your favourite food? \n(a)Rice \n(b)Emo tuo\n"

    ]

    print("Hello " + user_name + " my name is Bliss and I want to know how well you know " + user_name1 + "\n")

    test1 = [
        Question(question_prompts1[0], 'b'),
        Question(question_prompts1[1], "b"),
    ]

    test2 = [
        Question(question_prompts2[0], 'b'),
        Question(question_prompts2[1], "b"),
    ]

    while True:
        score = 0
        for question in test1:
            print(question.prompt)
            answer = input()
            if answer == question.answer:
                print('correct')
                score +=1
            else:
                print("wrong")
            if score == 2:
                print("You know " + user_name1 + " very well")

        print("Hello " + user_name + "! You are welcome to the 'Knowing Me' Game."
              "\nWhy don't you also tell us a little about yourself and let's find out how well your friends know you\n"
              )

        user_name1 = user_name

        question_prompts1 = [
            "What does " + user_name1 + " love to sleep in? \n(a)Pyjamas \n(b)Birthday suit\n",
            "What is " + user_name1 + "'s favourite food? \n(a)Rice \n(b)Emo tuo\n"

        ]
        test1 = [
            Question(question_prompts1[0], 'b'),
            Question(question_prompts1[1], "b"),
        ]
        for question in test1:
            question.answer = input(question.prompt)

        user_name = input("Enter your name: ")



knowing_me()
