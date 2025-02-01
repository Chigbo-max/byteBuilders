


class Payment:
    def __init__(self, order, amount):
        self.order = order
        self.amount = amount
        self.payment_status = False

    def pay(self):
        if self.amount <= 0:
            raise ValueError("Order total must be greater than zero")
        if self.amount < self.order.get_total_price:
            raise ValueError("Amount is less than order total")
        self.payment_status = True
        return f"""payment of {self.amount} on the following order was successful \n\n               ORDER DETAILS \n
        """ + "\n".join([str(order)for order in self.order.order_history]) + "Payment Status: SUCCESSFUL"


