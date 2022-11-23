from otree.api import currency_range, expect, Bot
from . import *
import random


class PlayerBot(Bot):
    def play_round(self):
        yield FinLitPage1, {
            'q1_correct': random.choice([True, False]),
            'q2_correct': random.choice([True, False]),
            'q3_correct': random.choice([True, False]),
            'q4_correct': random.choice([True, False]),
            'q5_correct': random.choice([True, False])
        }

        yield FinLitPage2, {
            'q6_correct': random.choice([True, False]),
            'q7_correct': random.choice([True, False]),
            'q8_correct': random.choice([True, False]),
            'q9_correct': random.choice([True, False]),
            'q10_correct': random.choice([True, False])
        }

        yield FinLitPage3, {
            'q11_correct': random.choice([True, False]),
            'q12_correct': random.choice([True, False]),
            'q13_correct': random.choice([True, False])
        }

