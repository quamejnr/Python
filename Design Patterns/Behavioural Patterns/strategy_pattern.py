class Order:

    def __init__(self, product, price, paid=False):
        self.product = product
        self.price = price
        self.paid = paid
        print("Initializing Order...")


def pay_via_momo(order: Order):
    print('Paying via Momo...')


def pay_via_visa(order: Order):
    print('Paying via Visa Card...')


def pay_via_cash(order: Order):
    print('Paying via Cash...')


class PaymentProcessor:

    def pay(self, order: Order, payment_method):
        payment_method(order)
        order.paid = True
        print('Paid')


# Initialize order
order = Order('Burger', 7000)
print(order.paid)

# Paying order
payment = PaymentProcessor()
payment.pay(order, payment_method=pay_via_cash)
print(order.paid)
