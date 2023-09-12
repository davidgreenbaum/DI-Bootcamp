#create class called Farm
# init with parameters farmer, animal breed, quantity
#


class Farm():
    def __init__(self, owner) :
        self.owner = owner
    


macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())