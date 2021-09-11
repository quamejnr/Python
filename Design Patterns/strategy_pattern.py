import string
import random
from typing import List, Callable


def generate_id(length=8):
    # helper function for generating an id
    return ''.join(random.choices(string.ascii_uppercase, k=length))


class SupportTicket:

    def __init__(self, customer, issue):
        self.id = generate_id()
        self.customer = customer
        self.issue = issue


def fifo_ordering(tickets: List[SupportTicket]) -> List[SupportTicket]:
    tickets.copy()
    for ticket in tickets:
        yield ticket


def filo_ordering(tickets: List[SupportTicket]) -> List[SupportTicket]:
    tickets.copy().reverse()
    for ticket in tickets:
        yield ticket


def random_ordering(tickets: List[SupportTicket]) -> List[SupportTicket]:
    tickets_copy = tickets.copy()
    random.shuffle(tickets_copy)
    for ticket in tickets:
        yield ticket


def black_hole_ordering(tickets: List[SupportTicket]) -> List[SupportTicket]:
    return []


class CustomerSupport:

    def __init__(self):
        self.tickets = []

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))

    def process_tickets(self, ordering: Callable[[List[SupportTicket]], List[SupportTicket]]):
        # create the ordered list
        ticket_list = ordering(self.tickets)

        # if it's empty, don't do anything
        if not ticket_list:
            print("There are no tickets to process. Well done!")
            return

        # go through the tickets in the list
        for ticket in ticket_list:
            self.process_ticket(ticket)

    @staticmethod
    def process_ticket(ticket: SupportTicket):
        print("==================================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("==================================")


if __name__ == '__main__':

    # create the application
    app = CustomerSupport()

    # register a few tickets
    app.create_ticket("John Smith", "My computer makes strange sounds!")
    app.create_ticket("Linus Sebastian", "I can't upload any videos, please help.")
    app.create_ticket("Arjan Egges", "VSCode doesn't automatically solve my bugs.")

    # process the tickets
    app.process_tickets(filo_ordering)