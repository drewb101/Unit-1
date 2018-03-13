class Car:
    
    def __init__(self, gas_level_x):
        self.x = gas_level_x

    def add_gas(self, gas):
        self.x += gas

    def fill_up(self):
        added = 13-self.x
        self.add_gas(added)

        if added > 0:
            return added
        return 0