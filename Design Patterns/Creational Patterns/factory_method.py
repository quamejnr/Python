from abc import ABC, abstractmethod


class Order:
    def __init__(self, product: str, price: int, quantity: int, paid=False):
        self.product = product
        self.price = price
        self.quantity = quantity
        self.paid = paid

    def total_cost(self) -> int:
        return self.price * self.quantity


class PaymentMethod(ABC):

    def __init__(self, money):
        self.money = money

    @abstractmethod
    def connect(self):
        pass


class VisaCard(PaymentMethod):

    def __init__(self, money):
        super().__init__(money)

    def connect(self):
        print('Connected to Visa Card...')


class Momo(PaymentMethod):

    def __init__(self, money):
        super().__init__(money)

    def connect(self):
        print('Connected to Momo...')


class DebitCard(PaymentMethod):

    def __init__(self, money):
        super().__init__(money)

    def connect(self):
        print('Connected to debit Card...')


class CheckoutCounter:

    @staticmethod
    def has_enough_money(order: Order, payment_method: PaymentMethod) -> bool:
        return payment_method.money >= order.total_cost()

    def receive_payment(self, order: Order, payment_method: PaymentMethod):
        print('Verifying payment method...')
        payment_method.connect()

        if self.has_enough_money(order, payment_method):
            payment_method.money -= order.total_cost()
            print(f"Payment for {order.product} received\tBalance: {payment_method.money}\n")
        else:
            raise Exception(f'Payment for {order.product} rejected: Not enough funds')


if __name__ == '__main__':
    order1 = Order('Corn', 3200, 1)
    order2 = Order('Burger', 3000, 1)
    visa_card = VisaCard(4000)
    momo = Momo(50000)
    counter = CheckoutCounter()
    counter.receive_payment(order1, visa_card)
    counter.receive_payment(order2, momo)
