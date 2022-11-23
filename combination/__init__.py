from otree.api import *


doc = """
Combines multiple student experiments
"""


class C(BaseConstants):
    NAME_IN_URL = 'combination'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    STUDY_LINKS = [
        'https://www.google.com',
        'https://www.apple.com',
        'https://www.nytimes.com',
        # 'https://www.uibk.ac.at'
    ]


class Subsession(BaseSubsession):
    study_link_1 = models.StringField()
    study_link_2 = models.StringField()
    study_link_3 = models.StringField()
    # study_link_4 = models.StringField()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    consent_given = models.BooleanField(initial=False, widget=widgets.CheckboxInput, label="I confirm that I have read these instructions, agree with them, and want to participate in this study.")
    click_count_link_1 = models.IntegerField(initial=0)
    click_count_link_2 = models.IntegerField(initial=0)
    click_count_link_3 = models.IntegerField(initial=0)
    # click_count_link_4 = models.IntegerField(initial=0)

    study_code_1 = models.StringField(label="Completion code for Study Part 1:")
    study_code_2 = models.StringField(label="Completion code for Study Part 2:")
    study_code_3 = models.StringField(label="Completion code for Study Part 3:")
    # study_code_4 = models.StringField(label="Completion code for Study Part 4:")


# PAGES
class Consent(Page):
    form_model = 'player'
    form_fields = ['consent_given']


class Instructions(Page):
    pass


class Distribution(Page):
    form_model = 'player'
    form_fields = [
        'click_count_link_1',
        'click_count_link_2',
        'click_count_link_3',
        # 'click_count_link_4',
        'study_code_1',
        'study_code_2',
        'study_code_3',
        # 'study_code_4'
    ]


# FUNCTIONS
def creating_session(subsession: Subsession):
    subsession.study_link_1 = C.STUDY_LINKS[0]
    subsession.study_link_2 = C.STUDY_LINKS[1]
    subsession.study_link_3 = C.STUDY_LINKS[2]
    # subsession.study_link_4 = C.STUDY_LINKS[3]


page_sequence = [
    Consent,
    Instructions,
    Distribution
]
