from otree.api import currency_range, expect, Bot
from . import *

import string
import random


def get_random_string(length):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))


class PlayerBot(Bot):
    def play_round(self):
        yield Consent, dict(consent_given=True)
        yield Instructions
        yield Distribution, {
            'click_count_link_1': 3,
            'click_count_link_2': 2,
            'click_count_link_3': 1,
            'study_code_1': get_random_string(6),
            'study_code_2': get_random_string(6),
            'study_code_3': get_random_string(6)
        }