class Container:
    def __init__(self, volume_in_ml):
        self.volume_in_ml = volume_in_ml

cup = Container(250)
print(f'There are {cup.volume_in_ml} ml in the cup.')
ex = input('How much do you want to spill out of the cup?')
cup.volume_in_ml = cup.volume_in_ml - float(ex)
print(f'New volume: {cup.volume_in_ml} ml.')
