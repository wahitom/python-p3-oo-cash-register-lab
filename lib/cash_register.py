#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    if isinstance(discount, (int, float)):
      self._discount = discount
      self._total = 0
      self._items = []
    else:
      print("Invalid input")
    
    # getting those items 
  def get_items(self):
        return self._items
  
  def get_discounted_items(self):
      if self._discount > 0:
          return [{'title': item['title'], 'price':  round(item['price'] * (1 - self._discount / 100), 2)} for item in self._items]

    # Adding items to the list set items 
  def add_item(self, title, price, quantity=1):
        for _ in range(quantity):
            self._items.append({'title': title, 'price': price})
            #update the total when adding an item
            self._total += price * quantity
    
    # Testing the discounts 
  def apply_discount(self):
      # calcualte the discount
      # apply the discount 
      # make it so that the discount reduces total
      # provide total if there is no discount

    if self._discount > 0:
            discount_amount = (self._discount / 100) * self._total
            self._total -= discount_amount
            # :2f is used to signify that there should only be two decimal points
            print(f"After the discount, the total is ${self._total:.2f}.")
    else:
            print(f"This item(s) does not have a discount. Your total is ${self._total:.2f}.")

  def void_last_transaction(self):
    # Redmove the last items from items list using pop()
    # it  does this by subtracting the cost of the last item from the current total
    if self._items:
        last_item = self._items .pop()
        self._total -= last_item['price'] * last_item.get('quantity', 1)
    
    print (f"Total: ${self._total:.2f}, Items: {self.get_items()}")
    

cash_register = CashRegister()
cash_register.add_item("apple", 6.99)
cash_register.add_item("milk", 4.99)
print("Before discount:", cash_register.get_items())
print(f"Total before discount:", cash_register._total)

# Apply discount
cash_register.apply_discount()

# Print items and total after discount
print("Items after discount:", cash_register.get_discounted_items())
print("Total after discount:", round(cash_register._total, 2))

cash_register.void_last_transaction()
print("After voiding last transaction:")
print(cash_register._total)