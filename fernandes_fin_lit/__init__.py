from otree.api import *


doc = """
Fernandes et al. 2014 - Financial Literacy Quiz
"""


class C(BaseConstants):
    NAME_IN_URL = 'fernandes_fin_lit'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    q1_correct = models.BooleanField(
        label="Imagine that the interest rate on your savings account was 1% per year and inflation was 2% per year. After 1 year, would you be able to buy:",
        choices=[
            (False, 'More than today with the money in this account'),
            (False, 'Exactly the same as today with the money in this account'),
            (True, 'Less than today with the money in this account'),
            (False, "Don't know"),
            (False, 'Refuse to answer')
        ],
        widget=widgets.RadioSelect
    )

    q2_correct = models.BooleanField(
        label="Do you think that the following statement is true or false? \"Bonds are normally riskier than stocks.\"",
        choices=[
            (False, 'True'),
            (True, 'False'),
            (False, "Don't know"),
            (False, 'Refuse to answer')
        ],
        widget=widgets.RadioSelect
    )

    q3_correct = models.BooleanField(
        label="Considering a long time period (for example, 10 or 20 years), which asset described below normally gives the highest return?",
        choices=[
            (False, 'Savings account'),
            (True, 'Stocks'),
            (False, 'Bonds'),
            (False, "Don't know"),
            (False, 'Refuse to answer')
        ],
        widget=widgets.RadioSelect
    )

    q4_correct = models.BooleanField(
        label="Normally, which asset described below displays the highest fluctuations over time?",
        choices=[
            (False, 'Savings account'),
            (True, 'Stocks'),
            (False, 'Bonds'),
            (False, "Don't know"),
            (False, 'Refuse to answer')
        ],
        widget=widgets.RadioSelect
    )

    q5_correct = models.BooleanField(
        label="When an investor spreads his money among different assets, does the risk of losing a lot of money:",
        choices=[
            (False, 'Increase'),
            (True, 'Decrease'),
            (False, 'Stay the same'),
            (False, "Don't know"),
            (False, 'Refuse to answer')
        ],
        widget=widgets.RadioSelect
    )

    q6_correct = models.BooleanField(
        label="Do you think that the following statement is true or false? \"If you were to invest $1,000 in a stock mutual fund, it would be possible to have less than $1,000 when you withdraw your money.\"",
        choices=[
            (True, 'True'),
            (False, 'False'),
            (False, "Don't know"),
            (False, 'Refuse to answer')
        ],
        widget=widgets.RadioSelect
    )

    q7_correct = models.BooleanField(
        label="Do you think that the following statement is true or false? \"A stock mutual fund combines the money of many investors to buy a variety of stocks.\"",
        choices=[
            (True, 'True'),
            (False, 'False'),
            (False, "Don't know"),
            (False, 'Refuse to answer')
        ],
        widget=widgets.RadioSelect
    )

    # Note: This question is really not suitable for students in Germany / Austria
    q8_correct = models.BooleanField(
        label="Do you think that the following statement is true or false? \"After age 70 1/2, you have to withdraw at least some money from your 401(k) plan or IRA.\"",
        choices=[
            (True, 'True'),
            (False, 'False'),
            (False, 'It depends on the type of IRA and/or 401(k) plan'),
            (False, "Don't know"),
            (False, 'Refuse to answer')
        ],
        widget=widgets.RadioSelect
    )

    q9_correct = models.BooleanField(
        label="Do you think that the following statement is true or false? \"A 15-year mortgage typically requires higher monthly payments than a 30-year mortgage, but the total interest paid over the life of the loan will be less.\"",
        choices=[
            (True, 'True'),
            (False, 'False'),
            (False, "Don't know"),
            (False, 'Refuse to answer')
        ],
        widget=widgets.RadioSelect
    )

    q10_correct = models.BooleanField(
        label="Suppose you have $100 in a savings account and the interest rate is 20% per year and you never withdraw money or interest payments. After 5 years, how much would you have in this account in total?",
        choices=[
            (True, 'More than $200'),
            (False, 'Exactly $200'),
            (False, 'Less than $200'),
            (False, "Don't know"),
            (False, 'Refuse to answer')
        ],
        widget=widgets.RadioSelect
    )

    q11_correct = models.BooleanField(
        label="Which of the following statements is correct?",
        choices=[
            (False, 'Once one invests in a mutual fund, one cannot withdraw the money in the first year'),
            (True, 'Mutual funds can invest in several assets, for example invest in both stocks and bonds'),
            (False, 'Mutual funds pay a guaranteed rate of return which depends on their past performance'),
            (False, 'None of the above'),
            (False, "Don't know"),
            (False, 'Refuse to answer')
        ],
        widget=widgets.RadioSelect
    )

    q12_correct = models.BooleanField(
        label="Which of the following statements is correct? If somebody buys a bond of firm B:",
        choices=[
            (False, 'He owns a part of firm B'),
            (True, 'He has lent money to firm B'),
            (False, 'He is liable for firm B’s debts'),
            (False, 'None of the above'),
            (False, "Don't know"),
            (False, 'Refuse to answer')
        ],
        widget=widgets.RadioSelect
    )

    # Not very suitable for Germany / Austria, as credit cards work differently. Technically we have "charge cards".
    q13_correct = models.BooleanField(
        label="Suppose you owe $3,000 on your credit card. You pay a minimum payment of $30 each month. At an annual percentage rate of 12% (or 1% per month), how many years would it take to eliminate your credit card debt if you made no additional new charges?",
        choices=[
            (False, 'Less than 5 years'),
            (False, 'Between 5 and 10 years'),
            (False, 'Between 10 and 15 years'),
            (True, 'Never'),
            (False, "Don't know"),
            (False, 'Refuse to answer')
        ],
        widget=widgets.RadioSelect
    )

    fin_lit_score = models.IntegerField()


# PAGES
class FinLitPage1(Page):
    template_name = 'fernandes_fin_lit/FinLitQuestionnaire.html'
    form_model = 'player'
    form_fields = [
        'q1_correct',
        'q2_correct',
        'q3_correct',
        'q4_correct',
        'q5_correct',
    ]


class FinLitPage2(Page):
    template_name = 'fernandes_fin_lit/FinLitQuestionnaire.html'
    form_model = 'player'
    form_fields = [
        'q6_correct',
        'q7_correct',
        'q8_correct',
        'q9_correct',
        'q10_correct',
    ]


class FinLitPage3(Page):
    template_name = 'fernandes_fin_lit/FinLitQuestionnaire.html'
    form_model = 'player'
    form_fields = [
        'q11_correct',
        'q12_correct',
        'q13_correct'
    ]

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.fin_lit_score = sum([
            player.q1_correct,
            player.q2_correct,
            player.q3_correct,
            player.q4_correct,
            player.q5_correct,
            player.q6_correct,
            player.q7_correct,
            player.q8_correct,
            player.q9_correct,
            player.q10_correct,
            player.q11_correct,
            player.q12_correct,
            player.q13_correct,
        ])


page_sequence = [
    FinLitPage1,
    FinLitPage2,
    FinLitPage3,
]
