import time


def timer(minutes):
    tim = 0
    while tim != minutes:
        time.sleep(60)
        tim +=1
    return tim


answers = ['yes', 'y', 'ok', 'sure', 'yh', 'yeah']

ans = input("Want to start focus?\n")
if ans in answers:
    focus_time = int(input("Focus time: "))
    break_time = int(input("Break time: "))
    while True:
        focus_ans = input("Begin?\n")
        if focus_ans in answers:
            focus = timer(focus_time)
            print(f'{focus} minutes is up')
            brk_ans = input("Take a break\n")
            if brk_ans in answers:
                timer(break_time)
                final_question = input("Break over. Want to focus again?\n")
                if final_question in answers:
                    continue
        break
