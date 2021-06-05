
class __Location(object):

    def __init__(self, name: str, lat: float, lon: float):
        self.__name: str = name
        self.__lat: float = lat
        self.__lon: float = lon

    def __hash__(self):
        return hash((self.name, self.lat, self.lon))

    def __repr__(self):
        return f"{self.name}|{self.lat}|{self.lon}"

    @property
    def name(self) -> str:
        return self.__name

    @property
    def lat(self) -> float:
        return self.__lat

    @property
    def lon(self) -> float:
        return self.__lon


class MajorLocation(__Location):

    def __init__(self, name, lat, lon, otherstuff):
        super().__init__(name, lat, lon)
        self.things: object = otherstuff

    def do_thing(self) -> object:
        return self.things

    @classmethod
    def empty_loc(cls):
        return cls("Anywhere", 0.0, 0.0, None)