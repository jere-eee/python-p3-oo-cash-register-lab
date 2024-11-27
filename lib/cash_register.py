#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0) -> None:
    self.discount = discount
    self.total = 0
    self.items = []
    
  def add_item(self, title, price, quantity=1):
    self.total += price*quantity
    self.items.extend([title] * quantity)
    self.last_transaction = {
      "title": title,
      "price": price,
      "quantity": quantity
    }
    
  def apply_discount(self, discount=20):
    self.total -= (discount / 100) * self.total
    if self.total > 0:
      print(f'After the discount, the total comes to ${int(self.total)}.')
    else:
      print('There is no discount to apply.')
      
  def void_last_transaction(self):
    if self.last_transaction:
      self.total -= self.last_transaction["price"] * self.last_transaction["quantity"]
      for word in self.items:
        if word == self.last_transaction["title"]:
          self.items.remove(word)