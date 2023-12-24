"""

"""
from domain.measured_command import MeasuredCommandBase
from preprocessing import preprocessing


class MeasuredCommandProlog(MeasuredCommandBase):
    def get_measure(self, user_input: str):
        norm_user_input = preprocessing(user_input)
        tokenized_norm_user_input = norm_user_input.split(" ")
