class ShoppingCart:
    def __init__(self):
        self._cart_list = []
    
    def add_item(self, name, price):
        self._cart_list.append([name, price])
        return self._cart_list.copy()

    def remove_item(self, name):
        for item in self._cart_list.copy():
            if item[0] == name:
                self._cart_list.remove(item)
        return self._cart_list.copy()

    def get_items(self):
        return self._cart_list.copy()

    def total(self):
        total = 0
        for item in self._cart_list:
            total += item[1]
        return total

cart = ShoppingCart()

print(cart.get_items())
print(cart.add_item('banana', 20))
cart.add_item('milk', 10)
print(cart.add_item('banana', 10))
print(cart.add_item('banana', 5))
cart.add_item('potato', 2.5)
print(cart.get_items())
print(cart.total())
cart.remove_item('banana')
print(cart.total())
print(cart.get_items())