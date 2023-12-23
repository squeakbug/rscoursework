import re
from enum import Enum
from dataclasses import dataclass

from nlp.preprocessing import preprocessing
from nlp.rules import *
from nlp.edit_distance_tools import *
from recomendation_system import RecomendationSystem, ClosenessStrategy
from rs_commands import *


def main_loop(rec_system: RecomendationSystem, user: User) -> int:
    user_input = input("> ")
    normalized_user_input = preprocessing(user_input)
    process_user_input(normalized_user_input, rec_system, user)
