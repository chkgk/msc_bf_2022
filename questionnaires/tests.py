from otree.api import currency_range, expect, Bot
from . import *
import random


class PlayerBot(Bot):
    def play_round(self):
        yield Risk, {
            'soep_risk': random.randint(0, 10),
            'soep_risk_others': random.randint(0, 10)
        }

        yield Demographics, {
            'age': random.randint(18, 120),
            'gender': random.choice(['female', 'male', 'other', 'prefer not to tell']),
            'field_of_study': random.choice(['Economics', 'VWL', 'BWL', 'Business', 'physics', 'chemistry']),
            'nationality': random.choice(['German', 'Austrian', 'USA', 'Swedish', 'Norway']),
            'religion': random.choice(C.RELIGIONS),
            'education_level': random.choice(C.EDUCATION)
        }

        if self.player.pay_participant:
            yield Payments, {
                'iban': 'asdf',
                'iban_repeat': 'asdf',
                'name': 'blah'
            }
        else:
            yield Credit, {
                'name': 'blah'
            }

        yield Submission(LastPage, check_html=False)
