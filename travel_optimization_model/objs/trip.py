from typing import List, Dict
import gurobipy as gp
import numpy as np
from location import MajorLocation
from traveler import Traveler, LeadTraveler
from mip import MIP


class Trip(object):

    def __init__(self, name: str, lead_traveler: LeadTraveler):
        self.__name: str = name
        self.__start_major_loc: MajorLocation = MajorLocation.empty_loc()
        self.__end_major_loc: MajorLocation = MajorLocation.empty_loc()
        self.__major_locations: List[MajorLocation] = []
        self.__time_per_major_loc: Dict[MajorLocation: float] = {}
        self.__max_duration_days: float = 0.0
        self.__lead_traveler: LeadTraveler = lead_traveler
        self.__travelers: List[Traveler] = []
        self.__traveler_major_loc_ratings: Dict[Traveler: List[float]] = {}
        self.__traveler_major_loc_times: Dict[Traveler: List[float]] = {}

    @property
    def name(self) -> str:
        return self.__name

    @property
    def lead_traveler(self) -> LeadTraveler:
        return self.__lead_traveler

    @property
    def start_major_loc(self) -> MajorLocation:
        return self.__start_major_loc

    @property
    def end_major_loc(self) -> MajorLocation:
        return self.__end_major_loc

    @property
    def major_locations(self) -> List[MajorLocation]:
        return self.__major_locations

    @property
    def time_per_major_loc(self) -> Dict[MajorLocation: float]:
        return self.__time_per_major_loc

    @property
    def max_duration_days(self) -> float:
        return self.__max_duration_days

    @property
    def travelers(self) -> List[Traveler]:
        return self.__travelers

    @property
    def num_major_locs(self) -> int:
        return len(self.major_locations)

    def add_traveler(self, traveler: Traveler) -> None:
        self.__travelers.append(traveler)

    def rm_traveler(self, traveler: Traveler) -> None:
        self.__travelers.remove(traveler)

    def add_start_loc(self, loc: MajorLocation) -> None:
        self.__start_major_loc = loc

    def add_end_loc(self, loc: MajorLocation) -> None:
        self.__end_major_loc = loc

    def add_major_loc(self, loc: MajorLocation) -> None:
        self.__major_locations.append(loc)

    def rm_major_loc(self, loc: MajorLocation) -> None:
        self.__major_locations.remove(loc)

    def log_traveler_preferences(self, traveler: Traveler) -> None:
        self.__traveler_major_loc_ratings[traveler] = traveler.major_loc_ratings
        self.__traveler_major_loc_times[traveler] = traveler.major_loc_times

    def _init_model(self) -> None:
        self.__model = MIP(self.name, self.lead_traveler)

    def _init_vars(self) -> None:

        self.__model.addMVar()