from otree.api import *
import random

doc = """
Questionnaire part for pre-test
"""


class C(BaseConstants):
    NAME_IN_URL = 'questionnaires'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    PAYMENT_PROBABILITY = 0.1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(min=0, max=120, label="How old are you (years)?")
    gender = models.StringField(choices=['female', 'male', 'other', 'prefer not to tell'], label="What is your gender?", widget=widgets.RadioSelect)
    economics = models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], label="Have you ever studied business or economics?")
    soep_risk = models.IntegerField(choices=list(range(0, 11)), label="How do you see yourself: Are you generally willing to take risks or do you try to avoid them (0 = not willing to take risks at all / 10 = very willing to take risks)", widget=widgets.RadioSelectHorizontal)

    pay_participant = models.BooleanField(initial=False)

    iban = models.StringField(required=True, label="IBAN:")
    iban_repeat = models.StringField(required=True, label="IBAN (repeat):")

    # indicators
    female = models.BooleanField()
    male = models.BooleanField()
    other_gender = models.BooleanField()
    na_gender = models.BooleanField()


# FUNCTIONS
def set_indicators(player: Player):
    player.female = player.gender == 'female'
    player.male = player.gender == 'male'
    player.other_gender = player.gender == 'other'
    player.na_gender = player.gender == 'prefer not to tell'


# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'economics', 'soep_risk']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        set_indicators(player)
        player.pay_participant = random.random() < C.PAYMENT_PROBABILITY


class Payments(Page):
    form_model = 'player'
    form_fields = ['iban', 'iban_repeat']

    @staticmethod
    def is_displayed(player: Player):
        return player.pay_participant

    @staticmethod
    def error_message(player, values):
        if values['iban'] != values['iban_repeat']:
            return 'The IBANs do not match.'


class LastPage(Page):
    pass


page_sequence = [Demographics, Payments, LastPage]
