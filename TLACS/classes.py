import datetime
import copy
import inflect


p = inflect.engine()      # Using inflect to format my text(singular and plural nouns)


class Shoe:
    database = []

    def __init__(self, brand, name, size, number=1):
        self.brand = brand
        self.name = name
        self.size = size

        if number > 1:
            for _ in (range(number)):
                # The number provided while creating objects duplicates the objects
                copy.deepcopy(self)
                self.database.append(self)
        else:
            self.database.append(self)

    def get_database(self):
        return self.database

    def similar(self):
        """ Checks if there are similar shoes in the database. """
        if len(self.database) != 0:
            for i in range(len(self.database)):
                for j in range(i+1, len(self.database)):
                    if self.database[i] == self.database[j]:
                        return True
        return False

    def get_brand(self, brand):
        """ Returns the number of shoes of a brand in the database. """
        result = []
        for obj in self.database:
            if obj.brand == brand:
                result.append(obj)
        return f"There {p.plural_verb('is',len(result))} {len(result)} {brand} {p.plural_noun('shoe',len(result))}"

    def __str__(self):
        return f'{self.brand} {self.name} \tSize:{self.size}'

    def __repr__(self):
        return f"{self.brand, self.name, self.size}"


# shoe1 = Shoe("Adidas", "Superstar", 42)
# shoe2 = Shoe("Nike", "Air Max", 41, 3)
# print(shoe2.similar())
# print(shoe1.get_database())
# print(shoe1.get_brand('Adidas'))


class SmsStore:
    log = []
    time = datetime.datetime.now()

    def __init__(self, text_message, form_number, has_viewed=False, time_arrived=time.strftime("%d/%m/%y %I:%M%p")):
        self.text_message = text_message
        self.time_arrived = time_arrived
        self.form_number = form_number
        self.has_viewed = has_viewed
        self.log.append(self)

    def add_new_arrival(self, person):
        self.log.append(person)

    def message_count(self):
        return len(self.log)

    def all_messages(self):
        return self.log

    def unread_indexes(self):
        unread = []
        for i in range(len(self.log)):
            if not self.log[i].has_viewed:
                unread.append(i)
        return unread

    def get_message(self, msg):
        messages = []
        for i in self.log:
            if msg in i.text_message:
                messages.append(i)
        return messages

    def delete(self, index):
        try:
            self.log.pop(index)
            return f'Message at index {index} removed'
        except IndexError:
            return "No message at index"

    def clear(self):
        ans = input("Are you sure you want to clear all your messages y/n\n")
        if ans.casefold() == 'y':
            self.log.clear()
            return 'All messages deleted'
        return "Delete cancelled"

    def __repr__(self):
        if self.has_viewed:
            return f"{self.text_message, self.form_number, self.time_arrived, 'Read'}"
        return f"{self.text_message, self.form_number, self.time_arrived, 'Unread'}"

    def __str__(self):
        if self.has_viewed:
            return f"{self.text_message, self.form_number, self.time_arrived, 'Read'}"
        return f"{self.text_message, self.form_number, self.time_arrived, 'Unread'}"


# my_inbox = SmsStore('I miss you', '0244483726', True)
# new_msg = SmsStore('I miss you', '0244483726', True)
# my_inbox.add_new_arrival(new_msg)
# my_inbox.add_new_arrival(SmsStore("Hello Babe!", '0501427202', True))
# print(my_inbox.message_count())
# print(my_inbox.unread_indexes())
# print(my_inbox.get_message("miss"))
# print(my_inbox.clear())
# print(my_inbox.all_messages())
# my_outbox = SmsStore("Ohemaa", '023400020')
# print(my_outbox.all_messages())


