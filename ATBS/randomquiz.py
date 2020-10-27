#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random


# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
            'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
            'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
            'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
            'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
            'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
            'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe',
            'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck',
            'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg',
            'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
            'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
            'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Generate 35 quiz files.
for quizNum in range(35):

    # Create the quiz and answer key files.
    with open(f'Quiz{quizNum+1}.txt', 'w') as quiz:
        with open(f"answers{quizNum + 1}.txt", 'w') as solutions:

            # Header for the quiz
            quiz.write('Name:\n\nDate:\n\nPeriod:\n\n')
            quiz.write(f'{" "*20}State Capitals Quiz (Form {quizNum+1})\n\n')

            # Shuffle the order of the states
            states = list(capitals.keys())
            random.shuffle(states)

            # writing questions
            for i in range(len(states)):
                quiz.write(f'{i+1}. What is the capital of {states[i]}\n')

                # writing answers
                correct_ans = capitals[states[i]]
                values = list(capitals.values())
                wrong_ans = random.sample(values, 3)
                answers = wrong_ans + [correct_ans]
                random.shuffle(answers)
                alpha = 'ABCD'
                for j in range(len(alpha)):
                    quiz.write(f"{' '*5}{alpha[j]}. {answers[j]}\n")
                quiz.write('\n')

                # writing solutions in answer_file
                solutions.write(f"{i+1}. {alpha[answers.index(correct_ans)]}\n")
