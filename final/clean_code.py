

import datetime, dataclasses
from typing import Optional

COMMISSION_RATE = 0.14

class InvalidAmount(Exception) : ...
class OrderNotExists (Exception) : ...
class CannotProcessThisOrder(Exception) : ...
class InActiveUser(Exception) : ...
class LowBalance(Exception) : ...

@dataclasses.dataclass()
class User:
    id : int
    name : str
    email : str
    balance : float
    is_active : bool

    def withdraw(self, amount : float) -> None:

        if amount < 0 :
            raise InvalidAmount("Please enter a valid amount")

        if amount > self.balance:
            raise LowBalance("You don't have this amount in your wallet")

        self.balance -= amount


@dataclasses.dataclass()
class OrderItem:
    name : str
    price : float
    quantity : int


def validate_order(order : 'Order') -> Optional['Order']:
    for i in group_of_orders:
        if i.id == order.id and order.is_pending:
            return i

    raise OrderNotExists(f"This order with id {order.id} not exists")

def validate_user_activity(user : User):
    if not user.is_active:
        raise InActiveUser("Cannot process this operation for inactive user")

def send_confirm_order_email(order : 'Order'):
    if order.send_email == True:
        print("Sending email to " + order.user.email + ": Order " + str(order.id) + " processed! Total: " + str(order.calculate_final_price()))


def create_order_invoice(user : User, total_paid : float) :  
    # Formatting / Output Arguments
    print("======== INVOICE ========")
    print("Customer: " + user.name)
    print("Total Paid: " + str(total_paid))
    print("Remaining Balance: " + str(user.balance))
    print("=========================")


@dataclasses.dataclass()
class Order:
    id : int
    user : User
    items : list[OrderItem]
    status : int
    apply_discount : bool
    discount_value : int
    send_email : bool

    @property
    def is_pending(self) -> bool:
        return self.status == 0

    def _calculate_total_item_price(self) -> float:
        total_price = 0.0
        for item in self.items:
            total_price += item.price * item.quantity
        return total_price

    def _calculate_after_discount(self) -> float: 
        total = self._calculate_total_item_price()
        if self.apply_discount:
            return total - self.discount_value
        return total

    def calculate_final_price(self) -> float:
        total = self._calculate_after_discount() 
        return total + (total * COMMISSION_RATE)

    def mark_as_processed(self) : 
        self.status = 1

    def checkout(self) : 
        validate_order(self)
        validate_user_activity(self.user)
        total_order_price = self.calculate_final_price()
        self.user.withdraw(total_order_price)
        self.mark_as_processed()

list_of_users : list[User] = [
    User(id=101, name="Ali", email='ali@gmail.com', balance=500.0, is_active=True),
    User(id=102, name="Omar", email='omar@gmail.com', balance=50.0, is_active=False),
]


group_of_orders = [
    Order(
        id=5001,
        user=list_of_users[0],
        items=[OrderItem(
            name="Laptop",
            price=300.0,
            quantity=1
        )],
        status=0,
        apply_discount=True,
        send_email=True,
        discount_value=20
    ),
]

def logger(content : str) :
    print(content)
        

def process_order(order : Order, log_to_file=False) -> None:
    order.checkout()
    send_confirm_order_email(order)
    if log_to_file:
        logger("LOG: Order " + str(order.id) + " updated at " + str(datetime.datetime.now()))
    create_order_invoice(order.user, order.calculate_final_price())



process_order(
    order=group_of_orders[0],
)