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

    RELIGIONS = [
        'Christian',
        "Muslim",
        "Jewish",
        "Buddhist",
        "Hindu",
        "other",
        "nothing in particular",
        'prefer not to tell'
    ]
    
    EDUCATION = [
        "A-levels, Abitur, Matura",
        "Bachelor's degree",
        "Master's degree",
        "Doctorate Degree"
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # demographics
    age = models.IntegerField(min=0, max=120, label="How old are you (years)?")
    gender = models.StringField(choices=['female', 'male', 'other', 'prefer not to tell'], label="What is your gender?", widget=widgets.RadioSelect)
    field_of_study = models.StringField(label="Which is your (major) field of studies?")
    nationality = models.StringField(label="What is your nationality?")
    # from: West Europe Survey (WEUP)
    religion = models.StringField(choices=C.RELIGIONS, label="What is your present religion, if any?")
    education_level = models.StringField(choices=C.EDUCATION, label="What is your highest level of educational achievement?")

    # risk (Socioeconomic Panel, Germany)
    soep_risk = models.IntegerField(choices=list(range(0, 11)), label="How do you see <b>yourself</b>: Are you generally willing to take risks or do you try to avoid them?<br> (0 = not willing to take risks at all / 10 = very willing to take risks)", widget=widgets.RadioSelectHorizontal)

    soep_risk_others = models.IntegerField(choices=list(range(0, 11)),
                                    label="How do you see <b>others</b>: Do you think most people are generally willing to take risks or do they try to avoid them?<br> (0 = most people are not willing to take risks at all / 10 = most people are very willing to take risks)",
                                    widget=widgets.RadioSelectHorizontal)

    # payments
    pay_participant = models.BooleanField(initial=False)
    iban = models.StringField(required=True, label="IBAN:")
    iban_repeat = models.StringField(required=True, label="IBAN (repeat):")
    name = models.StringField(required=True, label="Your name:")


# PAGES
class Risk(Page):
    form_model = 'player'
    form_fields = ['soep_risk', 'soep_risk_others']


class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'nationality', 'religion', 'field_of_study', 'education_level']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.pay_participant = random.random() < C.PAYMENT_PROBABILITY
        if player.pay_participant:
            player.payoff = 500


class Payments(Page):
    form_model = 'player'
    form_fields = ['iban', 'iban_repeat', 'name']

    @staticmethod
    def is_displayed(player: Player):
        return player.pay_participant

    @staticmethod
    def error_message(player, values):
        if values['iban'] != values['iban_repeat']:
            return 'The IBANs do not match.'


class Credit(Page):
    form_model = 'player'
    form_fields = ['name']

    @staticmethod
    def is_displayed(player: Player):
        return not player.pay_participant

class LastPage(Page):
    pass


page_sequence = [Risk, Demographics, Credit, Payments, LastPage]
