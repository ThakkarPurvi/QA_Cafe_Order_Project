# the order.py contains a constructor to create our order object,
# takes in string and numerical values from the runner / controller

class Order:
   def __init__(self, order_id: int, customer_name: str, order_date: str, item_name: str, item_quantity: int, item_price: float, total_cost: float):
       self.order_id = order_id
       self.customer_name = customer_name
       self.order_date = order_date
       self.item_name = item_name
       self.item_quantity = item_quantity
       self.item_price = item_price
       self.total_cost = total_cost

   def add_to_dict(self):
       return {"order_id": self.order_id,
               "customer_name": self.customer_name,
               "order_date": self.order_date,
               "item_name": self.item_name,
               "item_quantity": self.item_quantity,
               "item_price": self.item_price,
               "total_cost": self.total_cost}

