from random import choices
from random import randint

class Customer:

    prefered_segment = "keins"

    def __init__(self):
        self.shopping_amount = self.calc_shopping_amount(self.choose_household(), self.choose_shopping_type())
    

    def choose_household(self):
        # 1 Person household, prob = 42.3%
        # 2 Person household, prob = 33.2%
        # 3 Person household, prob = 11.9%
        # 4 Person household, prob = 9.1%
        # 5+ Person household, prob = 3.5%
        # source: https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Haushalte-Familien/Tabellen/1-1-privathaushalte-haushaltsmitglieder

        population = [1,2,3,4,5]
        weights = [0.423, 0.332, 0.119, 0.091, 0.035]
        return choices(population, weights)

    def choose_shopping_type(self):
        # shopping type (planned product amount):
        # spontaneous purchase (2-3), daily purchase (4-12), weekly purchase (13-25), sepcial offer (1)

        population = [randint(1 ,3), randint(3, 12), randint(12, 25), 0]
        weights = [0.45, 0.3, 0.2, 0.05]
        return choices(population, weights)


    def calc_shopping_amount(self, household_mlt, type_amount):

        # Segmententscheidung implementieren

        if type_amount[0] == 0:
            return 1
        else:
            return household_mlt[0] * type_amount[0]

    def choose_segment(self):
        population = ['Lebensmittel', 'Getränke']
        weights = [0.5, 0.5]
        prefered_segment = choices(population,weights)

print(Customer().shopping_amount)
print(Customer().prefered_segment)


class Shopping_sequence:

    def __init__(self, cust):
        self.cust = cust



# cust1 = Customer()
# ss1 = Shopping_sequence(cust1)

# print(ss1.cust.household_mlt)
# print(ss1.cust.choose_shopping_type())
