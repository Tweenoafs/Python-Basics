class Road:
    _length = 10000
    _width = 50

    def __init__(self, weight, thickness):
        self.asphalt_weight = weight
        self.thickness = thickness

    def asphalt_count(self):
        count = (self._width * self._length * self.asphalt_weight * self.thickness) // 1000
        print(f"Масса асфальта: {count} т.")


road = Road(30, 10)
road.asphalt_count()



