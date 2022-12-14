
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'Instructions1'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    pass
class Welcoming(Page):
    form_model = 'player'
class Introductionbanks1(Page):
    form_model = 'player'
class Trial1(Page):
    form_model = 'player'
page_sequence = [Welcoming, Introductionbanks1]