import pprint

# day = datetime.today().strftime('%A')
day = "Sunday"
weekday = ["Monday", 'Tuesday', "Wednesday", "Thursday", "Friday"]
weekend = ["Saturday", 'Sunday']


def sleep(day):
    if day in weekend:
        return "sleep in and watch movie"
    else:
        return wakeup(day)


def wakeup(day):
    if day != 'Saturday':
        print('Wake up Sleepy head, breakfast in 30')
        return breakfast(day)
    else:
        return sleep(day)


def breakfast(day):
    if day == 'Monday':
        print("Eat scrambled eggs and oatmeal")
    elif day == "Tuesday":
        print("Eat Tombrown with brown bread and peanut butter spread")
    return exercise(day)


def exercise(day):
    return f"Today's workout routine is {workout_routine(day)}"


def workout_routine(day):
    if day == 'Monday':
        return 'Chest'
    elif day == 'Tuesday':
        return 'Abs'
    elif day == 'Wednesday':
        return 'Legs'
    elif day == 'Friday':
        return 'HIIT'
    else:
        return 'Rest day'







