class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return f"{self.name} menu is available from {self.start_time} to {self.end_time}"
    
    def calculate_bill(self, purchased_items):
        total = 0
        for item in purchased_items:
            if item in self.items:
                total += self.items[item]
        return total

brunch = Menu("Brunch", {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}, "11am", "4pm")

first_order = brunch.calculate_bill(['pancakes', 'home fries', 'coffee'])

early_item_menu = Menu("Early Item", {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}, "3pm", "6pm")

kids = Menu("Kids", {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}, "11am", "9pm")


dinner = Menu("Dinner", {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}, "5pm", "11pm")


class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return f"The restaurant is located at {self.address}"

    def available_menus(self, time):
        available_menu = []
        for menu in self.menus:
            if time >= menu.start_time and time < menu.end_time:
                available_menu.append(menu)
        return available_menu

flagship_store = Franchise("1232 West End Road", [brunch, early_item_menu, kids, dinner])

new_installment = Franchise("12 East Mulberry Street", [brunch, early_item_menu, kids, dinner])

#print(flagship_store.available_menus("11am"))

class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises

basta_fazoolin = Business("Basta Fazoolin'", [flagship_store, new_installment])

arepas_menu_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

arepas_menu = Menu("Take a' Arepa", arepas_menu_items, "10am", "8pm")

print(arepas_menu)

arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

print(arepas_place)

arepa_business = Business("Take a' Arepa", [arepas_place])



